def calculate_area(radius):
    import math
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

def main():
    try:
        radius = float(input("Enter the radius: "))
        area = calculate_area(radius)
        print(f"The area is: {area}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
