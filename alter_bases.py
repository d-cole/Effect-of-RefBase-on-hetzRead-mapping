"""
Overwrites byte representing one base at specific location in .fa file.
Locations are specified by 'CHROM POS CURR_BASE NEW_BASE'
Byte offset is calculated given CHROM, POS and indexed reference

ASSUMES LINES ARE 80 bp long

Requires: 
    Reference file (.fa)
    Index of reference (.fai)
    List of bases to change and what to change them to
    
"""
import sys


if __name__ == "__main__":
    #http://stackoverflow.com/questions/508983/how-to-overwrite-some-bytes-in-the-middle-of-a-file-with-python <-- overwiting byte positions

    ref_loc = sys.argv[1]
    bases_loc = sys.argv[2]
    fai_loc = "pseudo_plastids.fa.fai"

    #Load position of bases to be modified
    bases_idx = [] 
    with open(bases_loc) as bases:
        for line in bases:
            sline = line.split('\t')
            sline[-1] = sline[-1].strip('\n')
            bases_idx.append(sline)
    bases.close()

    #Load chromosome offset byte info from .fai file
    chrom_offset = {}
    with open(fai_loc)as fai:
        for line in fai:
            sline = line.split()
            chrom_offset[sline[0]] = int(sline[2])
    fai.close()


    #For each base calculate the byte offset and
    line_length = 80
    bytes_per_line = 80
    bytes_per_bp = 1

    for base_mod_info in bases_idx:
        chrom = base_mod_info[0]
        pos = int(base_mod_info[1])

        #Get byte offset of chromosome
        offset = chrom_offset[chrom]
       
        ##pos starts from 0 offset from chrom offset
        pos = pos - 1 
        
        #Add byte offset for position in chromosome
        # one byte for each pos + additional byte for each line (to account for '\n')
        offset += pos + pos/line_length
        base_mod_info.append(offset)

 
    #Overwrite bases specified in bases_idx 
    # bases_idx: [CHROM, POS, OLD_BASE, NEW_BASE, BYTE_OFFSET]
    fp = open(ref_loc,"r+b")
    
    #Read bases at offset
    for base_edit in bases_idx:
        fp.seek(int(base_edit[-1]))        
#        fp.write(base_edit[3])
        found_base = fp.read(1)
        #if base_edit[2] != found_base:
        #    print "ERROR - Found base does not match expectations"
    
#        if str(found_base) != str(base_edit[2]):
#            print "NOT CHANGED"
#            print base_edit

        print "Given: ", base_edit
        print "Found base: ", found_base
 
    fp.close()







