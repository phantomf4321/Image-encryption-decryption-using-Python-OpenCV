# Image-encryption-decryption-using-Python-OpenCV

let's look at a basic (binary) calculation problem to help you understand the following things:</br>

<p align="center">
  <img src="https://s6.uupload.ir/files/f0fdd8fc0e56fa8d096deaa1f3990912_2k78.jpg"/>
</p>

This is where the XOR operation is more subtle. Then I will express those a, B, C and D mentioned above in vivid words. A: The original text, B: key, C: ciphertext, D: plaintext, according to the above mathematical expression, can be converted into the following expression: the original text can be combined with the key to obtain the ciphertext (encrypted data), and then if the ciphertext is combined with the key, the plaintext (decrypted data) can be obtained, so as to realize the encryption / decryption of data.

<p align="center">
  <img src="https://s6.uupload.ir/files/key_1_g2f.jpg"/>
</p>

<p align="center">
  <img src="https://s6.uupload.ir/files/alive_parrot_istl.png"/>
</p>

In fact, pictures are stored in the form of 0 and 1 inside the computer, that is to say, we can process pictures in this way.

- we use random numbers to generate a Key (or we can directly use an image as the Key)
- store the key in the file and keep it properly.
- load the image to be encrypted and display it.
-  decompose the picture into three channels (Blue, Green and Red) before encryption, so as to process the three channels in subsequent operations.
-   use the key to perform logical XOR operation with the three channels respectively, and then merge the three channels.
-   get an encrypted picture. Let's preview it and see the encryption effect.
