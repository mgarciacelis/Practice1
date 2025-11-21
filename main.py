#1 Area of a Circle
radius = float(input("Radius: "))
from math import pi 
area = round(pi * radius**2, 4)
def circ_area(r):
    return round(pi * r**2, 4)
print("Area: " + str(area))
area = circ_area(radius)

#2 Expression Solver
a=int(input("what is the value for a?"))
b=int(input("what is the value for b?"))
print("Let's solve for (a-b)+(a*b):")
answer=(a-b)+(a*b)
print("Answer:"+str(answer))

#3 ASCII Art
print("ASCII art display here!")
which_art=input("Do you want to see art#1 or art#2:")
if which_art == "1":
    print('''    
`;-.          ___,
  `.`\_...._/`.-"`
    \        /      ,
    /()   () \    .' `-._
   |)  .    ()\  /   _.'
   \  -'-     ,; '. <
    ;.__     ,;|   > \
   / ,    / ,  |.-'.-'
  (_/    (_/ ,;|.<`
    \    ,     ;-`
     >   \    /
    (_,-'`> .'
   (_,   (_,    
          ''')
else:
    print(''' 
    _______
   /      /,
  /      //
 /______//
(______(/
          ''')