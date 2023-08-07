#!python3

import PIL.Image
import os
import typer
from typing_extensions import Annotated

def get_colors_in_image(image_path: str, topn=128):
    image = PIL.Image.open(image_path).convert("RGB")
    colors = image.getcolors(maxcolors=5000)  # [(nb,(r,g,b))]
    sortedcolors = sorted(colors, key=lambda x: x[0], reverse=True)
    return sortedcolors[:topn]


def rgb_to_hex(rgb):
    r, g, b = rgb
    hex_code = "#%02x%02x%02x" % (r, g, b)
    return hex_code.upper()


def output_to_stdoud(colors):
    print(", ".join(map(lambda c: f"{c[0]}: {rgb_to_hex(c[1])}", colors)))


def output_to_html(colors, filename):
    with open(filename, "w") as f:
        f.write("<html><table style='border: 1px solid black; padding: 15px;'>")
        f.write("".join(map(lambda c: f"<tr><td>{c[0]}</td><td>{rgb_to_hex(c[1])}</td><td style='background-color:{rgb_to_hex(c[1])};'>lorem ipsum</td></tr>", colors)))
        f.write("</table></html>")
        f.close()


def main(image_path: str, nbcolors: Annotated[int, typer.Argument()] = 10, html_output: Annotated[str, typer.Argument()] = "colors.html"):
    colors = get_colors_in_image(image_path, nbcolors)
    output_to_stdoud(colors)
    output_to_html(colors, html_output)


if __name__ == "__main__":
    typer.run(main)
