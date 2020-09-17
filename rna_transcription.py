def to_rna(dna_strand):
    dna={
        "A": "U",
        "C" : "G",
        "G" : "C",
        "T" : "A"
    }
    rna=""
    for x in dna_strand:
        if x in dna.keys():
            rna+=dna[x]
    return rna
