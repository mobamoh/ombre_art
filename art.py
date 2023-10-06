import colorsys
import os
import random

from noise import pnoise2
from PIL import Image, ImageDraw, ImageFont


class Artwork:
    def __init__(
        self,
        size=(500, 500),
        grain_level=0.1,
        noise_level=1.5,
        noise_shift=2.0,
        debug=True,
    ) -> None:
        self.img = Image.new("RGBA", size)
        self.palette = (
            self.create_random_color(),
            self.create_random_color(),
            self.create_random_color(),
            self.create_random_color(),
        )
        self.grain_level = grain_level
        self.noise_base = random.randint(0, 999)
        self.noise_level = noise_level
        self.noise_shift = noise_shift
        self.debug = debug
        self.generate()
        if self.debug:
            self.add_debug()

    def save_to_file(self, filepath):
        self.img.save(filepath)

    def create_random_color(self):
        h = random.uniform(0, 1)
        s = random.uniform(0.5, 1)
        v = random.uniform(0.9, 1)
        (r, g, b) = colorsys.hsv_to_rgb(h, s, v)
        return (int(r * 255), int(g * 255), int(b * 255), 255)

    def get_random_points(self):
        points = []
        for x in range(self.img.width):
            for y in range(self.img.height):
                points.append((x, y))
        random.shuffle(points)
        return points

    def generate(self):
        for x, y in self.get_random_points():
            color = self.get_color_at_point(x, y)
            self.img.putpixel((x, y), color)

    def get_color_at_point(self, x, y):
        (tl, tr, bl, br) = self.palette
        px = x / self.img.width
        py = y / self.img.height

        grain_x = self.make_grain()
        grain_y = self.make_grain()
        noise_x = self.make_noise(px, py)
        noise_y = self.make_noise(px, py)

        grad1 = self.mix(tl, tr, px + grain_x + noise_x)
        grad2 = self.mix(bl, br, px + grain_x + noise_x)
        grad = self.mix(grad1, grad2, py + grain_y + noise_y)
        return grad

    def make_grain(self):
        if self.grain_level > 0:
            return random.uniform(-1 * self.grain_level, self.grain_level)
        else:
            return 0

    def mix(self, color1, color2, mixer):
        (r1, g1, b1, a1) = color1
        (r2, g2, b2, a2) = color2
        mixer = max(0, min(mixer, 1))
        return (
            self.mix_channel(r1, r2, mixer),
            self.mix_channel(g1, g2, mixer),
            self.mix_channel(b1, b2, mixer),
            self.mix_channel(a1, a2, mixer),
        )

    def mix_channel(self, c1, c2, mixer):
        return int(c1 + (c2 - c1) * mixer)

    def make_noise(self, px, py):
        return self.noise_level * pnoise2(
            px * self.noise_shift, py * self.noise_shift, base=self.noise_base
        )

    def add_debug(self):
        drawer = ImageDraw.Draw(self.img)
        (tl, tr, bl, br) = self.palette
        drawer.rectangle([16, 16, 24, 24], fill=tl)
        drawer.rectangle([32, 16, 40, 24], fill=tr)
        drawer.rectangle([48, 16, 56, 24], fill=bl)
        drawer.rectangle([64, 16, 72, 24], fill=br)

        messages = [
            "Generated art: artist Mo Bamoh",
            f"Grain Level:{self.grain_level}",
            f"Noise Level:{self.noise_level}",
            f"Noise Shift:{self.noise_shift}",
        ]
        font = ImageFont.truetype("ibm-plex-mono.ttf", 16)

        drawer.multiline_text(
            (16, 16), "\n".join(messages), font=font, fill=(0, 0, 0, 255)
        )


if __name__ == "__main__":
    print("generating grad artwort....")
    os.makedirs("art_output", exist_ok=True)
    filepath = os.path.join("art_output", "grads.png")

    art = Artwork()
    art.save_to_file(filepath)
