#!/usr/bin/env python3

# GNU AFFERO GENERAL PUBLIC LICENSE
# Version 3, 19 November 2007

# Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

import argparse
import os
from wand.image import Image


def convert_single(
    input_img, output_name, output_dir, base_size, convert_only_1x=False
):
    sizes = [int(base_size), int(base_size * 2), int(base_size * 3)]

    if convert_only_1x:
        sizes = sizes[:1]

    postfixes = ["@1x", "@2x", "@3x"]

    output_name = output_name + "-{}px-".format(base_size)

    for i in range(len(sizes)):
        png_name = output_name + postfixes[i] + ".png"
        final_name = os.path.join(output_dir, png_name)

        with Image(filename=input_img) as img:
            img.resize(sizes[i], sizes[i])
            img.save(filename=final_name)
            print("Converted: {}".format(png_name))

        # if input_img.lower().endswith('.svg'):
        #     pRecons = subprocess.Popen([
        #         'convert',
        #         '-background', 'none',
        #         '-density', '512',
        #         '-gravity', 'center',
        #         '-scale', '80%',
        #         '-resize', sizes_strings[i],
        #         '-extent', sizes_strings[i],
        #         input_img,
        #         final_name
        #     ])
        #     pRecons.wait()
        #     print('Converted: {}'.format(png_name))

        # elif input_img.lower().endswith(('.png', '.jpg', '.jpeg')):
        #     pRecons = subprocess.Popen([
        #         'convert',
        #         '-resize', sizes_strings[i],
        #         input_img,
        #         final_name
        #     ])
        #     pRecons.wait()

        #     print('Resized: {}'.format(png_name))


def convert(input_img, output_name, output_dir):
    print("\nConverting...")

    output_sizes = {
        "iphone": [20, 29, 40, 60],
        "ipad": [20, 29, 40, 76, 83.5],
        "appstore": [1024],
    }

    # Iterate over output sizes and create resized images
    for device, sizes in output_sizes.items():
        for size in sizes:
            output_name_with_device = f"{device}_icon_{output_name}"
            convert_single(input_img, output_name_with_device, output_dir, size)

    # for target in (
    #     conversion_targets_iphone
    #     + conversion_targets_ipad
    #     + conversion_targets_appstore
    # ):
    #     convert_single(input_img, output_name, output_dir, target)

    # convert_single(input_img, output_name, output_dir, 1024, True)

    print("\nFinished conversion!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert from SVG or PNGs to PNGs for all the sizes required by the appstore"
    )
    parser.add_argument("input", help="The input image to use for the conversion")
    parser.add_argument(
        "output_dir", help="The directory to use to use for the outputs"
    )
    parser.add_argument("--output_name", help="The name to use for the outputs' prefix")

    args = parser.parse_args()

    output_name = args.input.split("/")[-1]
    output_name = output_name.split(".")[0]

    if args.output_name is not None:
        output_name = args.output_name.split("/")[-1]
        output_name = output_name.split(".")[0]

    os.makedirs(args.output_dir, exist_ok=True)

    convert(args.input, output_name, args.output_dir)
