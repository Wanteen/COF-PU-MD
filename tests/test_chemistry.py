import pytest
from tppa_tpu.chemistry import check_stoichiometry, ptmg_molar_mass, nominal_hard_segment_wt_fraction
from tppa_tpu.ptmg import ptmg_smiles

def test_ratio():
    assert check_stoichiometry(3,2,1)["balanced"]
    assert check_stoichiometry(3,1,1)["NCO_OH_ratio"] == 1.5

def test_ptmg():
    assert ptmg_smiles(1) == "OCCCCO"
    assert ptmg_smiles(2) == "OCCCCOCCCCO"
    assert 1000 < ptmg_molar_mass(14) < 1040
    with pytest.raises(ValueError):
        ptmg_smiles(0)

def test_hard_fraction():
    value = nominal_hard_segment_wt_fraction(3,2,1,ptmg_molar_mass(14))
    assert 0.28 < value < 0.30
