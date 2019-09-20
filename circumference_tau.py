#!/usr/bin/env python3

# Created by: DJ Watson
# Created on: September 2019
# This program calculates area and perimeter of a rectangle
# with user input


import constants


def main():
    # this function calculates circumference
    # input
    radius = int(input("Enter radius of the circle (mm): "))
    # process
    circumference = constants.TAU*radius
    # output
    print("")
    print("Circumference is {}mm2".format(circumference))


if __name__ == "__main__":
    main()
