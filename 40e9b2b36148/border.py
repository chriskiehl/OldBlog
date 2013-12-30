from PIL import Image, ImageOps 

im = Image.open('asdf.png')
im = ImageOps.crop(im,4)
bordered_im = ImageOps.expand(im, 3, (255,255,255))
new_im = ImageOps.expand(bordered_im, 1, (206,206,206))
new_im.save('asdfasdf.png', 'png')
