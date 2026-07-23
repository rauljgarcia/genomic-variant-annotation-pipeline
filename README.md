# Genomic Variant Annotation Pipeline

A bioinformatics data engineering project that retrieves human genetic variants from the ClinVar REST API, standardizes HGVS variant notation, annotates variants using the Ensembl REST API (GRCh37), integrates the results into a normalized SQLite database, and provides SQL queries and an interactive Streamlit dashboard for exploring genomic variant data.

## Features

- Retrieve variant records from the ClinVar REST API
- Clean and standardize HGVS variant notation
- Annotate variants using the Ensembl GRCh37 REST API
- Integrate variant and annotation data into a normalized SQLite database
- Query genomic data using SQL
- Explore results through an interactive Streamlit dashboard

## Technologies

- Python
- pandas
- Requests
- SQLite
- SQL
- Streamlit
- Altair
- ClinVar REST API
- Ensembl REST API

## Repository Contents

```
app.py                              # Streamlit dashboard
variant_annotation_pipeline.ipynb   # Complete data pipeline
variants.db                         # SQLite database
merged_clinvar_ensembl.csv          # Integrated dataset
clinvar/                            # Cleaned ClinVar variants
ensembl/                            # Ensembl annotations and failed requests
```

## Data Pipeline

```
ClinVar REST API
        │
        ▼
Variant Extraction
        │
        ▼
HGVS Cleaning
        │
        ▼
Ensembl Annotation
        │
        ▼
Data Integration
        │
        ▼
SQLite Database
        │
   ┌────┴────┐
   ▼         ▼
 SQL     Streamlit
```

## Future Improvements

- Support configurable gene lists
- Improve transcript selection during annotation
- Refactor the notebook into reusable Python modules
- Add automated testing