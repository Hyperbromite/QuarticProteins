import sys

alphabet = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'a', 'b', 'c', 'd', 'e', 'f', '.', 'g', '!', 'h',
    'i', 'j', 'k', 'l', '?', 'm', 'n', 'o', 'p', 'q',
    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ',',
    ':', ';', '\'', '"', '(', ')', '<', '>', '#', '@',
    '$', '%', '*', '&', '^', '+', '-', '=', '/', '\\',
    '_', '[', ']', ' '
]

quartic = dict()
digitLeft = 0
digitCenter = 0
digitRight = 0
for character in alphabet:
    quartic[character] = f'{digitLeft}{digitCenter}{digitRight}'
    digitRight += 1
    if digitRight == 4:
        digitRight = 0
        digitCenter += 1
    if digitCenter == 4:
        digitCenter = 0
        digitLeft += 1

nucleicAcid = {
    '0': 'A',
    '1': 'T',
    '2': 'G',
    '3': 'C'
}

dna = dict()
for character, codeword in quartic.items():
    dna[character] = ''.join([nucleicAcid[digit] for digit in codeword])

codons = {
    'AAA': 'K',
    'AAT': 'N',
    'AAG': 'K',
    'AAC': 'N',
    'ATA': 'I',
    'ATT': 'I',
    'ATG': 'M',
    'ATC': 'I',
    'AGA': 'R',
    'AGT': 'S',
    'AGG': 'R',
    'AGC': 'S',
    'ACA': 'T',
    'ACT': 'T',
    'ACG': 'T',
    'ACC': 'T',
    'TAA': '*',
    'TAT': 'Y',
    'TAG': '*',
    'TAC': 'Y',
    'TTA': 'L',
    'TTT': 'F',
    'TTG': 'L',
    'TTC': 'F',
    'TGA': '*',
    'TGT': 'C',
    'TGG': 'W',
    'TGC': 'C',
    'TCA': 'S',
    'TCT': 'S',
    'TCG': 'S',
    'TCC': 'S',
    'GAA': 'E',
    'GAT': 'D',
    'GAG': 'E',
    'GAC': 'D',
    'GTA': 'V',
    'GTT': 'V',
    'GTG': 'V',
    'GTC': 'V',
    'GGA': 'G',
    'GGT': 'G',
    'GGG': 'G',
    'GGC': 'G',
    'GCA': 'A',
    'GCT': 'A',
    'GCG': 'A',
    'GCC': 'A',
    'CAA': 'Q',
    'CAT': 'H',
    'CAG': 'Q',
    'CAC': 'H',
    'CTA': 'L',
    'CTT': 'L',
    'CTG': 'L',
    'CTC': 'L',
    'CGA': 'R',
    'CGT': 'R',
    'CGG': 'R',
    'CGC': 'R',
    'CCA': 'P',
    'CCT': 'P',
    'CCG': 'P',
    'CCC': 'P'
}

if __name__ == '__main__':
    message = sys.argv[1]
    for character in message:
        codeword = quartic[character]
        codon = ''.join([nucleicAcid[digit] for digit in codeword])
        print(codons[codon], end='')
    print()
