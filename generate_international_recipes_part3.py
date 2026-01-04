import json

cuisines = {
    "iranian": {
        "start_id": 321,
        "recipes": [
            {"name": "Ghormeh Sabzi", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🥘", "description": "Herb stew with kidney beans and lamb.", "tags": ["Stew", "Aromatic"]},
            {"name": "Tahdig", "category": "Rice", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🍚", "description": "Crispy rice from the bottom of the pot.", "tags": ["Rice", "Crispy"]},
            {"name": "Fesenjan", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Hard", "emoji": "🍲", "description": "Chicken in walnut pomegranate sauce.", "tags": ["Rich", "Sweet"]},
            {"name": "Kabab Koobideh", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "�串", "description": "Grilled minced meat kebabs.", "tags": ["Grilled", "Popular"]},
            {"name": "Zereshk Polo", "category": "Rice", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍚", "description": "Rice with barberries and chicken.", "tags": ["Rice", "Festive"]},
            {"name": "Ash Reshteh", "category": "Soup", "type": "Vegetarian", "difficulty": "Hard", "emoji": "🍜", "description": "Thick noodle soup with herbs.", "tags": ["Soup", "Hearty"]},
            {"name": "Khoresh Bademjan", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍆", "description": "Eggplant stew with meat.", "tags": ["Stew", "Rich"]},
            {"name": "Sabzi Polo Mahi", "category": "Rice", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🐟", "description": "Herbed rice with fish.", "tags": ["Rice", "Traditional"]},
            {"name": "Kashk e Bademjan", "category": "Side Dish", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍆", "description": "Eggplant dip with whey.", "tags": ["Dip", "Appetizer"]},
            {"name": "Mirza Ghasemi", "category": "Side Dish", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍅", "description": "Smoky eggplant with tomato.", "tags": ["Smoky", "Vegetarian"]},
            {"name": "Baghali Polo", "category": "Rice", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🍚", "description": "Rice with dill and fava beans.", "tags": ["Rice", "Spring"]},
            {"name": "Kuku Sabzi", "category": "Main Course", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥚", "description": "Herb frittata.", "tags": ["Herbs", "Eggs"]},
            {"name": "Dolmeh", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Hard", "emoji": "🫑", "description": "Stuffed grape leaves or vegetables.", "tags": ["Stuffed", "Traditional"]},
            {"name": "Halim", "category": "Soup", "type": "Non-Vegetarian", "difficulty": "Hard", "emoji": "🥣", "description": "Wheat and meat porridge.", "tags": ["Porridge", "Hearty"]},
            {"name": "Abgoosht", "category": "Soup", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍲", "description": "Lamb and chickpea stew.", "tags": ["Stew", "Traditional"]},
            {"name": "Kotlet", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🥩", "description": "Persian meat patties.", "tags": ["Fried", "Snack"]},
            {"name": "Shirazi Salad", "category": "Side Dish", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥗", "description": "Cucumber tomato salad.", "tags": ["Fresh", "Simple"]},
            {"name": "Bastani", "category": "Dessert", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍨", "description": "Saffron ice cream with pistachios.", "tags": ["Dessert", "Cold"]},
            {"name": "Faloodeh", "category": "Dessert", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🍧", "description": "Frozen noodle dessert.", "tags": ["Dessert", "Cold"]},
            {"name": "Sholeh Zard", "category": "Dessert", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍮", "description": "Saffron rice pudding.", "tags": ["Dessert", "Sweet"]},
        ]
    },
    "middleeastern": {
        "start_id": 341,
        "recipes": [
            {"name": "Hummus", "category": "Side Dish", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥙", "description": "Chickpea dip with tahini.", "tags": ["Dip", "Healthy"]},
            {"name": "Falafel", "category": "Snack", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🧆", "description": "Fried chickpea balls.", "tags": ["Fried", "Vegetarian"]},
            {"name": "Shawarma", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🥙", "description": "Spiced meat wrap.", "tags": ["Wrap", "Street Food"]},
            {"name": "Tabbouleh", "category": "Side Dish", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥗", "description": "Parsley and bulgur salad.", "tags": ["Salad", "Fresh"]},
            {"name": "Baba Ganoush", "category": "Side Dish", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍆", "description": "Smoky eggplant dip.", "tags": ["Dip", "Smoky"]},
            {"name": "Mansaf", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Hard", "emoji": "🍚", "description": "Lamb with yogurt sauce over rice.", "tags": ["Traditional", "Festive"]},
            {"name": "Kibbeh", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Hard", "emoji": "🥩", "description": "Bulgur and meat croquettes.", "tags": ["Fried", "Traditional"]},
            {"name": "Fattoush", "category": "Side Dish", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥗", "description": "Salad with fried pita bread.", "tags": ["Salad", "Crunchy"]},
            {"name": "Mujadara", "category": "Main Course", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍚", "description": "Lentils and rice with caramelized onions.", "tags": ["Vegetarian", "Comfort"]},
            {"name": "Kofta", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍖", "description": "Spiced meatballs.", "tags": ["Grilled", "Spiced"]},
            {"name": "Maqluba", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Hard", "emoji": "🍚", "description": "Upside-down rice and meat casserole.", "tags": ["Rice", "Festive"]},
            {"name": "Fatayer", "category": "Snack", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🥟", "description": "Stuffed pastries with spinach.", "tags": ["Pastry", "Baked"]},
            {"name": "Manakish", "category": "Breakfast", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🫓", "description": "Flatbread with za'atar.", "tags": ["Bread", "Breakfast"]},
            {"name": "Labneh", "category": "Side Dish", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥛", "description": "Strained yogurt cheese.", "tags": ["Dip", "Creamy"]},
            {"name": "Shakshuka", "category": "Breakfast", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍳", "description": "Eggs poached in tomato sauce.", "tags": ["Breakfast", "Eggs"]},
            {"name": "Kunafa", "category": "Dessert", "type": "Vegetarian", "difficulty": "Hard", "emoji": "🍰", "description": "Cheese pastry with syrup.", "tags": ["Dessert", "Sweet"]},
            {"name": "Baklava", "category": "Dessert", "type": "Vegetarian", "difficulty": "Hard", "emoji": "🥐", "description": "Layered phyllo with nuts.", "tags": ["Dessert", "Sweet"]},
            {"name": "Ma'amoul", "category": "Dessert", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🍪", "description": "Date-filled cookies.", "tags": ["Dessert", "Cookie"]},
            {"name": "Halva", "category": "Dessert", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🍬", "description": "Sesame seed sweet.", "tags": ["Dessert", "Sweet"]},
            {"name": "Turkish Coffee", "category": "Dessert", "type": "Vegetarian", "difficulty": "Easy", "emoji": "☕", "description": "Strong unfiltered coffee.", "tags": ["Beverage", "Traditional"]},
        ]
    },
    "australian": {
        "start_id": 361,
        "recipes": [
            {"name": "Meat Pie", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🥧", "description": "Savory pie with meat filling.", "tags": ["Pie", "Classic"]},
            {"name": "Vegemite Toast", "category": "Breakfast", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍞", "description": "Toast with yeast extract spread.", "tags": ["Breakfast", "Australian"]},
            {"name": "Lamington", "category": "Dessert", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🍰", "description": "Sponge cake coated in chocolate and coconut.", "tags": ["Dessert", "Sweet"]},
            {"name": "Pavlova", "category": "Dessert", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🍰", "description": "Meringue dessert with cream and fruit.", "tags": ["Dessert", "Light"]},
            {"name": "Barramundi", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🐟", "description": "Grilled Australian fish.", "tags": ["Fish", "Grilled"]},
            {"name": "Anzac Biscuits", "category": "Dessert", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍪", "description": "Oat and coconut cookies.", "tags": ["Cookie", "Traditional"]},
            {"name": "Sausage Sizzle", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🌭", "description": "Grilled sausage in bread.", "tags": ["BBQ", "Simple"]},
            {"name": "Tim Tam Slam", "category": "Dessert", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍫", "description": "Chocolate biscuits with hot drink.", "tags": ["Dessert", "Fun"]},
            {"name": "Damper", "category": "Bread", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍞", "description": "Bush bread baked in coals.", "tags": ["Bread", "Traditional"]},
            {"name": "Chiko Roll", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🌯", "description": "Deep-fried savory roll.", "tags": ["Fried", "Street Food"]},
            {"name": "Fairy Bread", "category": "Dessert", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍞", "description": "Buttered bread with sprinkles.", "tags": ["Party", "Kids"]},
            {"name": "Kangaroo Steak", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🦘", "description": "Grilled kangaroo meat.", "tags": ["Game", "Australian"]},
            {"name": "Chicken Parmigiana", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍗", "description": "Breaded chicken with tomato and cheese.", "tags": ["Italian-Australian", "Popular"]},
            {"name": "Fish and Chips", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🐟", "description": "Battered fish with chips.", "tags": ["Fried", "Seafood"]},
            {"name": "Witchetty Grub", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🐛", "description": "Aboriginal bush food.", "tags": ["Traditional", "Bush"]},
            {"name": "Emu Steak", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🦢", "description": "Grilled emu meat.", "tags": ["Game", "Lean"]},
            {"name": "Beetroot Burger", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍔", "description": "Burger with beetroot slice.", "tags": ["Australian", "Burger"]},
            {"name": "Golden Gaytime", "category": "Dessert", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍦", "description": "Toffee ice cream on a stick.", "tags": ["Dessert", "Ice Cream"]},
            {"name": "Milo", "category": "Dessert", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥛", "description": "Chocolate malt drink.", "tags": ["Beverage", "Chocolate"]},
            {"name": "Cabanossi", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🌭", "description": "Semi-dried sausage.", "tags": ["Snack", "Portable"]},
        ]
    },
    "african": {
        "start_id": 381,
        "recipes": [
            {"name": "Jollof Rice", "category": "Rice", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍚", "description": "Spiced tomato rice with meat.", "tags": ["West African", "Popular"]},
            {"name": "Injera", "category": "Bread", "type": "Vegetarian", "difficulty": "Hard", "emoji": "🫓", "description": "Ethiopian sourdough flatbread.", "tags": ["Ethiopian", "Traditional"]},
            {"name": "Bobotie", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🥘", "description": "South African spiced meatloaf.", "tags": ["South African", "Spiced"]},
            {"name": "Bunny Chow", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍞", "description": "Curry in hollowed-out bread.", "tags": ["South African", "Street Food"]},
            {"name": "Peri-Peri Chicken", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍗", "description": "Spicy grilled chicken.", "tags": ["Spicy", "Grilled"]},
            {"name": "Fufu", "category": "Side Dish", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🥔", "description": "Pounded yam or cassava.", "tags": ["West African", "Staple"]},
            {"name": "Suya", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍖", "description": "Spicy grilled meat skewers.", "tags": ["Nigerian", "Grilled"]},
            {"name": "Egusi Soup", "category": "Soup", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍲", "description": "Melon seed soup with vegetables.", "tags": ["West African", "Hearty"]},
            {"name": "Boerewors", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🌭", "description": "South African sausage.", "tags": ["South African", "BBQ"]},
            {"name": "Tagine", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍲", "description": "Moroccan slow-cooked stew.", "tags": ["Moroccan", "Aromatic"]},
            {"name": "Couscous", "category": "Side Dish", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍚", "description": "Steamed semolina grains.", "tags": ["North African", "Versatile"]},
            {"name": "Chakalaka", "category": "Side Dish", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🌶️", "description": "Spicy vegetable relish.", "tags": ["South African", "Spicy"]},
            {"name": "Doro Wat", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Hard", "emoji": "🍗", "description": "Ethiopian chicken stew.", "tags": ["Ethiopian", "Spicy"]},
            {"name": "Biltong", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Hard", "emoji": "🥩", "description": "Dried cured meat.", "tags": ["South African", "Snack"]},
            {"name": "Pap", "category": "Side Dish", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥣", "description": "Maize porridge.", "tags": ["South African", "Staple"]},
            {"name": "Moin Moin", "category": "Snack", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🫘", "description": "Steamed bean pudding.", "tags": ["Nigerian", "Protein"]},
            {"name": "Koshari", "category": "Main Course", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🍚", "description": "Egyptian rice, lentils, and pasta.", "tags": ["Egyptian", "Vegetarian"]},
            {"name": "Malva Pudding", "category": "Dessert", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍮", "description": "Sweet spongy dessert.", "tags": ["South African", "Dessert"]},
            {"name": "Koeksister", "category": "Dessert", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🍩", "description": "Twisted fried dough in syrup.", "tags": ["South African", "Sweet"]},
            {"name": "Brik", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🥟", "description": "Tunisian fried pastry with egg.", "tags": ["Tunisian", "Fried"]},
        ]
    },
}

# Generate JSON files
for cuisine_name, cuisine_data in cuisines.items():
    start_id = cuisine_data["start_id"]
    recipes_list = cuisine_data["recipes"]
    
    for file_num in range(1, 3):
        filename = f"/Users/B1V6/tmp20/recipes-{cuisine_name}-0{file_num}.json"
        start_idx = (file_num - 1) * 10
        end_idx = start_idx + 10
        
        file_recipes = []
        for i, recipe_data in enumerate(recipes_list[start_idx:end_idx]):
            recipe_id = start_id + start_idx + i
            
            recipe = {
                "id": recipe_id,
                "name": recipe_data["name"],
                "category": recipe_data["category"],
                "type": recipe_data["type"],
                "difficulty": recipe_data["difficulty"],
                "prepTime": 15,
                "cookTime": 30,
                "servings": 4,
                "emoji": recipe_data["emoji"],
                "description": recipe_data["description"],
                "ingredients": [
                    "Main ingredient 1",
                    "Main ingredient 2",
                    "Spices and seasonings",
                    "Additional ingredients"
                ],
                "instructions": [
                    "Prepare ingredients",
                    "Cook main components",
                    "Combine and season",
                    "Serve hot"
                ],
                "tags": recipe_data["tags"]
            }
            file_recipes.append(recipe)
        
        with open(filename, 'w') as f:
            json.dump(file_recipes, f, indent=2)
        
        print(f"✓ Created {filename} (IDs {start_id + start_idx}-{start_id + end_idx - 1})")

print(f"\nCreated {len(cuisines) * 2} files with {len(cuisines) * 20} recipes!")
print(f"\nTotal international recipes: 260 (13 cuisines x 20 recipes)")
