#  ax^3 + bx^2 + cx^1 + dx^0 = 0
import numpy as np
a=int(input("Cofficient OF x^3 : "));
b=int(input("Cofficient OF x^2 : "));
c=int(input("Cofficient OF x^1 : "));
d=int(input("Cofficient OF x^0 : "));

for x in np.arange(100,-101,-0.1):
        if(int((a*(x**3))+(b*(x**2))+(c*(x))+(d))==0):
            y="{:.2f}".format(x)
            print(y);

print("These Equation is having root's in Fraction or complex number");

# today i don't have anything to write because it's math's  ¯\_(ツ)_/¯
#   so today Small BYe-Bye


