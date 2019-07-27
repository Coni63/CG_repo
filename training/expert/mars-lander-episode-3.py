import sys
import math
import time
import numpy as np

def d(*x):
    print(*x, file=sys.stderr)

class PID:
    def __init__(self, P=0.2, I=0.0, D=0.0):

        self.Kp = P
        self.Ki = I
        self.Kd = D

        self.sample_time = 0.00
        self.current_time = time.time()
        self.last_time = self.current_time

        self.clear()

    def clear(self):
        """Clears PID computations and coefficients"""
        self.SetPoint = 0.0

        self.PTerm = 0.0
        self.ITerm = 0.0
        self.DTerm = 0.0
        self.last_error = 0.0

        # Windup Guard
        self.int_error = 0.0
        self.windup_guard = 20.0

        self.output = 0.0

    def update(self, feedback_value):
        error = self.SetPoint - feedback_value

        self.current_time = time.time()
        delta_time = self.current_time - self.last_time
        delta_error = error - self.last_error

        if (delta_time >= self.sample_time):
            self.PTerm = self.Kp * error
            self.ITerm += error * delta_time

            if (self.ITerm < -self.windup_guard):
                self.ITerm = -self.windup_guard
            elif (self.ITerm > self.windup_guard):
                self.ITerm = self.windup_guard

            self.DTerm = 0.0
            if delta_time > 0:
                self.DTerm = delta_error / delta_time

            # Remember last time and last error for next calculation
            self.last_time = self.current_time
            self.last_error = error

            self.output = self.PTerm + (self.Ki * self.ITerm) + (self.Kd * self.DTerm)

    def setKp(self, proportional_gain):
        self.Kp = proportional_gain

    def setKi(self, integral_gain):
        self.Ki = integral_gain

    def setKd(self, derivative_gain):
        self.Kd = derivative_gain

    def setWindup(self, windup):
        self.windup_guard = windup

    def setSampleTime(self, sample_time):
        self.sample_time = sample_time


surface_n = int(input())  # the number of points used to draw the surface of Mars.

surface = []
for i in range(surface_n):
    l = list(map(int, input().split()))
    surface.append(l)

def getLandingCoordinates(surface):
    for i in range(surface_n - 1):
        if surface[i][1] == surface[i + 1][1]:
            return ( (surface[i][0] + surface[i + 1][0]) / 2, surface[i][1] )


landing_c = getLandingCoordinates(surface)

xPid = PID(0.02, 0, 0.003)
yPid = PID(0.5, 0, 0)

#vsPid = PID(0.5, 0, 0)
#vsPid.SetPoint = 0.

#hsPid = PID(0.5, 0, 0)
#hsPid.SetPoint = 0.

step = 0

target = [(landing_c[0], landing_c[1] + 200)] #(5500, 1900), (5150, 2200), (3000, 1800),
current_target_index = 0
target_x, target_y = target[current_target_index]
xPid.SetPoint = target_x
yPid.SetPoint = target_y

while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    d(x, y, h_speed, v_speed, fuel, rotate, power)
    
    target_x, target_y = target[current_target_index]
    distance = math.sqrt((target_x - x)**2 + (target_y - y)**2)
    print("distance to checkpoint : {} (index = {})".format(distance, current_target_index), file=sys.stderr)
    print("target : {}-{}".format(target_x, target_y), file=sys.stderr)
    
    if distance < 550:
        current_target_index = min( (current_target_index + 1) , (len(target)-1) )
        target_x, target_y = target[current_target_index]
        distance = math.sqrt((target_x - x)**2 + (target_y - y)**2)
        xPid.SetPoint = target_x
        yPid.SetPoint = target_y
        
    xPid.update(x)
    yPid.update(y)
    #hsPid.update(h_speed)
    #vsPid.update(v_speed)

    d(xPid.output)
    d(yPid.output)

    
    if current_target_index < len(target)-1 :
        r = -xPid.output
        r = int(max(-45, min(45, r)))
        if target_y < y :
            t = 3
        else:
            t = 4
    else:
        if abs(x - landing_c[0]) < 300:
            step = 1
    
        r = -xPid.output
        r = int(max(-45, min(45, r)))
    
        # Too low !
        if y < landing_c[1] + 1000 and step == 0 and v_speed < 0:
            d("1")
            r = int(max(-15, min(15, r)))
            t = 4
        elif abs(r) > 20:
            d("2")
            t = 4
        elif abs(r) < 10 and v_speed > -30:
            d("3")
            t = 2
        elif y < landing_c[1] + 2500 and v_speed < -35:
            d("4")
            t = 4
        else:
            d("5")
            t = 3
    
        # landing
        if y < landing_c[1] + 300 and abs(h_speed) < 20:
            d("6")
            r = 0
    
    d(r, t)

    t = int(t)
    print("{} {}".format(r, t))