from random import choice
import pandas as pd

# Define known mutation sequences
mutations = {
    "BRCA1": "AGCTAG",
    "CFTR": "ATCTTAT",
    "APOE": "AGCTGGC",
    "HTT": "CAGCAGCAG",
    "HBB": "GAGGTG"
}

# Define genetic markers for various traits
traits = {
    "Ginger Hair": "ACGTAGTC",
    "Blue Eyes": "GTCAGTCA",
    "Freckles": "TGCATGCA",
    "Tall Height": "CGTACGTA",
    "Curly Hair": "AGTCGATC"
}

def generate_random_sequence(length):
    """
    Generate a random DNA sequence of the given length.

    Parameters:
    - length (int): The length of the DNA sequence.

    Returns:
    - str: The randomly generated DNA sequence.
    """
    return ''.join(choice("CGTA") for _ in range(length))

def input_dna():
    """
    Get user input for a DNA sequence and perform error handling.
    
    Returns:
    - str: The valid DNA sequence entered by the user.
    - False: If the input is invalid.
    """
    while True:
        try:
            choice_input = input('Enter your desired DNA sequence for me to analyse: ').upper()
            if all(char in ['A', 'G', 'C', 'T'] for char in choice_input):
                print(f"DNA sequence: {choice_input}")
                return choice_input
            else:
                raise ValueError
        except ValueError:
            print(f'Invalid input: {choice_input}. Please enter only A, G, C, or T.')
            return False

def marker_dna():
    """
    Prompt the user to choose a genetic marker for comparison.

    Returns:
    - str: The selected DNA sequence for comparison.
    - None: If the user chooses not to compare against known genetic markers.
    """
    while True:
        choice_marker = input('Do you want to compare your sequence against known genetic diseases? (yes/no): ')
        if choice_marker.lower() == 'yes':
            print("Known Genetic Markers:")
            for idx, (identifier, sequence) in enumerate(mutations.items(), start=1):
                print(f"{idx}) {identifier}: {sequence}")

            try:
                marker_type = int(input('Which marker do you choose to make the comparison (1-5): '))
                if 1 <= marker_type <= 5:
                    selected_row = list(mutations.values())[marker_type - 1]
                    print(f"You selected: {list(mutations.keys())[marker_type - 1]}")
                    return selected_row
                else:
                    print("Invalid choice. Please choose a number between 1 and 5.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice_marker.lower() == 'no':
            return None
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def option_mutation(dna_sequence):
    """
    Compare the user's DNA sequence against a selected genetic marker.

    Parameters:
    - dna_sequence (str): The user's DNA sequence for comparison.
    """
    comparison = marker_dna()
    if comparison:
        if dna_sequence:
            position = dna_sequence.find(comparison)
            if position != -1:
                print(f"The sequence {comparison} was found at position {position} in the long sequence.")
            else:
                print(f"The sequence {comparison} was not found in the long sequence.")
        else:
            print("No valid DNA sequence available for comparison.")

if __name__ == "__main__":
    sequence_type_input = int(input("""
    1) Choose to enter a DNA sequence
    2) Generate one randomly
    Enter choice (1 or 2): """))

    if sequence_type_input == 1:
        dna_sequence = input_dna()
        if dna_sequence:  # Only proceed if the input is valid
            option_mutation(dna_sequence)
        else:
            print("Invalid DNA sequence. Exiting...")

    elif sequence_type_input == 2:
        seq_length = int(input('Enter the length of the sequence you want to analyze (The amount of characters): '))
        dna_sequence = generate_random_sequence(seq_length)
        print("Generated DNA sequence:", dna_sequence)

        option_mutation(dna_sequence)

    else:
        print('Invalid choice input')
