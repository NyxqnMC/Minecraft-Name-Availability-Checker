import requests

def is_name_available(username: str) -> bool:
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    response = requests.get(url)
    return response.status_code == 204  # 204 means not taken, 200 means taken

if __name__ == "__main__":
    while True:
        name = input("Enter Minecraft username to check (or 'quit' to exit): ").strip()
        if name.lower() == "quit":
            break
        
        if not (3 <= len(name) <= 16 and name.isalnum()):
            print("Invalid username. Must be 3–16 alphanumeric characters.")
            continue

        if is_name_available(name):
            print(f"✅ '{name}' is AVAILABLE!")
        else:
            print(f"❌ '{name}' is TAKEN.")
