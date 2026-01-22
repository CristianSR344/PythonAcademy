# Example 1: invalid conversion
text_values = ["10", "3.14", "abc"]

for t in text_values:
    print(f"Trying to convert {t!r} to int:")
    try:
        number = int(t)
        print("   Success:", number)
    except ValueError as e:
        print("   Failed with ValueError:", e)

print("\nFloat to int truncation:")
floats = [3.1, 3.5, 3.9, -2.7]

for f in floats:
    print(f"float: {f} -> int: {int(f)}")
    

# None and Missing Values

result = None

print("Initial result:", result)
print("Is result None?", result is None)
print("Is bool(result) truthy?", bool(result))

record = {"name": "Nova", "age": 5}
print("\nAccessing record['country'] with .get():")
country = record.get("country")  # returns None by default
print("country:", country)
print("Is country None?", country is None)

print("\nUsing a default when the key is missing:")
country_with_default = record.get("country", "Unknown")
print("country_with_default:", country_with_default)
