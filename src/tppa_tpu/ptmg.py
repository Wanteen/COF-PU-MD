"""Finite dihydroxy-terminated PTMG builder; no PCFF parameters supplied."""
def ptmg_smiles(repeats: int) -> str:
    if type(repeats) is not int or repeats < 1:
        raise ValueError("repeats must be a positive integer")
    return "O" + "CCCCO" * repeats

def build_ptmg(repeats: int, seed: int = 20261019):
    from rdkit import Chem
    from rdkit.Chem import AllChem
    mol = Chem.AddHs(Chem.MolFromSmiles(ptmg_smiles(repeats)))
    if AllChem.EmbedMolecule(mol, randomSeed=seed, maxAttempts=100) != 0:
        raise RuntimeError("RDKit embedding failed")
    if AllChem.MMFFGetMoleculeProperties(mol) is not None:
        AllChem.MMFFOptimizeMolecule(mol, maxIters=400)
    return mol
