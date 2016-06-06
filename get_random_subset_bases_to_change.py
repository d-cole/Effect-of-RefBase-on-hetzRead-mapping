"""
Gets subset_size random sites from bases_to_change_in and writes 
    them to bases_out_loc.
"""
import sys
from random import randint
import linecache

if __name__ == "__main__":
    bases_to_change_in, bases_out_loc = sys.argv[1], sys.argv[2]
   
    #Number of random sites to choose 
    subset_size = 50
    file_len = sum(1 for line in open(bases_to_change_in))  

    #Write random lines to output file
    f_out = open(bases_out_loc, "w")
    for i in range(0, subset_size):

        f_out.write(linecache.getline(bases_to_change_in,
            randint(0, file_len - 1)))

    f_out.close()
    
