# SEGMENTACIÓN DE COMPAÑIAS

Este repositorio contiene la primera etapa del análisis y procesamiento de 10.000 registros de compañíaas de Bogotá.

Se busca explorar y segmentar compañías según distintos factores financieros y de rentabilidad.

## Estructura del proyecto

.  
├── datos  
│   ├── componentes.csv  
│   ├── Export.xlsx  
│   ├── Pruebas2.csv  
│   └── Pruebas.csv  
├── eda.ipynb  
├── README.md  
└── requirements.txt  

** Los datos no estan incluidos en el repositorio, por políticas del proveedor **

## Participantes

Juan Daniel Castrellón (201729285)
Kevin Camilo Becerra Walteros (201812779) 
Laura Andrea Roncancio Pava (201815149)
Javier Alejandro Gómez Muñóz (201217975)
 

## Ejecución

Cree un ambiente virtual usando python3 e instale las librerias de `.requirements.txt`

## Conclusiones iniciales

- Predominio de Micro y Pequeñas Empresas: La industria de Bogotá está formada principalmente por empresas de menor escala (de 0 a 50 empleados). Esta característica podría ser un reflejo de la estructura empresarial de la ciudad, donde las micro y pequeñas empresas impulsan una parte significativa de la economía local.

- Concentración de las Exportaciones: Un reducido número de empresas realiza entre el 80% y el 100% de las exportaciones de Bogotá. Este hallazgo sugiere que las exportaciones de la ciudad dependen principalmente de industrias específicas, lo cual representa tanto una fortaleza para dichas industrias como un riesgo potencial en caso de cambios en el mercado.

- Relación entre Deuda y Efectivo Disponible: Se observó que las empresas con mayor deuda a largo plazo también tienden a tener mayores cantidades de efectivo disponible. Este patrón podría indicar que las empresas con mayor capacidad de financiamiento también cuentan con mejores recursos de liquidez para sus operaciones.

- Inversión en Activos Fijos y Ventas Totales: Existe una relación directa entre las inversiones en activos fijos, las ventas totales y la deuda a largo plazo. Esto sugiere que las empresas con mayores ventas y deuda invierten también en sus activos fijos, lo que probablemente les permite expandir y mejorar sus operaciones.

- Impacto de la Deuda a Corto Plazo en el Desempeño Financiero: Las empresas con mayores niveles de deuda a corto plazo podrían mostrar un desempeño financiero distinto, especialmente en términos de crecimiento de ingresos y beneficios. Este comportamiento sugiere que la gestión de deuda a corto plazo es un factor clave en el rendimiento financiero de las empresas.

- Correlaciones Financieras para Agrupación: Las correlaciones entre las variables analizadas permiten trazar un perfil general de la salud financiera de las empresas. Estos resultados serán la base para el siguiente paso en el análisis: seleccionar el mejor modelo de agrupación para clasificar a las empresas en diferentes clústeres de acuerdo con su rendimiento y segmentación NAICS, lo que permitirá una segmentación más precisa para la prospección.
