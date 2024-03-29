
# parcelfile

Welcome to the official Parcelfile python package. Parcelfile was made to "Properly Package Python Programs".
Most parcelfile functions are under construction, so they __may not work__

> __PARCEL__ stands for: 
**P**ython 
**A**ranger with 
**R**enduring 
**C**omplex 
**E**lement 
**L**eafs

__Parcelfile__ is good for 
+ concatinating files
+ zipping files
+ seperating file contents
 _and much more!_

### Simple example
This is a simple example of what parcelfile can do.

```py
from parcelfile import wrap
wrapped_text = wrap
print(wrapped_text)
```

### Functions:
These are the functions that are available in __parcelfile__
#### wrap
``` py
def wrap( type=None, spacing=true, *args ) -> str
```
_wrap_ takes arguments and concatinates them.

#### box
```py
def box( file, int startline, int endline) -> any
```
_box_ takes file contents and seperates them from the main file, while creating a new file.

**examples are available in the ___examples___ directory**
&nbsp;
### DISCLAIMERS:
__Parcelfile__ is still under construction, so some functions may not work yet, and more are to come.

&nbsp;

_Creation rights go to __@malachi196__. You can find me on github, discord, and replit._
