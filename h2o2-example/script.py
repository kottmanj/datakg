import tequila as tq
from pyscf import gto
import numpy

ZMAT = '''
    H
    O  1  0.96
    O  2  1.44  1 105
    H  3  0.96  2 105 1 {D}
    '''

results={}
for D in numpy.linspace(0.0,180,20):
    mol = gto.Mole()
    mol.atom = ZMAT.format(D=D)
    mol.build()
    
    name="h2o2_{:1.2f}".format(D)
    print(mol.atom)
    print(mol.tostring("xyz"), file=open("{}.xyz".format(name), "w"))
    
    mol = tq.Molecule(name=name, geometry="{}.xyz".format(name))
    H = mol.make_hardcore_boson_hamiltonian()
    U = mol.make_upccgsd_ansatz(name="HCB-SPA")
    E = tq.ExpectationValue(H=H,U=U)
    
    result=tq.minimize(E)
    results[D]=result.energy

print(results)
with open("results.txt", "w") as f:
    f.write(str(results))
