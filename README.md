#  Hirata equations converter

Hit

 `make`

to see the help.

For example to create ccsd equations hit

  `make ccsd`

# ISSUES

Cssdt does not work because there are more than 9 indices, i.e., p1 ---> p10 at
least, this must be generalised, we have to find a way of naming the indices
and thus separating them in holes and stuff.

In principle for us it does not really matter because we can leverage with the
name of the tensor, i.e., we can still use abcd... for all states, but put the
hole-particle partition of the space in the name, i.e., Thhhhppp["abcdefg"] it
is clear that the first three indices are holes and the others are particles.


# CCSD Amplitudes

Type

  make ccsd

It will create also the intermediates.

