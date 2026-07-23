
# Import required libraries for UI, data handling, database access, and visualization
import streamlit as st
import pandas as pd
import sqlite3
import altair as alt

# App title and description
st.title("Genomic Variant Dashboard")
st.markdown("Explore variant distributions and annotations by gene.")

# Connect to SQLite database and load data
conn = sqlite3.connect("variants.db")

# Query: total variant counts per gene (global summary)
variant_gene_counts = pd.read_sql("""
SELECT genes.gene_symbol,
COUNT(variants.variant_id) AS variant_count
FROM genes
JOIN variants
ON genes.gene_id = variants.gene_id
GROUP BY genes.gene_symbol
ORDER BY variant_count DESC;
""", conn)

# Query: overall mutation type distribution (not directly used but available if needed)
mutation_type_counts = pd.read_sql("""
SELECT mutation_type,
COUNT(*) AS count
FROM variants
GROUP BY mutation_type
ORDER BY count DESC;
""", conn)

# Query: full variant-level dataset for filtering and display
variants = pd.read_sql("""
SELECT variants.variant_id,
genes.gene_symbol,
variants.input,
variants.rsid,
variants.hgvsc,
variants.hgvsp,
variants.hgvsg,
variants.mutation_type
FROM variants
JOIN genes
ON genes.gene_id = variants.gene_id;
""", conn)

conn.close()

# User input to select gene
selected_gene = st.selectbox(
    "Select Gene",
    sorted(variants["gene_symbol"].unique())
)

# Filter dataset based on selected gene
filtered = variants[variants["gene_symbol"] == selected_gene]

# Display summary statistic for selected gene
st.write(f"Total variants for {selected_gene}: {len(filtered)}")

# Prepare mutation type distribution for selected gene
filtered_mutation_counts = (
    filtered["mutation_type"]
    .value_counts()
    .reset_index()
)

filtered_mutation_counts.columns = ["mutation_type", "count"]

# Layout is two-column dashboard view
col1, col2 = st.columns(2)

# Left chart: mutation type distribution for selected gene
with col1:
    st.subheader(f"Mutation Type Distribution for {selected_gene}")
    st.bar_chart(filtered_mutation_counts.set_index("mutation_type"))

# Right chart: overall gene variant counts with selected gene highlighted
with col2:
    st.subheader("Variant Counts by Gene")
    
    # Mark selected gene for highlighting
    gene_chart_data = variant_gene_counts.copy()
    gene_chart_data["selected"] = gene_chart_data["gene_symbol"] == selected_gene

    # Altair chart with conditional coloring
    gene_chart = alt.Chart(gene_chart_data).mark_bar().encode(
        x=alt.X("gene_symbol:N", sort="-y", title="Gene"),
        y=alt.Y("variant_count:Q", title="Variant Count"),
        color=alt.condition(
            alt.datum.selected,
            alt.value("magenta"),   # highlight selected gene
            alt.value("steelblue")  # default color
        ),
        tooltip=["gene_symbol", "variant_count"]
    ).properties(
        height=400
    )

    st.altair_chart(gene_chart, use_container_width=True)

# Display filtered variant records
st.subheader("Filtered Variant Records")
st.dataframe(filtered)
