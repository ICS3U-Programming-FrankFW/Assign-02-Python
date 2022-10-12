#!/usr/bin/env python3
# Created By: Frankie Fox Wagoosh
# Date: Oct, 3, 2022
# This program asks the user for the base ,base and height
# of a right trapezoid in cm. It then
#calculates and displays the area and perimeter

import math

def main():
    
    #input from the user .
    print("Today we will calculate the area and")
    print("perimeter of a right trapezoid")
    base1 = int(input("Enter the base (cm):"))
    base2 = int(input("Enter the base (cm):"))
    height = int(input("Enter the height(cm):"))

    #process of calculating the area and perimeter
    area = (base1+base2)/ 2 *height
    perimeter = base1 + base2 + base2 + height


    #output of the system giving the answer 
    print("")
    print("Area = {} cm^2".format(area))
    print("Perimeter = {} cm".format(perimeter))

if __name__ == "__main__":
    main()


