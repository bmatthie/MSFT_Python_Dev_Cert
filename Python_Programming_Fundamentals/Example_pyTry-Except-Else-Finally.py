#
# Example of raising an exception and try-except block.
# Functions RAISE errors.  Callers TRY-EXCEPT catch them.
#
def calculate_diameter_circle(radius: float) -> float:
    """
    Calculate the diameter of a circle given its radius.

    Args:
        radius: The radius of the circle.

    Returns:
        diameter of circle as a float.

    Raises:
        ValueError: If the input is negative.

    Example:
        >>> calculate_circle_diameter(3.5)
        7.0 
    """
    
    if radius < 0.0:
    	raise ValueError("Radius cannot be negative.")
        
    return radius * 2.0
# ***** End of function "calculate_diameter_circle" *****

#
# Main
#
radius = -0.1
try:
	diameter = calculate_diameter_circle(radius)                            # Risky code to be attempted.
except ValueError as e:
	print("Radius: " + str(radius) + ", Error: " + str(e))                  # Executed on ValueError
else:
	print("Radius: " + str(radius) + ", Diameter: " + str(diameter))        # Executed if NO errors
finally:
  print("This is always executed. Close files and freeing resourcess.")    # Always executed






