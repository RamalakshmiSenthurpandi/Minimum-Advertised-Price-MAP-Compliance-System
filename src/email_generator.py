def generate_email(seller_name, seller_df):
    """Draft a plain-text violation notice (printed to console)."""
    lines = []
    for _, row in seller_df.iterrows():
        sku      = getattr(row, "SKU",       "N/A")
        price    = getattr(row, "ADV_PRICE", "N/A")
        severity = getattr(row, "SEVERITY",  "N/A")
        lines.append(f"  - SKU: {sku} | Advertised Price: {price} | Severity: {severity}")

    details = "\n".join(lines)
    return f"""
Subject: Urgent: Pricing Policy Violation Notice

Dear {seller_name},

We have detected the following pricing violations in your marketplace listings:

{details}
