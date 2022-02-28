from gccalc import calc_gc_content
import pytest

def test_mid_gc():
    seq = "GCGCGCATATAT"
    obs = calc_gc_content(seq)
    exp = 50.0
    assert obs == exp

def test_high_gc():
    seq = "GGGGGCCCCC"
    obs = calc_gc_content(seq)
    exp = 100.0
    assert obs == exp

def test_low_gc():
    seq = "ATATATAT"
    obs = calc_gc_content(seq)
    exp = 0.0
    assert obs == exp    

def test_empty_seq():
    seq = ""
    obs = calc_gc_content(seq)
    exp = 0.0
    assert obs == exp

@pytest.mark.skip(reason="Cleaning not yet implemented.")    
def test_invalid_characters():
    seq = "GGGGGCCCCCAAAAATTTTTXXXXX"
    obs = calc_gc_content(seq)
    exp = 50.0
    assert obs == exp
