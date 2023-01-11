# we are given that 1 can of paint can cover 5m^2.
# given a random height and width calculate number of cans required.
import math


def paint_calc(height, width):
    height = (int(input("Enter the height of the wall: ")))
    width = (int(input("Enter the width of the wall: ")))
    area = height*width

    no_of_cans_required = math.ceil(area / 5)
    print(f"no_of cans required are:{no_of_cans_required}")


paint_calc(height=0, width=0)
