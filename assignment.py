def modify_and_write_file(input_filename, output_filename):
    """
    Reads a file, modifies its content, and writes it to a new file.

    Args:
        input_filename (str): The name of the file to read.
        output_filename (str): The name of the file to write to.

    Returns:
        bool: True if the operation was successful, False otherwise.
    """
    try:
        with open(input_filename, 'r') as infile:
            content = infile.readlines()

        modified_content = [line.upper() for line in content]  # Example modification: convert to uppercase

        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"Successfully read '{input_filename}', modified it, and wrote to '{output_filename}'.")
        return True

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        return False
    except PermissionError:
        print(f"Error: Permission denied to read '{input_filename}'.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    input_file = input("Enter the name of the file you want to read: ")
    output_file = input("Enter the name for the new output file: ")

    modify_and_write_file(input_file, output_file)

    print("\nOutcomes 🎉:")
    print("You've successfully attempted file reading, writing, and error handling in Python!")
    print("This is a crucial step towards building robust applications!")
