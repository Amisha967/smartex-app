import pandas as pd

# Load raw Kotak SMS dataset
df = pd.read_csv("data/SMS-Data.csv")

# Keep only sender and message text columns
df = df[["senderAddress", "text"]]

# Filter transactional messages (case-insensitive)
keywords = ["credit", "debit", "credited", "debited"]
pattern = "|".join(keywords)
df_filtered = df[df["text"].str.contains(pattern, case=False, na=False)]

# Save cleaned dataset
df_filtered.to_csv("data/cleaned-SMS-Data.csv", index=False)

print(f"✅ Cleaned data saved to data/cleaned-SMS-Data.csv")
print(f"🧾 Rows retained: {len(df_filtered)}")