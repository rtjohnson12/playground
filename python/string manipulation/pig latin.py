
def main():
  
  exceptions = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
  vowels = ["a", "e", "i", "o", "u"]
  plaintext = input("Type text and press ENTER.")
  plaintext = plaintext.split()
  
  for idx in range(len(plaintext)):
    word = plaintext[idx].lower()
    
    if word[0] in vowels: 
      plaintext[idx] = word + 'way'
      
    elif word[:2] in exceptions:
      plaintext[idx] = word[2:] + word[:2] + 'ay'
      
    elif word.isalpha() == False:
      plaintext[idx] = word
      
    else:
      plaintext[idx] = word[1:] + word[:1] + 'ay'
      
  ciphertext = ' '.join(plaintext)
  return ciphertext

if __name__ == "__main__":
  x = main()
  print(x)
