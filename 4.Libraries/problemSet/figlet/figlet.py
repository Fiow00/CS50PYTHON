# Import required modules
from pyfiglet import Figlet
from random import choice
import sys

# Variable
figlet = Figlet()

# zero command-line arguments
if len(sys.argv) == 1:

    # Prompt string from the user
    string = input("Input: ")

    # Convert string to Frank, Ian and Glen's Letters
    f = choice(figlet.getFonts())
    figlet.setFont(font = f)
    print("Output:\n"+figlet.renderText(string))

# Two command-line arguments
elif len(sys.argv) == 3:

    # The condition for the second command line
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in figlet.getFonts():
            figlet.setFont(font = sys.argv[2])
            string = input("Input: ")
            print("Output:\n"+figlet.renderText(string))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")
