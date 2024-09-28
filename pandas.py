import pandas as pd
from tabulate import tabulate #Estilo de tabla

data = {
    "NOMBRE": [
        "Sebastian Moreno Marin",  
        "Santiago Moreno Marin",
        "Arango Botero Diana Maria",
        "Barrios Perez Ivett Yohana",
        "Cabrales Barreto Yonis Alejandro",
        "Cancio Villa Neider Yesid",
        "Cañas Espinosa Jefferson Smith"
    ],
    "ESTADO": [
        "matriculado", "matriculado", "matriculado", 
        "matriculado", "matriculado", "matriculado", "eliminado"
    ],
    "03/08/2024": [1, 1, 1, 1, 1, 1, 1],
    "10/08/2024": [1, 1, 1, 1, 1, 1, 1],
    "17/08/2024": [1, 1, 1, 1, 1, 1, 1],
    "24/08/2024": [0, 1, 1, 1, 1, 1, 1],
    "31/08/2024": [1, 1, 1, 1, 1, 1, 1],
    "07/09/2024": [1, 1, 1, 1, 1, 1, 1],
    "14/09/2024": [1, 1, 1, 1, 1, 1, 1]
}

# Crear el cuadro
df = pd.DataFrame(data)

# Converimos exclusivamente la columna de fecha como un campo tipo fecha para el manejo de datos
df.columns = ['NOMBRE', 'ESTADO'] + list(pd.to_datetime(df.columns[2:], format='%d/%m/%Y').date)

# Estilos del dataFrame con la libreria tabulate
print(tabulate(df, headers='keys', tablefmt='grid'))
