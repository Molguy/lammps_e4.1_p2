import numpy as np

# Cambia esto por tu archivo real
xyz_file = "1.1a.xyz"
target_mol = 26  # Molécula cuyo COM quieres comparar

# Función para leer un archivo xyz tipo LAMMPS dump
def read_xyz_lammps(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    atom_data = []
    in_atoms = False
    for i, line in enumerate(lines):
        if line.strip().startswith("ITEM: ATOMS"):
            headers = line.strip().split()[2:]
            in_atoms = True
            continue
        elif line.strip().startswith("ITEM:"):
            in_atoms = False
        elif in_atoms:
            values = line.strip().split()
            atom = dict(zip(headers, values))
            atom_data.append(atom)

    return atom_data

# Carga y agrupa por mol
atoms = read_xyz_lammps(xyz_file)
mol_dict = {}
for atom in atoms:
    mol_id = int(atom['mol'])
    pos = np.array([float(atom['x']), float(atom['y']), float(atom['z'])])
    mol_dict.setdefault(mol_id, []).append(pos)

# Calcula COMs
com_dict = {mol: np.mean(positions, axis=0) for mol, positions in mol_dict.items()}

# Distancias al COM de la molécula objetivo
target_com = com_dict[target_mol]
distances = []
for mol_id, com in com_dict.items():
    if mol_id != target_mol:
        dist = np.linalg.norm(com - target_com)
        distances.append((mol_id, dist))

# Ordena por cercanía
distances.sort(key=lambda x: x[1])

# Resultado
print(f"Moleculas más cercanas al COM de la molécula {target_mol}:\n")
for mol_id, dist in distances[:5]:
    print(f"Molécula {mol_id} → distancia = {dist:.2f} Å")
