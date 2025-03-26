# Preferred Input: "Leucine/ Histidine/ Lysine/ Glutamic Acid/ Threonine"
# ---
# leucine: UUA, UUG, CUU, CUC, CUA, CUG
# histidine: CAU, CAC
# lysine: AAA, AAG
# glutamic acid: GAA, GAG
# threonine: ACU, ACC, ACA, ACG
# ---
# Output:   Leu: UUA, UUG, CUU, CUC, CUA, CUG
#           His: CAU, CAC
#           Lys: AAA, AAG
#           Glu: GAA, GAG
#           Thr: ACU, ACC, ACA, ACG
#
#           Possible sequences:
#           Leucine
#           UUA, CAU, AAA, GAA, ACU
#           UUG, CAU, AAA, GAA, ACU
#           CUU, CAU, AAA, GAA, ACU
#           CUC, CAU, AAA, GAA, ACU
#           CUA, CAU, AAA, GAA, ACU
#           CUG, CAU, AAA, GAA, ACU
#           
#           UUA, CAC, AAA, GAA, ACU
#           UUG, CAC
#           
#           
#           
#           
#           
#           
#           
#           
#           
#           

codon_table = {
    "U": {
        "U": {
            "U": "phenylalanine",
            "C": "phenylalanine",
            "A": "leucine",
            "G": "leucine",
        },
        "C": {
            "U": "serine",
            "C": "serine",
            "A": "serine",
            "G": "serine",
        },
        "A": {
            "U": "tyrosine",
            "C": "tyrosine",
            "A": "stop", # I changed STOP to stop
            "G": "stop", # I changed STOP to stop
        },
        "G": {
            "U": "cysteine",
            "C": "cysteine",
            "A": "stop", # I changed STOP to stop
            "G": "tryptophan",
        }
    },
    "C": {
        "U": {
            "U": "leucine",
            "C": "leucine",
            "A": "leucine",
            "G": "leucine",
        },
        "C": {
            "U": "proline",
            "C": "proline",
            "A": "proline",
            "G": "proline",
        },
        "A": {
            "U": "histidine",
            "C": "histidine",
            "A": "glutamine",
            "G": "glutamine",
        },
        "G": {
            "U": "arginine",
            "C": "arginine",
            "A": "arginine",
            "G": "arginine",
        }
    },
    "A": {
        "U": {
            "U": "isoleucine",
            "C": "isoleucine",
            "A": "isoleucine",
            "G": "methionine",
        },
        "C": {
            "U": "threonine",
            "C": "threonine",
            "A": "threonine",
            "G": "threonine",
        },
        "A": {
            "U": "asparagine",
            "C": "asparagine",
            "A": "lysine",
            "G": "lysine",
        },
        "G": {
            "U": "serine",
            "C": "serine",
            "A": "arginine",
            "G": "arginine",
        }
    },
    "G": {
        "U": {
            "U": "valine",
            "C": "valine",
            "A": "valine",
            "G": "valine",
        },
        "C": {
            "U": "alanine",
            "C": "alanine",
            "A": "alanine",
            "G": "alanine",
        },
        "A": {
            "U": "aspartic acid",
            "C": "aspartic acid",
            "A": "glutamic acid",
            "G": "glutamic acid",
        },
        "G": {
            "U": "glycine",
            "C": "glycine",
            "A": "glycine",
            "G": "glycine",
        }
    },
}

amino_acid_abbreviation = {
    "alanine": "Ala",
    "arginine": "Arg",
    "asparagine": "Asn",
    "aspartic acid": "Asp",
    "cysteine": "Cys",
    "glutamic acid": "Glu",
    "glutamine": "Gln",
    "glycine": "Gly",
    "histidine": "His",
    "isoleucine": "Ile",
    "leucine": "Leu",
    "lysine": "Lys",
    "methionine": "Met",
    "phenylalanine": "Phe",
    "proline": "Pro",
    "serine": "Ser",
    "stop": "Stop", # I changed STOP to stop/Stop.
    "threonine": "Thr",
    "tryptophan": "Trp",
    "tyrosine": "Tyr",
    "valine": "Val"
}

# Ended up being useless right now, but may still be necessary later.
# list_of_amino_acids = [
#     "alanine",
#     "arginine",
#     "asparagine",
#     "aspartic acid",
#     "cysteine",
#     "glutamic acid",
#     "glutamine",
#     "glycine",
#     "histidine",
#     "isoleucine",
#     "leucine",
#     "lysine",
#     "methionine",
#     "phenylalanine",
#     "proline",
#     "serine",
#     "threonine",
#     "tryptophan",
#     "tyrosine",
#     "valine"
# ]


# Program used for calculating the "amino_acid_to_codon" dictionary:
# for x in ["U", "C", "A", "G"]:
#     for y in ["U", "C", "A", "G"]:
#         for z in ["U", "C", "A", "G"]:
#             amino_acid_to_codon[codon_table[x][y][z]].append(x + y + z)
# print(amino_acid_to_codon)
amino_acid_to_codon = {
    "alanine": ["GCU", "GCC", "GCA", "GCG"],
    "arginine": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "asparagine": ["AAU", "AAC"],
    "aspartic acid": ["GAU", "GAC"],
    "cysteine": ["UGU", "UGC"],
    "glutamic acid": ["GAA", "GAG"],
    "glutamine": ["CAA", "CAG"],
    "glycine": ["GGU", "GGC", "GGA", "GGG"],
    "histidine": ["CAU", "CAC"],
    "isoleucine": ["AUU", "AUC", "AUA"],
    "leucine": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
    "lysine": ["AAA", "AAG"],
    "methionine": ["AUG"],
    "phenylalanine": ["UUU", "UUC"],
    "proline": ["CCU", "CCC", "CCA", "CCG"],
    "serine": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
    "stop": ["UAA", "UAG", "UGA"], # I changed "STOP" to "stop" TODO: change it in other dna/mrna python files
    "threonine": ["ACU", "ACC", "ACA", "ACG"],
    "tryptophan": ["UGG"],
    "tyrosine": ["UAU", "UAC"],
    "valine": ["GUU", "GUC", "GUA", "GUG"]
}

class AminoAcidCodonCombinations:
    amino_acids = None
    counter_max = None
    counter = None
    overflow = False

    def __init__(self, amino_acids):
        self.amino_acids = amino_acids
        self.counter_max = [len(amino_acid_to_codon[amino_acid]) for amino_acid in amino_acids]
        self.counter = [0 for _ in amino_acids]
    
    def zero(self):
        for i in range(len(self.counter)):
            self.counter[i] = 0
    
    def next(self):
        self.overflow = False
        self.counter[0] += 1
        for i in range(len(self.counter)):
            if self.counter[i] >= self.counter_max[i]:
                if i+1 >= len(self.counter):
                    self.overflow = True
                    self.counter[i] = 0
                    break
                self.counter[i+1] += 1
                self.counter[i] = 0
    
    def interpret(self):
        sequence = []
        for i in range(len(self.counter)):
            sequence.append(amino_acid_to_codon[self.amino_acids[i]][self.counter[i]])
        return sequence
    
    def num_of_combos_iterate(self):
        num_of_combos = 0
        self.zero()
        while self.counter != [x-1 for x in self.counter_max]:
            num_of_combos += 1
            self.next()
        num_of_combos += 1
        return num_of_combos
    
    def num_of_combos_calculate(self):
        product = 1
        for value in self.counter_max:
            product *= value
        return product
    
    def all(self):
        num_of_combos = 0
        self.zero()
        while self.counter != [x-1 for x in self.counter_max]:
            num_of_combos += 1
            print(str(self.interpret())[1:-1].replace("'", ""), self.counter)
            self.next()
        num_of_combos += 1
        print(str(self.interpret())[1:-1].replace("'", ""), self.counter)
        print(f"Number of combinations: {num_of_combos}")

def main():
    amino_acids = input("Enter amino acid sequence: ").lower().split("/ ")
    #amino_acids = "Leucine/ Histidine/ Lysine/ Glutamic Acid/ Threonine".lower().split("/ ") # for debugging
    print(amino_acids, len(amino_acids))
    for amino_acid in amino_acids:
        print(f"{amino_acid_abbreviation[amino_acid]}: {str(amino_acid_to_codon[amino_acid])[1:-1].replace("'", "")}; {len(amino_acid_to_codon[amino_acid])}")
    print()

    # It's a counter!
    # Leu: UUA, UUG, CUU, CUC, CUA, CUG
    # His: CAU, CAC
    # Lys: AAA, AAG
    # Glu: GAA, GAG
    # Thr: ACU, ACC, ACA, ACG

    # [0,0,0,0,0]
    # [1,0,0,0,0]
    # [2,0,0,0,0]
    # [3,0,0,0,0]
    # [4,0,0,0,0]
    # [5,0,0,0,0]
    # [0,1,0,0,0]
    # [1,1,0,0,0]
    # [2,1,0,0,0]
    #    . . .
    # [5,1,0,0,0]
    # [0,0,1,0,0]
    # It carries over!!!
    print("Possible combinations:")
    combos = AminoAcidCodonCombinations(amino_acids)
    combos.all()


if __name__ == "__main__":
    main()