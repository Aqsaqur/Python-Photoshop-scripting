#  Build a Python script where:

# The user selects an image.

# Chooses whether to apply Black & White, Blur, or Save as a different format.

# You display the output file.

from PIL import Image, ImageFilter

img_path = input("Enter the image file path: ")

img = Image.open(img_path)

# Show user the options
print("\nWhat do you want to do with this image?")
print("1. Convert to Black & White")
print("2. Apply Gaussian Blur")
print("3. Rotate the Image")
choice = input("Enter your choice (1/2/3): ")

# Perform the selected operation
if choice == '1':
    edited_img = img.convert('L')
    edited_img.save("output_bw.png")
    print("Converted to Black & White and saved as 'output_bw.png'.")

elif choice == '2':
    radius = int(input("Enter blur radius (e.g., 5): "))
    edited_img = img.filter(ImageFilter.GaussianBlur(radius))
    edited_img.save("output_blur.png")
    print(f"Applied Gaussian Blur and saved as 'output_blur.png'.")

elif choice == '3':
    angle = int(input("Enter rotation angle (e.g., 90): "))
    edited_img = img.rotate(angle)
    edited_img.save("output_rotate.png")
    print(f"Rotated the image and saved as 'output_rotate.png'.")

else:
    print("Invalid choice!")

print("✅ Image processing complete!")
