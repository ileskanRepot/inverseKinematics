import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Variables;
# https://cyberbotics.com/doc/guide/puma
dotSize = 10
# Lenght of first arm peace
len0 = 4
angle0 = 0
# Lenght of second arm peace
len1 = 3
angle1 = 0

# Lenght of hand peace
len2 = 1
angle2 = 0

# Rotation of stand
standRot = 0

# Functions:
def getElbolPos(elbolAngle,elbowLen):
	return ()

# Inputs:
targetPoint = (2,2,2)

# Code:
fig = plt.figure(figsize=(4,4))

ax = fig.add_subplot(111, projection='3d')

ax.scatter(2, 3, 4, s = dotSize) # plot the point (2,3,4) on the figure
ax.scatter(3, 3, 4, s = 1) # plot the point (2,3,4) on the figure
ax.scatter(*zip(targetPoint), s = dotSize)

plt.show()
