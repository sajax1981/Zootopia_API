import data_fetcher

def serialize_animal(animal_obj):
    """Serializes a single animal object into HTML."""
    output = f"""
    <li class="cards__item">
        <div class="card__title">{animal_obj['name']}</div>
        <p class="card__text">
            <strong>Diet:</strong> {animal_obj['characteristics'].get('diet', 'Unknown')}<br/>
            <strong>Location:</strong> {', '.join(animal_obj['locations'])}<br/>
            <strong>Type:</strong> {animal_obj['characteristics'].get('type', 'Unknown')}<br/>
        </p>
    </li>
    """
    return output


def generate_error_message(animal_name):
    """Generates an HTML error message for non-existent animals."""
    output = f"""
    <div class="error-message">
        <h2>The animal "{animal_name}" doesn’t exist.</h2>
        <p>It looks like we couldn’t find any information about "{animal_name}" in our database. 
           Maybe it’s typo? Try another name!</p>
    </div>
    """
    return output


def generate_html_content(animals, animal_name):
    """Generates the complete HTML string, with error message if no animals found."""
    if not animals:  # Check if the list is empty
        return generate_error_message(animal_name)

    html_list = ""
    for animal in animals:
        html_list += serialize_animal(animal)
    return html_list


def main():
    """Fetches data from API based on user input, generates HTML, and writes to a file."""

    # Prompt user for animal name
    animal_name = input("Enter a name of an animal: ")
    # Fetch data from the API
    animals_data = data_fetcher.fetch_data(animal_name)

    # Read the HTML template
    with open("animals_template.html", "r") as template_file:
        template_content = template_file.read()

    # Generate the animal list HTML or error message
    animal_html_list = generate_html_content(animals_data, animal_name)

    # Replace placeholder with generated HTML
    new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animal_html_list)

    # Write to output file
    with open("animals.html", "w") as output_file:
        output_file.write(new_html_content)
    print("Website was successfully generated to the file animals.html")

if __name__ == "__main__":
    main()