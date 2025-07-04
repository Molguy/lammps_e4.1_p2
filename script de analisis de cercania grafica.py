import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Simulamos que ya tienes este diccionario de COMs del script anterior
# Si lo guardas a archivo, podrías usar pickle o np.savez para cargarlo
# Para este ejemplo lo volvemos a calcular en este archivo

# Archivo original
xyz_file = "1.1a.xyz"
target_mol = 26  # Molécula a comparar
n_closest = 5    # Número de moléculas más cercanas a mostrar

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

# Carga y calcula COMs
atoms = read_xyz_lammps(xyz_file)
mol_dict = {}
for atom in atoms:
    mol_id = int(atom['mol'])
    pos = np.array([float(atom['x']), float(atom['y']), float(atom['z'])])
    mol_dict.setdefault(mol_id, []).append(pos)

com_dict = {mol: np.mean(pos_list, axis=0) for mol, pos_list in mol_dict.items()}
target_com = com_dict[target_mol]

# Distancias al objetivo
distances = []
for mol_id, com in com_dict.items():
    if mol_id != target_mol:
        dist = np.linalg.norm(com - target_com)
        distances.append((mol_id, dist))

distances.sort(key=lambda x: x[1])
closest_ids = [mol_id for mol_id, _ in distances[:n_closest]]

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for mol_id, com in com_dict.items():
    color = "blue"
    if mol_id == target_mol:
        color = "red"
        ax.scatter(*com, c=color, s=100, label="Mol. objetivo")
    elif mol_id in closest_ids:
        color = "green"
        ax.scatter(*com, c=color, s=60)
    else:
        ax.scatter(*com, c=color, s=30)

ax.set_title(f"Centros de masa - Molécula {target_mol} y cercanas")
ax.set_xlabel("X (Å)")
ax.set_ylabel("Y (Å)")
ax.set_zlabel("Z (Å)")
ax.legend()
plt.tight_layout()
plt.show()
