from src.postcode import postcode_area

def test_compare_postcode():
    assert postcode_area("B15 2TT") == "B"
    assert postcode_area("BA1 1AA") == "BA"
