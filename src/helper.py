def decode_pl(pl):
    parts = pl.split("_")
    if len(parts) < 3:
        return {"brand": None, "category": pl, "subcategory": "Unknown"}
    match    = re.match(r"^(HP|DELL)", pl)
    brand    = match.group(1) if match else None
    cat_code = parts[1]
    sub_code = "_".join(parts[2:])
    return {
        "brand":       brand,
        "category":    CATEGORY_MAP.get(cat_code, cat_code),
        "subcategory": SUBCATEGORY_MAP.get(sub_code, sub_code),
    }


def get_lpp_rate(subcategory, brand):
    return LPP_RATES.get(subcategory, {}).get(brand, 0.034)


def get_map(subcategory, rng):
    lo, hi = MAP_RANGES.get(subcategory, (50, 500))
    return round(rng.uniform(lo, hi), 2)


def get_season(rng):
    return rng.choice(SEASONS)


def get_promotion(category, season):
    return PROMOTION_TABLE.get(category, {}).get(season, "No promotion")


def clean_columns(df):
    df.columns = df.columns.str.strip().str.upper()
    return df
