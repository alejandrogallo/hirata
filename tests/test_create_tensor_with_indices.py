from hirata.utils import get_tensor_name_with_indices

def test_simple():

    assert(
        get_tensor_name_with_indices("T", "abij", "ocdm") == "Tabij[\"cdmo\"]"
    )
    assert(
        get_tensor_name_with_indices("T", "aibj", "ocdm") == "Taibj[\"cmdo\"]"
    )
    assert(
        get_tensor_name_with_indices("T", "aijb", "odmc") == "Taijb[\"cmod\"]"
    )

    try:
        get_tensor_name_with_indices("T", "ab", "ij")
    except SystemExit:
        assert True
    else:
        assert False

    try:
        get_tensor_name_with_indices("T", "ab", "abc")
    except SystemExit:
        assert True
    else:
        assert False
