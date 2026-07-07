import qrcode

text = input("Enter text or URL: ")

img = qrcode.make(text)

name = input("Enter the file name (with .png): ")

path = fr"C:\Users\ruben\OneDrive\Pictures\{name}"

img.save(path)

print(f"QR Code saved as {path}")