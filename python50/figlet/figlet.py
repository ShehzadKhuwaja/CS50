import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("invalid flag")
    if sys.argv[2] not in figlet.getFonts():
        sys.exit("invalid font")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(input("Input: ")))
elif len(sys.argv) == 1:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print(figlet.renderText(input("Input: ")))
else:
    sys.exit("invalid number of arguments")