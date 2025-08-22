import requests

def check_username(username):
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"'{username}' is TAKEN.")
    elif response.status_code == 204:
        print(f"'{username}' is AVAILABLE.")
    else:
        print(f"Error: Unable to check '{username}'. Status Code: {response.status_code}")

if __name__ == "__main__":
    username = input("Enter a Minecraft username to check: ").strip()
    check_username(username)
