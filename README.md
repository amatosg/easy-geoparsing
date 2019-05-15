easy-geoparsing
---

Easy-to-use module for streamlined parsing of countries from plaintext locations and top-level domains, plus manipulation of country names and ISO 2 & 3 character codes.

## installation

In future we will make this public and put it on PyPI.

## setup

If you've cloned the repository, the best way to make it work is using `pipenv`

To get it, you can do:

`pip install pipenv --upgrade`

Then, in the top level directory `easy-geoparsing` do:

`pipenv install --dev`

(The `--dev` flag will install pytest into the virtual environment)

## usage

### GETTING STARTED

Do the following to get the parser utilities:

```
from easy_geoparsing.parser import EasyCountryParser

ez_parser = EasyCountryParser()
```

or, if you don't want to use our alternative names for some of the countries (i.e. you want to exactly follow the RESTcountries standard)

`ez_parser = EasyCountryParser(altnames=False)`

The `EasyCountryParser` class provides utilities, based on the data from the RESTcountries API and the GeoText natural-language parser library, for easily extracting and handling country names and codes.

### PARSER RESOURCES

The parser is initialised with the following resources:

    - `.data`       - pandas DataFrame containing RESTcountries data
    - `.tld_to_a2c` - python dict, maps TLDs to 2-character ISO codes
    - `.tld_to_a3c` - python dict, maps TLDs to 3-character ISO codes
    - `.iso2to3`    - python dict, maps 2-character ISO codes to 3
    - `.iso3to2`    - python dict, maps 3-character ISO codes to 2
    - `.a2c_map`    - python dict, maps 2-char ISO codes to full names
    - `.a3c_map`    - python dict, maps 3-char ISO codes to full names

### PARSER METHODS

The parser has the following methods for handling locations data:

    - .retrieve_country - parses plaintext for extractable 2-character ISO codes for countries (which can then be manipulated using the mappers above)
