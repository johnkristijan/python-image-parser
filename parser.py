from PIL import Image

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

print('--- running parser.py ---')

img = Image.open('horgvegen17.gif')
pixels = img.convert('RGBA').load()
width, height = img.size
print(f'Image size: {width}x{height} px')

## offset
ox = 40
oy = 70
oz = 800

lines = ['#!/bin/sh']

for x in range(width):
    for y in range(height):
        r, g, b, a = pixels[x, y]
        # skip white pixels
        if r != 0 and g != 0 and b != 0:
            # print(f'RGB: {r} {g} {b}')
            #print 'x = %s, y = %s, hex = %s' % (x, y, rgb2hex(r, g, b))

            # black pixel
            if r == 255 and g == 255 and b == 255:
                # axis transformations
                dx = x
                dy = 0
                dz = y
                # result points
                rx = ox + dx
                ry = oy + dy
                rz = oz + dz

                fill_command = f'./mcc.sh "/fill {rx} {ry} {rz} {rx} {ry} {rz} dirt"'
                lines.append(fill_command)
                # print(fill_command)
            else:
                print(f'RGB: {r} {g} {b}')

with open('buildcommands.txt', 'w') as f:
    f.write('\n'.join(lines))
