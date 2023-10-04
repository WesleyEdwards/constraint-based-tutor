import nltk
from scaffolded_writing.cfg import ScaffoldedWritingCFG

# code taken from https://stackoverflow.com/questions/4972571/tool-for-drawing-parse-trees
def draw_parse_tree(grammar_string, sentence):
    # grammar = nltk.CFG.fromstring(grammar_string)
    grammar = ScaffoldedWritingCFG.fromstring(grammar_string)
    sentence = sentence.split()
    def parse(sent):
        #Returns nltk.Tree.Tree format output
        a = []
        parser = nltk.ChartParser(grammar)
        for tree in parser.parse(sent):
            a.append(tree)
        return a

    #Gives output as structured tree
    print(parse(sentence))

    #Gives tree diagrem in tkinter window
    # parse(sentence)[0].draw()
    for tree in parse(sentence):
        tree.draw()


outdoors_grammar = """
  S  -> NP VP
  NP -> Det Nom | PropN
  Nom -> Adj Nom | N
  VP -> V Adj | V NP | V S | V NP PP
  PP -> P NP
  PropN -> 'Buster' | 'Chatterer' | 'Joe'
  Det -> 'the' | 'a'
  N -> 'bear' | 'squirrel' | 'tree' | 'fish' | 'log'
  Adj  -> 'angry' | 'frightened' |  'little' | 'tall'
  V ->  'chased'  | 'saw' | 'said' | 'thought' | 'was' | 'put'
  P -> 'on'
"""
bear_chase_squirrel = 'the angry bear chased the frightened little squirrel'

# draw_parse_tree(outdoors_grammar, bear_chase_squirrel)

university_grammar = """
SENTENCE -> SUBJECT VERB_PHRASE OBJECT
SUBJECT -> 'This' | 'Computers' | 'I'
VERB_PHRASE -> ADVERB VERB | VERB
ADVERB -> 'never'
VERB -> 'is' | 'run' | 'am' | 'tell'
OBJECT -> 'the' NOUN | 'a' NOUN | NOUN
NOUN -> 'university' | 'world' | 'cheese' | 'lies'
"""

this_uni = 'This is a university'
comp_world = 'Computers run the world'
the_cheese = 'I am the cheese'
lies = 'I never tell lies'

# draw_parse_tree(university_grammar, this_uni)
# draw_parse_tree(university_grammar, comp_world)
# draw_parse_tree(university_grammar, the_cheese)
# draw_parse_tree(university_grammar, lies)

ds_grammar = """
    START -> "Use" "a" STUCTURE_TYPE REASON
    REASON -> "for" "efficient" OPERATION | EPSILON
    STUCTURE_TYPE -> "array" | "linked list" | "hash map" | "binary search tree"
    OPERATION -> "insertion" | "deletion" | "look" "up" | "memory usage"
    EPSILON ->
"""

# draw_parse_tree(ds_grammar, "Use a array for efficient look up")

if_then_grammar = """
    STATEMENT -> "if" CONDITION "then" STATEMENT | "if" CONDITION "then" STATEMENT "else" STATEMENT
    CONDITION -> "c1" | "c2"
    STATEMENT -> "s1" | "s2"
"""

draw_parse_tree(if_then_grammar, "if c1 then if c2 then s1 else s2")