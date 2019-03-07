from hirata.utils import permute_indices


def test_indices():
    assert permute_indices("ab", "ib", "bi") == "ai"
    assert permute_indices("abcd", "cd", "dc") == "abdc"
    assert permute_indices("abcd", "cd", "ij") == "abij"

    # identity
    assert permute_indices("abcd", "aa", "aa") == "abcd"



