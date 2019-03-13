holes=(i j k l m n o p)
parti=(a b c d e f g h)

{

for a in h p; do
for b in h p; do
for c in h p; do
for d in h p; do
for e in h p; do
for f in h p; do
for g in h p; do

  nholes=0
  nparti=0
  index=""

  for var in a b c d e f g; do
    [[ ${!var} = h ]] &&
      { index="${index}${holes[nholes]}"; let nholes+=1; } ||
      { index="${index}${parti[nparti]}"; let nparti+=1; }
  done

  echo ${a}${b}${c}${d}${e}${f}${g}=\"${index}\"

done
done
done
done
done
done
done

} | sort | uniq

#vim-run: bash % | less
