#!/bin/bash

# bwa index sacCer3.fa

# for sample in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63
# do
# 	echo "Aligning sample:" ${sample}
# 	bwa mem -R "@RG\tID:${sample}\tSM:${sample}" \
# 	  sacCer3.fa\
# 	  ${sample}.fastq > ${sample}.sam
# 	samtools sort -O bam -o ${sample}.bam ${sample}.sam
# 	samtools index ${sample}.bam 
# done

# freebayes -f sacCer3.fa A01_09.bam A01_11.bam A01_23.bam A01_24.bam A01_27.bam A01_31.bam A01_35.bam A01_39.bam A01_62.bam A01_63.bam -p 1 --genotype-qualities > calling.vcf 
# vcffilter -f "QUAL > 0.99" calling.vcf > calling_filtered.vcf
# vcfallelicprimitives -k -g calling_filtered.vcf > calling_decomposed.vcf
snpEff ann -v -c snpEff.config R64-1-1.105 calling_decomposed.vcf > annotated.vcf