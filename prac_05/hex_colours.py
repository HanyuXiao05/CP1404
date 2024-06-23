HEX_COLOURS = {"absolutezero": "#0048ba", "acidgreen": "#b0bf1a", "aliceblue": "#f0f8ff", "alizarincrimson": "#e32636",
               "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc", "antiquewhite": "#faebd7", "apricot": "#fbceb1", "aqua": "#00ffff"}

color_name = input("Enter color name: ").lower()
while color_name != "":
    try:
        print(HEX_COLOURS[color_name])
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color name: ")