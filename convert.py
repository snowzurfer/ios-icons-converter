                   # GNU AFFERO GENERAL PUBLIC LICENSE
                      # Version 3, 19 November 2007

# Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

import argparse
import os
import subprocess


def convert_single(svg, output_name, output_dir, base_size,
                   convert_only_1x=False):
    sizes = [
        base_size,
        base_size * 2,
        base_size * 3
            ]

    if convert_only_1x:
        sizes = sizes[:1]

    postfixes = ['@1x', '@2x', '@3x']
    sizes_strings = ['{}x{}'.format(x, x) for x in sizes]

    output_name = output_name + '-{}px-'.format(base_size)

    for i in range(len(sizes)):
        png_name = output_name + postfixes[i] + '.png'
        final_name = os.path.join(output_dir, png_name)

        pRecons = subprocess.Popen([
            'convert', '-background', 'none',
            '-density', '1000',
            '-size', sizes_strings[i],
            svg,
            final_name
        ])
        pRecons.wait()
        print('Converted: {}'.format(png_name))


def convert(svg, output_name, output_dir):
    print('\nConverting...')

    conversion_targets = [
        20,
        29,
        40,
        60,
        76,
        83
    ]

    for target in conversion_targets:
        convert_single(svg, output_name, output_dir, target)

    convert_single(svg, output_name, output_dir, 1024, True)

    print('\nFinished conversion!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='Convert from SVG to PNGs for all the sizes required by the appstore')
    parser.add_argument('svg', help='The SVG to user for the conversion')
    parser.add_argument('output_dir', help='The directory to use to use for the outputs')
    parser.add_argument('--output_name', help='The name to use for the outputs\' prefix')

    args = parser.parse_args()

    output_name = args.svg.split('/')[-1]
    output_name = output_name.split('.')[0]

    if args.output_name is not None:
        output_name = args.output_name.split('/')[-1]
        output_name = output_name.split('.')[0]

    os.makedirs(args.output_dir, exist_ok=True)

    convert(args.svg, output_name, args.output_dir)
