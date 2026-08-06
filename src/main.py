def main():

    # ── Stage 1: Build enriched reference tables ───────────────────────────
    print("=" * 60)
    print("STAGE 1: Enriching source data")
    print("=" * 60)

    pl_data   = load_pl_table(PL_TABLE_PATH)
    sku_to_pn = load_sku_xml(SKU_TABLE_PATH)
    print(f"  PL records  : {len(pl_data)}")
    print(f"  SKU->PN map : {len(sku_to_pn)} entries")

    records = enrich_records(pl_data, sku_to_pn)
    print(f"  Enriched    : {len(records)} records")

    write_pl_table(records,         "PL_table_enriched.xlsx")
    write_price_list(records,       "Price_list_enriched.xlsx")
    write_category_mapping(records, "Category_mapping_enriched.xlsx")
    write_promotion_table(records,  "Promotion_table_enriched.xlsx")

    # ── Stage 2: Load seller data ──────────────────────────────────────────
    print("\n" + "=" * 60)
    print("STAGE 2: Loading seller data")
    print("=" * 60)
    master_df = load_seller_data(SELLER_FOLDER)

    # ── Stage 3: Load enriched tables & merge ─────────────────────────────
    print("\n" + "=" * 60)
    print("STAGE 3: Merging tables")
    print("=" * 60)
    price_df = clean_columns(pd.read_excel("Price_list_enriched.xlsx"))
    pl_df    = clean_columns(pd.read_excel("PL_table_enriched.xlsx"))
    promo_df = clean_columns(pd.read_excel("Promotion_table_enriched.xlsx"))
    cat_df   = clean_columns(pd.read_excel("Category_mapping_enriched.xlsx"))

    df = merge_all(master_df, price_df, pl_df, promo_df, cat_df)

    # ── Stage 4: Detect violations ─────────────────────────────────────────
    print("\n" + "=" * 60)
    print("STAGE 4: Detecting violations")
    print("=" * 60)
    df = detect_violations(df)

    # ── Stage 5: Plain-text reports & console email drafts ────────────────
    print("\n" + "=" * 60)
    print("STAGE 5: Generating reports & email drafts (console)")
    print("=" * 60)
    summary, violators = build_seller_summary(df)

    for seller in violators["SELLER_NAME"].unique():
        seller_df = violators[violators["SELLER_NAME"] == seller]
        email_msg = generate_email(seller, seller_df)
        print("\n" + "─" * 50)
        print(email_msg)

    # ── Stage 6: Generate violation email documents (.docx + .pdf) ────────
    print("\n" + "=" * 60)
    print("STAGE 6: Generating violation email documents (.docx + .pdf)")
    print("=" * 60)
    print(f"  Output folder: {VIOLATION_DOCS_FOLDER}/")
    print("  Format: Formal email document (letterhead + email header + body + violation table)")

    for seller in violators["SELLER_NAME"].unique():
        seller_df = violators[violators["SELLER_NAME"] == seller]
        print(f"\n  Processing: {seller}  ({len(seller_df)} violations)")
        generate_violation_documents(seller, seller_df)

    # ── Stage 7: Save output Excel files ──────────────────────────────────
    print("\n" + "=" * 60)
    print("STAGE 7: Saving output files")
    print("=" * 60)
    df.to_excel("final_violation_data.xlsx", index=False)
    summary.to_excel("seller_violation_summary.xlsx", index=False)
    print("  Saved -> final_violation_data.xlsx")
    print("  Saved -> seller_violation_summary.xlsx")
    print("\nDone! Pipeline completed successfully.")


if __name__ == "__main__":
    main()
