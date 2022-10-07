# dependencies:
# pip install tequila-basic
# works for Linux-64 and Mac-OSX-64 with intel processors
# conda install madtequila -c kottmann
import tequila as tq

# needs the file with the geometry data c2h6.xyz present
# c2h6 has 7 bonds (6 C-H and one C-C)
# we will compute 6 orbitals for each pair (hf + 5 pnos)
# total number of orbitals n_orbitals = n_pno + n_electrons//2
# means we need n_pno=5*7=35
# maxrank:5 controls that 5 pnos are computed for each pair
mol = tq.Molecule(name="c2h6", n_pno=35, pno={"maxrank":5})

