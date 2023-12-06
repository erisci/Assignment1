# Doğa's Answer to Question 4
Write code that compares the GC ratios of two bacteria with known DNA sequences.


dna_fragment = input("Plese write the fragment for G/C analysis \n")
GC_value = (dna_fragment.count("C") + dna_fragment.count("G")/len(dna_fragment))

dna_fragment2 = input("Please write another fragment for G/C analysis \n")
GC_vae2 = (dna_fragment.count("C") + dna_fragment2.count("G")/len(dna_fragment2))

print("Please wait for a while for the C/G value anaylis!")

between_value = (GC_value/GC_value2)
print("This is the G/C ratio between the organisms " + str(between_value))
if (between_vale >= 9.5) and (between_value =< 1.2):
    print("These organisms are closely related")
elif (betwn_value =< 3) and (between_value >= 0.6):
    print("These organisms are somewhat related")
else:
    print("These organisms are not related")