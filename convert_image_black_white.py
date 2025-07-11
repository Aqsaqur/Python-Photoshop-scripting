from PIL import Image

img_path = r"C:\Users\HP\Pictures\Screenshots\me.png"
img = Image.open(img_path)

bw_image = img.convert('L')

bw_image.save(r"C:\Users\HP\Pictures\Screenshots\me1.png")

print("Image successfully converted to black and white")

