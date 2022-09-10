from PIL import Image

im = Image.open('lvl3.png') # Can be many different formats.
pix = im.load()
size_array = im.size
print(size_array)

height_of_img = 32 # height of one pixel
width_of_img = 32 # width of one pixel

for i in range(16, size_array[0], width_of_img):
  for j in range(16, size_array[1], height_of_img):
    result = pix[j,i]
    if(result != (255, 255, 255)):
      x = (j - 16) / width_of_img
      y = (i - 16) / height_of_img
      string_result = f'[{int(x)}, {int(y)}, obj_wall],' # modifies the result string for use in game engine
      print(string_result)

# print(im.size)  # Get the width and hight of the image for iterating over
# print(pix[1,1])  # Get the RGBA Value of the a pixel of an image
# pix[1,1] = value  # Set the RGBA Value of the image (tuple)
