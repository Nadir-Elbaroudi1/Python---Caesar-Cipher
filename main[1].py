alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#creating a function that decode or encodes your message depending on what the user inputs their message
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  shift_amount = shift_amount % 26       
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #keeping the number/symbol/space when the text is encoded/decoded?
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

#Importing and printing the logo from art.py when the program starts.

from art import logo

print(logo)

cipher_program = True

#giving the user an option on whether or not they would like to keep playing or not
while cipher_program:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  again = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
  if again == "no":
    cipher_program = False
    print("Have a Good Day and GoodBye :) ")



    
  
