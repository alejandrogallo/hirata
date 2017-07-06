from hirata import get_tensor_name_with_indices

assert get_tensor_name_with_indices("T", "abij", "ocdm") == "Tabij[\"cdmo\"]"
