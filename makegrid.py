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
    
    xstep = X[1]-X[0]
    ystep = Y[1]-Y[0]
    zstep = Z[1]-Z[0]

    XX,YY,ZZ = np.meshgrid(X,Y,Z)

    return XX,YY,ZZ,x_min,y_min,z_min,xstep,ystep,zstep
0.000000        
def wavefunc_one_s(x,y,z,ngrid_points,x_min,y_min,z_min,xstep,ystep,zstep):
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    IFLAG = 1
    Z = 1
    a = 5.291772*10**-11  # m
    sqrtpi = 1.7724
    c = 1/sqrtpi*(Z/a)**(3/2)
    r = np.sqrt(x**2+y**2+z**2)*10**(-11) # m
    #f = c*np.exp(-Z*r/a)
    f = (x**2+y**2+z**2)*10**-6
    outfile = open('out.cube','w')
    outfile.write(' Title Card Required Density=SCF\n')
    outfile.write(' Electron density from Total SCF Density\n')
    #outfile.write('CPMD CUBE FILE. \nOUTER LOOP: X, MIDDLE LOOP: Y, INNER LOOP: Z\n')
    outfile.write('    %g   %2.6g      %2.6g      %2.6g         1\n' % (IFLAG,x_min,y_min,z_min))
    outfile.write('   %g    %2.6g  0.000000   0.000000\n' % (ngrid_points,xstep))
    outfile.write('   %g    0.000000   %2.6g  0.000000\n' % (ngrid_points,ystep))
    outfile.write('   %g    0.000000   0.000000   %2.6g\n' % (ngrid_points,zstep))
    outfile.write('    1    1.000000   0.000000   0.000000    0.000000\n')
                  
    #outfile.write('\n %g  0.000000    0.000000    0.000000' % (len(x)))
    #outfile.write('\n %g  %g    0.000000    0.000000' % (ngrid_points,stepsize))   
    #outfile.write('\n %g  0.000000    %g    0.000000' % (ngrid_points,stepsize))
    #outfile.write('\n %g  0.000000    0.000000    %g' % (ngrid_points,stepsize))
    
    for i in range(len(x)):
        for j in range(len(y)):
            for l in range(len(z)):
                outfile.write(' %12.5E' % (f[i][l][j]))
                if  l %6 == 5:
                    outfile.write("\n")
            outfile.write("\n")    
    
               
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

xx,yy,zz,x_min,y_min,z_min,xstep,ystep,zstep = makegrid(x,y,z,atom_l,80)
#print(xx)
#print(xx.shape)

L = wavefunc_one_s(xx,yy,zz,80,x_min,y_min,z_min,xstep,ystep,zstep)

#print(L)

#l = (xx+yy+zz)
#print(l)
#print(yy)
#print(zz)
