# oligo-structure-analyzer
Python tool to estimate DNA primer ΔG and detect potential stem-loop regions.

---

## Features
- Calculate ΔG of DNA primers using nearest-neighbor thermodynamics.
- Detect potential hairpins (stem-loop structures) in primers.
- Supports relaxed detection with mismatches for realistic scenarios.

---

## Installation

Clone the repository and install any dependencies (if needed):

```bash
git clone https://github.com/paraskevi98/oligo-structure-analyzer.git
cd oligo-structure-analyzer

## USAGE
#ΔG Calculation
from primer_dg import estimate_dg

sequence = "GAATATACGATGCGT"
dg = estimate_dg(sequence)
print("Estimated ΔG (kcal/mol):", dg)

#Hairpin Detection
from stemloop_finder import find_relaxed_loops

primer = "CGGCGGCCTCTAAA"
template = "GGTCGGGGTGGATGCATGCGAT"

loops = find_relaxed_loops(primer, template)
print("Detected hairpins:", loops)

##Example Output

Estimated ΔG (kcal/mol): -25.36
Detected hairpins: [
    {
        "template_start": 5,
        "primer_start": 3,
        "primer_end": 12,
        "stem_length": 4,
        "left_stem": "CGCG",
        "right_stem": "CGCG",
        "loop": "T"
    },
    ...
]

## Citation

The ΔG nearest-neighbor thermodynamic parameters used in this tool are based on:

SantaLucia Jr, J. (1998). *A unified view of polymer, dumbbell, and oligonucleotide DNA nearest-neighbor thermodynamics*. Proceedings of the National Academy of Sciences, 95(4), 1460–1465.
