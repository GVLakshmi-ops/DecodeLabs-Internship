import pandas as pd
# STEP 1: Loading the raw dataset
df = pd.read_excel('Dataset for Data Analytics.xlsx')
print("=" * 50)
print("RAW DATASET AUDIT")
print("=" * 50)
print(f"Shape: {df.shape}")
print(f"\nNull values per column:\n{df.isnull().sum()}")
print(f"\nDuplicate rows: {df.duplicated().sum()}")
print(f"Duplicate OrderIDs: {df['OrderID'].duplicated().sum()}")
print(f"\nData types:\n{df.dtypes}")


# CR001 - Handle Missing Values (CouponCode)

missing_before = df['CouponCode'].isnull().sum()
df['CouponCode'] = df['CouponCode'].fillna('No Coupon')
print(f"\n[CR001] Filled {missing_before} missing CouponCode values with 'No Coupon'")

# CR002 - Remove Duplicates

before = len(df)
df = df.drop_duplicates(subset='OrderID', keep='first')
after = len(df)
print(f"[CR002] Duplicate check: {before - after} duplicate rows removed. {after} records retained.")

# CR003 - Standardize Date Format (YYYY-MM-DD)
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
print(f"[CR003] Date column standardized to YYYY-MM-DD format.")


# CR004 - Fix Numeric Precision (2 decimals)
df['UnitPrice'] = df['UnitPrice'].round(2)
df['TotalPrice'] = df['TotalPrice'].round(2)
print(f"[CR004] UnitPrice and TotalPrice rounded to 2 decimal places.")

# CR005 - Standardize Text Columns
text_cols = ['Product', 'PaymentMethod', 'OrderStatus', 'ReferralSource', 'CouponCode']
for col in text_cols:
    df[col] = df[col].str.strip().str.title()
print(f"[CR005] Text columns trimmed and converted to Proper Case.")

# FINAL VERIFICATION (Threshold Check)
print("\n" + "=" * 50)
print("FINAL VERIFICATION")
print("=" * 50)

import re
assert df['OrderID'].duplicated().sum() == 0, "FAIL: Duplicate IDs found!"
print("PASSED: Zero duplicate OrderIDs")

bad_dates = df['Date'].apply(lambda x: not bool(re.match(r'^\d{4}-\d{2}-\d{2}$', str(x))))
assert bad_dates.sum() == 0, "FAIL: Bad date formats found!"
print("PASSED: All dates in YYYY-MM-DD format")

assert df.isnull().sum().sum() == 0, "FAIL: Null values still present!"
print("PASSED: Zero null values remaining")

print(f"\nFinal dataset shape: {df.shape}")


# EXPORT Cleaned File
df.to_excel('Cleaned_Dataset.xlsx', index=False)
print("\n [success] Cleaned dataset saved as 'Cleaned_Dataset.xlsx'")