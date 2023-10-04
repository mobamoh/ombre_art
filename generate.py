import os

from PIL import Image

print("generating art!")
os.makedirs("output", exist_ok=True)
for i in range(1, 11):
    filepath = os.path.join("test", f"test-{i}.png")
    img = Image.new("RGBA", (500, 500), color=(255, 255, 0, 255))
    img.save(filepath)
