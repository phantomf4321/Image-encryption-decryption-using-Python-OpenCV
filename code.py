import cv2
import numpy

Key_1 = numpy.random.randint(0, 255, size=[300, 500], dtype=numpy.uint8)
cv2.imwrite("Key_1.jpg", Key_1)  # Save key

img_originalData = cv2.imread("shamaeejoons.png", -1)
img_originalData = cv2.resize(img_originalData, (500, 300))
cv2.imshow("OriginalData", img_originalData)

img_originalData_B = img_originalData[:, :, 0]
img_originalData_G = img_originalData[:, :, 1]
img_originalData_R = img_originalData[:, :, 2]


ciphertext_B = cv2.bitwise_xor(img_originalData_B, Key_1)
ciphertext_G = cv2.bitwise_xor(img_originalData_G, Key_1)
ciphertext_R = cv2.bitwise_xor(img_originalData_R, Key_1)
ciphertext_BGR = cv2.merge([ciphertext_B, ciphertext_G, ciphertext_R])

cv2.imshow("Ciphertext", ciphertext_BGR)  # Show encrypted pictures

decryptedtext_B = cv2.bitwise_xor(ciphertext_B, Key_1)  # XOR the B-channel of the ciphertext with the key
decryptedtext_G = cv2.bitwise_xor(ciphertext_G, Key_1)  # XOR the G-channel of the ciphertext with the key
decryptedtext_R = cv2.bitwise_xor(ciphertext_R, Key_1)  # XOR the R channel of the ciphertext with the key
decryptedtext_BGR = cv2.merge([decryptedtext_B, decryptedtext_G, decryptedtext_R])  # Merge channel
cv2.imshow("Decryptedtext", decryptedtext_BGR)  # Show decrypted pictures
