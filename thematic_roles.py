import defs, Global

POS = Global.POS
null = "_none_"

class agent:

    def __init__(self, words):
        self.det, self.descriptors, self.core = null, [], null
        for word in words:
            pos = word.POS
            if pos == POS.det: self.det = word
            elif pos == POS.adj: self.descriptors.append(word)
            elif pos == POS.noun: self.core = word

    def __str__(self):        
        s = "Agent: \n"

        if self.det == null: s += "Determiner: none given\n"
        else: s += ("Determiner: " + self.det.val + "\n")

        if len(self.descriptors) == 0: s += "Descriptors: none given\n"
        else:
            desc_strs = [desc.val for desc in self.descriptors]
            s += ("Descriptors: " + ", ".join(desc_strs) + "\n")

        s += "Core: none given" if self.core == null else ("Core: " + self.core.val)
        return s

    def __repr__(self):
        return str(self)


class action:

    def __init__(self, words):
        self.descriptors, self.core = [], null
        for word in words:
            pos = word.POS
            if pos == POS.adv: self.descriptors.append(word)
            elif pos == POS.verb: self.core = word

    def __str__(self):
        s = "Action: \n"

        if len(self.descriptors) == 0: s += "Descriptors: none given\n"
        else:
            desc_strs = [desc.val for desc in self.descriptors]
            s += ("Descriptors: " + ", ".join(desc_strs) + "\n")

        s += "Core: none given" if self.core == null else ("Core: " + self.core.val)
        return s

    def __repr__(self):
        return str(self)


#always check whether a theme's isnp field is true or not!
#need to treat it differently depending!
class theme:

    def __init__(self, words):
        self.det, self.descriptors, self.core = null, [], null
        self.isnp = False

        for word in words:
            pos = word.POS
            if pos == POS.det or POS.noun: 
                self.isnp = True
                break
        
        if self.isnp:
            self.core = null
            for word in words:
                pos = word.POS
                if  pos == POS.det: self.det = word
                elif pos == POS.adj: self.descriptors.append(word)
                elif pos == POS.noun: self.core = word

        else:
            self.core = []
            for word in words:
                pos = word.POS
                if pos == POS.adj: self.core.append(word)

    def __str__(self):
        s = "Theme: \n"

        if self.isnp:
            if self.det == null: s += "Determiner: none given"
            else: s += ("Determiner: " + self.det.val + "\n")

            if len(self.descriptors) == 0: s += "Descriptors: none given\n"
            else:
                desc_strs = [desc.val for desc in self.descriptors]
                s += ("Descriptors: " + ", ".join(desc_strs) + "\n")

            s += "Core: none given" if self.core == null else ("Core: " + self.core.val)
        else:
            core_strs = [core.val for core in self.core]
            s += ("Core: " + ", ".join(core_strs))

        return s
        
    def __repr__(self):
        return str(self)

            
    
