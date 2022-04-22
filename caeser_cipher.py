
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift%26

def caesar(text,shift,direction): 
  t = list(text)
  for i in range(len(t)):
    if t[i] in alphabet:
      position = alphabet.index(t[i])
      if direction == "encode":
        new_position = position+shift
        if (new_position) > 25:
          t[i] = alphabet[(new_position)-26]
        else:
          t[i] = alphabet[new_position]
      elif direction == "decode":
        new_position = position-shift
        if (new_position) < 0:
          t[i] = alphabet[26+(new_position)]
        else:
          t[i] = alphabet[new_position]
    else:
      t[i] = t[i]
  end_text = "".join(t)
  print(f"The {direction}d text is: {end_text}")
  continue_or_not = input("Type 'yes' if want to go again. Otherwise type'no'. ")
  if continue_or_not == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%26
    caesar(text,shift,direction)

caesar(text,shift,direction)


# def encrypt(text,shift):
#   t = list(text)
#   for i in range(len(t)):
#     position = alphabet.index(t[i])
#     new_position = position+shift
#     if (new_position) > 25:
#       t[i] = alphabet[(new_position)-26]
#     else:
#       t[i] = alphabet[new_position]
      
#   print("".join(t))
# def decrypt(text,shift):
#   t = list(text)
#   for i in range(len(t)):
#     position = alphabet.index(t[i])
#     new_position = position-shift
#     if (new_position) < 0:
#       t[i] = alphabet[26+(new_position)]
#     else:
#       t[i] = alphabet[new_position]
#   print("".join(t))

#if direction == "encode":
  #encrypt(text,shift)
#elif direction == "decode":
  #decrypt(text,shift)
 