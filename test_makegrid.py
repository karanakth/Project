# this is the unittest
import unittest
import makegrid
import numpy as np

class TestMakegrid(unittest.TestCase):
	def test_makegrid_one(self):
		x = np.array([0])
		y = np.array([0])
		z = np.array([0])
		atom_l = ['H']
		XX = np.array([[[-1.09,-1.09], [ 1.09,1.09]] ,[[-1.09,-1.09] ,[ 1.09,1.09]]])

		xx,yy,zz = makegrid.makegrid(x,y,z,atom_l,2)
		self.assertEqual(xx.all(),XX.all())
		