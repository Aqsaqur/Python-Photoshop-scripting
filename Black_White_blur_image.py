from PIL import Image, ImageFilter

# Method 1
img_path = r"C:\Users\HP\Pictures\Screenshots\me.png"
img = Image.open(img_path)

bw_img = img.convert('L')

blurred_img = bw_img.filter(ImageFilter.BLUR)

blurred_img.save(r"C:\Users\HP\Pictures\Screenshots\me4.png")

print("Image edited successfully")

# Method 2
img_path = r"C:\Users\HP\Pictures\Screenshots\me.png"
img = Image.open(img_path)

bw_img = img.convert('L')

blurred_img = bw_img.filter(ImageFilter.GaussianBlur(radius=5))

blurred_img.save(r"C:\Users\HP\Pictures\Screenshots\me4.png")

print("Image edited successfully")

