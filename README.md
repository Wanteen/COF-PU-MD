# COF-PU-MD

Task-specific workspace for **TpPa covalent organic framework / flexible thermoplastic polyurethane (TPU)** molecular dynamics and eventual topology-controlled in-situ polymerization.

**Baseline:** 4,4'-MDI : PTMG : 1,4-butanediol = **3:2:1** (molar); PTMG approximately Mn 1000 g/mol, discretized to 14 ether repeat units; stoichiometric NCO/OH = 1.

**Research status:** scaffold only. PCFF parameters, reactive templates, reaction cutoffs, probabilities, and TpPa structure are **not validated or provided**. Do not use these placeholders for production simulations.

## Tasks
1. Generate finite PTMG soft segment; check chemistry and stoichiometry.
2. Import a verified beta-ketoenamine TpPa periodic structure.
3. Evaluate open-source PCFF typing via LUNAR and a legally supplied parameter library. Fail on missing Class-II cross terms.
4. Validate urethane pre/post templates in LAMMPS fix bond/react using a single reaction event.
5. Compare bulk TPU to TpPa/TPU with identical reaction rules.
6. Consider TpPa-OH grafting as a separate later phase.

## Run
```bash
conda env create -f environment.yml
conda activate tppa-tpu
pip install -e .
python -m tppa_tpu.cli validate-config configs/baseline.yaml
python -m tppa_tpu.cli build-ptmg --repeats 14 --output ptmg_n14.sdf
pytest -q
```

The Python generator is for **initial molecular connectivity and coordinates**, not a substitute for PCFF force-field parameterization or polymerization dynamics.

Reference: Hao et al., ACS Nano 2024, DOI: 10.1021/acsnano.3c11787.

## LUNAR integration
The project now includes a **real CLI subprocess adapter** for upstream CMMRLab/LUNAR (external checkout, not vendored). See [docs/LUNAR.md](docs/LUNAR.md).

```bash
bash scripts/install_lunar.sh
python -m tppa_tpu.lunar --root external/LUNAR --tool atom_typing -- -man
python -m tppa_tpu.lunar --root external/LUNAR --tool all2lmp -- -man
```

Actual parameterization requires validated molecular input, a supported PCFF `.frc`, and full Class-II parameter/energy checks; none have been certified yet.

## Research campaign (2026-10)

See [evidence-led research plan](docs/RESEARCH_PLAN.md) and [candidate campaign](configs/campaign.yaml). Validate and create **metadata-only** model workspaces:

```bash
python -m tppa_tpu.campaign configs/campaign.yaml --output workspaces
```

The resulting manifests are **not** molecular coordinates or runnable simulations; every candidate remains unbuilt until structure, PCFF, and physics checks pass.
