import random
import math

primeNumbers = set()
public_key = None
private_key = None
keyFile = "static/python/keys.txt"
n = None

def fillPrimeSet():
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
			primeNumbers.add(i)

def pickPrimeNumber():
	global primeNumbers
	k = random.randint(0, len(primeNumbers) - 1)
	it = iter(primeNumbers)
	for _ in range(k):
		next(it)
	ret = next(it)
	primeNumbers.remove(ret)
	return ret

def setKeys():
	global public_key, private_key, n
	prime1 = pickPrimeNumber()
	prime2 = pickPrimeNumber()
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

def enableEncryption():
	global public_key, private_key
	hasPublicKey = False
	hasPrivateKey = False
	f = open(keyFile, "r")
	# Check if file has keys stored
	for line in f:
		if str(line)[0] == "_":
			lineparts = line.split("=")
			potentialKey = 0
			if int(lineparts[1].removesuffix("\n"), 2) != "" and int(lineparts[1].removesuffix("\n"), 2) != 0:
				potentialKey = int(lineparts[1].removesuffix("\n"), 2)

			if lineparts[0] == "_PUBLICKEY" and potentialKey != 0:
				hasPublicKey = True
				public_key = potentialKey
			
			if lineparts[0] == "_PRIVATEKEY" and potentialKey != 0:
				hasPrivateKey = True
				private_key = potentialKey
	
	f.close()

	if hasPrivateKey == False or hasPublicKey == False:
		fillPrimeSet()
		setKeys()
		f = open(keyFile, 'w')
		f.write(f"_PUBLICKEY={format(public_key, "b")}\n_PRIVATEKEY={format(private_key, "b")}")
		f.close()

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