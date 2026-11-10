# Augustine
# Assignment Library Records

week1 = {"Amina", "Brian", "Cynthia", "Dan", "Esther"}
week2 = {"Brian", "Dan", "Faith", "George", "Amina"}

print("Both weeks:", sorted(week1 & week2))
print("Either week:", sorted(week1 | week2))
print("Only week 1:", sorted(week1 - week2))
print("Only week 2:", sorted(week2 - week1))
print(len(week1 | week2), "different members")

genres = ["Fiction", "Science", "Fiction", "History", "Science", "Fiction", "Business", "History"]

print(len(genres), "books,", len(set(genres)), "genres,", sorted(set(genres)), ",", "Poetry" in genres)

book = {"title": "The River Between", "author": "Ngugi wa Thiong'o", "year": 1965, "copies": 3}

print(book["title"])

book["copies"] = book["copies"] - 1
book["shelf"] = "B4"

print(book.get("isbn", "not recorded"))

for key, value in book.items():
    print(key, "->", value, end=", ")
print()

counts = {}
for g in genres:
    counts[g] = counts.get(g, 0) + 1

print(counts)