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

```
python recolor.py ibm--datastage.svg 00FFFF
```

## Resources

[stackoverflow - how-can-i-change-the-color-of-an-svg-element](#https://stackoverflow.com/questions/22252472/how-can-i-change-the-color-of-an-svg-element)
