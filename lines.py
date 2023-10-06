import math
import os
import random

from PIL import ImageDraw

from art import Artwork


class LinesArtwork(Artwork):
    def generate(self):
        drawer = ImageDraw.Draw(self.img)

        for x, y in self.get_random_points():
            color = self.get_color_at_point(x, y)
            lenght = random.randint(2, 10)
            angle = random.uniform(0, 3.141)

            sx = lenght * math.sin(angle)
            sy = lenght * math.cos(angle)
            drawer.line([(x - sx, y - sy), (x + sx, y + sy)], fill=color)


if __name__ == "__main__":
    print("generating lines artwort....")
    os.makedirs("art_output", exist_ok=True)
    filepath = os.path.join("art_output", "lines.png")

    art = LinesArtwork()
    art.save_to_file(filepath)
