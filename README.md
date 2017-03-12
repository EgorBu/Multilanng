# Multilanng
Python simple multi-language module.  
Focus on be easy to use.  
Work in Windows and Linux, probably on Mac, as multilanng is Python based.  

Warning: Still in early alpha, only support 2 languages  


## How to use
Import the library multilanng
Choose a file to store translations (will be created if missing):  
You can set whatever path you want, until your program have the permissions to write at that path.  

In your program, you call the static methed "Multilanng.getDumbTranslation(key)" that return the translatoin of the key that you will configure next.  
I recommend to rename that method by something short as "_", that will enable to make something like "print(_("welcome"))"  
Call "Multilanng.saveTrads()" at the end of your program to use the interactive mode, and translate missing strings.  
You can delete that call for release your program, or just set the mode on "Multilanng.setTradsFile(file,mode="dev")" to "release" or delete the kw-argument 'mode="dev"' to hide the interactive mode and don't let users see it. 

## Example 
(try it by launching multilanng.py with python):  

~~~
import multilanng
Multilanng.defineLanguages({"fr":0,"en":1}) # if needed, change the name of the langs for interactive mode (default are these ones, so that call is useless here)

Multilanng.setTradsFile("jsonSave.json", mode="dev")
# Set mode to "realease" or delete that args to disable interactive mode

_ = Multilanng.getDumbTranslation
# Set a shortcut to that static method

Multilanng.setLanguage("fr")
print(_("hello")+" "+_("world"))

Multilanng.setLanguage("en")
print('{0} {1}'.format(_("hello"), _('world')))

Multilanng.saveTrads()  # if mode != "dev" : do nothing!
~~~

## Interactive mode
The "Multilanng.saveTrads()" will display an intercative mode if executed on the "dev" mode.  
It will ask the translation of strings that wasn't translated yet.  
Simply type the translations for the key system ask.

### Exemple
Try by executing multilanng.py itself if you delete or empty "jsonSave.json":
~~~
[No translation for 'hello'] [No translation for 'world']                                                             [No translation for 'hello'] [No translation for 'world']                                                                                                                                                                       --Multilanng interactive Mode--                                                                                   Translation fr of [hello] : bonj   <--our input is 'bonj'                                                         Translation en of [hello] : hi                                                                                      Translation fr of [world] : monde                                                                                 Translation en of [world] : world  
~~~

New execution will produce: 
~~~
bonj monde
hi world

--Multilanng interactive Mode--
Everything well translated
~~~
