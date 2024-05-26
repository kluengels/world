country_data = [
    {"cca3": "DNK", "name": "Denmark"},
    {"cca3": "USA", "name": "United States of America"},
    # more countries...
]

dnk_country = country for country in country_data if country["cca3"] == "DNK"
print(dnk_country)  # Output: {'cca3': 'DNK', 'name': 'Denmark'}