
def detect_violations(df):
    for required in ["ADV_PRICE", "MAP"]:
        if required not in df.columns:
            raise KeyError(
                f"Column '{required}' not found after merge.\n"
                f"Available columns: {df.columns.tolist()}"
            )

    df["VIOLATION_MAP"] = df["ADV_PRICE"] < df["MAP"]

    if "MRP" in df.columns and "ALLOWED_DISCOUNT" in df.columns:
        df["DISCOUNT_PCT"]       = ((df["MRP"] - df["ADV_PRICE"]) / df["MRP"]) * 100
        df["VIOLATION_DISCOUNT"] = df["DISCOUNT_PCT"] > df["ALLOWED_DISCOUNT"]
    else:
        print("  Note: MRP / ALLOWED_DISCOUNT not found — discount violation check skipped.")
        df["DISCOUNT_PCT"]       = None
        df["VIOLATION_DISCOUNT"] = False

    if "ALLOWED_REGION" in df.columns and "REGION" in df.columns:
        df["VIOLATION_REGION"] = df["REGION"] != df["ALLOWED_REGION"]
    else:
        df["VIOLATION_REGION"] = False

    df["IS_VIOLATION"] = (
        df["VIOLATION_MAP"] |
        df["VIOLATION_DISCOUNT"] |
        df["VIOLATION_REGION"]
    )

    def _severity(row):
        if row["VIOLATION_MAP"]:
            return "HIGH"
        elif row["VIOLATION_DISCOUNT"]:
            return "MEDIUM"
        else:
            return "LOW"

    df["SEVERITY"] = df.apply(_severity, axis=1)

    total = df["IS_VIOLATION"].sum()
    print(f"\n  Total violations detected: {total}")
    return df
