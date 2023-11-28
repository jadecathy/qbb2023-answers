#!/usr/bin/env python

import sys

from model_peaks import load_bedgraph, bin_array
import numpy
import scipy.stats
import matplotlib.pyplot as plt
from scipy.stats import poisson


def main():
    # Load file names and fragment width
    forward_sname, reverse_sname = sys.argv[1:3]
    frag_width = sys.argv[3]
    forward_cname, reverse_cname = sys.argv[4:6]
# pass the parameters: ./find_peaks.py sample1.fwd.bg sample1.rev.bg 198 control.fwd.bg control.rev.bg 

 # for control best offset is 52
 # for sample1 best offset is 198
 # for sample2 best offset is 199

    # Define what genomic region we want to analyze
    chrom = "chr2R"
    chromstart = 10000000
    chromend =  12000000
    chromlen = chromend - chromstart

    # Load the sample bedgraph data, reusing the function we already wrote
    sample_forward = load_bedgraph(forward_sname, chrom, chromstart, chromend)
    sample_reverse = load_bedgraph(reverse_sname, chrom, chromstart, chromend)
    # print('sample_forward size:',sample_forward.shape)    
    # print('sample_reverse size:',sample_reverse.shape) 

    # Combine tag densities, shifting by our previously found fragment width
    combined_samp = numpy.zeros(chromlen)
    combined_samp[:(chromlen-99)] = sample_forward[99:]
    combined_samp[-(chromlen-99):] += sample_reverse[:-99]
    print('conbined_saple size:',combined_samp.shape)

    # Load the control bedgraph data, reusing the function we already wrote
    control_forward = load_bedgraph(forward_cname, chrom, chromstart, chromend)
    control_reverse = load_bedgraph(reverse_cname, chrom, chromstart, chromend)

    # Combine tag densities
    combined_ctrl = control_forward + control_reverse
    print('conbined_ctrl size:',combined_ctrl.shape)   

    # Adjust the control to have the same coverage as our sample
    adjust_index = float(numpy.sum(combined_samp)/numpy.sum(combined_ctrl))
    combined_ctrl = combined_ctrl * adjust_index

    # Create a background mean using our previous binning function and a 1K window
    # Make sure to adjust to be the mean expected per base
    binned_ctrl = bin_array(combined_ctrl, 1000)/1000
    print(binned_ctrl)

    # Find the mean tags/bp and make each background position the higher of the
    # the binned score and global background score
    mean_ctrl = numpy.mean(binned_ctrl)
    for i in range(binned_ctrl.shape[0]):
        binned_ctrl[i] = max(binned_ctrl[i], mean_ctrl)
    print(binned_ctrl)

    # Score the sample using a binsize that is twice our fragment size
    # We can reuse the binning function we already wrote
    binned_samp = bin_array(combined_samp, 2*198)
    print(binned_samp)
    print(binned_samp.shape)


    # Find the p-value for each position (you can pass a whole array of values
    # and and array of means). Use scipy.stats.poisson for the distribution.
    # Remeber that we're looking for the probability of seeing a value this large
    # or larger
    # Also, don't forget that your background is per base, while your sample is
    # per 2 * width bases. You'll need to adjust your background
    adjusted_binned_ctrl = binned_ctrl * (2 * 198)
    p_values = poisson.sf(binned_samp, adjusted_binned_ctrl)
    # print(p_values)
    # for p in range(len(p_values)):
    #     if binned_samp[p] < adjusted_binned_ctrl[p]:
    #         p_values[p] = 1
    # print(p_values)


    # Transform the p-values into -log10
    # You will also need to set a minimum pvalue so you doen't get a divide by
    # zero error. I suggest using 1e-250
    minimum_pvalue = 1e-250
    p_values[p_values < minimum_pvalue] = minimum_pvalue
    log_pvalues= -numpy.log10(p_values)
    # keep = log_pvalues >= 10
    # # print(keep)
    # filtered_log_pvalues = log_pvalues[keep]

    

    # Write p-values to a wiggle file
    # The file should start with the line
    # "fixedStep chrom=CHROM start=CHROMSTART step=1 span=1" where CHROM and
    # CHROMSTART are filled in from your target genomic region. Then you have
    # one value per line (in this case, representing a value for each basepair).
    # Note that wiggle files start coordinates at 1, not zero, so add 1 to your
    # chromstart. Also, the file should end in the suffix ".wig"
    write_wiggle(log_pvalues,chrom,chromstart,str(forward_sname)[0:7]+'.wig')

    # Write bed file with non-overlapping peaks defined by high-scoring regions 
    write_bed(log_pvalues,chrom,chromstart,chromend,198,str(forward_sname)[0:7]+'.bed')



def write_wiggle(pvalues, chrom, chromstart, fname):
    output = open(fname, 'w')
    print(f"fixedStep chrom={chrom} start={chromstart + 1} step=1 span=1",
          file=output)
    for i in pvalues:
        print(i, file=output)
    output.close()

def write_bed(scores, chrom, chromstart, chromend, width, fname):
    chromlen = chromend - chromstart
    output = open(fname, 'w')
    while numpy.amax(scores) >= 10:
        pos = numpy.argmax(scores)
        start = pos
        while start > 0 and scores[start - 1] >= 10:
            start -= 1
        end = pos
        while end < chromlen - 1 and scores[end + 1] >= 10:
            end += 1
        end = min(chromlen, end + width - 1)
        print(f"{chrom}\t{start + chromstart}\t{end + chromstart}", file=output)
        scores[start:end] = 0
    output.close()


if __name__ == "__main__":
    main()