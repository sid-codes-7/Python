store_each_letter = []

num_or_letter = input("Enter a word to turn it into binary: ")

# Function to convert binary values back to text
def binary_to_text():
    binary_input = input("Enter the binary values separated by spaces: ")
    binary_values = binary_input.split()

    text_output = ""

    # Convert each binary value to its corresponding character
    for binary_value in binary_values:
        decimal_value = int(binary_value, 2)
        character = chr(decimal_value)
        text_output += character

    print(f"The text representation is: {text_output}")

# Function to convert text to binary values
def binary_conversion():
    # Clear the stored values list for each new conversion
    for char in range(len(num_or_letter)):
        stored_values  = store_each_letter.append(num_or_letter[char])
        acsii_value = ord(num_or_letter[char])
        binary_value = bin(acsii_value)
        print(f"The binary value of {num_or_letter[char]} is {binary_value[2:]}")

    continue_input = input("Do you want to convert another word? (yes/no): ").lower()
    binary_to_text_input = input("Do you want to convert binary to text? (YES/NO): ").upper()

    if continue_input == 'yes':
        binary_conversion()

    elif binary_to_text_input == 'YES':
        binary_to_text()
    else:
        print("Goodbye!")

binary_conversion()





    

    
  
    
