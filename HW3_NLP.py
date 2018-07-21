import nltk
from nltk import *
from collections import Counter



my_grammer_test = nltk.CFG.fromstring("""
  S -> NP VP | VP 
  NP -> Prop | Det PP N |  ADJ N | Prop N | ADJ N ADV 
  VP -> V NP | V NP NP | V PP | MD VP | V ADV PP | V ADV | AUX NP
  PP -> P NP | P VP | ADV ADJ | ADJ N | ADJ
  AUX -> "had"
  V -> "came" | "go" | "visit"  | "are" | "am" | "went" | "meet" | "is"
  ADJ -> "nice" | "naive" | "two" | "good" | "three" | "greatest"
  ADV -> "ago" | "now" | "not" | "always"
  Prop -> "We" | "She" | "You" | "Their" | "me" | "I" | "John" | "Maria" | "Rock"
  Det -> "a" | "the"
  MD -> "may"
  N -> "party" | "yesterday" | "kids" | "days" | "person" | "years" | "WWE" | "champion"
  P -> "to" 
  """)

rd_parser = nltk.RecursiveDescentParser(my_grammer_test)
sent1 = 'We had a nice party yesterday'.split()
sent2 = 'She came to visit me two days ago'.split()
sent3 = 'You may go now'.split()
sent4 = 'Their kids are not always naive'.split()
extra1 = 'Rock is the greatest WWE champion'.split()
extra2 = 'John went to meet Maria three years ago'.split()
extra3 = 'I am a good person'.split()
sense1 = 'John meet to Maria'.split()
print("Testing begins")
print("Sentence 1")
for tree in rd_parser.parse(sent1):
	print (tree)
print("Sentence 2")
for tree in rd_parser.parse(sent2):
	print (tree)
print("Sentence 3")
for tree in rd_parser.parse(sent3):
	print (tree)
print("Sentence 4")
for tree in rd_parser.parse(sent4):
	print (tree)
print("Extra 1")
for tree in rd_parser.parse(extra1):
	print (tree)
print("Extra 2")
for tree in rd_parser.parse(extra2):
	print (tree)
print("Extra 3")
for tree in rd_parser.parse(extra3):
	print (tree)
print("Sense less Sentence")
for tree in rd_parser.parse(sense1):
	print (tree)

file_content = open("/Users/rishi/Desktop/HW3_corpus.txt").read()
tokens = nltk.word_tokenize(file_content)
print (tokens)

print(Counter(tokens))

# As the frequency of each word is only one time the probability of a words are equal

prob_grammar_prac = nltk.PCFG.fromstring("""
  S -> NP VP [0.9]| VP  [0.1]
  VP -> TranV NP [0.17]| TranV NP NP [0.166] | TranV VP[0.166]
  VP -> InV ADV [0.166]
  VP -> DatV ADV PP [0.166]| DatV PP [0.166]
  PP -> P NP [0.5] | P VP [0.3]| ADV ADJ [0.2]
  TranV -> "visit" [0.34] | "had" [0.33] | "may" [0.33]
  InV -> "go" [1.0] 
  DatV -> "came" [0.5] | "are"[0.5]
  NP -> Prop [0.4]| Det ADJ N N [0.25]|  ADJ N [0.15]| Prop N [0.1]| ADJ N ADV[0.1]
  ADJ -> "nice" [0.34] | "naive" [0.33] | "two" [0.33]
  ADV -> "ago" [0.25] | "now" [0.25] | "not" [0.25] | "always" [0.25]
  Prop -> "We" [0.2] | "She" [0.2] | "You" [0.2] | "Their" [0.2] | "me" [0.2]
  Det -> "a" [1.0] 
  N -> "party" [0.25] | "yesterday" [0.25] | "kids" [0.25] | "days" [0.25]
  P -> "to" [1.0]
  """)

print("Probabilistic CFG")

viterbi_parser = nltk.ViterbiParser(prob_grammar_prac)
print("Sentence 1")
for tree in viterbi_parser.parse(['We', 'had', 'a', 'nice', 'party', 'yesterday']):
    print (tree)
print("Sentence 2")
for tree in viterbi_parser.parse(['She', 'came', 'to', 'visit', 'me', 'two', 'days', 'ago']):
    print (tree)
print("Sentence 3")
for tree in viterbi_parser.parse(['You', 'may', 'go', 'now']):
    print (tree)
print("Sentence 4")
for tree in viterbi_parser.parse(['Their', 'kids', 'are', 'not', 'always', 'naive']):
    print (tree)


