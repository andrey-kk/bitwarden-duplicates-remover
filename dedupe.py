import json

def deduplicate():
    file_path = 'bitwarden_export.json'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: bitwarden_export.json not found.")
        return

    items = data.get('items', [])
    seen = {}
    unique_items = []
    dup_count = 0

    for item in items:
        if item.get('type') == 1: # Login type
            login = item.get('login', {})
            uris = tuple(sorted([u.get('uri') for u in login.get('uris', []) if u.get('uri')]))
            key = (uris, login.get('username'), login.get('password'))
            
            if key in seen:
                dup_count += 1
                continue
            seen[key] = True
        
        unique_items.append(item)

    data['items'] = unique_items
    with open('cleaned_vault.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    
    print(f"Done! Removed {dup_count} duplicates. Saved to cleaned_vault.json")

if __name__ == "__main__":
    deduplicate()
