import os

from PIL import Image

from art import Artwork
from blocks import BlocksArtwork
from circles import CirclesArtwork
from lines import LinesArtwork

print("generating art...")
os.makedirs("art_output", exist_ok=True)

for i in range(1, 4):
    filepath = os.path.join("art_output", f"grad-{i}.png")
    art = Artwork()
    art.save_to_file(filepath)

for i in range(1, 4):
    filepath = os.path.join("art_output", f"cicles-{i}.png")
    art = CirclesArtwork()
    art.save_to_file(filepath)

for i in range(1, 4):
    filepath = os.path.join("art_output", f"lines-{i}.png")
    art = LinesArtwork()
    art.save_to_file(filepath)

for i in range(1, 4):
    filepath = os.path.join("art_output", f"blocks-{i}.png")
    art = BlocksArtwork()
    art.save_to_file(filepath)
