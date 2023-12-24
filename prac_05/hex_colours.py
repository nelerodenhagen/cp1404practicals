"""
CP1404 Practical
colours in HEX codes
"""

COLOR_TO_HEX = {'ALICEBLUE': '#f0f8ff', 'AMBER': '#ffbf00', 'AQUA': '#00ffff', 'BEIGE': '#f5f5dc',
                'BRONZE': '#cd7f32', 'DARKGREEN': '#006400', 'DENIM': '#1560bd', 'GRAY': '#bebebe',
                'MINT': '#3eb489', 'PINK': '#ffc0cb'}

color = input("Please insert a color: ").upper()

while color != "":
    try:
        print(COLOR_TO_HEX[color])
    except KeyError:
        print("You entered a false color")
    color = input("Please insert a color: ").upper()