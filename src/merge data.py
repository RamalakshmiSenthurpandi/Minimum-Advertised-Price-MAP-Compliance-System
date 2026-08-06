def merge_all(master_df, price_df, pl_df, promo_df, cat_df):
    for df in [price_df, pl_df, promo_df, cat_df]:
        clean_columns(df)

    pl_df_clean    = pl_df.drop(columns=["BRAND", "CATEGORY", "SUB_CATEGORY"], errors="ignore")
    promo_df_clean = promo_df.drop(columns=["BRAND", "CATEGORY", "SUB_CATEGORY", "PL"], errors="ignore")
    cat_df_clean   = cat_df.drop(columns=["BRAND", "CATEGORY", "SUB_CATEGORY", "PL"], errors="ignore")

    df = (
        master_df
        .merge(price_df,       on="SKU", how="left", suffixes=("", "_PRICE"))
        .merge(pl_df_clean,    on="SKU", how="left", suffixes=("", "_PL"))
        .merge(promo_df_clean, on="SKU", how="left", suffixes=("", "_PROMO"))
        .merge(cat_df_clean,   on="SKU", how="left", suffixes=("", "_CAT"))
    )

    if "MAP_PRICE" in df.columns and "MAP" not in df.columns:
        df.rename(columns={"MAP_PRICE": "MAP"}, inplace=True)
    elif "MAP_x" in df.columns:
        df.rename(columns={"MAP_x": "MAP"}, inplace=True)
        df.drop(columns=["MAP_y"], errors="ignore", inplace=True)

    print(f"\n  Merged shape  : {df.shape}")
    print(f"  Merged columns: {df.columns.tolist()}")
    return df

