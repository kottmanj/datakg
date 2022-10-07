import tequila as tq

# try to reload
# you need h2o2_xtensor.npy with x=h and x=g, and h2o2_pnoinfo.txt
# if they are in a separate directory, specify via datadir="/path/to/whatever"
mol = tq.Molecule(name="h2o2", n_pno="read")
print("{} with {} qubits and {} electrons".format(mol.parameters.name, mol.n_orbitals*2, mol.n_electrons))

# as this thing has already more than 20 qubits it's recommended to solve the SPA in the HCB encoding
H_hcb = mol.make_hardcore_boson_hamiltonian()
U_hcb = mol.make_ansatz(name="HCB-SPA")
E_hcb = tq.ExpectationValue(H=H_hcb, U=U_hcb)

result = tq.minimize(E_hcb, silent=True)


print("SPA/MRA-PNO({},{}) : {:+2.5f}".format(mol.n_electrons, 2*mol.n_orbitals, result.energy))
# need pyscf from here on
ccsd = mol.compute_energy("ccsd") 
print("SPA/CCSD({},{})    : {:+2.5f}".format(mol.n_electrons, 2*mol.n_orbitals, ccsd))
fci = mol.compute_energy("fci") # will take a while
print("SPA/FCI({},{})     : {:+2.5f}".format(mol.n_electrons, 2*mol.n_orbitals, fci))
"""
SPA/MRA-PNO(14,28) : -150.97233
SPA/CCSD(14,28)    : -151.06600
SPA/FCI(14,28)     : -151.06764
"""
