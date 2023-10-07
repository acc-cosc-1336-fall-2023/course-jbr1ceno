#

def get_hamming_distance(dna1, dna2):
    count = 0


    for n in range(len(dna1)):
        if(dna1[n] != dna2[n]):
            count += 1
            
    return count
    
def get_dna_complement(dna):
    count = 0
    dna = dna.replace("A", "t").replace("C", "g").replace("T", "a").replace("G", "c")
    dna = dna.upper()
    dna = dna[::-1]
    return dna