# Build s_orbitals
import numpy as np

# use math.pi
def S_orb(x,y,z,a,xx,yy,zz):
	X = x-xx
	Y = y-yy
	Z = z-zz
	r2 = X**2+Y**2+Z**2
	return (8*a**3/(3.14)**3)**(0.25)*np.exp(-a*r2)

#x = np.array([0 ,1])
#y = np.array([0 ,1])
#z = np.array([0 ,1])

#xx = np.linspace(x[0],x[1],2)
#yy = np.linspace(y[0],y[1],2)
#zz = np.linspace(z[0],z[1],2)

#XX,YY,ZZ = np.meshgrid(xx,yy,zz)

#a = 18.7311370
#c = 0.03349460

#l = S_orb(x[0],y[0],z[0],a,XX,YY,ZZ)+ S_orb(x[1],y[1],z[1],a,XX,YY,ZZ)
#print(c*l)
