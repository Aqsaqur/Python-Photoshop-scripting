from PIL import Image, ImageFilter

# Method 1
img_path = r"C:\Users\HP\Pictures\Screenshots\me.png"
img = Image.open(img_path)

sharp = img.filter(ImageFilter.SHARPEN)
blurred_sharp = sharp.filter(ImageFilter.GaussianBlur(3))
blurred_sharp.save(r"C:\Users\HP\Pictures\Screenshots\me(5).png")

print("Image edited successfully")