Proyecto Sugerido - Razonamiento antes del codigo.

#CLASES

## SENSOR
- ID - IDENTIFICADOR DE CADA MAQUINA
- TYPE - QUE ES LO QUE ESTA MIDIENDO
- UNITS - QUE ES LO QUE ESTA MIDIENDO, PSI,GRADOS C,ETC
- MACHINE LIMIT BREAKER - LIMITE PERMITIDO DE ERROR, MARGEN SUPERADO = ALGO MALO ESTA OCURRIENDO

## MONITOR
- WAREHOUSE - LISTA INTERNA DONDE ALMACENA LAS LECTURAS QUE RECIBE
- METHOD = ACTUALIZAR ESA LISTA CON LAS NUEVAS LECTURAS
- METHOD = RECORRE Y DETECTA LOS DATOS PELIGROSOS
- METHOD = GENERA REPORTE CON RESUMEN DE LOS PELIGROS ENCONTRADOS
        - Total de lecturas recibidas
        - Cuántas fueron inválidas (y qué porcentaje representa)
        - Cuántas generaron alerta (valor fuera de límite)
        - Cuál sensor tuvo más problemas
        - Una línea de conclusión: ¿la fábrica está operando con normalidad o hay riesgo?

## LECTURA
- SENSOR ID - DE QUE SENSOR PROVIENE
- VALOR
- TIMESTAP  - FECHA/HORA
- VALIDA/INVALIDA

## LECTURA VALIDA!? - VALIDACION

