# python 2.7
dna = raw_input('Enter DNA sequence: ')
# python 3 use input() rather than raw_input()
print type(dna)

if len(dna) < 1 :  dna = 'acgctcgcgcggcgatagctgatcgatcggcgcgctttttttttaaaag'
no_c = dna.count('c') # number of 'c' in dna sequence
no_g = dna.count('g') # number of 'g' in dna sequence
dna_length = len(dna) # dna length
gc_percent = (no_c + no_g) * 100.0 / dan_length # gc percentage in dna sequence

# print ('The DNA sequence\'s GC content is', gc_percent, '%')
print ('The DNA sequence\'s GC content is %5.3f%%' % gc_percent)