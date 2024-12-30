def modify_content(content):
    return content.upper()
def main():
    try:
        #Ask the user for the file name
        input_file = input("Enter the filename to read from:")
        
        #Try opening the file for reading
        with open(input_file, 'r') as file:
                content = file.read()
        # Modify the content
        modified_content  = modify_content(content)   
           #Ask for the output filename
        output_file = input("Enter the filename to save the modified content:")
            #Try writing the modified content into the new file
        with open(output_file, 'w')as file:
                file.write( modified_content)
        print(f"Modified content has been saved to{output_file} successfully!")
    except FileNotFoundError:   
        print(f"Error: Input file '{input_file}'not found.")
    except IOError:
         print("An I/O error occurred.")
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")     
    finally:
        print("Program execution completed.")
if __name__ == " __main__ " :
    main()       
