import data_fetcher


def generate_website():
    animal_name = input("Please enter an animal: ")

    data = data_fetcher.fetch_data(animal_name)

    if not data:
        print("No data found for the animal.")
        return

    for animal in data:
        print(f"Generating website for {animal['name']}...\n")

        print(f"Animal Name: {animal['name']}")
        print(f"Taxonomy: {animal['taxonomy']}")
        print(f"Locations: {', '.join(animal['locations'])}")
        print(f"Characteristics: {animal['characteristics']}\n")

    with open(f"{animal_name}_website.html", "w") as file:
        file.write(f"<html><head><title>{animal_name} Info</title></head><body>\n")
        for animal in data:
            file.write(f"<h1>{animal['name']}</h1>\n")
            file.write(f"<h2>Taxonomy:</h2><pre>{animal['taxonomy']}</pre>\n")
            file.write(f"<h2>Locations:</h2><p>{', '.join(animal['locations'])}</p>\n")
            file.write(f"<h2>Characteristics:</h2><pre>{animal['characteristics']}</pre>\n")
        file.write("</body></html>")

    print(f"Website generated for {animal_name}!")


if __name__ == "__main__":
    generate_website()
