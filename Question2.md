# Didem's Answer to Question 2

Please assign variables to the individual components of your favorite gene! (e.g.
promoter, 5' UTR, start codon, exon1, intron, exon2, stop codon, 3' UTR). Print the entire gene
by using the string concatenation operator, on the standard output! Note: Feel free to create a
fictional gene sequence by randomly filling in the gene components by the characters
corresponding to individual nucleotide bases

promotor= "TTA GCAAATCGGAAATTTTAGCTT"
5_prime_UTR = "AAAAAAATTTTGGGGGGGGGGGGG"
start_kodon="ATG"
exon1="GCATAAAATGCTATAAAATT"
apoe_gene=AAATTTGCCCCAAATTTG
vegfa_gene= "GSCCSGAATTT"
esrı_gene= "ATGSSTTTGCATGSAC"
exon2="AGGCCTTAAGACCCG"
stop-codon="TGA"
3_prime_UTR="TTTTTTAAAAAAAAAAAAA"

my_fav_gene = promoter + 5_prime_UTR + start_kodon + exon1 + apoe_gene + vegfa_gene + esrı_gene + exon2 + stop-codon + 3_prime_UTR

print("My favourite gene sequence is as follows:")
print(my_fav_gene)

