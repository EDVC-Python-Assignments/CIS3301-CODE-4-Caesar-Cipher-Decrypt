
def main():
   print("\nCaesar Cipher - Program")
   word = input("\nEnter the secret to decrypt: ")
   key = int(input("Enter your key: "))
  
   secret = [chr(ord(x)-key) for x in word]
   secret = "".join(secret)

   # for c in word:
   #    encrypted_word += chr(ord(c)+1)
   
   print(f"\nThe secret is {secret}\n")
    

if __name__ == "__main__":
    main()