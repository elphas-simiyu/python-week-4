# Error Handling Lab: File Reader
def read_file_with_error_handling():
    while True:
        try:
            # Ask the user for a filename
            filename = input("Enter the filename to read: ")
            
            # Attempt to open and read the file
            with open(filename, 'r') as file:
                content = file.read()
            
            # Print the file content
            print("\nFile Content:")
            print(content)
            break  # Exit the loop if successful
        
        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist. Please try again.")
        except PermissionError:
            print(f"Error: Permission denied for file '{filename}'. Please check the file permissions.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Run the function
read_file_with_error_handling()
