# users.py

from utils import clean_name, valid_email, count_vowels

users = [
    {"id": 1, "name": "Amara Diallo",      "email": "amara@example.com",   "role": "Admin"},
    {"id": 2, "name": "Kwame Asante",      "email": "kwame@example.com",   "role": "Editor"},
    {"id": 3, "name": "Fatou Ndiaye",      "email": "fatou@example.com",   "role": "Viewer"},
    {"id": 4, "name": "Ibrahim Coulibaly", "email": "ibrahim@example.com", "role": "Editor"},
]

def get_all_users():
    return users
def add_user(name, email, role):
    errors = {}

    if not name.strip():
        errors["name"] = "Name is required"

    if not valid_email(email):
        errors["email"] = "Invalid email — no spaces, needs @ and a dot after it"

    if email in [u["email"] for u in users]:
        errors["email"] = "That email is already registered"

    if errors:
        return {"success": False, "errors": errors}

    new_user = {
        "id": len(users) + 1,
        "name": clean_name(name),
        "email": email.strip(),
        "role": role,
    }
    users.append(new_user)
    return {"success": True, "user": new_user}

def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]

def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None
if __name__ == "__main__":
    print("--- All users ---")
    for u in get_all_users():
        print(u)

    print("\n--- Add valid user ---")
    print(add_user("AMINA TRAORE", "amina@example.com", "Viewer"))

    print("\n--- Add duplicate email ---")
    print(add_user("Someone Else", "amara@example.com", "Viewer"))

    print("\n--- Add invalid email ---")
    print(add_user("Test User", "notvalid", "Editor"))

    print("\n--- Delete user 1 ---")
    delete_user(1)
    for u in get_all_users():
        print(u)

    print("\n--- Get user by id ---")
    print(get_user_by_id(3))
    print(get_user_by_id(99))