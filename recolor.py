#!python3

import sys, os, re

#https://pinetools.com/invert-image-colors
#https://stackoverflow.com/questions/22252472/how-can-i-change-the-color-of-an-svg-element

def rename(imgpath):
    path, filename = os.path.split(imgpath)
    name, ext  = filename.split(".")
    newname = f"{name}-mod.{ext}"
    return os.path.join(path, newname)

def recolorSVG(imgpath,color):
    # read file
    infile = open(imgpath, "r")
    content = infile.read()
    # style    	.white{fill:#FFFFFF;}
    content = re.sub('</style>',r'.mycolor{fill:#'+color+';}\n</style>', content)
    # add style to <path
    content = re.sub('<path',r'<path class="mycolor" ', content)
    # add style to <polygon
    content = re.sub('<polygon',r'<polygon class="mycolor" ', content)
    # output
    outfile = open(rename(imgpath), "w")
    outfile.write(content)
    outfile.close()

if __name__ == "__main__":
    args = sys.argv[1:]
    color = 'FFFFFF'
    if len(args) > 1:
        color = args[1]
        assert len(color)==6, "Color should be RRGGBB"
    if len(args) > 0:
        filename = args[0]
        assert os.path.isfile(filename), "File not found"
        _, ext  = filename.split(".")
        assert ext.lower() == "svg", "Requires SVG file"
        recolorSVG(filename,color)