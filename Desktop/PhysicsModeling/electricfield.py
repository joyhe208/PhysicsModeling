from vpython import *
import math
from electrostaticforce import Charge
import numpy as np


#define the field
def getEField(position):
	return vector(0, 2,0)

def getFieldForce(charge):
	return pow(10, -9)*charge.magnitude*getEField(charge.pos)

if __name__ == "__main__":
	#initialize charge
	testCharge = Charge(0,-50,0,7, color.white, pow(10, 6) , -1)
	testChargeMass = .002 #in KG
	testChargeVel = vector(0,0,0)
	t = 0
	dt = 1

	#define how speed, acceleration, position change
	while testCharge.pos.x >-100 and testCharge.pos.x < 100 and testCharge.pos.y >-100 and testCharge.pos.y <100 and testCharge.pos.z > -100 and testCharge.pos.z <100:
		rate(1)
		testChargeAccel = getFieldForce(testCharge)/testChargeMass
		testCharge.pos += testChargeVel*dt 
		testChargeVel += testChargeAccel*dt
		print(testCharge.pos.y)
		t+=dt





