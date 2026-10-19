from pathlib import Path
import pytest
from tppa_tpu.lunar import locate, invoke

def test_missing_checkout(tmp_path):
    with pytest.raises(FileNotFoundError):
        locate(tmp_path, "all2lmp")

def test_unknown_tool(tmp_path):
    with pytest.raises(ValueError):
        locate(tmp_path, "bad")

def test_preview_is_safe(tmp_path):
    (tmp_path / "all2lmp.py").write_text("raise Exception('must not execute')")
    assert invoke(tmp_path, "all2lmp", ["-x", "test"]) == 0

def test_requires_options(tmp_path):
    (tmp_path / "all2lmp.py").write_text("")
    with pytest.raises(ValueError):
        invoke(tmp_path, "all2lmp", [])
