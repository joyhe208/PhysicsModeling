from vpython import *
import math
#Charge class that is made up of a vpython sphere along with other attributes
class Charge(sphere):
	def __init__(self, xpos, ypos, zpos,r, c, m, s):
		super().__init__(pos = vector(xpos,ypos,zpos), radius = r, color = c)
		self.magnitude = m #magnitude in 1e-9
		self.sign = s #-1, +1
	
	#calculate distance between central charge and another charge
	def getSqDistance(self, otherCharge):
		return (otherCharge.pos.x)**2 + (otherCharge.pos.y)**2 + (otherCharge.pos.z)**2

	#calculate net force between two charges
	def getFmag(self, otherCharge):
		return (9*self.magnitude*otherCharge.magnitude)/(self.getSqDistance(otherCharge))

	#calculate net force between two charges
	def getFmagXY(self, otherCharge):
		return self.getFmag(otherCharge)* (sqrt(otherCharge.pos.x**2 + otherCharge.pos.y**2)/sqrt(self.getSqDistance(otherCharge)))

	#calculate cosine of the angle between two charges with respect to the x-y plane
	def getCos(self, otherCharge):
		return (otherCharge.pos.x)/sqrt(otherCharge.pos.x**2 + otherCharge.pos.y**2)

	#calculate sine of the angle between two charges with respect to the x-y plane
	def getSin(self, otherCharge):
		return (otherCharge.pos.y)/sqrt(otherCharge.pos.x**2 + otherCharge.pos.y**2)

	#calculate sine of the angle between two charges with respect to the z-axis
	def getZSin(self, otherCharge):
		return (otherCharge.pos.z)/sqrt(self.getSqDistance(otherCharge))

	#calculate net force in the X direction on the central charge
	def getNetFX(self, otherCharges):
		sum = 0
		for otherCharge in otherCharges:
				sum = sum + (-1)*(self.sign)*(otherCharge.sign)*(self.getFmagXY(otherCharge))*(self.getCos(otherCharge))
		return sum
	
	#calculate net force in the Y direction on the central charge
	def getNetFY(self, otherCharges):
		sum = 0
		for otherCharge in otherCharges:
				sum = sum + (-1)*(self.sign)*(otherCharge.sign)*(self.getFmagXY(otherCharge))*(self.getSin(otherCharge))
		return sum

	#calculate net force in the Z direction on the central charge
	def getNetFZ(self, otherCharges):
		sum = 0
		for otherCharge in otherCharges:
				sum = sum + (-1)*(self.sign)*(otherCharge.sign)*(self.getFmag(otherCharge))*(self.getZSin(otherCharge))
		return sum



if __name__ == "__main__":
	#Initial set-up of charges/force line
	charge1 = Charge(0,0,0,.1, color.white, 5, -1)
	otherCharges = []
	charge2 = Charge(.5,.5,.5,.1, color.blue, 5, 1)
	otherCharges.append(charge2)
	charge3 = Charge (-.5,.5, -.5, .1, color.blue, 5, -1)
	otherCharges.append(charge3)
	charge4 = Charge(-.5, -.5, .5, .1, color.blue, 2.5, 1)
	otherCharges.append(charge4)
	Fnline = arrow(pos = vector(0,0,0), axis = vector(charge1.getNetFX(otherCharges)/100, charge1.getNetFY(otherCharges)/100, charge1.getNetFZ(otherCharges)/100), shaftwidth = .05)

	#animation
	t = 0
	while t <= 2*pi:
		rate(2)
		charge2.pos.x = .5*math.cos(t) + .5
		charge2.pos.y = .5*math.sin(t) + .5
		charge2.pos.z = .5*t + .5
		charge3.pos.z = -.5 + t
		Fnline.axis = vector(charge1.getNetFX(otherCharges)/100, charge1.getNetFY(otherCharges)/100, charge1.getNetFZ(otherCharges)/100)
		t +=pi/6
		if t > 2*pi:
			t = 0
			charge2.pos.x = 0
			charge2.pos.y = 0
			charge2.pos.z = 0
			charge3.pos.z = -.5
	








