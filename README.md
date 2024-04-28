## ECE 548 Cybersecurity Project
This contains the python script responsible for generating random, repeatable passwords and their corresponding hash values. Execute the script with python, and include md5, sha1, sha256, and/or sha512 in the arguments to generate a set of output hash files of the corresponding function name. 
Additionally, salted password hashes can be generated instead by including the word *salt* as an input argument.
Inside the script, options exist for the alphabet to use in the random passwords, 

The output files will contain each hash on a separate line, for use with hashcat input, e.g.
`time hashcat -a 3 -m 1410 openssl_sha256_salt.hash '?a?a?a?a?a?a' -O -w 3`
Where mode (-m) 0 should be used with MD5, 10 for MD5 with salt in this format, 100 for SHA1, 110 for SHA1 salt, 1400 for SHA256, 1410 for SHA256 salt, 1700 for SHA512, and 1710 for SHA512 salt. The (-a) argument designates the attack mode and the password format is listed (to save time so that illustrations are possible), and (-O and -w 3) arguments are used to optimize performance. 
If passwords are salted, it will be of the format HASH:SALT, matching the hashcat input format.

A copy of the hashcat executable is also included.