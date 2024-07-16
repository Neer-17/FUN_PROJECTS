key_index =0
alphabet = 'abcdefghijklmnopqrstuvwxyz'
final_message = ''
pattern ='@&(§€£}-!?<|×√°π%#$∆✓^{÷=*'
f_msg=''
def cipher(message, key, direction=1):
    global key_index,alphabet,final_message,pattern,ch,f_msg
    for char in message.lower():

# Append any non-letter character to the message

        if not char.isalpha():

            final_message += char

        else:

# Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index +=1
            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += pattern[new_index]
            f_msg+=alphabet[new_index]
    if ch =='E':
         return final_message
    elif ch=='D':
   				   return f_msg


def encrypt(message, key):
    print (cipher(message, key))
def decrypt(message,key):
    global key_index,alphabet,final_message,pattern
 
    alpha=''
    for i in message:
          indx=pattern.find(i)
          alpha+=alphabet[indx]
    print(cipher(alpha,key,-1))

message = input("Enter message :")

key = input("Enter Key :")

ch = input ("Enter choice (E/D) :")

if ch =="E" :
    print("Encrypted message:",end="")
    encrypt(message,key)

elif ch =="D" :
    print("Decrypted message :",end="")
    decrypt(message,key)

