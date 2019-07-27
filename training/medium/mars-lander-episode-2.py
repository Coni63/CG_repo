"""
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
surface_x, surface_y = [], []
mars_gravity = 3.711
vertical_max_speed = 40
horizontal_max_speed = 20
margin_for_error_y = 20
margin_for_speed = 5
map_thrust = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4
}


# to get the location to land.
# it will check where the land is flat
def move_to_location(pos_x, pos_y):
    perv_x = -1
    prev_y = -1
    for i in range(0, surface_n):
        if pos_y[i] == prev_y:
            # checking if the landing space is at least 1000
            if abs(prev_x - pos_x[i]) >= 1000:
                return [prev_x, prev_y, pos_x[i], pos_y[i]]
            else:
                prev_y = pos_y[i]
                prev_x = pos_x[i]
        else:
            prev_y = pos_y[i]
            prev_x = pos_x[i]


# this checks if the mars lander is in the landing site.
def ship_over_location(current_x, landing_site):
    return landing_site[0] < current_x < landing_site[2]


# this is to check if the mars lander is nearing the end.
def check_nearing_landing(current_y, landing_site):
    return current_y < landing_site[1] + margin_for_error_y


# check if speed is safe
def check_if_speed_safe(current_speed_x, current_speed_y):
    return abs(current_speed_x) <= horizontal_max_speed - margin_for_speed and abs(current_speed_y) <= vertical_max_speed - margin_for_speed


# check if mars lander is moving in wrong direction
def check_direction(current_x, current_hor_speed, landing_site):
    return (current_x < landing_site[0] and current_hor_speed < 0) or (landing_site[2] < current_x and current_hor_speed > 0)


# check if going horizontal too fast
def check_horizontal_speed(current_hor_speed, type):
    if type == "FAST":
        return abs(current_hor_speed) > 4 * horizontal_max_speed
    elif type == "SLOW":
        return abs(current_hor_speed) < 2 * horizontal_max_speed

def angle_to_target(current_x, landing_site):
    angle = int(math.degrees(math.acos(mars_gravity / 4.0)))
    if current_x < landing_site[0]:
        return -angle
    elif landing_site[2] < current_x:
        return angle
    else:
        return 0

def hover(current_speed_y):
    if current_speed_y >= 0:
        return 3
    else:
        return 4

def angle_to_slow_down(current_speed_x, current_speed_y):
    speed = math.sqrt((current_speed_x * current_speed_x) + (current_speed_y * current_speed_y))
    return int(math.degrees(math.asin(current_speed_x / speed)))


for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]
    surface_x.append(land_x)
    surface_y.append(land_y)

# game loop
while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    correct_site = move_to_location(surface_x, surface_y)
    if not ship_over_location(x, correct_site):
        if (check_direction(x, h_speed, correct_site)) or (check_horizontal_speed(h_speed, "FAST")):
            print("%s %s" % (angle_to_slow_down(h_speed, v_speed), map_thrust.get(4)))
        elif check_horizontal_speed(h_speed, "SLOW"):
            print("%s %s" % (angle_to_target(x, correct_site), map_thrust.get(4)))
        else:
            print("%s %s" % (map_thrust.get(0), hover(v_speed)))
    else:
        if check_nearing_landing(y, correct_site):
            print("0 3")
        elif check_if_speed_safe(h_speed, v_speed):
            print("0 2")
        else:
            print("%s 4" % angle_to_slow_down(h_speed, v_speed))
"""

import sys
import math

def d(*x):
    print(*x, file=sys.stderr)

# PID -- start --
#!/usr/bin/python
#
# This file is part of IvPID.
# Copyright (C) 2015 Ivmech Mechatronics Ltd. <bilgi@ivmech.com>
#
# IvPID is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# IvPID is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# title           :PID.py
# description     :python pid controller
# author          :Caner Durmusoglu
# date            :20151218
# version         :0.1
# notes           :
# python_version  :2.7
# ==============================================================================

"""Ivmech PID Controller is simple implementation of a Proportional-Integral-Derivative (PID) Controller at Python Programming Language.
More information about PID Controller: http://en.wikipedia.org/wiki/PID_controller
"""
import time

class PID:
    """PID Controller
    """

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
        """Calculates PID value for given reference feedback

        .. math::
            u(t) = K_p e(t) + K_i \int_{0}^{t} e(t)dt + K_d {de}/{dt}

        .. figure:: images/pid_1.png
           :align:   center

           Test PID with Kp=1.2, Ki=1, Kd=0.001 (test_pid.py)

        """
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
        """Determines how aggressively the PID reacts to the current error with setting Proportional Gain"""
        self.Kp = proportional_gain

    def setKi(self, integral_gain):
        """Determines how aggressively the PID reacts to the current error with setting Integral Gain"""
        self.Ki = integral_gain

    def setKd(self, derivative_gain):
        """Determines how aggressively the PID reacts to the current error with setting Derivative Gain"""
        self.Kd = derivative_gain

    def setWindup(self, windup):
        """Integral windup, also known as integrator windup or reset windup,
        refers to the situation in a PID feedback controller where
        a large change in setpoint occurs (say a positive change)
        and the integral terms accumulates a significant error
        during the rise (windup), thus overshooting and continuing
        to increase as this accumulated error is unwound
        (offset by errors in the other direction).
        The specific problem is the excess overshooting.
        """
        self.windup_guard = windup

    def setSampleTime(self, sample_time):
        """PID that should be updated at a regular interval.
        Based on a pre-determined sampe time, the PID decides if it should compute or return immediately.
        """
        self.sample_time = sample_time
# PID -- end --

surface_n = int(input())  # the number of points used to draw the surface of Mars.

surface = []
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points
    # together in a sequential fashion, you form the surface of Mars.

    surface.append(list(map(int, input().split())))


# Calcul de la zone d’atterissage

def getLandingCoordinates(surface):
    for i in range(surface_n - 1):
        # print(surface[i], surface[i + 1], file=sys.stderr)
        if surface[i][1] == surface[i + 1][1]:
            return ( (surface[i][0] + surface[i + 1][0]) / 2, surface[i][1] )


landing_c = getLandingCoordinates(surface)
xPid = PID(0.02, 0, 0.003)
xPid.SetPoint = landing_c[0]

yPid = PID(0.5, 0, 0)
yPid.SetPoint = landing_c[1] + 200

vsPid = PID(0.5, 0, 0)
vsPid.SetPoint = 0.

hsPid = PID(0.5, 0, 0)
hsPid.SetPoint = 0.

step = 0

while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    d(x, y, h_speed, v_speed, fuel, rotate, power)

    xPid.update(x)
    yPid.update(y)
    hsPid.update(h_speed)
    vsPid.update(v_speed)

    d(xPid.output)
    d(yPid.output)

    if abs(x - landing_c[0]) < 300:
        step = 1

    r = -xPid.output
    r = int(max(-45, min(45, r)))

    # Too low !
    if y < landing_c[1] + 1000 and step == 0 and v_speed < 0:
        r = int(max(-15, min(15, r)))
        t = 4
    elif abs(r) > 20:
        t = 4
    elif abs(r) < 10 and v_speed > -30:
        t = 2
    elif y < landing_c[1] + 2500 and v_speed < -35:
        t = 4
    else:
        t = 3

    # landing
    if y < landing_c[1] + 300 and abs(h_speed) < 20:
        r = 0

    d(r, t)

    t = int(t)
    print("{} {}".format(r, t))