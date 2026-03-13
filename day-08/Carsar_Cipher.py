# This progrgam is inpired by the Ceasar Cipher who in order to send secret military signal
# used to encrypt it by shifting letters of alphabet like for a can be represented by say d
# This program using the same methodology asks for the input and shift no. and return he encoded string.
# I made use of function to get modula approach
# I am preferring only lower cases to work with
def encrypt(string, shift_number,direction):
    # print("\n\n"+str(art.logo)+"\n") SORRY UNAVAILABLE LOGO ART
    string= string.lower()
    encrypted_list = []
    if direction == "decode":
        for index in range(len(string)):
            if ord(string[index])>=97 and ord(string[index])<=122: # to only change alphabet, keep other character same
                if(ord(string[index])+shift_number>122):
                    new_shift_to =97+((ord(string[index])+shift_number) -122)
                    encrypted_list.append(str(chr(new_shift_to)))
                else:
                    encrypted_list.append(str(chr(ord(string[index])+shift_number)))
            else:
                encrypted_list.append(string[index])
        for index in range(len(encrypted_list)):
            print(encrypted_list[index],end="")
    else:
        for index in range(len(string)):
        # ord() function which returns the ASCII value of a character
            if ord(string[index])>=97 and ord(string[index])<=122: # to only change alphabet, keep other character same
                if(ord(string[index])-shift_number<97):
                    new_shift_to =123-((97-(ord(string[index])-shift_number)))# Experimentally prooved
                    encrypted_list.append(str(chr(new_shift_to)))
                else:
                        encrypted_list.append(str(chr(ord(string[index])-shift_number)))
            else:
                encrypted_list.append(string[index])
        for index in range(len(encrypted_list)):
            print(encrypted_list[index],end="")
        # ord() function which returns the ASCII value of a character
        
# Calling the function
string = input("\nEnter the desired String:  ")
shift_number=int(input("Enter the shift number:  "))
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:  ")
print("************************** The encrypted string is BELOW **************************\n ")
encrypt(string,shift_number,direction)
print("\n\n************************** The encrypted string is ABOVE************************** ")

# note: my teacher made a list of alphabet but I used ascii codes for both encode and decode, working same way.
