# Grades-Calculator

This Python script calculates your current mark for each unit in a semester based on the marks received in assignments and their respective weightings. Additionally, it calculates the average mark needed in remaining assignments to achieve a desired overall mark. You can add or modify assignments and units as needed.

Whilst this script is structured using a new dictionary per semester, you could modify the code so there is only one dictionary that contains all of your grades over a year or even your entire degree.

## Usage

### 1. Setup Semester Data:

- Define a dictionary for each semester, where each key is a unit code and each value is another dictionary of assignments.
- For each assignment, specify:
  - mark received: The mark you received.
  - maximum mark: The maximum possible mark.
  - weight: The weight of the assignment as a percentage of the total mark for the unit.


For example, here is a dictionary for year one semester one showing one unit and its assignments:

```py
Y1S1 = {
    'UNIT1001': {
        'Assignment 1': {'mark received': 90, 'maximum mark': 100, 'weight': 10},
        'Assignment 2': {'mark received': 80, 'maximum mark': 100, 'weight': 15},
        'Assignment 3': {'mark received': 62, 'maximum mark': 71, 'weight': 20},
        'Assignment 4': {'mark received': 7, 'maximum mark': 12, 'weight': 5},
        'Final Exam': {'mark received': 75, 'maximum mark': 100, 'weight': 50}
    },
    ...
}
```

If you have not received a mark for an assignment, either don't include the assignment or simply comment it by pressing command + /, and remove the comma from the end of the assignment directly above if not the first assignment

```py
Y1S1 = {
    'UNIT1001': {
        'Assignment 1': {'mark received': 90, 'maximum mark': 100, 'weight': 10},
        'Assignment 2': {'mark received': 80, 'maximum mark': 100, 'weight': 15}
        # 'Assignment 3': {'mark received': 62, 'maximum mark': 71, 'weight': 20},
        # 'Assignment 4': {'mark received': 7, 'maximum mark': 12, 'weight': 5},
        # 'Final Exam': {'mark received': 75, 'maximum mark': 100, 'weight': 50}
    },
    ...
}
```

You can add as many or few units and assignments as desired

```py
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
```

### 2. Run the Script:

Ensure the correct semester dictionary is referenced in the main function. You can change where it says Y1S1 to any other dictionary of semester units to look at your marks for that semester e.g. Y2S2

```py
def main():
    for unit, unit_assignments in Y1S1.items():
        calculate_current_mark(unit_assignments, unit)
```
Execute the script to see the current marks

### 3. Desired marks

Enter the desired mark when prompted for units that have incomplete assignments

```
What is your desired mark for <unit name>? 
```

## Functions 
### calculate_current_mark(unit_assignments, unit)
- Description: Calculates the current mark for a given unit.
- Parameters:
  - unit_assignments: Dictionary of assignments for the unit.
  - unit: Unit code (string).
- Output: Prints the current mark for the unit and calls calculate_needed_for_desired if there are remaining assignments.

### calculate_needed_for_desired(unit_assignments, unit, current_weight, remaining_weight)
- Description: Calculates the mark needed in remaining assignments to achieve a desired overall mark.
- Parameters:
  - unit_assignments: Dictionary of assignments for the unit.
  - unit: Unit code (string).
  - current_weight: Total weight of completed assignments.
  - remaining_weight: Total weight of remaining assignments.
- Output: Prompts the user for the desired mark and prints the average mark needed in the remaining assignments.

### main()
- Description: Iterates through each unit in the semester dictionary and calculates the current mark.
- Parameters: None.
- Output: Prints the current marks for all units in the given semester dictionary.
