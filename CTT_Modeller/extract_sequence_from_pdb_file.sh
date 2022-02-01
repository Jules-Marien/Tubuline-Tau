#https://yossadh.github.io/posts/2019/03/extract-pdb-sequence/
#extract_sequence_from_pdb_file.sh
declare -A aa_dict=(
[ALA]=A
[ARG]=R
[ASN]=N
[ASP]=D
[CYS]=C
[GLU]=E
[GLN]=Q
[GLY]=G
[HIS]=H
[ILE]=I
[LEU]=L
[LYS]=K
[MET]=M
[PHE]=F
[PRO]=P
[SER]=S
[THR]=T
[TRP]=W
[TYR]=Y
[VAL]=V
)

for resid_chain_resnum in $(grep ^ATOM $1 | grep CA | cut -c 18-26 | sed 's/ /_/g'); do
    if [[ "${aa_dict[${resid_chain_resnum:0:3}]}" == "" ]]; then
        printf "%s>%s\n" "$resid_chain_resnum" "???"
        continue
    fi
    printf "%s>%s\n" "$resid_chain_resnum" "${aa_dict[${resid_chain_resnum:0:3}]}"
done | sed 's/_/ /g' | pr --output-tabs=' 1' -5 -t
echo

echo ">$1"
for resid in $(grep ^ATOM $1 | grep CA | cut -c 18-20); do
    printf "%s" "${aa_dict[$resid]}"
done | fold
echo 
