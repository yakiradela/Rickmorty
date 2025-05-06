import requests
import csv

def get_electric_pokemon():
    url = "https://pokeapi.co/api/v2/type/electric"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    electric_pokemon = data['pokemon']
    results = []

    for entry in electric_pokemon:
        poke_url = entry['pokemon']['url']
        poke_data = requests.get(poke_url).json()
        
        weight_kg = poke_data['weight'] / 10  # מהגרם לק"ג

        if weight_kg < 100:
            name = poke_data['name']
            height = poke_data['height']
            weight = poke_data['weight']
            image = poke_data['sprites']['front_default']
            results.append([name, height, weight, image])

    with open('electric_pokemon.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Height', 'Weight', 'Image'])
        writer.writerows(results)

if __name__ == "__main__":
    get_electric_pokemon()
