from parcelfile import wrap
#functions for the command "wrap" are still under construction, so they may not work to well.
#def wrap(type=any, spacing:Bool=any, *args) -> str
#wrap takes multiple arguments and combines them

#===pre defined literals:
#STR = str()
#INT = int()                                                                                         combination of literals
#BOOL = bool()                                                                                             V    V
#MULTI = None #used for other combinations of values, such as "wrap(type=MULTI, spacing=True, "hello", "world", 27, True)
#FLOAT = float()

text = wrap(type=STR, spacing=True, "hello,", "Pythonista!") #text accepted as *args
#if "spacing = True", parcelfile automatically adds spacing beetween the args 

print(text) #this should output "hello, Pythonista"
