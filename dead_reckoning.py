#Benjamin Ramirez
#August 9, 2016
#using the encoders for odometry, pose(x, y, theta)

import sys, os, time
from actuators import motors
from sensors import encoders
import RPi.GPIO as GPIO
import math

FORWARD = 1
BACK = 2
left = 0.0
right = 1000.0
bottom = 0.0
top = 1000.0

#important robot dimensions
TPR = 48 #ticks per rotation
RW = 36.5 #radius of wheels (mm)
L = 165.0 #Length between centers of the two wheels (mm))
PI2 = 2*math.pi


def main():

#important odometry variables for initial pose
    dtheta = 0.0
    theta = math.pi/2
    x = 50.0
    y = 50.0
    dx = 0.0
    dy = 0.0
    theta_trn = 0.0
    motors = motors.Motors()
    left_encoder = encoder.Encoder(22,23)
    right_encoder = encoder.Encoder(16,19)
    #created motors and encoder objects
    try:
        print "Moving the car"
        motors.move(FORWARD, FORWARD, 150, 150, 3)
        print "edge counts:", left_encoder.get_ticks(), right_encoder.get_ticks()
        left_encoder.reset()
        right_encoder.reset()
        motors.move(FORWARD, FORWARD, 150,150)
        while (y < 500):
            dtheta = math.pi * (RW/L) * (float(abs(left_encoder.get_ticks())-abs(right_encoder.get_ticks()))/TPR)
            theta = math.fmod(theta + dtheta, PI2)
            print theta
            theta_trn = theta_trn + dtheta
        
            dx = cos(theta) * (PI2*RW * (left_encoder.get_ticks()/TPR))
            x = x + dx
            dy = sin(theta) * (PI2*RW * (right_encoder.get_ticks()/TPR))
            y = y + dy
            print "ticks:", left_encoder.get_ticks(), right_encoder.get_ticks()
            left_encoder.reset()
            right_encoder.reset()
            print "POSE:", x, y, theta

    finally:
        pass        
    

if __name__ == "__main__":
    main()
