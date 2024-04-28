import hashlib
import random
import sys

random.seed(0)	# seed for repeatable results
pwnum = 100	# how many do we want
pwlen = 6			# how long is each string
pwrange = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
							# what characters can they use
saltrange = '0123456789'	# use mode 10; $pass$salt, hash:salt
saltlen = 3

def genhash(func, input, salt = False):
	filename = func.__name__ + "_salt.hash" if salt else func.__name__ + ".hash"
	print(f'generating {filename}')
	if salt:
		print('with salt')
		hashes = [func((p + saltlist[i]).encode()).hexdigest() + ":" + saltlist[i] for i, p in enumerate(input)]
	else:
		hashes = [func((p).encode()).hexdigest() for p in input]
	print(f"generated {filename} ({hashes[:5]} ...)\n")
	with open(filename, 'w') as f: 
		f.write(('\n').join(hashes))


print(f"generating {pwnum} passwords, length {pwlen}")
pwlist = [''.join([random.choice(pwrange) for i2 in range(pwlen)]) for i in range(pwnum)]
saltlist = [''.join([random.choice(saltrange) for i2 in range(saltlen)]) for i in range(pwnum)]
print(f"generated passwords ({pwlist[:5]} ...)\n")

salt = 'salt' in sys.argv

if 'md5' in sys.argv:
	genhash(hashlib.md5, pwlist, salt)

if 'sha1' in sys.argv:
	genhash(hashlib.sha1, pwlist, salt)

if 'sha256' in sys.argv:
	genhash(hashlib.sha256, pwlist, salt)

if 'sha512' in sys.argv:
	genhash(hashlib.sha512, pwlist, salt)
