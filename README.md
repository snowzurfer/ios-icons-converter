# ios-icons-converter

Convert SVGs to PNGs of all the sizes required by the appstore.

## Prerequisites

* python >= 3
* imagemagick

### Installing

On MacOS:

```sh
brew install python3
brew install https://github.com/Homebrew/homebrew-core/raw/46a2ef7c9f0380b8e19f8dfe37270caa27581353/Formula/imagemagick.rb --with-librsvg
```

The latter seems to be [the simplest](https://stackoverflow.com/a/55637475/495611) way to install `imagemagick` with `librsvg` as of May 2020. If you get an error about `libldtl` when installing, try reinstalling `libtool` as suggested [here](https://github.com/Homebrew/legacy-homebrew/issues/27226):

```sh
brew remove libtool && brew install libtool
```

Then try installing `imagemagick` again.

## Example usage

```sh
python3 convert.py ~/pictures/my-svg-logo.svg ~/projects/icons/
```
or

```sh
python3 convert.py ~/pictures/my-svg-logo.svg ~/projects/icons/ --output_name my_base_name
```

## Output images sizes

The sizes have been hardcoded to the ones required by iOS projects as of XCode
10.0. If they need to be changed, simply change them in `convert.py:convert`.

## License

See [LICENSE](LICENSE)
