# dependencies:
# pip install tequila-basic
# works for Linux-64 and Mac-OSX-64 with intel processors
# conda install madtequila -c kottmann
import tequila as tq

# needs the file with the geometry data c2h4.xyz present
mol = tq.Molecule(name="c2h4")

