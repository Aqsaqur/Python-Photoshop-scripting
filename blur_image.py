from PIL import Image, ImageFilter

# Open the image
img_path = r"C:\Users\HP\Pictures\Screenshots\me.png"
img = Image.open(img_path)

# Apply Gaussian blur with a radius of 5
blurred_img = img.filter(ImageFilter.GaussianBlur(5))

# Save the blurred image
blurred_img.save(r"C:\Users\HP\Pictures\Screenshots\me2.png")

# Optionally, display the blurred image
print("Image Edited successfully")

