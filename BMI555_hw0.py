# code review by Yuxin Wu BMI 500, my comments begin with YW

# YW: below shows the content of a specific task, the block code is self explainable, easy to understand

####1. Write a code that prints the numbers from 0 to 100, with the following conditions:
##### If the number is divisible by 3, print the string 'a' instead of the number.
###### If the number is divisible by 5, print the string 'b' instead of the number.
####### If the number is divisible by both 3 and 5, print the string 'ab' instead of the number.
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print('ab')
    elif i % 3 == 0:
        print('a')
    elif i % 5 == 0:
        print('b')
    else:
        print(i)


# YW: for this task, the coder make comments for some lines which are diffult to understand
# which is great!

####2. Created a 3x3 2D array filled with random integers between 1 and 10 (inclusive)
#####Calculate and print the sum of each row
######Find and print the maximum and minimum values in the matrix, along with their
#######positions (row and column indices).

import numpy as np
# Create a 3x3 2D array with random integers between 1 and 10
matrix = np.random.randint(1, 11, (3, 3))
print("Matrix:\n", matrix)
# Calculate and print the sum of each row
row_sums = matrix.sum(axis=1)
print("Sum of each row:", row_sums)
# Find and print the maximum and minimum values in the matrix, with their positions
max_value = np.max(matrix)
min_value = np.min(matrix)
max_position = np.unravel_index(np.argmax(matrix), matrix.shape)
min_position = np.unravel_index(np.argmin(matrix), matrix.shape)

print(f"Maximum value: {max_value} at position {max_position}")
print(f"Minimum value: {min_value} at position {min_position}")



#####3. Write a code that checks whether a given number x is part of the Fibonacci sequence.
#####The program should output True if x is in the sequence and False otherwise.
def is_fibonacci(x):
    a, b = 0, 1
    while a <= x:
        if a == x:
            return True
        a, b = b, a + b
    return False

# YW: just considering if the codes above can be defined into a function would be better.

#####4.Write a program that:
######Allows the user to provide a source folder, a destination folder, and a filename string
######in command line.
#######Copies all files from the source folder that starts with the filename string to the
#######destination folder.
########Need to be able to handle errors (wrong folder name, etc.). Return a message “Error”
########if any error occurs.
import os
import shutil
import sys

def copy_files_with_prefix(src_folder, dest_folder, filename_prefix):
    try:
        # Check if source folder exists
        if not os.path.exists(src_folder):
            print("Error: Source folder does not exist.")
            return

        # Check if destination folder exists
        if not os.path.exists(dest_folder):
            print("Error: Destination folder does not exist.")
            return

        # Iterate over files in source folder
        for filename in os.listdir(src_folder):
            # Check if the file name starts with the given prefix
            if filename.startswith(filename_prefix):
                # Full path for the source and destination
                src_file_path = os.path.join(src_folder, filename)
                dest_file_path = os.path.join(dest_folder, filename)

                # Copy file to destination folder
                shutil.copy2(src_file_path, dest_file_path)

        print("Files copied successfully.")

    except Exception as e:
        print("Error")
        print(f"Exception occurred: {e}")

if __name__ == "__main__":
    # Read command line arguments
    if len(sys.argv) != 4:
        print("Usage: python script.py <source_folder> <destination_folder> <filename_prefix>")
    else:
        source_folder = sys.argv[1]
        destination_folder = sys.argv[2]
        filename_prefix = sys.argv[3]

        copy_files_with_prefix(source_folder, destination_folder, filename_prefix)
