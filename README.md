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
variant_dashboard.py                 # Streamlit dashboard
variant_annotation_pipeline.ipynb   # Complete data pipeline
requirements.txt                    # Python dependencies
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

## Running the Project

### Requirements

The project was tested locally using **Python 3.12.0**.

The required Python packages are listed in `requirements.txt`.

### Local Setup

Clone the repository and move into the project directory:

```bash
git clone https://github.com/rauljgarcia/genomic-variant-annotation-pipeline.git
cd genomic-variant-annotation-pipeline
```

Create and activate a Python virtual environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

On Windows, activate the environment with:

```bash
.venv\Scripts\activate
```

Install the project dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Running the Streamlit Dashboard

The Streamlit dashboard provides an interactive view of the annotated variant data. Users can select a gene to explore its mutation type distribution and view the corresponding variant records.

The repository includes `variants.db`, allowing the dashboard to be explored without rerunning the complete annotation pipeline.

From the repository root, with the virtual environment activated, run:

```bash
streamlit run variant_dashboard.py
```

Streamlit will start a local server and provide a URL for opening the dashboard in a web browser.

### Running the Annotation Pipeline

The complete data workflow is contained in:

```text
variant_annotation_pipeline.ipynb
```

The notebook contains the complete workflow for retrieving ClinVar variant data, cleaning and standardizing HGVS notation, annotating variants through the Ensembl REST API, integrating the resulting data, and building the SQLite database used by the dashboard.

By default, the notebook uses the committed ClinVar and Ensembl datasets and the existing SQLite database. This allows the notebook to be run without repeating API extraction or modifying the committed data artifacts.

Three runtime controls are provided for regenerating project data:

- `RUN_CLINVAR = True` retrieves fresh ClinVar variants and regenerates the cleaned ClinVar dataset.
- `RUN_ENSEMBL = True` reruns the Ensembl annotation pipeline. During development, a complete run took approximately 1.5 hours, although runtime depends on API response times.
- `REBUILD_DATABASE = True` drops and rebuilds the SQLite tables from the processed data.

All three controls are set to `False` by default. Regenerating ClinVar or Ensembl data requires an internet connection and depends on the availability and response times of the external APIs.

## Future Improvements

- Support configurable gene lists
- Improve transcript selection during annotation
- Refactor the notebook into reusable Python modules
- Add automated testing