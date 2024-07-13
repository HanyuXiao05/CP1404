"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ")
    
max_state_length = max([len(i) for i in CODE_TO_NAME])

print(max_state_length)

for state,state_fullname in CODE_TO_NAME.items():
    print(f"{state:<{max_state_length}} is {state_fullname}")
