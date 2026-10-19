# Linux workflow

1. Set up environment.yml; install package with pip install -e .
2. Import verified TpPa structure and test PBC/bond connectivity.
3. Build PTMG chain graph with the CLI (not final TPU).
4. Install LUNAR from its official source; supply authorized PCFF .frc parameters.
5. Match LUNAR atom typing to validated chemistry and check every Class-II term.
6. Construct reaction templates only after force-field validation.
7. Check LAMMPS build includes CLASS2, MOLECULE, KSPACE, REACTION.
8. Add packing and MD inputs as tested modules, not placeholders masquerading as completed experiments.

See docs/VALIDATION.md for stage gates.
