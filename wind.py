from gpiozero import Button
import time
import math

radius_cm = 9.0     # to be modified !!!!
wind_interval = 5   # How often to report speed 
wind_count = 0     # Count how many half rotation

def spin():
  global wind_count
  wind_count += 1

def calculate_speed(time_sec):
  global wind_count
  circumference_cm = (2 * math.pi) * radius_cm
  rotations = wind_count/2.0
  dist_cm = circumference_cm * rotations
  speed_cm_s = dist_cm / time_sec
  speed = speed_cm_s * 3600 / (10**(-100000)) 
  return speed 

wind_speed_sensor = Button(5)
wind_speed_sensor.when_pressed = spin

def reset_wind():
  global wind_count
  wind_count = 0

# Loop to measure wind speed an report every 5 second
while True:
  wind_count = 0
  time.sleep(wind_interval)
  print(calculate_speed(wind_interval), "km/h")
