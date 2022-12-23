orig_message = input('<Enter message> ')

orig_text = input('<Enter carrier text> ')

message = orig_message.replace(' ', '')

text = orig_text.replace(' ', '')

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

binary_dict = {}

bin_mess = ''

coded_message = ''

for letter in alphabet:
    # Get each letter's ASCII code
    ascii_code = ord(letter)
    # Convert ASCII to a binary string 5 digits long
    binary = bin(ascii_code)[4:]
    # Add the upper & lower case letter binary value
    binary_dict[letter] = binary
    binary_dict[letter.lower()] = binary

for l in message:
    # Add the binary output to a string
    bin_mess += binary_dict[l]

for i in range (0, len(bin_mess)):
    # Add the letter to the output
    if bin_mess[i] == '0':
        coded_message += text[i]
    # Add the letter in italics
    elif bin_mess[i] == '1':
        coded_message += '\x1B[3m'
        coded_message += text[i]
        coded_message += '\x1B[0m'

#for o in range(0, len(orig_message)):
#    if orig_message[o] == ' ':
#        frangments = [coded_message[0:o], coded_message[o+1:-1]]
#        coded_message = ' '.join(fragments)

print(coded_message)
