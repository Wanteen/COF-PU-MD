# Using LUNAR without Materials Studio

LUNAR upstream: https://github.com/CMMRLab/LUNAR (GPL-3.0). We **do not vendor LUNAR**; download it and record its exact Git SHA.

## 1. Install

```bash
bash scripts/install_lunar.sh
python -m tppa_tpu.lunar --root external/LUNAR --tool atom_typing -- -man
python -m tppa_tpu.lunar --root external/LUNAR --tool all2lmp -- -man
```

The two help calls invoke upstream documentation; non-help commands are **dry-run by default**. Put `--execute` before the `--` delimiter after reviewing the printed command.

## 2. Actual data pipeline

1. Use RDKit to build molecules with complete atom connectivity and hydrogens; export supported topologies (check upstream `atom_typing.py -man`).
2. Run LUNAR `atom_typing.py` for the *appropriate* PCFF type set. Inspect assignment logs and unknown types; never infer coverage from exit code alone.
3. Run LUNAR `all2lmp.py` using the verified typing output and a legally usable `.frc` parameter source. Inspect `all2lmp.py -man` for option names, including its class-II selection. Require complete cross terms; **do not use ignore-missing-parameters**.
4. Check individual MDI, BDO, PTMG, urethane-fragment and beta-ketoenamine TpPa (including charge neutrality or intended net charge).
5. Fixed-geometry and minimized-energy reference comparisons must pass before any reactive run.
6. For `fix bond/react` develop `pre/post` reaction templates and use LUNAR's `bond_react_merge_prep` / `bond_react_merge` utilities where applicable; independently verify molecular graph, atom mapping, charges, and PCFF coefficients.

## 3. Run a vetted command

```bash
python -m tppa_tpu.lunar --root external/LUNAR --tool atom_typing -- -man
# First preview (replace ... with REAL upstream options from -man):
python -m tppa_tpu.lunar --root external/LUNAR --tool atom_typing -- ...
# Then execute the identical vetted arguments:
python -m tppa_tpu.lunar --root external/LUNAR --tool atom_typing --execute --log results/typing.log -- ...
```

No synthetic .frc files, default chemistry guesses, or fake final LAMMPS inputs are supplied. **LUNAR is an external dependency and has not been run against the project molecular systems.**
