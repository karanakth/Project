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

    numatoms = len(atom_l)
    
    # Evaluate the function
    Z = 1
    a = 5.291772*10**-11  # m
    sqrtpi = 1.7724
    c = 1/sqrtpi*(Z/a)**(3/2)
    r = np.sqrt(XX**2+YY**2+ZZ**2)*10**(-11) # m
    f = c*np.exp(-Z*r/a)
    #f = (XX**2+YY**2+ZZ**2)*10**-6
    
    
    # out put code
    outfile = open('out_two.cube','w')
    outfile.write(' Title Card Required Density=SCF\n')
    outfile.write(' Electron density from Total SCF Density\n')
    #outfile.write('CPMD CUBE FILE. \nOUTER LOOP: X, MIDDLE LOOP: Y, INNER LOOP: Z\n')
    outfile.write('%5d%12.6f%12.6f%12.6f%5d\n' % (numatoms,x_min,y_min,z_min,1))
    outfile.write('%5d%12.6f%12.6f%12.6f\n' % (ngridpoints,xstep,0,0))
    outfile.write('%5d%12.6f%12.6f%12.6f\n' % (ngridpoints,0,ystep,0))
    outfile.write('%5d%12.6f%12.6f%12.6f\n' % (ngridpoints,0,0,zstep))
    for oo in range(len(atom_l)):
         outfile.write('%5d%12.6f%12.6f%12.6f%12.6f\n' % (atomic_data.charge(atom_l[oo]),atomic_data.charge(atom_l[oo]),x[oo],y[oo],z[oo]))
   
    
    for i in range(len(XX)):
        for j in range(len(YY)):
            for l in range(len(ZZ)):
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
#x = np.array([0])
#y = np.array([0])
#z = np.array([0])
#atom_l = ['H']


#Test case 2 - Two hydrogen atoms
x = np.array([0,0])
y = np.array([0 ,0])
z = np.array([0.36741100,-0.36741100])
atom_l = ['H','H']


makegrid(x,y,z,atom_l,80)

#xx,yy,zz,x_min,y_min,z_min,xstep,ystep,zstep = makegrid(x,y,z,atom_l,80)
#print(xx)
#print(xx.shape)

#L = wavefunc_one_s(xx,yy,zz,80,x_min,y_min,z_min,xstep,ystep,zstep)

#print(L)

#l = (xx+yy+zz)
#print(l)
#print(yy)
#print(zz)
