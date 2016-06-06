#Effect of reference base on frequency of alt/ref bases in mapped reads

**find_diffs.py**

Finds sites where the alternate base is of a consistantly high frequency in all samples of a single genotype.

**find_excl_other_genotype.py**

Given set of high frequency alternate base sites from find_diffs.py, finds these in the other genotype.

**find_good_diffs.py**

Given two .mpileup files, one for each genotype, finds sites where one genotoype is homozygous for the alternate base, the other homozygous for the reference. This could be run on unfiltered .mpileup files but would be costly. Filtering genotype .mpileup files using find_diffs.py and find_excl_other_genotype.py is essential. 

**get_random_subset_bases_to_change.py**

Given the sites returned by find_good_diffs.py, generates a random subset of sites.

**alter_bases.py**

Overwrites specified bases in reference. Requires tab delimited file representing bases to change. The reference must be indexed.

