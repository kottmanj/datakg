# Content

- [c2h6-minimal](c2h6-minimal): C2H6(14,28) data, each bond/edge represented by 2 orbitals
- [c2h6-large](c2h6-large): C2H6(14,84) and C2H6(2,12) data, each bond/edge represented by 6 orbitals.
- [h2o2](h2o2): H2O2(14,28) data, each bond/edge represented by 2 orbitals
- [c2h4](c2h4): H2O2(12,24) data, each bond/edge represented by 2 orbitals
- [h2o2-example](h2o2-example): H2O2(14,28) example calculation for relative energies

## Most folder contain the files
- `compute_data.py`: script used to compute stuff
- `load_data.py`: code to load the data
- Data tequila needs to read in the molecules
  - `NAME_htensor.npy`: one-body integrals 
  - `NAME_gtensor.npy`: two-body integrals 
  - `NAME_pnoinfo.txt`: information about orbitals computed by madness
- Additional info:
  - `input`: original madness input file generated by tequila
  - `NAME_pno_integrals.out`: mandness output file (contains runtimes and more information - most of the time not important) 

## More info
- [arxiv:2105.03836](https://arxiv.org/abs/2105.03836): Paper on SPA circuits with MRA-PNOs
- [arxiv:2207.12421](https://arxiv.org/abs/2207.12421): Connection to chemical graphs, usage with standard basis sets, extension beyond SPA
