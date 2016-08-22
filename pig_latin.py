'''
This program was written by Jon Scheaffer.

It prompts the user for a word, then translates that word into Pig Latin.
'''

print "Pig Latin Translator \n \n"

# prompts user for an English word
rawword = raw_input('Enter an English word: ')
origword = rawword.lower()

# checks to make sure word contains letters and at least one vowel
while not (origword.isalpha() or ('a' in origword or 'e' in origword or 'i' in origword or 'o' in origword or 'u' in origword)):
    print "\nThat is not a word."
    origword = raw_input('Try again, fucknut: ')

# finds the vowel in the world and sets its position to 'n'
n = 0
while n <= len(origword) and not origword[n] in 'aeiou':
    n = n + 1

#translates the word into pig latin
if n == 0:
    pigword = origword[1:len(origword)] + origword[0] + 'ay'
else:
    pigword = origword[n:len(origword)] + origword[0:n] + 'ay'

# displays the pig latin
print "The Pig Latin translation of %s is %s " % (origword, pigword)