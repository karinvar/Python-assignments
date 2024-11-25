import argparse
import math

def area(radius):
    """Calculate the area of a circle given its radius."""
    return math.pi * (radius ** 2)

parser = argparse.ArgumentParser(description="Calculate the area of a circle.")
parser.add_argument(
    "--radius",  
    type=float,
    help="Radius of the circle"
)

args = parser.parse_args()

if args.radius is None:
    radius = float(input("Please enter the radius of the circle: "))
else:
    radius = args.radius


print("The area of the circle is:", area(radius))

