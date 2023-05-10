#!python3

import sys
import os
import re

# https://pinetools.com/invert-image-colors
# https://stackoverflow.com/questions/22252472/how-can-i-change-the-color-of-an-svg-element


def rename(imgpath):
    path, filename = os.path.split(imgpath)
    name, ext = filename.split(".")
    newname = f"{name}-mod.{ext}"
    return os.path.join(path, newname)


def resizeSVG(imgxml, originalsize, targetsize):
    viewBoxShift = int((targetsize-originalsize)/2)
    imgxml = re.sub(f'viewBox="0 0 {originalsize} {originalsize}"',
                    f'viewBox="-{viewBoxShift} -{viewBoxShift} {targetsize} {targetsize}"', imgxml)
    imgxml = re.sub(f'0 0 {originalsize} {originalsize}',
                    f'0 0 {targetsize} {targetsize}', imgxml)
    imgxml = re.sub(f'"{originalsize}px"', f'"{targetsize}px"', imgxml)
    imgxml = re.sub(f'"{originalsize}"', f'"{targetsize}"', imgxml)
    return imgxml


def recolorSVG(imgxml, color):
    # style    	.white{fill:#FFFFFF;}
    imgxml = re.sub('</style>', r'.mycolor{fill:#'+color+';}\n</style>', imgxml)
    # add style to <path
    imgxml = re.sub('<path', '<path class="mycolor" ', imgxml)
    # add style to <polygon
    imgxml = re.sub('<polygon', '<polygon class="mycolor" ', imgxml)
    return imgxml


def modifySVG(imgpath, color, originalsize, targetsize):
    # read file
    infile = open(imgpath, "r")
    content = infile.read()
    if color != None:
        content = recolorSVG(content, color)
    if targetsize != None:
        content = resizeSVG(content, originalsize, targetsize)
    # output
    outfile = open(rename(imgpath), "w")
    outfile.write(content)
    outfile.close()


def getsize(imgpath):
    import xml.etree.ElementTree as ET
    tree = ET.parse(imgpath)
    svgroot = tree.getroot()
    sizepx = svgroot.get("width")
    size = re.sub('px', "", sizepx)
    return int(size)


if __name__ == "__main__":
    args = sys.argv[1:]
    print(args)
    color = originalsize = targetsize = None
    if len(args) > 0:
        filename = args[0]
        assert os.path.isfile(filename), f"File not found {filename}"
        _, ext = filename.split(".")
        assert ext.lower() == "svg", "Requires SVG file"
        if len(args) > 1:
            color = args[1]
            assert len(color) == 6, f"Color should be RRGGBB, got {color}"
        if len(args) > 2:
            originalsize = getsize(filename)
            targetsizearg = args[2]
            assert targetsizearg.isdigit(), f"Size should be a number, got {targetsizearg}"
            targetsize = int(targetsizearg)
            assert targetsize >= originalsize, f"Size should be bigger than original size of {originalsize}"
        modifySVG(filename, color, originalsize, targetsize)
