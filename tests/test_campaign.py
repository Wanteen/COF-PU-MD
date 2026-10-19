from pathlib import Path
from tppa_tpu.campaign import load_campaign, scaffold
import pytest

CONFIG = Path(__file__).resolve().parents[1] / "configs" / "campaign.yaml"

def test_campaign_has_controls():
    data = load_campaign(CONFIG)
    ids = {m["id"] for m in data["models"]}
    assert {"P0", "P1", "P3_5nm", "P4", "R0", "R1", "R2"} <= ids

def test_scaffold_no_overwrite(tmp_path):
    files = scaffold(CONFIG, tmp_path)
    assert len(files) == len(load_campaign(CONFIG)["models"])
    assert all(p.exists() for p in files)
    with pytest.raises(FileExistsError):
        scaffold(CONFIG, tmp_path)
