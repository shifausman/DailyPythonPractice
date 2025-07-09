
#from PIL import Image

#blackandwhite
"""from PIL import Image

img = Image.open("IMG-20250209-WA0025[1].jpg")
bw = img.convert("L") 
bw = bw.point(lambda x: 0 if x < 128 else 255, '1') 
bw.show()
bw.save("bw_image.jpg")"""

#grayscale
"""from PIL import Image

img = Image.open("IMG-20250209-WA0025[1].jpg")
gray = img.convert("L") 
gray.show()
gray.save("gray_image.jpg")"""


#Blur
"""from PIL import Image, ImageFilter

img = Image.open("IMG-20250209-WA0025[1].jpg")
blurred = img.filter(ImageFilter.GaussianBlur(radius=5))  # Try radius=2, 5, etc.
blurred.show()"""

#Edge Detection
"""from PIL import Image, ImageFilter

img = Image.open("IMG-20250209-WA0025[1].jpg")
edges = img.filter(ImageFilter.FIND_EDGES)
edges.show()"""


            
            



