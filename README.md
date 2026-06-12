# DecodeLabs Internship — Data Analytics Project

A data analytics internship project completed as part of the **DecodeLabs** program. The project focuses on real-world data cleaning and preprocessing using Python and Excel, producing a verified, analysis-ready dataset from a raw e-commerce orders file.

---

## 📁 Repository Contents

| File | Description |
|---|---|
| `data_cleaning.py` | Python script that audits and cleans the raw dataset |
| `Dataset for Data Analytics.xlsx` | Raw input dataset (e-commerce orders) |
| `Cleaned_Dataset.xlsx` | Output dataset after all cleaning transformations |
| `Change_Log.pdf` | Documented changelog of all cleaning rules applied |
| `DATA ANALYTICS p1.pdf` | Project report / Phase 1 write-up |

---

## 🔧 What the Script Does

The `data_cleaning.py` script performs a full audit and cleaning pipeline on the raw Excel dataset, following numbered change requests (CR):

| Change Request | Action |
|---|---|
| **CR001** | Fill missing `CouponCode` values with `"No Coupon"` |
| **CR002** | Remove duplicate rows (keyed on `OrderID`) |
| **CR003** | Standardize the `Date` column to `YYYY-MM-DD` format |
| **CR004** | Round `UnitPrice` and `TotalPrice` to 2 decimal places |
| **CR005** | Strip whitespace and apply Proper Case to all text columns |

After cleaning, the script runs a **final verification** step with assertions to confirm:
- Zero duplicate `OrderID` values
- All dates match the `YYYY-MM-DD` format
- No null values remain anywhere in the dataset

The cleaned output is saved as `Cleaned_Dataset.xlsx`.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- `pandas` library
- `openpyxl` (for Excel read/write)

### Installation

```bash
pip install pandas openpyxl
```

### Running the Script

Ensure `Dataset for Data Analytics.xlsx` is in the same directory as `data_cleaning.py`, then run:

```bash
python data_cleaning.py
```

The script will print a full audit log to the console and produce `Cleaned_Dataset.xlsx` in the same directory.

---

## 📊 Dataset Overview

The dataset contains e-commerce order records with columns including:

- `OrderID` — unique order identifier
- `Date` — order date
- `Product` — product name
- `UnitPrice` — price per unit
- `TotalPrice` — total order value
- `PaymentMethod` — method of payment
- `OrderStatus` — current status of the order
- `ReferralSource` — how the customer was referred
- `CouponCode` — discount coupon used (if any)

---

## 🛠️ Tech Stack

- **Language:** Python
- **Libraries:** pandas
- **Data Format:** Excel (`.xlsx`)

---

## 👤 Author

**GVLakshmi** — [GitHub Profile](https://github.com/GVLakshmi-ops)

Internship completed under the **DecodeLabs** program.
