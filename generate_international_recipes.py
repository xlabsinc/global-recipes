import json

# Define all cuisines and their recipes
cuisines = {
    "chinese": {
        "start_id": 161,
        "recipes": [
            {"name": "Kung Pao Chicken", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍗", "description": "Spicy stir-fried chicken with peanuts and vegetables.", "tags": ["Spicy", "Stir-fry"]},
            {"name": "Sweet and Sour Pork", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍖", "description": "Crispy pork in tangy sweet and sour sauce.", "tags": ["Sweet", "Tangy"]},
            {"name": "Mapo Tofu", "category": "Main Course", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥘", "description": "Spicy Sichuan tofu with minced pork and chili oil.", "tags": ["Spicy", "Sichuan"]},
            {"name": "Spring Rolls", "category": "Snack", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🥢", "description": "Crispy fried rolls with vegetable filling.", "tags": ["Fried", "Appetizer"]},
            {"name": "Peking Duck", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Hard", "emoji": "🦆", "description": "Crispy roasted duck with thin pancakes.", "tags": ["Roasted", "Traditional"]},
            {"name": "Fried Rice", "category": "Rice", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍚", "description": "Stir-fried rice with vegetables and eggs.", "tags": ["Quick", "Easy"]},
            {"name": "Dim Sum", "category": "Snack", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🥟", "description": "Steamed dumplings with various fillings.", "tags": ["Steamed", "Traditional"]},
            {"name": "Hot Pot", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍲", "description": "Communal pot of simmering broth with ingredients.", "tags": ["Interactive", "Spicy"]},
            {"name": "Chow Mein", "category": "Main Course", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍜", "description": "Stir-fried noodles with vegetables.", "tags": ["Noodles", "Quick"]},
            {"name": "Wonton Soup", "category": "Soup", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🥣", "description": "Clear broth with pork-filled wontons.", "tags": ["Soup", "Comfort"]},
            {"name": "Char Siu", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🥓", "description": "Cantonese BBQ pork with sweet glaze.", "tags": ["BBQ", "Sweet"]},
            {"name": "Ma La Xiang Guo", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🌶️", "description": "Spicy stir-fry with numbing Sichuan peppercorns.", "tags": ["Spicy", "Numbing"]},
            {"name": "Congee", "category": "Breakfast", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥣", "description": "Rice porridge with toppings.", "tags": ["Breakfast", "Comfort"]},
            {"name": "Xiaolongbao", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Hard", "emoji": "🥟", "description": "Soup dumplings with pork filling.", "tags": ["Steamed", "Delicate"]},
            {"name": "Twice Cooked Pork", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🥩", "description": "Sichuan-style pork belly with leeks.", "tags": ["Spicy", "Rich"]},
            {"name": "Dan Dan Noodles", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍜", "description": "Spicy Sichuan noodles with minced pork.", "tags": ["Spicy", "Noodles"]},
            {"name": "Century Egg Tofu", "category": "Side Dish", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥚", "description": "Cold dish with preserved eggs and silken tofu.", "tags": ["Cold", "Traditional"]},
            {"name": "Scallion Pancake", "category": "Snack", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🥞", "description": "Crispy flatbread with scallions.", "tags": ["Fried", "Savory"]},
            {"name": "Steamed Fish", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🐟", "description": "Whole fish steamed with ginger and soy.", "tags": ["Steamed", "Healthy"]},
            {"name": "Sesame Balls", "category": "Dessert", "type": "Vegetarian", "difficulty": "Medium", "emoji": "⚪", "description": "Deep-fried glutinous rice balls with sesame.", "tags": ["Sweet", "Dessert"]},
        ]
    },
    "vietnamese": {
        "start_id": 181,
        "recipes": [
            {"name": "Pho", "category": "Soup", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍜", "description": "Aromatic beef noodle soup with herbs.", "tags": ["Soup", "Traditional"]},
            {"name": "Banh Mi", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🥖", "description": "Vietnamese baguette sandwich with pork.", "tags": ["Sandwich", "Street Food"]},
            {"name": "Spring Rolls", "category": "Snack", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🌯", "description": "Fresh rice paper rolls with vegetables.", "tags": ["Fresh", "Healthy"]},
            {"name": "Bun Cha", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍲", "description": "Grilled pork with noodles and herbs.", "tags": ["Grilled", "Noodles"]},
            {"name": "Cao Lau", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍜", "description": "Hoi An specialty noodles with pork.", "tags": ["Regional", "Noodles"]},
            {"name": "Com Tam", "category": "Rice", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍚", "description": "Broken rice with grilled pork.", "tags": ["Rice", "Grilled"]},
            {"name": "Goi Cuon", "category": "Snack", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🌯", "description": "Fresh summer rolls with shrimp.", "tags": ["Fresh", "Light"]},
            {"name": "Banh Xeo", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🥞", "description": "Crispy turmeric crepe with pork and shrimp.", "tags": ["Crispy", "Street Food"]},
            {"name": "Bun Bo Hue", "category": "Soup", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍜", "description": "Spicy beef noodle soup from Hue.", "tags": ["Spicy", "Soup"]},
            {"name": "Cha Ca", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🐟", "description": "Turmeric fish with dill and noodles.", "tags": ["Fish", "Aromatic"]},
            {"name": "Banh Cuon", "category": "Breakfast", "type": "Non-Vegetarian", "difficulty": "Hard", "emoji": "🌯", "description": "Steamed rice rolls with pork.", "tags": ["Steamed", "Delicate"]},
            {"name": "Mi Quang", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍜", "description": "Turmeric noodles with pork and shrimp.", "tags": ["Noodles", "Regional"]},
            {"name": "Canh Chua", "category": "Soup", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🥣", "description": "Sweet and sour fish soup.", "tags": ["Soup", "Tangy"]},
            {"name": "Ga Nuong", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍗", "description": "Grilled lemongrass chicken.", "tags": ["Grilled", "Aromatic"]},
            {"name": "Banh Bao", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🥟", "description": "Steamed buns with pork filling.", "tags": ["Steamed", "Bun"]},
            {"name": "Che", "category": "Dessert", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍨", "description": "Sweet dessert soup with beans.", "tags": ["Dessert", "Sweet"]},
            {"name": "Ca Kho To", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🐟", "description": "Caramelized fish in clay pot.", "tags": ["Braised", "Sweet"]},
            {"name": "Nem Nuong", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🌭", "description": "Grilled pork sausage skewers.", "tags": ["Grilled", "Snack"]},
            {"name": "Xoi", "category": "Breakfast", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍚", "description": "Sticky rice with toppings.", "tags": ["Breakfast", "Rice"]},
            {"name": "Banh Flan", "category": "Dessert", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🍮", "description": "Vietnamese crème caramel.", "tags": ["Dessert", "French"]},
        ]
    },
    "korean": {
        "start_id": 201,
        "recipes": [
            {"name": "Kimchi", "category": "Side Dish", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🥬", "description": "Fermented spicy cabbage.", "tags": ["Fermented", "Spicy"]},
            {"name": "Bibimbap", "category": "Rice", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍚", "description": "Mixed rice with vegetables and egg.", "tags": ["Rice", "Healthy"]},
            {"name": "Bulgogi", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🥩", "description": "Marinated grilled beef.", "tags": ["Grilled", "Sweet"]},
            {"name": "Japchae", "category": "Main Course", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🍜", "description": "Stir-fried glass noodles with vegetables.", "tags": ["Noodles", "Festive"]},
            {"name": "Kimchi Jjigae", "category": "Soup", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍲", "description": "Spicy kimchi stew with pork.", "tags": ["Spicy", "Stew"]},
            {"name": "Tteokbokki", "category": "Snack", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🌶️", "description": "Spicy stir-fried rice cakes.", "tags": ["Spicy", "Street Food"]},
            {"name": "Korean Fried Chicken", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍗", "description": "Crispy chicken with sweet-spicy glaze.", "tags": ["Fried", "Popular"]},
            {"name": "Samgyeopsal", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🥓", "description": "Grilled pork belly slices.", "tags": ["Grilled", "BBQ"]},
            {"name": "Sundubu Jjigae", "category": "Soup", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥘", "description": "Soft tofu stew with vegetables.", "tags": ["Spicy", "Stew"]},
            {"name": "Galbi", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍖", "description": "Marinated beef short ribs.", "tags": ["BBQ", "Sweet"]},
            {"name": "Kimbap", "category": "Snack", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍱", "description": "Seaweed rice rolls with vegetables.", "tags": ["Rolled", "Portable"]},
            {"name": "Jajangmyeon", "category": "Main Course", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🍜", "description": "Noodles in black bean sauce.", "tags": ["Noodles", "Comfort"]},
            {"name": "Pajeon", "category": "Snack", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥞", "description": "Savory scallion pancake.", "tags": ["Fried", "Crispy"]},
            {"name": "Bossam", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🥩", "description": "Boiled pork belly with wraps.", "tags": ["Boiled", "Wraps"]},
            {"name": "Naengmyeon", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍜", "description": "Cold buckwheat noodles in broth.", "tags": ["Cold", "Summer"]},
            {"name": "Mandu", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🥟", "description": "Korean dumplings with meat filling.", "tags": ["Steamed", "Dumplings"]},
            {"name": "Yukgaejang", "category": "Soup", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍲", "description": "Spicy beef soup with vegetables.", "tags": ["Spicy", "Hearty"]},
            {"name": "Hodugwaja", "category": "Dessert", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🥜", "description": "Walnut-shaped pastry with red bean.", "tags": ["Sweet", "Pastry"]},
            {"name": "Bindaetteok", "category": "Snack", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🥞", "description": "Mung bean pancake.", "tags": ["Fried", "Savory"]},
            {"name": "Patbingsu", "category": "Dessert", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍧", "description": "Shaved ice with sweet toppings.", "tags": ["Dessert", "Summer"]},
        ]
    },
    "thai": {
        "start_id": 221,
        "recipes": [
            {"name": "Pad Thai", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍜", "description": "Stir-fried rice noodles with shrimp.", "tags": ["Noodles", "Popular"]},
            {"name": "Tom Yum", "category": "Soup", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍲", "description": "Spicy sour shrimp soup.", "tags": ["Spicy", "Sour"]},
            {"name": "Green Curry", "category": "Curry", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍛", "description": "Spicy coconut curry with chicken.", "tags": ["Spicy", "Coconut"]},
            {"name": "Pad Krapow", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍚", "description": "Basil chicken stir-fry with rice.", "tags": ["Spicy", "Quick"]},
            {"name": "Som Tam", "category": "Side Dish", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥗", "description": "Spicy green papaya salad.", "tags": ["Spicy", "Fresh"]},
            {"name": "Massaman Curry", "category": "Curry", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍛", "description": "Rich curry with potatoes and peanuts.", "tags": ["Mild", "Rich"]},
            {"name": "Larb", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🥗", "description": "Spicy minced meat salad.", "tags": ["Spicy", "Fresh"]},
            {"name": "Khao Soi", "category": "Soup", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍜", "description": "Northern Thai curry noodle soup.", "tags": ["Curry", "Noodles"]},
            {"name": "Satay", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "�串", "description": "Grilled meat skewers with peanut sauce.", "tags": ["Grilled", "Peanut"]},
            {"name": "Tom Kha Gai", "category": "Soup", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🥥", "description": "Coconut chicken soup.", "tags": ["Coconut", "Mild"]},
            {"name": "Pad See Ew", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍜", "description": "Stir-fried flat noodles with soy sauce.", "tags": ["Noodles", "Savory"]},
            {"name": "Pla Pao", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🐟", "description": "Grilled whole fish with herbs.", "tags": ["Grilled", "Fish"]},
            {"name": "Gaeng Keow Wan", "category": "Curry", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🥦", "description": "Green curry with vegetables.", "tags": ["Spicy", "Vegetable"]},
            {"name": "Moo Ping", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🥓", "description": "Grilled pork skewers.", "tags": ["Grilled", "Street Food"]},
            {"name": "Khao Pad", "category": "Rice", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍚", "description": "Thai fried rice.", "tags": ["Rice", "Quick"]},
            {"name": "Panaeng Curry", "category": "Curry", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍛", "description": "Thick red curry with meat.", "tags": ["Rich", "Spicy"]},
            {"name": "Kai Jeow", "category": "Snack", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍳", "description": "Thai omelet.", "tags": ["Quick", "Simple"]},
            {"name": "Mango Sticky Rice", "category": "Dessert", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥭", "description": "Sweet sticky rice with mango.", "tags": ["Dessert", "Sweet"]},
            {"name": "Khanom Krok", "category": "Dessert", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🥥", "description": "Coconut pancakes.", "tags": ["Dessert", "Sweet"]},
            {"name": "Thai Tea", "category": "Dessert", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🧋", "description": "Sweet iced tea with milk.", "tags": ["Beverage", "Sweet"]},
        ]
    },
}

# Generate JSON files (2 files per cuisine, 10 recipes each)
for cuisine_name, cuisine_data in cuisines.items():
    start_id = cuisine_data["start_id"]
    recipes_list = cuisine_data["recipes"]
    
    # Create 2 files per cuisine
    for file_num in range(1, 3):
        filename = f"/Users/B1V6/tmp20/recipes-{cuisine_name}-0{file_num}.json"
        start_idx = (file_num - 1) * 10
        end_idx = start_idx + 10
        
        file_recipes = []
        for i, recipe_data in enumerate(recipes_list[start_idx:end_idx]):
            recipe_id = start_id + start_idx + i
            
            # Create full recipe object
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
        
        # Write to file
        with open(filename, 'w') as f:
            json.dump(file_recipes, f, indent=2)
        
        print(f"✓ Created {filename} (IDs {start_id + start_idx}-{start_id + end_idx - 1})")

print(f"\nCreated {len(cuisines) * 2} files with {len(cuisines) * 20} recipes!")
