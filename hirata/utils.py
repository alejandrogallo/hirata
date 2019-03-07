import hirata.conf as conf
import logging
import re
import sys

logger = logging.getLogger("main")


def permute_indices(index, start_indices, permuted_indices):
    try:
        from string import maketrans
    except:
        maketrans = str.maketrans
    assert(len(start_indices) == len(permuted_indices))
    new_index = index
    changed=[]
    trans_table = maketrans(start_indices, permuted_indices)
    new_index = index.translate(trans_table)
    return new_index


def get_tensor_name_with_indices(name, hp_partition, indices):
    """For example it should do
    T , abij, klbc -> Tabij["bclk"]
    T , abcj, klbc -> error because klbc is not pphh or any combination
    :returns: String containing the tensor expression
    """
    particles = conf.PARTICLE_INDICES.values()
    ordered_indices = ""
    holes = conf.HOLE_INDICES.values()
    hole_indices = [i for i in indices if i in holes]
    particle_indices = [i for i in indices if i in particles]
    # sort
    hole_indices.sort()
    particle_indices.sort()
    if not len([i for i in hp_partition if i in holes]) == len(hole_indices):
        logger.error("%s must have as many holes as %s" % (hp_partition, indices))
        sys.exit(1)
    if not len(hp_partition) == len(indices):
        logger.error("%s must have as many indices as %s" % (hp_partition, indices))
        sys.exit(1)
    for k in hp_partition:
        if k in holes:
            ordered_indices += hole_indices[0]
            hole_indices.pop(0)
        else:
            ordered_indices += particle_indices[0]
            particle_indices.pop(0)
    tensor_name = "{tensor}{partition}[\"{indices}\"]".format(
        tensor=name,
        partition=hp_partition,
        indices=ordered_indices
    )
    return tensor_name


