# Bitwarden Vault Deduplicates Remover

A lightweight Python utility to identify and remove duplicate login entries from a Bitwarden vault export.

## ⚠️ Disclaimer
**Your data is your responsibility.**
- **Always** create a permanent backup of your vault before performing a purge/import.
- **Never** upload your `.json` export files to GitHub.

## Usage
1. Export your Bitwarden vault as **JSON**.
2. Name it `bitwarden_export.json` in this folder.
3. Run `python dedupe.py`.
4. Import `cleaned_vault.json` back to Bitwarden after purging the old vault.
