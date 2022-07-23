#  ax^3 + bx^2 + cx^1 + dx^0 = 0
import numpy as np
a=int(input("Cofficient OF x^3 : "));
b=int(input("Cofficient OF x^2 : "));
c=int(input("Cofficient OF x^1 : "));
d=int(input("Cofficient OF x^0 : "));

for x in np.arange(1000,-1001,-1):
        if(int((a*(x**3))+(b*(x**2))+(c*(x))+(d))==0):
            if(x == 0) and a != 0 and b != 0 and c != 0:
                    
                    bita=((b)/a);
                    gama=(c/a);
                    print((-bita+(((((bita)**2)-4*gama))**(1/2)))/2,(-bita-(((((bita)**2)-4*gama))**(1/2)))/2,x);
                    exit();
            elif x!=0 and a != 0 and b != 0 and c != 0:
                    
                    bita=(((-b)/a)-x);
                    gama=((c/a)-(x*(bita)));
                    print((bita+(((((bita)**2)-4*gama))**(1/2)))/2,(bita-(((((bita)**2)-4*gama))**(1/2)))/2,x);
                    exit();
                    
for x in np.arange(1000,-1001,-0.1):
        if(int((a*(x**3))+(b*(x**2))+(c*(x))+(d))==0) and a != 0 and b != 0 and c != 0:
                
                    bita=(((-b)/a)-x);
                    gama=((c/a)-(x*(bita)));
                    print((bita+(((((bita)**2)-4*gama))**(1/2)))/2,(bita-(((((bita)**2)-4*gama))**(1/2)))/2,x);
                    exit();

for x in np.arange(1000,-1001,-0.01):
        if(int((a*(x**3))+(b*(x**2))+(c*(x))+(d))==0) and a != 0 and b != 0 and c != 0:
                
                    bita=(((-b)/a)-x);
                    gama=((c/a)-(x*(bita)));
                    print((bita+(((((bita)**2)-4*gama))**(1/2)))/2,(bita-(((((bita)**2)-4*gama))**(1/2)))/2,x);
                    exit();

        
if(a==0):
        
        print((-c+(((((c)**2)-(4*d*b)))**(1/2)))/(2*b),(-c-(((((c)**2)-(4*d*b)))**(1/2)))/(2*b));
        exit();       
                   
# today i don't have anything to write because it's math's  ¯\_(ツ)_/¯
#   so today Small BYe-Bye


