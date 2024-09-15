def replace_even_instances(file_path, target_word, replacement_word, output_file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Initialize a counter for occurrences of 'cbkadal'
    counter = 1

    # Define a function to replace only even occurrences
    def replace_cbkadal(match):
        nonlocal counter
        # Replace the even-numbered occurrence (0th, 2nd, 4th, etc.)
        replacement = replacement_word if counter % 2 == 0 else target_word
        counter += 1
        return replacement

    # Use a regular expression to find all occurrences and replace as needed
    import re
    pattern = re.compile(re.escape(target_word))
    new_content = pattern.sub(replace_cbkadal, content)

    # Write the new content to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(new_content)

# Example usage
input_file = 'WEEK02-MYNAME.txt'  # Input file
  # Input file
output_file = 'output.txt'  # New file to store the results
replace_even_instances(input_file, 'cbkadal', 'Mcflurrins', output_file)

