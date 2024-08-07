""""
Este sistema determina los días de vacaciones a los que tiene un trabajador. 
"""

print("===========================")
print("SISTEMA DE VACACIONES RAPPI")
print("===========================")

nombre = input("\nIngrese su nombre: ")
clave = int(input("Ingrese clave de departamento: "))
antiguedad = int(input("Ingrese años de antiguedad: "))

#Departamento de atención al cliente
if clave == 1:
    print("\nDepartamento de Atención al cliente.")
    if antiguedad == 1:
        print(f"==> {nombre} de acuerdo a tu antiguedad tienes derecho a 6 días de vacaciones.")
    elif antiguedad > 1 and antiguedad <= 6:
        print(f"==> {nombre} de acuerdo a tu antiguedad tienes derecho a 14 días de vacaciones.")
    elif antiguedad >= 7:
        print(f"==> {nombre} de acuerdo a tu antiguedad tienes derecho a 20 días de vacaciones.")
    else:
        print("No tienes derecho a vacaciones.")

#Departamento de Logistica
elif clave == 2:
    print("\nDepartamento de Logistica.")
    if antiguedad == 1:
        print(f"==> {nombre} de acuerdo a tu antiguedad tienes derecho a 7 días de vacaciones.")
    elif antiguedad > 1 and antiguedad <= 6:
        print(f"==> {nombre} de acuerdo a tu antiguedad tienes derecho a 15 días de vacaciones.")
    elif antiguedad >= 7:
        print(f"==> {nombre} de acuerdo a tu antiguedad tienes derecho a 22 días de vacaciones.")
    else:
        print("No tienes derecho a vacaciones.")

#Gerencia
elif clave == 3:
    print("\nGerencia.")
    if antiguedad == 1:
        print(f"==> {nombre} de acuerdo a tu antiguedad tienes derecho a 10 días de vacaciones.")
    elif antiguedad > 1 and antiguedad <= 6:
        print(f"==> {nombre} de acuerdo a tu antiguedad tienes derecho a 20 días de vacaciones.")
    elif antiguedad >= 7:
        print(f"==> {nombre} de acuerdo a tu antiguedad tienes derecho a 30 días de vacaciones.")
    else:
        print("No tienes derecho a vacaciones.")

else:
    print("Clave no valida.")


print("Fin.")
