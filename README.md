# Bitwarden Vault Deduplicator[cite: 1]

A lightweight Python utility to identify and remove duplicate login entries from a Bitwarden vault export.[cite: 1]

## ⚠️ Disclaimer[cite: 1]
**Your data is your responsibility.**[cite: 1]
- **Always** create a permanent backup of your vault before performing a purge/import.[cite: 1]
- **Never** upload your `.json` export files to GitHub.[cite: 1]

## Usage[cite: 1]
1. Export your Bitwarden vault as **JSON**.[cite: 1]
2. Name it `bitwarden_export.json` in this folder.[cite: 1]
3. Run `python dedupe.py`.[cite: 1]
4. Import `cleaned_vault.json` back to Bitwarden after purging the old vault.[cite: 1]
