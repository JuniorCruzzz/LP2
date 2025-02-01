#Junior Cruz 21-1680

# Definir nombres de estudiantes y sus notas
nombres_estudiantes = ["Carlos", "María", "Luis", "Andrea", "Sofía"]
notas_estudiantes = {
    "Carlos": (85, 90, 80),
    "María": (70, 75, 80),
    "Luis": (95, 92, 94),
    "Andrea": (88, 84, 87),
    "Sofía": (60, 65, 70)
}

# Calcular promedios e imprimir resultados
for estudiante, notas in notas_estudiantes.items():
    promedio = sum(notas) / len(notas)
    print(f"{estudiante} tiene un promedio de {promedio:.2f}")
    
    if promedio >= 85:
        print(f"{estudiante} tiene un desempeño sobresaliente.")
    else:
        print(f"{estudiante} necesita mejorar.")
    print()
