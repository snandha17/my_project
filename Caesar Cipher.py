# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?

print(logo)
try_again = False
while not try_again:
    def caesar(original_text, shift_amount, encode_or_decode):
        output_text = ""
        if encode_or_decode == "decode":
            shift_amount *= -1
        for letter in original_text:
            if letter not in alphabet:
                output_text += letter

            shifted_position = alphabet.index(letter) + shift_amount #-2
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        print(f"Here is the {encode_or_decode}d result: {output_text}")

    # TODO-3: Can you figure out a way to restart the cipher program?

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    retry = input(f"Type 'yes' if you want to go again, otherwise type 'no'.\n").lower()
    if retry == "yes":
        try_again = False
    else:
        try_again = True
# coded line is 27
