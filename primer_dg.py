# Define DNA ΔG (kcal/mol) of primers
NN_DG = {
    'AA': -1.00, 'TT': -1.00,
    'AT': -0.88, 'TA': -0.58,
    'CA': -1.45, 'TG': -1.45,
    'GT': -1.44, 'AC': -1.44,
    'CT': -1.28, 'AG': -1.28,
    'GA': -1.30, 'TC': -1.30,
    'CG': -2.17, 'GC': -2.24,
    'GG': -1.84, 'CC': -1.84
}

def estimate_dg(sequence):
    dg = 0
    for i in range(len(sequence)-1):
        pair = sequence[i:i+2]
        dg += NN_DG.get(pair, 0)
    return dg

sequence = "GCGTATGCATGCATGCGT"
dg = estimate_dg(sequence)
print("Estimated ΔG (kcal/mol):", dg)
