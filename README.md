# Minimum-Advertised-Price-MAP-Compliance-System
# MAP Compliance Pipeline

## Project Overview

This project automates the detection of Minimum Advertised Price (MAP) violations by processing multiple product and seller datasets. It consolidates pricing information, validates compliance rules, identifies violations, and generates reports for business teams.

---

## Objectives

- Load product and pricing data from multiple file formats.
- Standardize seller pricing information.
- Merge datasets using SKU information.
- Detect MAP, discount, and regional violations.
- Generate violation reports.
- Prepare seller notification data.

---

## Technologies Used

- Python
- Pandas
- OpenPyXL
- PyYAML
- XML Processing
- JSON

---

## Project Workflow

1. Load Product Line data
2. Load SKU information
3. Load MAP logic table
4. Load Seller Marketplace data
5. Standardize pricing columns
6. Merge all datasets
7. Detect pricing violations
8. Generate final compliance report

---

## Violation Rules

### MAP Violation

Advertised Price < MAP Price

### Discount Violation

Discount exceeds the allowed limit.

### Region Violation

Seller region differs from the permitted region.

---

## Output

The pipeline generates a consolidated report containing:

- Product Details
- Seller Details
- Advertised Price
- MAP Price
- Violation Type
- Severity
- Compliance Status

---

## Features

- Automated data integration
- Multi-format file support
- Rule-based validation
- Scalable processing
- Easy report generation

---

## Folder Structure

```
MAP-Compliance-Pipeline
│
├── data
├── src
├── output
├── screenshots
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Future Improvements

- Dashboard Integration
- Automated Email Notifications
- Database Connectivity
- Web Application Interface

---

## Disclaimer

This repository contains only sample data and demonstration files. No confidential or client-owned datasets are included.
