while True:
    height = input("Enter your height in meters: ")
    weight = input("Enter your weight: ")


    # Calculate the bmi using weight and height.
    try:
        bmi = float(weight) / (float(height) ** 2)
        print(bmi)
        break
    except ValueError:
        print("Please enter a float")
    except TypeError:
        print("Please enter a float")
