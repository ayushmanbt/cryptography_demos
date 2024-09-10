import os
from sys import platform 

if __name__ == "__main__":
    letter_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while(True):
        try:
            print("1. Encrypt text")
            print("2. Decrypt text")
            print("3. Clear Screen")
            print("4. Exit")
            option = int(input("Enter the option: "))
        
            if(option == 3):
                if(platform == "win32"):
                    os.system("cls")
                else:
                    os.system("clear")
                continue
            if(option == 4): 
                print("See you soon!")
                break
            if(option > 4):
                print("Unkown option, try again!")
                break

            input_text =  input("Enter the text (in all capital letters): ")
            key  = int(input("Enter an integer key: "))
            ans  = ''
            
            input_text = input_text.upper()

            if(option == 2):
                for letter in input_text:
                    if(letter == " "):
                        ans += letter
                        continue
                    letter_code = letter_list.find(letter)
                    new_code = (letter_code - (key % 26)) 
                    ans += letter_list[new_code]
                print("The decrypted text is", ans)
            elif(option == 1):
                for letter in input_text:
                    if(letter == " "):
                        ans += letter
                        continue
                    letter_code = letter_list.find(letter)
                    new_code = (letter_code + key) % 26
                    ans += letter_list[new_code]
                print("The encrypted text is", ans)
            
        except:
            print("You were supposed to input a number!")

    
