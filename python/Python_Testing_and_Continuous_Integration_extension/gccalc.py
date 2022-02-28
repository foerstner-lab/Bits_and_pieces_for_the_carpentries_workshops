def calc_gc_content(seq):
    if len(seq) == 0:
        return 0.0
    gc_count = (seq.upper().count("G") + seq.upper().count("C")) * 100
    gc_value = gc_count / len(seq)
    return gc_value
