namelist = input("Which file do you want to remove duplicates from?: ")

# Open the input file in read mode
with open(namelist, 'r') as file:
    # Read all lines from the file
    lines = file.readlines()

# Create a set to store unique lines
unique_lines = set(lines)

# Open the output file in write mode
with open('output.txt', 'w') as file:
    # Write the unique lines to the output file
    file.writelines(unique_lines)

print("Duplicate lines removed successfully.")
