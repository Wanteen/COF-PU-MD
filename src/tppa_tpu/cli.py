"""Project-specific chemistry utilities."""
import argparse
from pathlib import Path
import yaml
from .chemistry import check_stoichiometry, ptmg_molar_mass, nominal_hard_segment_wt_fraction

def validate_config(path: Path) -> None:
    cfg = yaml.safe_load(path.read_text())
    pu = cfg["polyurethane"]
    counts = (pu["mdi_moles"], pu["ptmg_moles"], pu["bdo_moles"])
    stoich = check_stoichiometry(*counts)
    mass = ptmg_molar_mass(pu["ptmg_repeat_units"])
    hard = nominal_hard_segment_wt_fraction(*counts, mass)
    print(f"NCO/OH={stoich['NCO_OH_ratio']:.3f}; PTMG={mass:.2f} g/mol; hard segment={hard:.2%}")
    if not stoich["balanced"]:
        raise ValueError("Initial formulation must have balanced NCO and OH")
    if cfg["reaction"]["templates_verified"] and any(cfg["reaction"][key] is None for key in ("probability", "cutoff_angstrom")):
        raise ValueError("Reaction parameters absent despite templates_verified=true")
    print("Configuration passed. PCFF and chemistry dynamics NOT validated.")

def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    v = sub.add_parser("validate-config")
    v.add_argument("config", type=Path)
    b = sub.add_parser("build-ptmg")
    b.add_argument("--repeats", type=int, default=14)
    b.add_argument("--output", type=Path, required=True)
    a = parser.parse_args()
    if a.command == "validate-config":
        validate_config(a.config)
    else:
        from rdkit import Chem
        from .ptmg import build_ptmg
        a.output.parent.mkdir(parents=True, exist_ok=True)
        w = Chem.SDWriter(str(a.output))
        w.write(build_ptmg(a.repeats))
        w.close()
        print(f"Wrote {a.output}; not PCFF optimized")

if __name__ == "__main__":
    main()
