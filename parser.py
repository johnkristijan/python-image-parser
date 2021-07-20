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
oy = 71
oz = 800

tall = 5

lines = ['#!/bin/sh']

for x in range(width):
    for y in range(height):
        r, g, b, a = pixels[x, y]
        # skip white pixels
        if r != 255 and g != 255 and b != 255:
            # print(f'RGB: {r} {g} {b}')
            #print 'x = %s, y = %s, hex = %s' % (x, y, rgb2hex(r, g, b))

            # black pixel
            if r == 0 and g == 0 and b == 0:
                # axis transformations
                dx = y # -x
                dy = 0
                dz = x # -y
                # result points
                rx = ox + dx
                ry = oy + dy
                ry_end = ry + tall
                rz = oz + dz

                fill_command = f'./mcc.sh "/fill {rx} {ry} {rz} {rx} {ry_end} {rz} stone"'
                lines.append(fill_command)
                # print(fill_command)
            else:
                print(f'RGB: {r} {g} {b}')

with open('buildcommands.txt', 'w') as f:
    f.write('\n'.join(lines))
