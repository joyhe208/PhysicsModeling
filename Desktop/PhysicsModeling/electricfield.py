from vpython import *
import math
from electrostaticforce import Charge
import numpy as np


#define the field
def getEField(position):
	return vector(0, 5-position.y,0)

def getFieldForce(charge, position):
	return math.pow(10, -9)*charge.magnitude*getEField

#initialize charge
testCharge = Charge(0,0,0,.1, color.white, math.pow(10, 6) , -1)
testChargeVel = vector(0,0,0)
testChargeMass = .002 #in KG
testChargeAccel = vector(0,0,0)

#define how speed, acceleration, position change
#while testCharge.pos.x >-5 and testCharge.pos.x < 5 and testCharge.pos.y >-5 and testCharge.pos.y <5 and testCharge.pos.z > -5 and testCharge.pos.z <5:
print(getFieldForce(testCharge, vector(1,1,1)).y)


