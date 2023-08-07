# Manually change colors in a .svg file

## Manual steps

Open the svg file with a text (or XML) editor

- in the `<style>` section, add a style with your color, here white.

```
	.white{fill:#FFFFFF;}
```

- in each shape tag, add the style, ex:

`<polygon points="22,2 22,4 26.6,4 11,19.6 12.4,21 28,5.4 28,10 30,10 30,2 "/>`

=>

`<polygon class="white" points="22,2 22,4 26.6,4 11,19.6 12.4,21 28,5.4 28,10 30,10 30,2 "/>`

## Python script

Arguments:

- svg file
- target color - optional
- target size - optional

Example:

```
python recolor.py ibm--datastage.svg 00FFFF 48
```

## Resources

- [stackoverflow - how-can-i-change-the-color-of-an-svg-element](#https://stackoverflow.com/questions/22252472/how-can-i-change-the-color-of-an-svg-element)
- [SVG ViewBox](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/viewBox)
- [Python XML](https://docs.python.org/3/library/xml.etree.elementtree.html)