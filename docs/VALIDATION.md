# Validation gates

- **G0 composition:** verify NCO/OH = 1, PTMG terminal hydroxyls and chemical graph.
- **G1 PCFF:** supply an authorized .frc; validate all atom types, charges and Class-II bonded/cross terms. Never invent coefficients. Compare energies of identical coordinates to an independent trusted reference.
- **G2 single reaction:** atom-conserving O-H cleavage, N-H formation, C-O formation and N=C-to-N-C type change. Pre/post atom maps, charges, valence, all new PCFF terms must pass.
- **G3 stability:** test one event with prob=1 for debugging; minimize, short NVT, replicate random seeds, sweep distance/probability. Neither distance nor acceptance probability is a measured rate constant.
- **G4 controls:** simulate neat TPU and TpPa/TPU under identical rules; compare conversion, local density, H-bonding, chain distributions, segment segregation.
- **G5 future:** TpPa-OH requires plausible OH placement and graft-specific reaction template. Account for additional OH stoichiometry.

No production reactive LAMMPS input should be issued before G1-G3 pass.
