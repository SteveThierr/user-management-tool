def clean_name(name):
    return name.strip().title()


def valid_email(email):
    email = email.strip()
    if " " in email:
        return False
    if "@" not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    return "." in parts[1]


def count_vowels(word):
    count = 0
    for letter in word.lower():
        if letter in "aeiou":
            count += 1
    return count


def is_palindrome(s):
    cleaned = "".join(c.lower() for c in s if c.isalpha())
    return cleaned == cleaned[::-1]


def filter_by_name_length(users, min_length):
    filtered = []
    for user in users:
        if len(user["name"]) > min_length:
            filtered.append(user)
    return filtered


def summarise(users):
    if not users:
        return None
    vowel_counts = [count_vowels(u["name"]) for u in users]
    total = sum(vowel_counts)
    average = round(total / len(vowel_counts), 1)
    longest = max(users, key=lambda u: len(u["name"]))
    return {
        "total": total,
        "average": average,
        "longest": longest["name"]
    }


def top_two(users):
    first = {"name": "", "vowels": float("-inf")}
    second = {"name": "", "vowels": float("-inf")}

    for user in users:
        v = count_vowels(user["name"])
        if v > first["vowels"]:
            second = first
            first = {"name": user["name"], "vowels": v}
        elif v > second["vowels"]:
            second = {"name": user["name"], "vowels": v}

    return [x for x in [first, second] if x["vowels"] > float("-inf")]