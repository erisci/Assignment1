dna_fragment = input("Plese write the fragment for G/C analysis \n")
GC_value = (dna_fragment.count("C") + dna_fragment.count("G")/len(dna_fragment))

dna_fragment2 = input("Please write another fragment for G/C analysis \n")
GC_vae2 = (dna_fragment.count("C") + dna_fragment2.count("G")/len(dna_fragment2))

print("Please wait for a while for the C/G value anaylis!")

between_value = (GC_value/GC_value2)
print("This is the G/C ratio between the organisms " + str(between_value))
if between_vale >= 10:
    print("These organisms are closely related")
elif (betwn_value < 10) and (between_value >= 5):
    print("These organisms are somewhat related")
else:
    print("These organisms are not related")