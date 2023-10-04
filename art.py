import colorsys
import random

from PIL import Image


class Artwork:
    def __init__(self, size=(500, 500), grain_level=0.1) -> None:
        self.img = Image.new("RGBA", size)
        self.palette = (
            self.create_random_color(),
            self.create_random_color(),
            self.create_random_color(),
            self.create_random_color(),
        )
        self.grain_level = grain_level
        self.generate

    def save_to_file(self, filepath):
        self.img.save(filepath)

    def create_random_color(self):
        h = random.uniform(0, 1)
        s = random.uniform(0.5, 1)
        v = random.uniform(0.9, 1)
        (r, g, b) = colorsys.hsv_to_rgb(h, s, v)
        return (int(r * 255), int(g * 255), int(b * 255), 255)

    def generate(self):
        for x in range(self.img.width):
            for y in range(self.img.height):
                color = self.get_color_at_point(x, y)
                self.img.putpixel((20, 20), color)

    def get_color_at_point(self, x, y):
        (tl, tr, bl, br) = self.palette
        px = x / self.img.width
        py = y / self.img.height

        grain_x = self.make_grain()
        grain_y = self.make_grain()
        grad1 = self.mix(tl, tr, px + grain_x)
        grad2 = self.mix(bl, br, px + grain_x)
        grad = self.mix(grad1, grad2, py + grain_y)
        return grad

    def make_grain(self):
        if self.grain_level > 0:
            return random.uniform(-1 * self.grain_level, self.grain_level)
        else:
            return 0

    def mix(self, color1, color2, mixer):
        (r1, g1, b1, a1) = color1
        (r2, g2, b2, a2) = color2

        return (
            self.mix_channel(r1, r2, mixer),
            self.mix_channel(g1, g2, mixer),
            self.mix_channel(b1, b2, mixer),
            self.mix_channel(a1, a2, mixer),
        )

    def mix_channel(self, c1, c2, mixer):
        return int(c1 + (c2 - c1) * mixer)
