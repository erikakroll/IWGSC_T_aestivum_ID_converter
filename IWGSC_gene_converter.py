import pandas as pd

def build_id_mapping(df):
    """Build a dictionary mapping each gene ID to all corresponding IDs."""
    id_mapping = {}
    for _, row in df.iterrows():
        ids = [id for id in row if id != '-']  # Filter out '-' placeholders
        for gene_id in ids:
            id_mapping[gene_id] = ids  # Map each ID to the list of related IDs
    return id_mapping

def get_related_ids(gene_ids, id_mapping):
    """Retrieve all related IDs for the given gene IDs."""
    related_ids = {}
    for gene_id in gene_ids:
        related_ids[gene_id] = id_mapping.get(gene_id, "ID not found in the mapping")
    return related_ids

def gene_processing(input_ids):
    """Main processing function to handle user input and retrieve related IDs."""
    gene_ids = [gene_id.strip() for gene_id in input_ids.split(',')]
    related_ids = get_related_ids(gene_ids, id_mapping)
    
    for gene_id, ids in related_ids.items():
        print(f"Related IDs for {gene_id}: {ids}")

if __name__ == '__main__':
    file_path = 'iwgsc_refseq_all_correspondances.csv'  # Update to your actual file path
    df = pd.read_csv(file_path, sep=r"\s+")  # Load the space-separated file into a DataFrame
    
    # Build the mapping dictionary from the DataFrame
    id_mapping = build_id_mapping(df)
    
    # Take user input for gene IDs
    input_ids = input("Please type gene IDs separated by commas: ")
    gene_processing(input_ids)
