"""
CP1404/CP5632 Practical
Hexadecimal colour lookup program
"""

COLOUR_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blueviolet": "#8a2be2"
}

colour_name = input("Enter colour name: ").strip().lower()
while colour_name != "":
    if colour_name in COLOUR_CODES:
        print(f"The code for {colour_name} is {COLOUR_CODES[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").strip().lower()
