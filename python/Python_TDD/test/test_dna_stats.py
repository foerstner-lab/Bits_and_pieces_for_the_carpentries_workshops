import sys
sys.path.append(".")
import bio_stats.dna_stats

def test_count_a():
    seq = "AAAATTTT"
    obs = bio_stats.dna_stats.nucleotide_count(seq)
    exp = {"A": 4, "C": 0, "G": 0, "T": 4}
    assert obs == exp

    
