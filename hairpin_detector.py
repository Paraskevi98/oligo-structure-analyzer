primer = "CGGCGGCCTCTAAA"
template = "GGTCGGGGTGGATGCATGCGAT"
# Check if two bases can pair (Watson-Crick)
def is_pair(base1, base2):
    pairs = {"A":"T", "T":"A", "C":"G", "G":"C"}
    return pairs.get(base1) == base2

# Relaxed stem-loop detection
def find_relaxed_loops(primer, template, min_stem=1, min_loop=0, max_loop=20):
    results = []
    n = len(primer)
    m = len(template)
    
    # Slide the primer along template
    for t_start in range(m - n + 1):
        for i in range(n):
            for j in range(i + min_stem + min_loop, n):
                stem_len = 0
                mismatches = 0
                # Try forming a stem with some allowed mismatches
                while i + stem_len < j - stem_len:
                    if is_pair(primer[i + stem_len], template[t_start + j - stem_len]):
                        stem_len += 1
                    else:
                        mismatches += 1
                        if mismatches > 1:  # allow 1 mismatch
                            break
                        stem_len += 1
                loop_len = j - i + 1 - 2*stem_len
                if stem_len >= min_stem and min_loop <= loop_len <= max_loop:
                    left_stem = primer[i:i+stem_len]
                    right_stem = template[t_start + j - stem_len + 1 : t_start + j + 1][::-1]
                    loop = primer[i+stem_len:j-stem_len+1]
                    results.append({
                        "template_start": t_start,
                        "primer_start": i,
                        "primer_end": j,
                        "stem_length": stem_len,
                        "left_stem": left_stem,
                        "right_stem": right_stem,
                        "loop": loop
                    })
    return results

# Detect loops
loops = find_relaxed_loops(primer, template)

# Print results
if loops:
    print("Primer-template relaxed stem-loop regions:\n")
    for idx, l in enumerate(loops):
        print(f"Loop {idx+1}:")
        print(f" Primer positions: {l['primer_start']} - {l['primer_end']}")
        print(f" Template start: {l['template_start']}")
        print(f" Stem: {l['left_stem']} --- {l['right_stem']}")
        print(f" Loop: {l['loop']}\n")
else:
    print("No relaxed loops found.")

loops_sorted = sorted(loops, key=lambda x: x['stem_length'], reverse=True)

for l in loops_sorted[:5]:   # show top 5
    print(f"Stem length: {l['stem_length']}")
    print(f"Stem: {l['left_stem']} --- {l['right_stem']}")
    print(f"Loop: {l['loop']}\n")
