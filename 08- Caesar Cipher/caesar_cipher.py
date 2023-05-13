import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)
continuee = True
while continuee == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26


    def caesar(start_text, shift_amount, cipher_direction):
        new_text = ""
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                if direction == "encode":
                    new_position = position + shift_amount
                elif direction == "decode":
                    new_position = position - shift_amount
                else:
                    print("That is not a valid option.")
                new_letter = alphabet[new_position]
                new_text += new_letter
            else:
                new_text += char
        print(f"The {cipher_direction}d text is: {new_text}")


    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if again == "no":
        continuee = False
