from PIL import Image
import sys

def tipuqr_rgba_to_file(image_path, extension="bin"):
    img = Image.open(image_path).convert("RGBA")

    pixels = list(img.getdata())
    bytes_out = bytearray()

    for r, g, b, a in pixels:
        bytes_out.append(r)
        bytes_out.append(g)
        bytes_out.append(b)
        bytes_out.append(a)

    output_path = f"recovered_file.{extension}"
    with open(output_path, "wb") as f:
        f.write(bytes_out)

    print(f"✅ Tipu RGBA QR decoded and saved to file: {output_path}")
    print(f"📦 Recovered size: {len(bytes_out)} bytes")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tipu2file.py qrcode_image.png [extension_without_dot]")
    else:
        image_path = sys.argv[1]
        extension = sys.argv[2] if len(sys.argv) > 2 else "bin"
        tipuqr_rgba_to_file(image_path, extension)
