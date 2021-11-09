#OOP method
class MadLib():
    adjective = ""
    noun = ""
    past_tense_verb = ""
    adverb = ""
    verb = ""
    
    def __init__(self,adjective,noun,past_tense_verb,adverb,verb):
        self.adjective = adjective
        self.noun = noun
        self.past_tense_verb = past_tense_verb
        self.adverb = adverb
        self.verb = verb
        
    def print_MadLib_class(self):
        print("Today I went to the zoo. I saw a" + self.adjective + self.noun + " jumping up and down in its tree. He "  + self.past_tense_verb + " through the large tunnel that led to its" + self.adjective + self.noun )
        print("I got peanuts and passed them through the cage to a gigantic gray" + self.noun + " towering above my head ")
        print("Feeding that animal made me hungry. I went to get a" + self.adjective +  " scoop of ice cream. It filled my stomach." )
        print("Afterwards I had to" + self.verb + " to catch our bus. When I got home I " + self.past_tense_verb + " my mom for a" + self.adjective + " day at the zoo.")
        
Game =MadLib(" pink", " Skittle"," smiled", " happily"," stretch")
Game.print_MadLib_class()
