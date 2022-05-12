# caesar-cipher
### lab 18
### Harvey Francois

### Overview
Cryptographic classic - the Caesar Cipher.
Devise a method to encrypt a message that can then be decrypted when supplied with the corresponding key.
Devise a way to decipher the encrypted message event when you do NOT have the key!

### Feature Tasks
Create an encrypt function that takes in a plain text phrase and a numeric shift.
the phrase will then be shifted that many letters.

shifts that exceed 26 should wrap around.
shifts that push a letter out or range should wrap around.

Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back 
to its original form when correct key is supplied.

create a crack function that will decode the cipher so that an encrypted message can be transformed into its original 
state WITHOUT access to the key.

Devise a method for the computer to determine if code was broken with minimal human guidance.