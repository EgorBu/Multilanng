# Python simple Multilanng module.
# Still in alpha, work only with 2 differents languages
# Only use with 'interface' data, do not use with user input

import json
import __future__  

try:
    from builtins import input
except Exception as e:
    print (str(e)+"\n\n")
    print ("On python2 you need to install 'future' package in order to get 'builtins'")
    print ("Try : pip install future")
    print ("or : (may be 'python2' or 'py -2') -m pip install future")
    print ("also consider the use of argument '--user' to avoid using pip as sudo")
    exit()


class Multilanng: 
    instance = None
    filenameTrads = None
    trads = {} #{"hello":["bonjour","hi"],"world":["monde","world"]}
    lang = 0
    LANG = {"fr":0,"en":1}
    missingTranslations = []
    
    interactiveMode = False   # interactive Mode : if program ask for translations at the end
    
    
    @staticmethod
    def defineLanguages(langs):
        Multilanng.LANG = langs
        
    @staticmethod
    def setTradsFile(fn,mode= "release"):
        Multilanng.interactiveMode = (mode == "dev")
        try:
            f = open(fn,"r")
            s = f.read()
            f.close()
            Multilanng.trads = json.loads(s) #converting json to python
                        
        except Exception :
            #no file or empty
            pass
        
        Multilanng.filenameTrads = fn
        
    @staticmethod
    def setLanguage(language):
        try: Multilanng.lang = Multilanng.LANG[language]
        except KeyError : 
            print(language+ " is not supported")
            exit()
    
    @staticmethod
    def getInstance():
        if(Multilanng.instance == None):
            Multilanng.instance = Multilanng()
        return(Multilanng.instance)
    
    @staticmethod
    def getDumbTranslation(s):
        try: res = Multilanng.trads[s][Multilanng.lang]
        except KeyError : 
            res = "[No translation for '"+s+"']"
            Multilanng.addMissingTranslation(s)
        return(res)
    
    @staticmethod
    def addMissingTranslation(s):
        if(s not in Multilanng.missingTranslations):
            Multilanng.missingTranslations.append(s)
    
    @staticmethod
    def saveTrads():
        
        if(Multilanng.interactiveMode == True):
            print ("\n--Multilanng interactive Mode--")
            
            if(len(Multilanng.missingTranslations) == 0): 
                print ("Everything well translated")
            
            langs = list(Multilanng.LANG.keys())
            l0 = langs[0]
            l1 = langs[1]
            
            res = "{\n"
            for i,t in enumerate(Multilanng.missingTranslations):
                s1 = input("Translation "+l0+" of ["+t+"] : ")
                s2 = input("Translation "+l1+" of ["+t+"] : ")
                
                res += "\t\""+t+"\": [\""+s1+"\",\""+s2+"\"]"
                if( i < len(Multilanng.missingTranslations)-1 or len(Multilanng.trads)>0):
                    res += ","
                    res += "\n"
            
            for i, t in enumerate(Multilanng.trads):
                t1 = str(Multilanng.trads[t][0])
                t2 = str(Multilanng.trads[t][1])
                res += "\t\""+t+"\": [\""+t1+"\",\""+t2+"\"]"
                if(i < len(Multilanng.trads)-1):
                    res += ","
                res += "\n"
            
            res += "}\n"
            
            with open(Multilanng.filenameTrads, 'w') as f:
                f.write(res)

if __name__ == "__main__": 
    
    #import multilanng
    Multilanng.defineLanguages({"fr":0,"en":1})
    Multilanng.setTradsFile("jsonSave.json", mode="dev")
    
    _ = Multilanng.getDumbTranslation
    
    Multilanng.setLanguage("fr")
    print(_("hello")+" "+_("world"))
    
    Multilanng.setLanguage("en")
    print('{0} {1}'.format(_("hello"), _('world')))
    
    Multilanng.saveTrads()