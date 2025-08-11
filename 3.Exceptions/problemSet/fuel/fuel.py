# Loop
while True:
    try:
        # Prompt user for fraction 
        fraction = input("Fraction: ")

        # Convertions
        x, y = fraction.split("/")
        x = int(x); y = int(y)
        z = round((x / y) * 100)

        # checking the percent
        if z >= 99:
            print("F")
            break
        elif z <= 1:
            print("E")
            break
        else:
            print(f"{z}%")
            break
        
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    except x > y:
        pass