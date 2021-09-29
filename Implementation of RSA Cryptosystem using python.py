# This is a program to calculate the RSA Cryptosystem.

# This function checks whether a number is prime or not.
def is_prime(number):
    for i in range(2, number // 2):
        if number % i == 0:
            print('you did not enter prime number')
            return False
    return True

# For simplicity, I have created an other function to check the two numbers is prime and distinct numbers.

def check_prime(p,q):
    if (p==q) or is_prime(p) or is_prime(q):
        return False
    return True

# Now we form a function that calculates the gcd of two numbers a and b.
def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a, a)

# To find the possible values of encryption keys, we calculate the gcd of a number ranging
# from 2 up to Eulers toitent have to be one.

def list_of_encryption_values(Eulers_Toitent):
    list_of_encryption_key = []
    for i in range(2, Eulers_Toitent):
        if gcd(i, Eulers_Toitent) == 1:
            list_of_encryption_key.append(i)
    return list_of_encryption_key

# using encryption key, we can calculate decryption key.

def decryption_key(encryption_key, Eulers_Toitent):
    decryption_key = 2
    while (decryption_key * encryption_key) % Eulers_Toitent !=1:
        decryption_key += 1
    return decryption_key

# we can then formulate our encoding function by using the idea that
# encoded message is the remainder of message the power of encryption code modulo RSA Modulus

def encoding(message, RSA_Modulus, encryption_key):
    if gcd(RSA_Modulus, message) != 1:
         return print("The gcd of RSA modulus and the m of message is not 1")
    encoded_message = (message**encryption_key) % RSA_Modulus
    return encoded_message

# The decoding can be done using the concept the encoded message the power of decryption key
# modulo RSA modulus is the message.

def deconding(encoded_message, decryption_key, RSA_Modulus):
    message = (encoded_message**decryption_key) % RSA_Modulus
    return message

''''We start implementing the function we have created from now on.'''
#step 1: we have to generate two distinct primes, p and q. Since they can be
# used to generate the secret key, they must be kept hidden.
print("This is a program to calculate the RSA encryption decryption system")
p = int(input("Enter a prime number for p: "))
q = int(input("Enter a distinct prime number for q: "))
# we have to check whether the two numbers you created are different and prime.

if check_prime(p,q):
    # step 2: formulate the RSA modulus and Eulers_toitent to proceed.
    # the RSA modulus is the multiple of the two primes.
    RSA_Modulus = p * q
    Eulers_Toitent = (p - 1) * (q - 1)

    # step 2: using the gcd function we have to find the possible values of encryption key.
    list_of_encryption_keys = list_of_encryption_values(Eulers_Toitent)
    encryption_key = list_of_encryption_keys[0]
    decryption_key = decryption_key(encryption_key,  Eulers_Toitent)

    # now we have the public key
    print("-----------------------")
    print(f"The public key is ({encryption_key},{RSA_Modulus})")
    # we can find also the private key.
    print("-----------------------")
    print(f"The secrete key is ({decryption_key},{RSA_Modulus})")
    print("------------------------")
    # Now we can accept from the user the message to be encrypted.
    message = int(input("Enter the message: "))
    print("------------------------")
    print("The original message is: ", message)
    encoded_message = encoding(message, RSA_Modulus, encryption_key)
    print("------------------------")
    print("The encode message sent to the receiver is: ", encoded_message)
    decoded_message = deconding(encoded_message, decryption_key, RSA_Modulus)
    print("---------------------------------------------")
    print("The message after decrypted by the receiver is: ", decoded_message)








