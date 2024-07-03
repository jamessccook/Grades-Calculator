from math import ceil

# A dictionary for an example semester which contains four units which each have assignments with a specified mark received, maximum mark, and weighting
# If you add an assignment but have not yet received a mark, comment it out by highlighling it and press command + / which will add a # before it making it non-executable code, and remove the comma from the end of the above assignment if not the first assignment
# You can add as many or few assignments as desired
Y1S1 = {
    'UNIT1001': {
        'Assignment 1': {'mark received': 90, 'maximum mark': 100, 'weight': 10},
        'Assignment 2': {'mark received': 80, 'maximum mark': 100, 'weight': 15},
        'Assignment 3': {'mark received': 62, 'maximum mark': 71, 'weight': 20},
        'Assignment 4': {'mark received': 7, 'maximum mark': 12, 'weight': 5},
        'Final Exam': {'mark received': 75, 'maximum mark': 100, 'weight': 50}
    },

    'UNIT1002': {
        'Assignment 1': {'mark received': 90, 'maximum mark': 100, 'weight': 10},
        'Assignment 2': {'mark received': 80, 'maximum mark': 100, 'weight': 15},
        'Assignment 3': {'mark received': 62, 'maximum mark': 71, 'weight': 10},
        'Assignment 4': {'mark received': 7, 'maximum mark': 12, 'weight': 5}
        # 'Assignment 5': {'mark received': <val>, 'maximum mark': 100, 'weight': 5},
        # 'Assignment 6': {'mark received': <val>, 'maximum mark': 50, 'weight': 15},
        # 'Final Exam': {'mark received': <val>, 'maximum mark': 65, 'weight': 40}
    },

    'UNIT1003': {
        'Assignment 1': {'mark received': 90, 'maximum mark': 100, 'weight': 30},
        'Assignment 2': {'mark received': 80, 'maximum mark': 100, 'weight': 35},
        'Assignment 3': {'mark received': 62, 'maximum mark': 71, 'weight': 35}
    },

    'UNIT1004': {
        'Assignment 1': {'mark received': 90, 'maximum mark': 100, 'weight': 10},
        'Assignment 2': {'mark received': 80, 'maximum mark': 100, 'weight': 20}
        # 'Final Exam': {'mark received': <val>, 'maximum mark': 100, 'weight': 70}
    }
}

# This is a further example with a more genearlised structure. This is how you would add a further semester; simply copy this and fill it in
Y1S2 = {
    'UNIT1005': {
        '<name>': {'mark received': <val>, 'maximum mark': <val>, 'weight': <val>},
        '<name>': {'mark received': <val>, 'maximum mark': <val>, 'weight': <val>}
    },

    'UNIT1006': {
        '<name>': {'mark received': <val>, 'maximum mark': <val>, 'weight': <val>},
        '<name>': {'mark received': <val>, 'maximum mark': <val>, 'weight': <val>}
    },

    'UNIT1007': {
        '<name>': {'mark received': <val>, 'maximum mark': <val>, 'weight': <val>},
        '<name>': {'mark received': <val>, 'maximum mark': <val>, 'weight': <val>}
    },

    'UNIT1008': {
        '<name>': {'mark received': <val>, 'maximum mark': <val>, 'weight': <val>},
        '<name>': {'mark received': <val>, 'maximum mark': <val>, 'weight': <val>}
    }
}

# Calculates your current mark for a given unit
def calculate_current_mark(unit_assignments, unit):
    total = 0
    current_weight = 0

    # Loops through each completed assignment and sums their weighting
    for assignment, info in unit_assignments.items():
        current_weight += info['weight']

    # Loops through each completed assignment and sums their mark received
    for assignment, info in unit_assignments.items():
        total += (info['weight']/current_weight) * ((100/info['maximum mark']) * info['mark received'])

    # Calculates the weight of the assignments that are not completed
    remaining_weight = 100 - current_weight

    if remaining_weight == 0 :
        print(f"Current mark for {unit} is {total:.2f}; displayed on transcript as {round(total)}")
    else:
        print(f"Current mark for {unit} is {total:.2f}")
        calculate_needed_for_desired(unit_assignments, unit, current_weight, remaining_weight)

# Calculates what mark you will need to get in the remaining assignments for a given unit to attain a desired mark
def calculate_needed_for_desired(unit_assignments, unit, current_weight, remaining_weight):
    current_total_of_whole = 0

    # Loops through each completed assignment and sums their mark received as a percentage of the weight of all assignments (not just the completed assignments)
    for assignment, info in unit_assignments.items():
        current_total_of_whole += (info['weight']/100) * ((100/info['maximum mark']) * info['mark received'])

    # Gets the desired mark from the user
    while True:
        try:
            desired = float(input(f"What is your desired mark for {unit}? "))
            if desired < 0 or desired > 100:
                print("Please enter a valid desired mark between 0 and 100")
            else: 
                break
        except ValueError:
            print("Please enter a valid number")

    # Calculates the average mark needed in the remaining assignments to attain the desired mark
    percentage_needed = desired - current_total_of_whole
    needed = (100/remaining_weight)*percentage_needed

    # Ensures a negative mark is not presented to the user
    if needed < 0:
        needed = 0

    print(f"To achieve the desired mark of {desired} for {unit}, you will need to average {needed:.2f} in the remaining assignments - ceiling value {ceil(needed)}")

    # Message for when the desired mark is unattainable
    if needed > 100:
        maximum = current_total_of_whole + remaining_weight
        print(f"Your desired mark is unattainable; your maximum mark is {maximum:.2f}")

# Calls for the calculation of the current mark of each unit in the given semester dictionary
def main():
    for unit, unit_assignments in Y3S1.items():
        calculate_current_mark(unit_assignments, unit)

if __name__ == "__main__":
    main()
