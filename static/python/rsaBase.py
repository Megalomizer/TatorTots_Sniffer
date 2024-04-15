import random
import math

# A set will be the collection of prime numbers,
# where we can select random primes p and q
prime = set()

public_key = None
private_key = None
n = None

# Fill the set of prime numbers
def primefiller():
	# Method used to fill the primes set is Sieve of Eratosthenes (a method to collect prime numbers)
	seive = [True] * 250
	seive[0] = False
	seive[1] = False
	for i in range(2, 250):
		for j in range(i * 2, 250, i):
			seive[j] = False

	# Filling the prime numbers
	for i in range(len(seive)):
		if seive[i]:
			prime.add(i)


# Picking a random prime number and erasing that prime number from list because p!=q
def pickrandomprime():
	global prime
	k = random.randint(0, len(prime) - 1)
	it = iter(prime)
	for _ in range(k):
		next(it)
	ret = next(it)
	prime.remove(ret)
	return ret

# Define the keys, both public & private
def setkeys():
	global public_key, private_key, n
	prime1 = pickrandomprime() # First prime number
	prime2 = pickrandomprime() # Second prime number
	n = prime1 * prime2
	fi = (prime1 - 1) * (prime2 - 1)
	e = 2
	while True:
		if math.gcd(e, fi) == 1:
			break
		e += 1
	public_key = e

	d = 2
	while True:
		if (d * e) % fi == 1:
			break
		d += 1
	private_key = d


# To encrypt the given ascii value to a number
def encrypt(message):
	global public_key, n
	e = public_key
	encrypted_text = 1
	while e > 0:
		encrypted_text *= message
		encrypted_text %= n
		e -= 1
	return encrypted_text


# To decrypt the given number to an ascii value
def decrypt(encrypted_text):
	global private_key, n
	d = private_key
	decrypted = 1
	while d > 0:
		decrypted *= encrypted_text
		decrypted %= n
		d -= 1
	return decrypted


# Convert each character of the msg to its ascii value and then encrypting each ascii value
def encoder(message):
	encoded = []
	# Calling the encrypting function in encoding function
	for letter in message:
		encoded.append(encrypt(ord(letter)))
	return encoded

# Convert each number in the encryption to the ascii and then to characters
def decoder(encoded):
	s = ''
	# Calling the decrypting function decoding function
	for num in encoded:
		s += chr(decrypt(num))
	return s


primefiller()
setkeys()
message = "Norayr is heel lief!"

# Calling the encoding function
coded = encoder(message)

print("Initial message:")
print(message)
print("\n\nThe encoded message(encrypted by public key)\n")
print(''.join(str(p) for p in coded))
print("\n\nThe decoded message(decrypted by public key)\n")
print(''.join(str(p) for p in decoder(coded)))