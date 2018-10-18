# ios-icons-converter

Convert SVGs to PNGs of all the sizes required by the appstore.

## Prerequisites

* python >= 3
* imagemagik

### Installing

On MacOS:

```sh
brew install python3
brew install imagemagik --with-librsvg
```

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
