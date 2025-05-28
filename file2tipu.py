from PIL import Image
import math
import sys

def file_to_tipuqr_rgba(file_path, output_path="tipuqr.png"):
    with open(file_path, "rb") as f:
        data = f.read()

    length = len(data)

    size = math.ceil(math.sqrt(length / 4))

    total_bytes = size * size * 4
    padded_data = data + bytes([0] * (total_bytes - length))

    pixels = []
    for i in range(0, total_bytes, 4):
        r = padded_data[i]
        g = padded_data[i + 1]
        b = padded_data[i + 2]
        a = padded_data[i + 3]
        pixels.append((r, g, b, a))

    img = Image.new("RGBA", (size, size))
    img.putdata(pixels)
    img.save(output_path, optimize=True)

    print(f"Tipu RGBA QR code saved to file: {output_path}")
    print(f"Original file size: {length} bytes")
    print(f"Tipu QR code size: {size}x{size} pixels")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python file2tipu.py file")
    else:
        file_to_tipuqr_rgba(sys.argv[1])
