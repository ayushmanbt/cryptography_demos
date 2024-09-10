
from sys import platform
import os

if __name__ == "__main__":
    
    while(True):
        domain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Clear Screen")
        print("4. Exit")

        i = int(input("choose your option: "))

        if(i > 4 or i < 0):
            print("Choice out of range")
            continue

        if(i == 4):
            break

        if(i == 3):
            if(platform == "WIN32" or platform == "WIN64"):
                os.system("cls")

            else:
                os.system("clear")

            continue

        text = input("enter the text (no space allowed) ")
        key = input("enter the key text (no space allowed): ")

        # convert the text and the key to uppercase
        text = text.upper()
        key = key.upper()

        ans = ""
            
        # encryption
        if(i == 1):
            current_key_index = 0
            for letter in text:
                current_key = key[current_key_index]

                if current_key not in domain:
                    print("You have an impossible key!")
                    break

                elif letter not in domain:
                    ans += letter
                    continue

                else:
                    letter_index = domain.find(letter)
                    key_index = domain.find(current_key)

                    new_index = (letter_index + key_index)%26

                    ans += domain[new_index]
                        
                    current_key_index = (current_key_index + 1) % len(key)
                    
                    print(letter, "(", letter_index, ")", end = "+")
                    print(current_key, "(", key_index, ")", end = "=")

                    print(domain[new_index], "(", new_index ,")")

            print("The encrypted text is:", ans)

        # decryption
        if(i == 2):
            current_key_index = 0
            for letter in text:
                current_key = key[current_key_index]

                if current_key not in domain:
                    print("You have an impossible key!")
                    break

                elif letter not in domain:
                    ans += letter
                    continue

                else:
                    letter_index = domain.find(letter)
                    key_index = domain.find(current_key)

                    new_index = (letter_index - key_index)%26

                    ans += domain[new_index]

                    current_key_index = (current_key_index + 1) % len(key)
                    print(letter, "(", letter_index, ")", end = "+")
                    print(current_key, "(", key_index, ")", end = "=")

                    print(domain[new_index], "(", new_index ,")")


            print("The decrypted text is:", ans)
