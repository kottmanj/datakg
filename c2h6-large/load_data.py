import tequila as tq

# try to reload
# you need c2h6_xtensor.npy with x=h and x=g, and c2h6_pnoinfo.txt
# if they are in a separate directory, specify via datadir="/path/to/whatever"
mol = tq.Molecule(name="c2h6", n_pno="read")
print("{} with {} qubits and {} electrons".format(mol.parameters.name, mol.n_orbitals*2, mol.n_electrons))

U = mol.make_ansatz(name="SPA")
print("circuit with {} gates and {} variables".format(len(U.gates), len(U.extract_variables())))

# as this thing has already 84 qubits I would not compute Hamiltonians ( will take forever)

# printing the molecule will display information about the orbitals
print(mol)

# from this we can see that the (6,6) pair corresponds to the C-C bond (the others are C-H bonds indicated as they are degenerate in all values)
# the orbitals from (6,6) are: 6, 15, 34, 35, 36, 43 
# let's form the active space molecule with only the C-C bond
mol = tq.Molecule(name="c2h6", n_pno="read", active_orbitals=[6,15,34,35,36,43])
print("{} with {} qubits and {} electrons".format(mol.parameters.name, mol.n_orbitals*2, mol.n_electrons))
U = mol.make_ansatz(name="SPA")
print("circuit with {} gates and {} variables".format(len(U.gates), len(U.extract_variables())))

H = mol.make_hamiltonian()
E = tq.ExpectationValue(H=H , U=U)
result = tq.minimize(E, silent=True)

print("SPA/MRA-PNO({},{}) : {:+2.5f}".format(mol.n_electrons, 2*mol.n_orbitals, result.energy))
# need pyscf from here on
ccsd = mol.compute_energy("ccsd")
print("SPA/CCSD({},{})    : {:+2.5f}".format(mol.n_electrons, 2*mol.n_orbitals, ccsd))
fci = mol.compute_energy("fci") # will take a while
print("SPA/FCI({},{})     : {:+2.5f}".format(mol.n_electrons, 2*mol.n_orbitals, fci))

