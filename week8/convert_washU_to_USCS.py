#!/usr/bin/env python

import sys
import re
import pandas as pd

# baitmap_file = sys.argv[1]
# washu_file = sys.argv[2]
# output_file = sys.argv[3]
# # command line: ./convert_washU_to_USCS.py raw/Design/h19_chr20and21.baitmap GM1/data/GM1_washU_text.txt output.bed

# ucsc_track_header = 'track type=interact name="pCHIC" description="Chromatin interactions" useScore=on maxHeightPixels=200:100:50 visibility=full\n'

# # Read baitmap to determine bait fragments and their corresponding genes
# bait_map = {}
# with open(baitmap_file, 'r') as f:
# 	for line in f:
# 		coordinate = ''
# 		parts = re.split(r'\s+', line.strip())
# 		print(parts)
# 		coordinate = 'chr' + str(parts[0]) + ',' + str(parts[1]) + ',' + str(parts[2])
# 		bait_map[coordinate] = parts[4]
# print(bait_map)


# # define variables to store WashU contents
# sourceName_lst = []
# source_lst = []
# targetName_lst = []
# target_lst = []
# targetStrand_lst = []
# max_strength = 0
# strength_lst = []
# score_lst = []
# chrom_lst = []
# chromStart_lst = []
# chromEnd_lst = []

# # Read WashU format interactions and calculate max interaction strength
# with open(washu_file, 'r') as f:
# 	for line in f:
# 		parts = re.split(r'\s+', line.strip())
# 		frag1_locs = parts[0]
# 		frag2_locs = parts[1]
# 		strength = float(parts[2])
# 		strength_lst.append(strength)
		
#         # compare chromStart and end 
# 		chrom_lst.append(frag1_locs.split(',')[0])
# 		chromStart_lst.append(min([int(frag1_locs.split(',')[1]), int(frag2_locs.split(',')[1])]))
# 		chromEnd_lst.append(max([int(frag1_locs.split(',')[2]), int(frag2_locs.split(',')[2])]))

# 	# print(strength_lst)
# 	# print(len(chromStart_lst))
# 	# print(len(chromEnd_lst))

# 		# Determine which fragments are baits and get corresponding genes
# 		if frag1_locs in bait_map:
# 			sourceName_lst.append(bait_map[frag1_locs])
# 			source_lst.append(frag1_locs)
# 			target_lst.append(frag2_locs)
# 			if frag2_locs in bait_map:
# 				targetName_lst.append(bait_map[frag2_locs])
# 				targetStrand_lst.append('+')
# 			else:
# 				targetName_lst.append('.')
# 				targetStrand_lst.append('-')

# 		elif frag2_locs in bait_map:
# 			print(1)
# 			sourceName_lst.append(bait_map[frag2_locs])
# 			source_lst.append(frag2_locs)
# 			target_lst.append(frag1_locs)
# 			if frag1_locs in bait_map:
# 				targetName_lst.append(bait_map[frag1_locs])
# 				targetStrand_lst.append('+')
# 			else:
# 				targetName_lst.append('.')
# 				targetStrand_lst.append('-')	
            
# 	# Calculate interaction score
# 	max_strength = max(strength_lst)
# 	for strength in strength_lst:
# 		score_lst.append(int(strength / max_strength * 1000))
# 	# print(score_lst)

# 	# print(len(source_lst))
# 	# print(len(target_lst))
# 	# print(len(sourceName_lst))
# 	# print(len(targetName_lst))


# # Prepare UCSC interaction bed format entry
# 	interactions = []
# 	for i in range(len(source_lst)):
# 		interaction_entry = '\t'.join([chrom_lst[i], str(chromStart_lst[i]), str(chromEnd_lst[i]), '.',
# 			str(score_lst[i]), str(strength_lst[i]), '.', '0', 
# 			source_lst[i].split(',')[0], source_lst[i].split(',')[1], source_lst[i].split(',')[2], sourceName_lst[i], '+',
# 			target_lst[i].split(',')[0], target_lst[i].split(',')[1], target_lst[i].split(',')[2], targetName_lst[i], targetStrand_lst[i],
# 			])
# 		interactions.append(interaction_entry)
# 	# print(interactions)


# # Write interactions to the output file with UCSC track header
# with open(output_file, 'w') as f:
# 	f.write(ucsc_track_header)
# 	for interaction in interactions:
# 		f.write(interaction + '\n')



## find the top interaction 

df = pd.read_csv('output.bed', sep = '\t', skiprows = 1, header = None)
# print(df.head())
propro_sets = df.loc[ df[17] == '+' ]
top_propro_interactions = propro_sets.nlargest(6, 4)
print(top_propro_interactions)

proenh_sets = df.loc[ df[17] == '-' ]
top_proenh_interactions = proenh_sets.nlargest(6, 4)
print(top_proenh_interactions)