#!/usr/bin/env python

import numpy as np
import pandas as pd
import sys
from fasta import readFASTA

#================#
#  	exercise 1	 #
#================#


## 1.1 define globally input and output

# get FASTA sequences
fasta_file = sys.argv[1]
input_sequences = readFASTA(open(fasta_file))
print(input_sequences)
seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]

# record scoring matrix
scoring_matrix = pd.read_csv(sys.argv[2], header = None)

gap_penalty = sys.argv[3]
output_file = sys.argv[4]

## 1.2 initializing matrices
F_matrix = np.zeros(len(sequence1)+1, len(sequence2)+1)
traceback_matrix = np.zeros(len(sequence1)+1, len(sequence2)+1)

## 1.3 populating the matrices


##### commmand line in terminal:./hw3.py CTCF_38_M27_AA.faa HOXD70.txt
