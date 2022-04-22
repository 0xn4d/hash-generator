import hashlib

print('')
string = input("let me know the text to generate the hash: ")
print('')

choice = int(input(''' --- choose the hash type ---

   1) MD5
   2) SHA1
   3) SHA256
   4) SHA512

 give me the number of your choice: '''))
print('')

if choice == 1:
   result = hashlib.md5(string.encode('utf-8'))
   print('the MD5 hash for the string', string, 'is: ', result.hexdigest())
elif choice == 2:
   result = hashlib.sha1(string.encode('utf-8'))
   print('the SHA1 hash for the string', string, 'is: ', result.hexdigest())
elif choice == 3:
   result = hashlib.sha256(string.encode('utf-8'))
   print('the SHA256 hash for the string', string, 'is: ', result.hexdigest())
elif choice == 4:
   result = hashlib.sha512(string.encode('utf-8'))
   print('the SHA512 hash for the string', string, 'is: ', result.hexdigest())
else:
   print('something is wrong...')
