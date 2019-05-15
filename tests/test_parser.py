### import libraries for testing
import pytest

### import items to be tested
from easy_geoparsing.parser import EasyCountryParser

### define fixtures
@pytest.fixture
def ez_parser():
    """
    Fixture provides an instance of EasyCountryParser
    """
    return EasyCountryParser()


### define tests
@pytest.mark.parametrize(
    "attribute",
    [
        ("tld_to_a2c"),
        ("tld_to_a3c"),
        ("iso2to3"),
        ("iso3to2"),
        ("a2c_map"),
        ("a3c_map"),
    ],
)
def test_expected_attributes_exist(ez_parser, attribute):
    """ tests the the __init__ sequence has the expected effect """
    assert hasattr(ez_parser, attribute)


def test_retrieve_country(ez_parser):
    """ tests that the parser method can retrieve a 2char ISO code """
    isocode = ez_parser.retrieve_country("London")
    assert isocode == "GB"


@pytest.mark.parametrize("tld, iso", [(".uk", "GB"), (".scot", "GB"), (".gov", "US")])
def test_tld_a2c_map(ez_parser, tld, iso):
    """ tests that the TLD map generated behaves as expected """
    assert iso == ez_parser.tld_to_a2c.get(tld)


@pytest.mark.parametrize(
    "tld, iso", [(".uk", "GBR"), (".scot", "GBR"), (".gov", "USA")]
)
def test_tld_a3c_map(ez_parser, tld, iso):
    """ tests that the TLD map generated behaves as expected """
    assert iso == ez_parser.tld_to_a3c.get(tld)


def test_codemaps(ez_parser):
    """ tests that the code maps work as anticipated """
    assert ez_parser.iso2to3["GB"] == "GBR"
    assert ez_parser.iso3to2["GBR"] == "GB"


def test_countrymaps(ez_parser):
    assert ez_parser.a2c_map["MK"] == "Macedonia"
    assert ez_parser.a3c_map["MKD"] == "Macedonia"
