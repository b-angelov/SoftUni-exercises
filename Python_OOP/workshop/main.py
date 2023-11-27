from hash_table import HashTable

if __name__ == "__main__":
    table = HashTable()
    print(bool(table))
    table["name"] = "Peter"
    table["age"] = 25
    table["name"] = "Bobby"
    table["age"] = 35
    table["other"] = None
    table["else"] = 5
    table["value"] = "Invaluable"

    print(table)
    print(table.get("name"))
    print(table["age"])
    print(len(table))

    for i in table:
        print(i)
    del table["value"]
    for i in table:
        print(i)
    new_table = HashTable()
    new_table["others_name"] = "No name"
    sibling_table = table + new_table
    print(sibling_table, len(sibling_table))
    print(bool(table))