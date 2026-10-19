"""Deterministic research campaign manifest validation and scaffolding.

Creates directories and metadata only; NOT molecular coordinates or runnable MD.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import json
import yaml

VALID_STAGES = {"fixed_topology", "heterogeneity", "reactive", "future_grafting"}

def load_campaign(path: Path) -> dict:
    obj = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(obj, dict) or not isinstance(obj.get("models"), list):
        raise ValueError("Campaign must contain a list of models")
    ids = [m.get("id") for m in obj["models"]]
    if len(set(ids)) != len(ids) or not all(isinstance(i, str) and i for i in ids):
        raise ValueError("Model IDs must be unique nonempty strings")
    for model in obj["models"]:
        if model.get("stage") not in VALID_STAGES:
            raise ValueError(f"Unsupported stage in {model.get('id')}")
        if model.get("geometry") == "finite_nanosheet" and model["id"].startswith("P3_"):
            if float(model.get("lateral_size_nm", 0)) <= 0:
                raise ValueError("Finite nanosheets require positive lateral_size_nm")
    comp = obj.get("formulation", {})
    from .chemistry import check_stoichiometry
    if not check_stoichiometry(comp["mdi"], comp["ptmg"], comp["bdo"])["balanced"]:
        raise ValueError("NCO/OH stoichiometry not balanced")
    return obj

def scaffold(config: Path, destination: Path) -> list[Path]:
    campaign = load_campaign(config)
    # Do not overwrite existing simulations or model configurations.
    manifest_paths = [destination / m["id"] / "manifest.json" for m in campaign["models"]]
    existing = [p for p in manifest_paths if p.exists()]
    if existing:
        raise FileExistsError(f"Refusing overwrite: {existing}")
    for entry, path in zip(campaign["models"], manifest_paths):
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = {"status": "unbuilt", "description": entry,
                   "source_campaign": str(config), "validated_pcff": False,
                   "validated_reaction": False}
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    return manifest_paths

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("campaign", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = load_campaign(args.campaign)
    print(f"Validated {len(result['models'])} candidate models")
    if args.output is not None:
        paths = scaffold(args.campaign, args.output)
        print(f"Wrote {len(paths)} manifests (not simulation inputs) to {args.output}")

if __name__ == "__main__":
    main()
