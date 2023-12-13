## PART2
**Are the majority of the CpG dinucleotides methylated or unmethylated?**
- No. Only the promoter region. 

## Part3
**Q1. Calculate the number of sites present only in the bismark file, present only in the nanopore file, and the shared sites as a percentage of total sites (both unique and shared sites)**
- data1 unique reads: (2.9552115872243196) %
- data2 unique reads: (1.1901070261959186) %
- shared reads: (95.85468138657977) %

**Q2. How does using nanopore for methylation calling differ from bisulfite sequencing in terms of coverage? Which method appears better and why?**
- The bisulfite(in red) works better because it has higher coverage.

**Q3. What can you infer about the two different approaches and their ability to detect methylation changes?**
- Their bilityto detect methylation changes are identical.

**Q4: What is the effect of tumorigenesis on global methylation patterns?**
- Tumorigenesis increase and decrease mythylation at different sites. Overall, it increases methylation levels.



The command lines for Part4:
1. samtools index normal.ONT.chr2.bam
2. samtools index tumor.ONT.chr2.bam

**Q5: What changes can you observe between the normal and tumor methylation landscape? What do you think the possible effects are of the changes you observed?**
- The methylation level is higher in normal cell lines, meaning that its expression is lower. Given this is a gene responsible for de novo methylation of cytosines, the 5-mc activity in normal cells is lower than in tumor cells. 

**Q6: What does it mean for a gene to be “imprinted”?**
-  It means gene expression is inherited from their parents. 

**Q7: What is happening when you select the option to phase the reads? What is required in order to phase the reads?**
- Phasing reads involves grouping aligned sequencing reads into sets that likely originated from the same DNA molecule. It organizes reads based on shared variants or differences between alleles and infer the specific haplotype for a region of interest. 
- It requires the sequencing data, variant information, and the genomics contextprovided by indexing.

**Q8: Can any set of reads be phased? Explain your answer.**
- No. Phasing reads relies on identifying variants or differences between alleles within the reads to infer the haplotype. It depends on factors like distance between Variants.

