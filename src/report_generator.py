def build_seller_summary(df):
    violators = df[df["IS_VIOLATION"]]

    if "SELLER_NAME" not in violators.columns:
        raise KeyError(
            "Column 'SELLER_NAME' not found.\n"
            f"Available: {violators.columns.tolist()}"
        )

    marketplace_col = "MARKETPLACE" if "MARKETPLACE" in violators.columns else None
    agg = {"SKU": "count"}
    if marketplace_col:
        agg[marketplace_col] = "nunique"

    summary = (
        violators
        .groupby("SELLER_NAME")
        .agg(agg)
        .reset_index()
        .rename(columns={
            "SKU": "VIOLATION_COUNT",
            **({"MARKETPLACE": "MARKETPLACE_COUNT"} if marketplace_col else {}),
        })
    )
    return summary, violators
