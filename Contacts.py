import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

def add_contact(ip, nickname):
    contacts = load_contacts()
    contacts[ip] = nickname
    save_contacts(contacts)
    print(f"Added {ip} as '{nickname}'.")

def main():
    ip = input("Enter IP address: ")
    nickname = input("Enter nickname: ")
    add_contact(ip, nickname)

if __name__ == "__main__":
    main()
