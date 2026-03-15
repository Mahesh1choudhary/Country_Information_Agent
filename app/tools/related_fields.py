from app.data import data_loader


def find_matching_fields(base_word:str) -> list[str]:
    matching_fields = set()
    matching_fields.add("name")
    for field, synonyms in data_loader.FIELDS_MAP.items():
        if field == base_word:
            matching_fields.add(field)
        if base_word in synonyms:
            matching_fields.add(field)

    return list(matching_fields)



def find_matching_countries(base_word:str) -> list[str]:
    matching_countries = set()
    for official_name, aliases in data_loader.COUNTRIES_MAP.items():
        if base_word == official_name:
            matching_countries.add(official_name)

        if base_word in aliases:
            matching_countries.add(official_name)

    return list(matching_countries)



