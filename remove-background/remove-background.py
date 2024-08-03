from rembg import remove
from PIL import Image

input_path = '<path-for-original-image>/family.jpg'
output_path = '<path-for-generated-image>/family.png'

try:
    inputImage = Image.open(input_path)
    outputImage = remove(inputImage)
    outputImage.save(output_path)
    Image.open(output_path)

except Exception as e:
    print(f"An error occurred: {e}")