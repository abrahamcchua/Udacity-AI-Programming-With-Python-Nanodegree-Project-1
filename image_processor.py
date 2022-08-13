from PIL import Image
import os


os.chdir("unprocessed_images")
# Preprocessed the images
for image in os.listdir():
    img = Image.open(image)
    os.chdir("..")
    os.chdir("uploaded_images")
    img.resize((400, 400))
    img.save(image.split(".")[0] + ".jpg", "jpeg")
    os.chdir("..")
    os.chdir("unprocessed_images")
