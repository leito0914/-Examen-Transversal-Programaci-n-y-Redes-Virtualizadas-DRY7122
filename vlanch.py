vlan_id = int(input("Ingrese el número de VLAN: "))

if 1 <= vlan_id <= 1005:
    print(f"La VLAN {vlan_id} corresponde al rango NORMAL (1-1005).")
elif 1006 <= vlan_id <= 4094:
    print(f"La VLAN {vlan_id} corresponde al rango EXTENDIDO (1006-4094).")
else:
    print(f"La VLAN {vlan_id} no es válida. Debe estar entre 1 y 4094.")
