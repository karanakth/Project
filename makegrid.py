import numpy as np
import atomic_data
import S_orb
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def makegrid(x,y,z,atom_l,ngridpoints):
    ## change to atom_radii, atomicdata
    #### Find dimensions of the box ####
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

    ##### Make linspace #####
    
    X = np.linspace(x_min,x_max,ngridpoints)
    Y = np.linspace(y_min,y_max,ngridpoints)
    Z = np.linspace(z_min,z_max,ngridpoints)
    
    ###### Make meshgrid  #####

    XX,YY,ZZ = np.meshgrid(X,Y,Z)
   
    #### Plot a grid for demonstration ###
    
    XV = np.linspace(x_min,x_max,12)
    YV = np.linspace(y_min,y_max,12)
    ZV = np.linspace(z_min,z_max,12)
    
    XXV,YYV,ZZV = np.meshgrid(XV,YV,ZV)        
    fig = plt.figure()

    ax = fig.add_subplot(111, projection = '3d')
    ax.scatter(XXV,YYV,ZZV, c='r', marker = 'o')

    plt.show()

    ###### Evaluate the function ######
    
    ##### Valance shell for hydrogens 6-31G 3 tight ####
    
    exponents = np.array([18.7311370,2.8253937,0.6401217])
    coeff = np.array([0.03349460 ,0.23472695, 0.81375733])
    
    f = np.zeros((ngridpoints,ngridpoints,ngridpoints))
    ff = np.zeros((ngridpoints,ngridpoints,ngridpoints))
    
    for i in range(len(exponents)):
        for l in range(len(atom_l)):
            m = coeff[i]*S_orb.S_orb(x[l],y[l],z[l],exponents[i],XX,YY,ZZ)
            print("index,atom")
            print(i,l)
            f += m 
            
    #### 1 loose  ####
    exponent =   0.1612778            
    coeffs =   1.0000000  
    for l in range(len(atom_l)):
        mm = coeffs*S_orb.S_orb(x[l],y[l],z[l],exponent,XX,YY,ZZ)
        ff += mm
        
        
    ####  Framework for p type Gaussians ###
    
    Exponents_c = np.array([3047.5249000, 457.3695100, 103.9486900,  29.2101550, 9.2866630, 3.1639270 ])
    coeffs_C = np.array([0.0018347,0.0140373, 0.0688426,0.2321844, 0.4679413,0.3623120 ])
                     
    
    
    #### Add inner and out shell ####
    
    f = f + ff
    
    ## square to get density ####
    
    f = f**2
    
          #### outfile code #### put it into a function
    outfile = open('out_two.cube','w')
    outfile.write(' Title Card Required Density=SCF\n')
    outfile.write(' Electron density from Total SCF Density\n')
    #outfile.write('CPMD CUBE FILE. \nOUTER LOOP: X, MIDDLE LOOP: Y, INNER LOOP: Z\n')
    outfile.write('%5d%12.6f%12.6f%12.6f%5d\n' % (len(atom_l),x_min,y_min,z_min,1))
    outfile.write('%5d%12.6f%12.6f%12.6f\n' % (ngridpoints,X[1]-X[0],0,0))
    outfile.write('%5d%12.6f%12.6f%12.6f\n' % (ngridpoints,0,Y[1]-Y[0],0))
    outfile.write('%5d%12.6f%12.6f%12.6f\n' % (ngridpoints,0,0,Z[1]-Z[0]))
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
z = np.array([0.694307,-0.694307])
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



