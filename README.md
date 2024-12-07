# Ontology of Bacteria and Antibiotic Resistance Genes (ARGs)

This repository contains the ontology of bacteria and antibiotic resistance genes (ARGs), developed to model relationships between bacteria, ARGs, resistance mechanisms, drug classes, and pathogens.

## Description
The ontology is structured to provide a semantic framework for representing:
- **Bacteria** and their scientific properties.
- **Antibiotic Resistance Genes (ARGs):** Genes that confer resistance to antibiotics.
- **Antibiotics:** Substances that inhibit bacterial growth.
- **Resistance Mechanisms:** Mechanisms by which bacteria resist antibiotics.
- **Drug Classes:** Groups of antibiotics categorized by structure and mechanism.
- **Pathogens:** Microorganisms capable of causing disease.

The ontology is expressed in Turtle (`.ttl`) format and is compliant with OWL standards.

---

## Usage

### Importing the Ontology
You can import the ontology into tools such as [Protégé](https://protege.stanford.edu/) or SPARQL endpoints.

1. Download the file `ontology.ttl`.
2. Open it in a compatible RDF/OWL editor or load it into a semantic database like **Apache Jena** or **Virtuoso**.

### Example SPARQL Query
The following query retrieves bacteria and the antibiotics they are resistant to:

```sparql
PREFIX ont: <https://upm.es/bactery/ontology#>
SELECT ?bacteria ?antibiotic
WHERE {
    ?bacteria ont:resistantTo ?antibiotic .
}
```

---

## Classes and Properties Overview

### Classes:
- **`ont:Bacteria`**: Represents bacteria.
- **`ont:ARG`**: Represents antibiotic resistance genes.
- **`ont:Antibiotic`**: Represents antibiotics.
- **`ont:ResistanceMechanism`**: Mechanisms of resistance.
- **`ont:DrugClass`**: Categories of antibiotics.
- **`ont:Pathogen`**: Microorganisms causing diseases.

### Key Properties:
- **Object Properties:**
  - `ont:resistantTo`: Links bacteria to antibiotics.
  - `ont:containsARG`: Links bacteria to ARGs.
  - `ont:associatedDrugClass`: Links antibiotics to drug classes.
  - `ont:foundInPathogen`: Links ARGs to pathogens.

- **Data Properties:**
  - `ont:pathogenName`: The name of the pathogen.
  - `ont:argName`: The name of the ARG.
  - `ont:aroID`: Identifier for the ARG in the Antibiotic Resistance Ontology (ARO).
  - `ont:frequency`: Frequency of ARG occurrence in populations.

---

## License
This ontology is licensed under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You are free to use and adapt it, provided appropriate credit is given.

## Authors
- Universidad Politécnica de Madrid (UPM)

For questions or contributions, please contact the development team.

---

## Citation
If you use this ontology, please cite:

```
Ontology of Bacteria and Antibiotic Resistance Genes (ARGs).
Universidad Politécnica de Madrid, 2024.
Available at: 
