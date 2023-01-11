alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
            'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
            'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("type 'encode' to encrypt,type 'decode' to decrypt: ")
text = input("type your message: ")
shift = int(input("type the shift number: "))


def encrypt(message, shift_amount):
    code = ""
    for letter in message:
        position = alphabet.index(letter)  # position vaneko letter ko index
        new_position = position+shift  # shift garisakepaxi ko position is new position
        # lets take the word'hello'as example.
        new_letter = alphabet[new_position]
        code += new_letter
    print(f"the encoded text is {code}")


encrypt(message=text, shift_amount=shift)
# if text=yz then there will be error because firstly z position is 25 and if there will be shift=2 then the position will be 27 which don't exixt.
# to solve this,we can use the alphabets twice in list.


# now the code should be again converted into text.
def decrypt(code, shift_amount):
    for letter in code:
        position = alphabet.index(letter)
        new_position = position-shift_amount
        code += alphabet[new_position]
    print(f"the decoded text is {code} ")


if direction == "encode":
    encrypt(message=text, shift_amount=shift)
elif direction == "decode":
    decrypt(code=text, shift_amount=shift)
