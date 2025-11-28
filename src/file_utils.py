from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent
SOURCE_DATA_DIR = PROJECT_DIR / "source_data"
CHARTS_DIR = PROJECT_DIR / "charts"
CHARTS_DIR.mkdir(exist_ok=True)

BODY_MEASUREMENTS_CSV = SOURCE_DATA_DIR / "Body_Measurements_original_CSV.csv"
