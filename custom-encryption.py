
# Yusuf Khan

# global constant variables
MAX_ASCII = 126 # largest printable char
MIN_ASCII = 34 # smallest printable char


# encryption
#############################################################################################
"""
    customEncrypt returns encrypted string
    inputText: string to be encrypted
    N:  integer shift value >= 1
    D: integer 1 for right shift, -1 for left shift
"""
def customEncrypt(inputText, N, D):
    reversed = inputText[::-1] # reverses string using slicing
    resultStr = ""

    for letter in reversed:
    # traverses through each letter in reversed
        if D == 1: # shift right
            ascii = ord(letter) + N # converting letter to its new shifted ascii num
            if(ascii > MAX_ASCII):
                ascii = ascii - MAX_ASCII + MIN_ASCII - 1 # wrap around printable character list
            resultStr += chr(ascii) # convert back to char and append to result

        elif D == -1: #shift left
            ascii = ord(letter) - N # converting letter to its new shifted ascii num
            if(ascii < MIN_ASCII):
                ascii = ascii + MAX_ASCII - MIN_ASCII + 1 # wrap around printable character list
            resultStr += chr(ascii) # convert back to char and append to result
    
    return resultStr
#############################################################################################





# decryption and testing
#############################################################################################
def testCustomEncrypt():
    while True: # keeps repeating until valid userID entered
        try:
            userID = input("Enter userID as text: ")
            for char in userID: # checks each char in userID
                if(ord(char) < MIN_ASCII or ord(char) > MAX_ASCII): # not a valid printable char
                    raise Exception
            break
        except:
            print("INVALID userID, please try again!") # invalid input prompt
    while True:
        try:
            password = input("Enter password as text: ") # passwd prompt for user
            for char in password:
                if(ord(char) < MIN_ASCII or ord(char) > MAX_ASCII): # not a valid printable char
                    raise Exception
            break
        except:
            print("INVALID password, please try again!") # invalid input prompt
    while True: # loops until valid value for n
        try:
            n = int(input("Enter value of n: ")) # prompt for value of N
            if n >= 1:
                break
            else:
                raise Exception # inalid value (n < 1 or n is float)
        except:
            print("INVALID input value of n, please try again!") # prompt for invalid input n
    while True: # loops until correct input d
        try:
            d = int(input("Enter value of d: "))
            if d == 1 or d == -1: # if d is correct value
                break
            else: 
                raise Exception # n entered is not 1 or -1
        except:
            print("INVALID input value of d, please try again!") # error message for invalid d

    encryptedUserID = customEncrypt(userID, n, d) # encrypts userID
    encryptedPassword = customEncrypt(password, n, d) # encrypts passwd
    
    print("encrypted userID: ", encryptedUserID) 
    print("encrypted password: ", encryptedPassword)
    # reverses encrypted string by encrypting again and shifting in opposite direction
    print("original userid: ", customEncrypt(encryptedUserID, n, -d))
    print("original password: ", customEncrypt(encryptedPassword, n, -d))
#############################################################################################


def main():
    testCustomEncrypt()
main()