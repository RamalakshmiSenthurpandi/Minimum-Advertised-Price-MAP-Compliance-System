import os

# -----------------------------
# Folder Paths
# -----------------------------
DATA_FOLDER = "data"
SELLER_FOLDER = "Seller data"
OUTPUT_FOLDER = "output"

# -----------------------------
# Input Files
# -----------------------------
PL_TABLE_PATH = os.path.join(DATA_FOLDER, "PL table.json")
SKU_TABLE_PATH = os.path.join(DATA_FOLDER, "SKU table.xml")
LPP_TABLE_PATH = os.path.join(DATA_FOLDER, "Lpp logic table.xlsx")

# -----------------------------
# Output Folder
# -----------------------------
VIOLATION_DOCS_FOLDER = os.path.join(OUTPUT_FOLDER, "Violation_Documents")

# -----------------------------
# Mapping Dictionaries
# -----------------------------
CATEGORY_MAP = {}
SUBCATEGORY_MAP = {}
LPP_RATES = {}
MAP_RANGES = {}
PROMOTION_TABLE = {}
SEASONS = {}
