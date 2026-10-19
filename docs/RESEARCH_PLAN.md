# TpPa/TPU research plan (2026-10)

## Evidence and falsifiable hypotheses

Observed: low-angle PXRD reflections are broadened in the composite. This suggests reduced in-plane coherent domain length and/or strain/background effects; it does **not** directly establish lateral interlayer slipping, defect density, or COF bond disorder.

H1: Finite TpPa domain size and edge exposure change the adsorption and spatial organization of TPU hard/soft segments at comparable interfacial coverage.

H2: Small lateral stacking offsets in multilayer TpPa have a weaker effect on TPU than edge chemistry unless TPU precursors can access pores or interlayer regions.

H3: In-situ chain growth near TpPa produces a different interface from preformed TPU blending **after matching conversion, molecular weight distribution, density, and sample history**.

## Stage gates

P0: Molecular composition and force field
- MDI : PTMG : BDO = 3 : 2 : 1; NCO/OH = 1.
- Finite PTMG n=14 initial approximation; polydispersity later.
- Verify beta-ketoenamine TpPa bonding/tautomerism, periodicity and edges.
- LUNAR atom typing and legally supplied PCFF .frc: no missing class-II cross terms; validate fixed-coordinate energy against independent reference.
- Never claim a model is production-ready without full parameter coverage.

P1: Frozen-topology interfaces
- P0 neat TPU (prebuilt), P1 periodic single layer TpPa, P3 finite 3/5/8 nm nanosheets.
- For finite domains, use chemically justified capping, label edge and basal sites, and normalize by exposed area.
- Replicate independent TPU placements/seeds. Check box dimensions, temperature, density, pressure, equilibration and sampling.

P2: Structural heterogeneity
- Add stacked domains with modest lateral shifts and layer-spacing fluctuations.
- Compare unconstrained relaxation and constrained displacement scans. Record distributions P(dx,dy,d) rather than treating one ideal slip as 'experimentally measured'.
- PXRD validation is a **separate diffraction-modeling activity**: instrument broadening, peak overlap, crystallite size and microstrain must be considered.

P3: Reaction models
- First validate a single NCO/OH reaction and post-reaction class-II typing/charges.
- Then neat MDI/PTMG/BDO reactive model and TpPa-present reactive model; ensure identical candidate-selection criteria and acceptance rules.
- Acceptance probability is algorithmic; do not call it a measured kinetic rate constant.

P4: Structure-property
- Hydrogen bond counts/lifetimes, z-dependent densities, segment orientation, interfacial work of separation, mobility, tensile/shear response.
- Normalization, uncertainty across seeds, and relaxation convergence required.

P5: Separate TpPa-OH hypothesis after unmodified TpPa baseline; add new graft reaction and OH stoichiometry.

## Hypothesis acceptance criteria

- H1: statistically reproducible changes versus control after normalizing surface area and matching polymer composition.
- H2: free-relaxation stability plus uncertainty-aware comparisons; if no effect, report as null result.
- H3: differences persist after conversion, molecular weight distribution, and density matching.

## Not yet implemented
- Full TPU chain assembler; finite TpPa edge termination and PBC tools; standalone PXRD simulator; LUNAR end-to-end PCFF assignment; LAMMPS reaction templates and simulations.
