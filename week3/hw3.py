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
seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]
# print(sequence1)
# print(sequence2)

# record scoring matrix
scoring_matrix = pd.read_csv(sys.argv[2], sep = '\s+', header = 0, index_col = 0)
print(scoring_matrix.shape)
print(scoring_matrix)
gap_penalty = float(sys.argv[3])
output_file = sys.argv[4]


## 1.2 initializing matrices
F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))
traceback_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))


## 1.3 populating thse matrices
m = len(sequence1)
n = len(sequence2)


# F matrix

# write the 1st row and column
for i in range(m+1):
	# print(i * gap_penalty)
	F_matrix[i][0] = i * gap_penalty

for j in range(n+1):
	F_matrix[0][j] = j * gap_penalty
# print(F_matrix)

for i in range(1,m+1):
	for j in range(1,n+1):
		# print(scoring_matrix.loc[str(sequence1[i-1])][str(sequence2[j-1])])
		match_score = float(scoring_matrix.loc[str(sequence1[i-1])][str(sequence2[j-1])])
		# print(match_score)
		F_matrix[i][j] = max(
    	F_matrix[i-1][j-1] + match_score,
    	F_matrix[i-1][j] + gap_penalty,
    	F_matrix[i][j-1] + gap_penalty
		)
# print(F_matrix)
# print(sequence1)
# print(sequence2)
# np.savetxt('f-matrix', F_matrix)


## traceback matrice

# write the 1st row and column
for i in range(m+1):
	# print(i * gap_penalty)
	F_matrix[i][0] = i * gap_penalty

for j in range(n+1):
	F_matrix[0][j] = j * gap_penalty
# print(F_matrix)

for i in range(1,m+1):
	for j in range(1,n+1):
		# print(scoring_matrix.loc[str(sequence1[i-1])][str(sequence2[j-1])])
		match_score = float(scoring_matrix.loc[str(sequence1[i-1])][str(sequence2[j-1])])
		# print(match_score)
		if F_matrix[i][j] == F_matrix[i-1][j-1] + match_score:
			traceback_matrix[i][j] = 0  # Align, diagonal denoted as 0
		elif F_matrix[i][j] == F_matrix[i-1][j] + gap_penalty:
			traceback_matrix[i][j] = 1  # Gap in sequence 1, up denote as 1
		else:
			traceback_matrix[i][j] = 2  # Gap in sequence 2, left denote as 2
# print(traceback_matrix)
np.savetxt('traceback-matrix', traceback_matrix)

F_matrix = np.loadtxt('f-matrix')
traceback_matrix = np.loadtxt('traceback-matrix')

## 1.4 Find the optimal alignment
aligned_seq1 = ''
aligned_seq2 = ''
i = len(sequence1)
j = len(sequence2)
while i > 0 or j > 0:
    if traceback_matrix[i][j] == 0:
        aligned_seq1 = sequence1[i - 1] + aligned_seq1
        aligned_seq2 = sequence2[j - 1] + aligned_seq2
        i -= 1
        j -= 1
    elif traceback_matrix[i][j] == 1:
        aligned_seq1 = sequence1[i - 1] + aligned_seq1
        aligned_seq2 = '-' + aligned_seq2
        i -= 1
    else:
        aligned_seq1 = '-' + aligned_seq1
        aligned_seq2 = sequence2[j - 1] + aligned_seq2
        j -= 1
    # if i > 0 and j > 0 and traceback_matrix[i][j] == 0:
    #     aligned_seq1 = sequence1[i - 1] + aligned_seq1
    #     aligned_seq2 = sequence2[j - 1] + aligned_seq2
    #     i -= 1
    #     j -= 1
    # elif i > 0 and traceback_matrix[i][j] == 1:
    #     aligned_seq1 = sequence1[i - 1] + aligned_seq1
    #     aligned_seq2 = '-' + aligned_seq2
    #     i -= 1
    # else:
    #     aligned_seq1 = '-' + aligned_seq1
    #     aligned_seq2 = sequence2[j - 1] + aligned_seq2
    #     j -= 1
        # try:
        #     aligned_seq1 = '-' + aligned_seq1
        #     aligned_seq2 = sequence2[j - 1] + aligned_seq2
        #     j -= 1
        # except:
        #     break
# print(aligned_seq1)
# print(aligned_seq2)


# 1.5 Write the alignment to the output

num_gaps_seq1 = aligned_seq1.count('-')
num_gaps_seq2 = aligned_seq2.count('-')
alignment_score = F_matrix[-1][-1]
# print(alignment_score)
# print(num_gaps_seq1)
# print(num_gaps_seq2)


with open(output_file, 'w') as f_out:
	f_out.write(f"Sequence 1 alignment: '{aligned_seq1}'\n")
	f_out.write(f"Sequence 2 alignment: '{aligned_seq2}'\n")
	f_out.write(f"Number of gaps in sequence 1: {num_gaps_seq1}\n")
	f_out.write(f"Number of gaps in sequence 2: {num_gaps_seq2}\n")
	f_out.write(f"Alignment score: {alignment_score}\n")

f_out.close()

# ##### commmand line in terminal:./hw3.py CTCF_38_M27_AA.faa BLOSUM62.txt -10 AA_alignment
# ##### commmand line in terminal:./hw3.py CTCF_38_M27_DNA.fna HOXD70.txt -300 DNA_alignment