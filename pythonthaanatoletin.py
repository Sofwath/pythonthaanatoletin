# coding: utf8


letin=[" ","","h","hs","n","r","b","hl","k","v","m","f","dh","th","l","g","ng","s","d","j","hc","z","t","p","y","tt","h","h","dh","s","s","t","t̤","g","q","a","aa","i","ee","u","oo","e","ye","o","ao",""]
thaana=[" ","އ","ހ","ށ","ނ","ރ","ބ","ޅ","ކ","ވ","މ","ފ","ދ","ތ","ލ","ގ","ޏ","ސ","ޑ","ޖ","ޗ","ޒ","ޓ","ޕ","ޔ","ޘ","ޙ","ޚ","ޛ","ޝ","ޞ","ޟ","ޠ","ޣ","ޤ"," ަ"," ާ"," ި"," ީ"," ު"," ޫ"," ެ"," ޭ "," ޮ"," ޯ"," ް"]

exceptions=["އަ","އާ","އި","އީ","އު","އޫ","އެ","އޭ","އޮ","ޢަ","ޢާ","ޢި","ޢީ","ޢު","ޢޫ","ޢެ","ޢޭ","ޢޮ", "އޯ", "ުއް", "ިއް",  "ެއް", "ަށް", "ައް", "ށް","ތް", "ާއް","އް","އް"]

expfix=["a","aa","i","ee","u","oo","e","ey","o","a","aa","i","ee","u","oo","e","ey","o","oa","uh","ih","eh","ah","ah","h","i","aah","ih","h"]

str=u'ހުރިހާ އިންސާނުން ވެސް އުފަންވަނީ، ދަރަޖައާއި ޙައްޤުތަކުގައި މިނިވަންކަމާއި ހަމަހަމަކަން ލިބިގެންވާ ބައެއްގެ ގޮތުގައެވެ. އެމީހުންނަށް ހެޔޮވިސްނުމާއި، ހެޔޮ ބުއްދީގެ ބާރު ލިބިގެންވެއެވެ. އަދި އެމީހުން އެކަކު އަނެކަކާ މެދު މުޢާމަލާތް ކުރަންވަނީ، އުޚުއްވަތްތެރި ކަމުގެ ރޫޙެއްގައެވެ. ' #[::-1]


def latin(str):
    excp=""
    akuru=""
    message=""
    alifex=False

    it = iter(xrange(0,len(str)))
    for i in it:
        try :
            s=(str[i].encode("utf-8"))
            nexts=(str[i+1].encode("utf-8"))
        except IndexError:
            pass

        for j in range(0,len(thaana)):
            if (s==" "):
                message+=" "
                break
	    akuru=thaana[j].replace(" ","")
            exindex = [exceptions.index(i) for i in exceptions if ((s+nexts)) ==  i]
            # check for exceptions 
            if exindex:
                if ((exceptions[exindex[0]])==(s+nexts)):
                    alifex=True
            if (alifex==True):
                message+=expfix[exindex[0]] # exceptions
                break
            elif (akuru==s):
                message+=letin[j]  # normal mappings
                break

        if (alifex==True):
            alifex=False
            i=next(it) # skip iteration in main loop if exception 


    return message #[::-1]

print str
print latin(str)
