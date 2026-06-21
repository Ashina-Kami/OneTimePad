# OneTimePad
OneTimePad encryption over 95 characters in Python

## What is it? 
One Time Pad (OTP) is an encryption technique where each character 
is encrypted using a randomly generated key.

Given one character list, every character in the original message is shifted by the position of the corresponding key character in the character list.

* Theoretically unbreakable

## How to use?
### To encrypt
### Encrypt Message
- Enter message to encrypt
- Store key
### Encrypt File
- Enter filepath
- Enter save location for encrypted file
- Store key
### To decrypt
### Decrypt Message
- Enter key
- Enter encrypted message
### Decrypt File
- Enter filepath
- Enter Key
- Enter save location for decrypted file


## Example (outdated v1)
### ✔️ Correct Use
**Example 1**
- Message: I like Pizza
- key: <izU~LGSpk6b
- Encrypted Message: tTH4d;O(Ok
-  Decrypted Message: I like Pizza
  
**Example 2**
-  Message: 1 like Pizza
-  key: )aDnH;U4&'J'
-  Encrypted Message: DLLxLz2>}'
-  Decrypted Message: 1 like Pizza
  
**Example 3**
- Message: I Lik3 P1zz@
- key: M63ROEU?e7jU
- Encrypted Message: +b"1b*fnDW
- Decrypted Message: I Lik3 P1zz@
  
### ⚠️ Incorrect Use
**Example 1**
-  Message: I Would Like 1 Pizza
-  key: IG>wSOAk=4"slNxr_C"*
-  Encrypted Message: '=bQ3R"s{8w7t#Wr
-  Decrypted Message: I Would Like1 Pizza (space before number is lost)

**Example 2**
- Message: I would like pizza
- key: ]>+J\rn'*}fFn6IRYF
- Encrypted Message: Aj]3cuy/>cuNM@I
- Decrypted Message: Iwouldlikepizza (space between word is lost)
