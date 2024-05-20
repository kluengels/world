countries = [
    {"capital": "cologne"},
    {"capital": "Berlin"},
    {},
 ]

countries = [c for c in countries if "capital" in c]
print(countries)