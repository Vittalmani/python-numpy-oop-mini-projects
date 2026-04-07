heights = input("Enter heights in inches separated by commas: ").split(',')
heights_cm = [round(float(h) * 2.54, 2) for h in heights]
print("Heights in cm:", heights_cm)
