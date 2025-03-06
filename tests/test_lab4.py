import sys
sys.path.append('.')

def test_<my module>():
    # the naming of this test and the purpose is a bit obscure... 
    # we're testing the normalize csv functionality, but we're not importing the normalizer...
    test_def normalize_csv(input_path):
    """Reads a raw stock CSV, extracts required fields, and saves a normalized version."""
    assert os.path.exists(input_path), f"File not found: {input_path}"
    assert input_path.endswith(".csv"), "Input file must be a CSV"

    # Load raw CSV
    df = pd.read_csv(input_path)

    # Expected column names in raw CSV
    expected_columns = ["symbol", "price", "price_change", "price_percent_change"]
    
    # Check if required columns are present
    for col in expected_columns:
        assert col in df.columns, f"Missing column in input CSV: {col}"

    # Select only the required columns
    normalized_df = df[expected_columns]

    # Save new CSV with `_norm` suffix
    output_path = input_path.replace(".csv", "_norm.csv")
    normalized_df.to_csv(output_path, index=False)

    logging.info(f"Normalized CSV saved to {output_path}")

    assert len(sys.argv) == 2, "Usage: python bin/normalize_csv.py <path to raw gainers csv>"
