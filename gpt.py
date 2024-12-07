import sys
import os
import time
import numpy as np
import getInputData


# Ensure the parent directory is in the system path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Helper to parse the input data
def parse_input(data):
    try:
        # Split into rules and lists
        split_idx = data.index(",") - 2
        order_rules_string = data[:split_idx].strip()
        lists_string = data[split_idx:].strip()
        
        # Parse rules
        order_rules = [
            (int(rule.split(",")[0]), int(rule.split(",")[1]))
            for rule in order_rules_string.splitlines()
        ]

        # Parse lists
        lists = [
            [int(x) for x in line.split(",")] for line in lists_string.splitlines()
        ]
        return order_rules, lists
    except Exception as e:
        raise ValueError(f"Error parsing input data: {e}")

# Check if an order is valid based on rules
def is_order_valid(instruction, rules):
    for A, B in rules:
        if A in instruction and B in instruction:
            index_a = instruction.index(A)
            index_b = instruction.index(B)
            if index_b < index_a:
                return False
    return True

# Sort a list to comply with rules
def sort_instruction(instruction, rules):
    changed = True
    while changed:
        changed = False
        for A, B in rules:
            if A in instruction and B in instruction:
                idx_a = instruction.index(A)
                idx_b = instruction.index(B)
                if idx_b < idx_a:
                    instruction[idx_a], instruction[idx_b] = instruction[idx_b], instruction[idx_a]
                    changed = True
    return instruction

# Solve Part 2
def part_two(data_input):
    try:
        # Parse the input
        rules, instructions = parse_input(data_input)

        invalid_instructions = []
        for instruction in instructions:
            if not is_order_valid(instruction, rules):
                invalid_instructions.append(instruction)

        # Fix invalid instructions
        fixed_instructions = [
            sort_instruction(instruction, rules) for instruction in invalid_instructions
        ]

        # Calculate the result
        return sum(instruction[len(instruction) // 2] for instruction in fixed_instructions)
    except Exception as e:
        raise ValueError(f"Error processing Part 2: {e}")

# Main script execution
if __name__ == "__main__":
    start_time = time.time()

    try:
        # Get input data
        input_data = getInputData.getTodaysData(5)

        # Solve Part 2
        result = part_two(input_data)
        print(f"Part 2 result = {result}")

    except Exception as e:
        print(f"Error: {e}")

    end_time = time.time()
    print(f"Executed in {end_time - start_time:.4f} seconds")
