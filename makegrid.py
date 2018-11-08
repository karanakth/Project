import numpy as np
import atomic_data
import sys


def makegrid(x,y,z,atom_l,ngridpoints):
    atoms = []
    for i in range(len(atom_l)):
        atoms.append(atomic_data.vdW(atom_l[i]))
                  
    atoms = np.array(atoms)
    x_max = np.max(x + atoms)
    x_min = np.max(x - atoms)

    y_max = np.max(y + atoms)
    y_min = np.max(y - atoms)

    z_max = np.max(z + atoms)
    z_min = np.max(z - atoms)

    # Make linspace
    X = np.linspace(x_min,x_max,ngridpoints)
    Y = np.linspace(y_min,y_max,ngridpoints)
    Z = np.linspace(z_min,z_max,ngridpoints)

    XX,YY,ZZ = np.meshgrid(X,Y,Z)

    return XX,YY,ZZ

def wavefunc_one_s(x,y,z):
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    ngrid_points = 80
    stepsize = 0.1
    Z = 1
    a = 5.291772*10**-11  # m
    sqrtpi = 1.7724
    c = 1/sqrtpi*(Z/a)**(3/2)
    r = np.sqrt(x**2+y**2+z**2)*10**(-11) # m
    outfile = open('out','w')
    outfile.write('CPMD CUBE FILE. \nOUTER LOOP: X, MIDDLE LOOP: Y, INNER LOOP: Z')
    outfile.write('\n %g  0.000000    0.000000    0.000000' % (len(x)))
    outfile.write('\n %g  %g    0.000000    0.000000' % (ngrid_points,stepsize))   
    outfile.write('\n %g  0.000000    %g    0.000000' % (ngrid_points,stepsize))
    outfile.write('\n %g  0.000000    0.000000    %g' % (ngrid_points,stepsize))
    outfile.write('\n {} ' .format(np.array(r)))
                

# write cube file

        

#def wavefunc_two_p(x,y,z):
    #return x**2
    # call makegrid
    # call subroutine in veloxchem to get density 
    # print cube file to filename
    
        
#if __name__ == ' __main__':
 #   x = np.array([6,1,-3,-3.2,6.1])
 #   y = np.array([6,1,-3,-3.2,6.1])
 #   z = np.array([6,1,-3,-3.2,6.1])
 #   atom_l = ['Rn', 'O', 'O','Rn','C']
 #   print makegrid(x,y,z,atom_l)
#else:
    
    
    	 

#x = np.array([6,1,-3,-3.2,6.1])
#y = np.array([6,1,-3,-3.2,6.1])
#z = np.array([6,1,-3,-3.2,6.1])
#atom_l = ['Rn', 'O', 'O','Rn','C']

#Test case 1 - Only hydrogen atom
x = np.array([0])
y = np.array([0])
z = np.array([0])
atom_l = ['H']

xx,yy,zz = makegrid(x,y,z,atom_l,80)
#print(xx)
#print(xx.shape)

L = wavefunc_one_s(xx,yy,zz)

#print(L)

#l = (xx+yy+zz)
#print(l)
#print(yy)
#print(zz)
