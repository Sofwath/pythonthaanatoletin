# coding: utf8


letin=[" ","","h","hs","n","r","b","hl","k","v","m","f","dh","th","l","g","ng","s","d","j","hc","z","t","p","y","tt","h","h","dh","s","s","t","t̤","g","q","a","aa","i","ee","u","oo","e","ye","o","ao","","ﷲ"]
thaana=[" ","އ","ހ","ށ","ނ","ރ","ބ","ޅ","ކ","ވ","މ","ފ","ދ","ތ","ލ","ގ","ޏ","ސ","ޑ","ޖ","ޗ","ޒ","ޓ","ޕ","ޔ","ޘ","ޙ","ޚ","ޛ","ޝ","ޞ","ޟ","ޠ","ޣ","ޤ"," ަ"," ާ"," ި"," ީ"," ު"," ޫ"," ެ"," ޭ "," ޮ"," ޯ"," ް","ﷲ"]

exceptions=["އަ","އާ","އި","އީ","އު","އޫ","އެ","އޭ","އޮ","ޢަ","ޢާ","ޢި","ޢީ","ޢު","ޢޫ","ޢެ","ޢޭ","ޢޮ", "އޯ", "ުއް", "ިއް",  "ެއް", "ަށް", "ައް", "ށް","ތް", "ާއް","އް","އް","ﷲ"]
expfix=["a","aa","i","ee","u","oo","e","ey","o","a","aa","i","ee","u","oo","e","ey","o","oa","uh","ih","eh","ah","ah","h","i","aah","ih","h","ﷲ"]

symbols = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '؟', '#', '$', ')', '/','1','2','3','4','5','6','7','8','9','0']
symbolsrev = ['~', ':', "'", '+', '[', '/', '@', '^', '}', '%', '(', '-', '"', '*', '|', ',', '&', '>', '`', '{', '.', '_', '=', '[', '!', '<', ';', '?', '#', '$', ')', '\\','1','2','3','4','5','6','7','8','9','0']


str=u'ބަޖެޓްގައިވާ ޚަރަދުގެ ތަފްސީލަށް ބަލާއިރު ކެޕިޓަލް ހަރަދުގެ އެންމެ ބޮޑު ބައެއް (12 ބިލިއަން) ހޭދަވާނީ އިޖްތިމާއީ ތަރައްގީއަށެވެ. އަދި ރައްޔިތުންނަށް ދޭ އާންމު ހިދުމަތްތަކަށް 7.8 ބިލިއަން ރުފިޔާ ހޭދަވާނެ އެވެ. ދަރަނީގެ ހިދުމަތާއި ދަރަނި އަދާކުރުމަށް 2.6 ބިލިއަން ރުފިޔާ ބަޖެޓްގައި ހިމަނާފައިވާ އިރު، އިގްތިސާދީ ތަރައްގީ އަށް 4.4 ބިލިއަން ރުފިޔާ ހޭދަވާނެ އެވެ.' 


def latin(str):
    akuru=""
    message=""
    alifex=False

    it = iter(xrange(0,len(str)))
    for i in it:
        try :
            s=(str[i].encode("utf-8")).strip()
            two=(str[i:+2].encode("utf-8"))
            three=(str[i:i+3].encode("utf-8"))
        except IndexError:
            pass

        for j in range(0,len(thaana)):
            if (s==" "):
                message+=" "
                break
	    akuru=thaana[j].replace(" ","")
            exindex = ([exceptions.index(i) for i in exceptions if ((two) or (three)) ==  i])
            # check for exceptions 
            if exindex:
                if ((exceptions[exindex[0]]==(two)) or (exceptions[exindex[0]]==(three))):
                    alifex=True
            if (alifex==True):
                message+=expfix[exindex[0]] # exceptions
                break
            elif (akuru==s):
                message+=letin[j]  # normal mappings
                break
            else:
                try:
                    sb=symbols.index(s)
                except ValueError:
                    sb=None
                if sb:
                    message+=symbolsrev[sb]
                    break

        if (alifex==True):
            alifex=False
            i=next(it) # skip iteration in main loop if exception 


    return message

print str
print latin(str)
