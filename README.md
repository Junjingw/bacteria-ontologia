# Ontología de Bacterias y Genes de Resistencia a Antibóticos (ARGs)

## Descripción General
Este repositorio contiene la **Ontología de Bacterias y Genes de Resistencia a Antibóticos (ARGs)**, un marco semántico diseñado para representar organismos bacterianos, sus genes de resistencia a antibióticos asociados y fenómenos biológicos relacionados. La ontología está escrita en formato OWL y puede utilizarse para anotar y analizar datos en microbiología, investigación sobre resistencia a antibióticos y campos relacionados.

## Detalles de la Ontología
- **IRI**: [https://Junjingw.github.io/bacteria-ontologia](https://Junjingw.github.io/bacteria-ontologia)
- **Título**: Ontología de Bacterias y Genes de Resistencia a Antibóticos (ARGs)
- **Descripción**: Esta ontología proporciona un vocabulario estructurado para modelar organismos bacterianos, genes de resistencia a antibióticos, mutaciones y antibióticos, junto con sus relaciones y metadatos asociados.
- **Formato**: OWL (Web Ontology Language)

## Componentes Clave

### Clases Principales
La ontología define las siguientes clases principales:

1. **Bacteria**:
   - Representa un organismo bacteriano.
   - **IRI**: `ont:Bacteria`

2. **ARG (Gen de Resistencia a Antibóticos)**:
   - Representa un gen que confiere resistencia a uno o más antibióticos.
   - **IRI**: `ont:ARG`

3. **Antibiótico**:
   - Representa una sustancia utilizada para inhibir el crecimiento bacteriano o destruir bacterias.
   - **IRI**: `ont:Antibiotic`

4. **Mutación**:
   - Representa una mutación que ocurre en una bacteria vinculada a un ARG.
   - **IRI**: `ont:Mutation`

### Propiedades de Objeto
La ontología define relaciones entre las clases:

- **`ont:occursIn`**: Relaciona una mutación con la bacteria donde ocurre (inversa de `ont:hasMutation`).
- **`ont:hasMutation`**: Relaciona una bacteria con las mutaciones que contiene (inversa de `ont:occursIn`).
- **`ont:linkedToARG`**: Relaciona una mutación con el ARG que representa (inversa de `ont:hasMutationARG`).
- **`ont:resistantTo`**: Relaciona un ARG con los antibióticos a los que es resistente.

### Propiedades de Datos
La ontología incluye atributos para describir características de las entidades:

- **`ont:frequency`**: La frecuencia de aparición de una mutación en una población bacteriana (tipo de dato: `xsd:float`).
- **`ont:symptomsAndSigns`**: Indicaciones físicas o fisiológicas de una enfermedad causada por bacterias (tipo de dato: `xsd:string`).

### Metadatos
- **Prefijos de Espacio de Nombres**:
  - `ont`: [https://Junjingw.github.io/bacteria-ontologia#](https://Junjingw.github.io/bacteria-ontologia#)
  - `rdf`: [http://www.w3.org/1999/02/22-rdf-syntax-ns#](http://www.w3.org/1999/02/22-rdf-syntax-ns#)
  - `rdfs`: [http://www.w3.org/2000/01/rdf-schema#](http://www.w3.org/2000/01/rdf-schema#)
  - `owl`: [http://www.w3.org/2002/07/owl#](http://www.w3.org/2002/07/owl#)
  - `dc`: [http://purl.org/dc/elements/1.1/](http://purl.org/dc/elements/1.1/)
  - `xsd`: [http://www.w3.org/2001/XMLSchema#](http://www.w3.org/2001/XMLSchema#)

## Uso

### Requisitos
Para utilizar esta ontología, necesitas una herramienta que soporte formatos OWL y RDF, como:
- [Protégé](https://protege.stanford.edu/)
- RDF4J
- Puntos de consulta SPARQL

### Carga de la Ontología
1. Clona este repositorio o descarga el archivo de la ontología.
2. Abre la ontología en tu editor OWL o herramienta de análisis de datos RDF preferido.

### Ejemplo de Consulta SPARQL
Consulta para encontrar todas las bacterias vinculadas a un gen de resistencia a antibióticos específico:

```sparql
PREFIX ont: <https://Junjingw.github.io/bacteria-ontologia#>
SELECT ?bacteria ?arg
WHERE {
    ?mutation ont:linkedToARG ?arg .
    ?mutation ont:occursIn ?bacteria .
}
```




