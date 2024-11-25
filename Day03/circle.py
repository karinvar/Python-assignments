import argparse
import math

def area(radius):
    """Calculate the area of a circle given its radius."""
    return math.pi * (radius ** 2)

# Set up the argument parser
parser = argparse.ArgumentParser(description="Calculate the area of a circle.")
parser.add_argument(
    "--radius",  # The argument we'll use in the command line
    type=float,
    help="Radius of the circle"
)

# Parse the arguments passed from the command line
args = parser.parse_args()

# If the radius was passed as an argument, use it; otherwise, ask for interactive input
if args.radius is None:
    radius = float(input("Please enter the radius of the circle: "))
else:
    radius = args.radius

# Calculate and print the area
print("The area of the circle is:", area(radius))
print("hello world")
