import random
import math

primeNumbers = set()
public_key = None
private_key = None
keyFile = "static/python/keys.txt"
n = None

def binaryToInt(binary):
	i = 0
	pwr = 0
	# Reverse string
	binary = str(binary)[::-1]
	# Convert string
	for c in binary:
		if c == "1":
			i += pow(2, pwr)
		else:
			i += 0
		pwr += 1
	return i

def setPrimeSet():
	global primeNumbers
	# Fills the set with primenumbers between
	primeNumbers.clear()
	for num in range(1001,2001, 2):
		if all(num%i!=0 for i in range(2, int(math.sqrt(num))+1)):
			primeNumbers.add(num)

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
		test2 = math.gcd(e, fi)
		if math.gcd(e, fi) == 1:
			break
		e += 1
	public_key = e

	print("\n...\n")

	d = 1001*1001
	while True:
		test = (d*e)%fi
		if (d * e) % fi == 1:
			break
		d += 1
	private_key = d
	print(f"pub - {public_key} | pri - {private_key}")

def fileencryption(key):
	e = ""
	for i in range(0,5):
		e += str(random.randint(3,9))
	keycharacters = str(key)
	for num in keycharacters:
		e += "2"
		e += str(format(int(num), 'b'))
	return int(e)

def filedecryption(line):
	newline = line[5:]
	splitline = newline.split("2")
	key = ""
	for i in splitline:
		if i != "": 
			newint = binaryToInt(i)
			key += str(newint)
	return int(key)

def getKeys():
	global public_key, private_key
	hasPublicKey = False
	hasPrivateKey = False
	f = open(keyFile, "r")
	# Check if file has keys stored
	for line in f:
		if str(line)[0] == "_":
			lineparts = line.split("=")
			lineparts[1] = lineparts[1].removesuffix("\n")
			potentialKey = 0
			if lineparts[1] != "" and int(lineparts[1]) != 0:
				potentialKey = int(filedecryption(lineparts[1]))

			if lineparts[0] == "_PUBLICKEY" and potentialKey != 0:
				print("\nPublic Key has been found!")
				hasPublicKey = True
				public_key = potentialKey
			
			if lineparts[0] == "_PRIVATEKEY" and potentialKey != 0:
				print("\nPrivate key has been found!")
				hasPrivateKey = True
				private_key = potentialKey
	
	f.close()

	if hasPrivateKey == False or hasPublicKey == False:
		print("\nNot all keys were found")
		if len(primeNumbers) <= 1:
			setPrimeSet()
		print("\nGenerating new keys...")
		setKeys()
		print("\nNew keys were generated!")
		f = open(keyFile, 'w')
		pbk = int(fileencryption(public_key))
		pvk = int(fileencryption(private_key))
		#f.write(f"_PUBLICKEY={format(public_key, 'b')}\n_PRIVATEKEY={format(private_key, 'b')}")
		f.write(f"_PUBLICKEY={pbk}\n_PRIVATEKEY={pvk}")
		f.close()
		print("\nKeys have been saved!")

# To encrypt the given ascii value to a number
def encrypt(message, key):
	global n
	e = key
	encrypted_text = 1
	while e > 0:
		encrypted_text *= message
		encrypted_text %= n
		e -= 1
	return encrypted_text

# To decrypt the given number to an ascii value
def decrypt(encrypted_text, key):
	global n
	d = key
	decrypted = 1
	while d > 0:
		decrypted *= encrypted_text
		decrypted %= n
		d -= 1
	return decrypted

# Convert each character of the msg to its ascii value and then encrypting each ascii value
def encoder(message):
	global public_key
	key = public_key
	encoded = []
	# Calling the encrypting function in encoding function
	for letter in message:
		encoded.append(encrypt(ord(letter), key))
	return encoded

# Convert each number in the encryption to the ascii and then to characters
def decoder(encoded):
	global private_key
	key = private_key
	s = ''
	# Calling the decrypting function decoding function
	for num in encoded:
		s += chr(decrypt(num, key))
	return s