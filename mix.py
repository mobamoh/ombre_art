from PIL import Image

from art import Artwork

art1 = Artwork()
art2 = Artwork()

new_art = Image.blend(art1.img, art2.img, 0.5)
new_art.save("mix.png")
