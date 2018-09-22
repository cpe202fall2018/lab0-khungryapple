#
# Name: Juyeong Lee
# Student ID:
# Date: September 21st, 2018
#
# Lab 0
# Section 15
# Purpose of the Lab:
#    To learn how to use github functionality with file modificaiton.

def weight_on_planets():
   # write your code here
   
   weightEarth = float(input("What do you weigh on earth? "))
   weightMars = weightEarth*0.38
   weightJupiter = weightEarth*2.34

   print("\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds.".format(weightMars,weightJupiter))
   
   
if __name__ == '__main__':
   weight_on_planets()
