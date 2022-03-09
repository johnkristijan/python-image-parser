from PIL import Image

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

print('--- running parser.py ---')

img = Image.open('ranheim_heightmap-halved.png')
pixels = img.convert('RGBA').load()
width, height = img.size

print(f'Image size: {width}x{height} px')

## offset
ox = 0
oy = 62
oz = 0

tall = 1

lines = ['#!/bin/sh']

for x in range(width):
    for y in range(height):
        r, g, b, a = pixels[x, y]

        # rgb 0 0 0 => BLACK (0m height)
        # rgb 255 255 255 => WHITE (65 meter height)

        height_diff_black_to_white = 65
        factor = 255 / height_diff_black_to_white
        # avr = (r + b + g) / 3
        avr = r
        tall = round(avr / factor)

        # axis transformations
        dx = y # -x
        dy = 0
        dz = -x # -y
        # result points
        rx = ox + dx
        ry = oy + dy
        ry_end = ry + tall
        rz = oz + dz

        # clear with air before fill
        oy_end = oy + height_diff_black_to_white
        fill_command = f'./mcc.sh "/fill {rx} {oy} {rz} {rx} {oy_end} {rz} air"'
        lines.append(fill_command)

        if tall == 1:
            # sand level limit
            fill_command = f'./mcc.sh "/fill {rx} {ry} {rz} {rx} {ry_end} {rz} sandstone"'
        elif tall == 0:
            # sea level limit
            fill_command = f'./mcc.sh "/fill {rx} {ry} {rz} {rx} {ry_end} {rz} water"'
        else:
            if r != g:
                # print(f'Light blue? RGB: {r} {g} {b}')
                fill_command = f'./mcc.sh "/fill {rx} {ry} {rz} {rx} {ry_end} {rz} stone"'
            else:
                fill_command = f'./mcc.sh "/fill {rx} {ry} {rz} {rx} {ry_end} {rz} grass_block"'

        lines.append(fill_command)

        
        # else:
        #     print(f'x: {x}, y: {y}, tall: {tall}')

with open('buildcommands.txt', 'w') as f:
    f.write('\n'.join(lines))
