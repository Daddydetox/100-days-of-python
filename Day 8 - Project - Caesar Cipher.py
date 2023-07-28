def cipher(direction, text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = []

    for char in text:
        if char.isalpha():
            index = alphabet.index(char)
            if direction == "encode":
                new_index = (index + shift) % 26
            elif direction == "decode":
                new_index = (index - shift) % 26
            result.append(alphabet[new_index])
        else:
            result.append(char)

    return ''.join(result)


gameRunning = True

while gameRunning:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while direction not in ["encode", "decode"]:
        direction = input("Invalid input. Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()

    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            break
        except ValueError:
            continue

    encrypted_text = cipher(direction, text, shift)
    print(f"The {direction}d text is: {encrypted_text}\n")

    restart = input("Enter [Q] to quit or anything else to restart:\n").lower()
    if restart == "q":
        gameRunning = False
