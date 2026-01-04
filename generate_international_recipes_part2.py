import json

cuisines = {
    "japanese": {
        "start_id": 241,
        "recipes": [
            {"name": "Sushi", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Hard", "emoji": "🍣", "description": "Vinegared rice with raw fish.", "tags": ["Raw", "Traditional"]},
            {"name": "Ramen", "category": "Soup", "type": "Non-Vegetarian", "difficulty": "Hard", "emoji": "🍜", "description": "Noodle soup with rich broth.", "tags": ["Noodles", "Comfort"]},
            {"name": "Tempura", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍤", "description": "Batter-fried seafood and vegetables.", "tags": ["Fried", "Crispy"]},
            {"name": "Tonkatsu", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🥩", "description": "Breaded deep-fried pork cutlet.", "tags": ["Fried", "Crispy"]},
            {"name": "Yakitori", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍢", "description": "Grilled chicken skewers.", "tags": ["Grilled", "Savory"]},
            {"name": "Udon", "category": "Soup", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍜", "description": "Thick wheat noodles in broth.", "tags": ["Noodles", "Simple"]},
            {"name": "Okonomiyaki", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🥞", "description": "Savory cabbage pancake.", "tags": ["Griddled", "Savory"]},
            {"name": "Takoyaki", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🐙", "description": "Octopus balls with sauce.", "tags": ["Street Food", "Fried"]},
            {"name": "Soba", "category": "Main Course", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍜", "description": "Buckwheat noodles served cold or hot.", "tags": ["Noodles", "Healthy"]},
            {"name": "Katsudon", "category": "Rice", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍚", "description": "Rice bowl with breaded pork and egg.", "tags": ["Rice", "Comfort"]},
            {"name": "Gyoza", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🥟", "description": "Pan-fried dumplings.", "tags": ["Dumplings", "Crispy"]},
            {"name": "Teriyaki Chicken", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍗", "description": "Glazed chicken with sweet soy sauce.", "tags": ["Sweet", "Grilled"]},
            {"name": "Miso Soup", "category": "Soup", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥣", "description": "Soybean paste soup with tofu.", "tags": ["Soup", "Simple"]},
            {"name": "Onigiri", "category": "Snack", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍙", "description": "Rice balls with various fillings.", "tags": ["Rice", "Portable"]},
            {"name": "Shabu Shabu", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍲", "description": "Hot pot with thinly sliced meat.", "tags": ["Hot Pot", "Interactive"]},
            {"name": "Curry Rice", "category": "Rice", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍛", "description": "Japanese-style curry with rice.", "tags": ["Curry", "Comfort"]},
            {"name": "Sukiyaki", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🥘", "description": "Sweet beef hot pot.", "tags": ["Hot Pot", "Sweet"]},
            {"name": "Dorayaki", "category": "Dessert", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥞", "description": "Pancake sandwich with red bean.", "tags": ["Dessert", "Sweet"]},
            {"name": "Matcha Ice Cream", "category": "Dessert", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍨", "description": "Green tea flavored ice cream.", "tags": ["Dessert", "Cold"]},
            {"name": "Yakisoba", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍜", "description": "Stir-fried noodles with vegetables.", "tags": ["Noodles", "Stir-fry"]},
        ]
    },
    "european": {
        "start_id": 261,
        "recipes": [
            {"name": "Pizza Margherita", "category": "Main Course", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🍕", "description": "Italian pizza with tomato and mozzarella.", "tags": ["Italian", "Classic"]},
            {"name": "Pasta Carbonara", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍝", "description": "Creamy pasta with bacon and egg.", "tags": ["Italian", "Creamy"]},
            {"name": "Paella", "category": "Rice", "type": "Non-Vegetarian", "difficulty": "Hard", "emoji": "🥘", "description": "Spanish saffron rice with seafood.", "tags": ["Spanish", "Seafood"]},
            {"name": "Moussaka", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Hard", "emoji": "🍆", "description": "Greek eggplant casserole.", "tags": ["Greek", "Baked"]},
            {"name": "Ratatouille", "category": "Side Dish", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🍅", "description": "French vegetable stew.", "tags": ["French", "Vegetable"]},
            {"name": "Schnitzel", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🥩", "description": "Austrian breaded veal cutlet.", "tags": ["Austrian", "Fried"]},
            {"name": "Goulash", "category": "Soup", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍲", "description": "Hungarian beef stew with paprika.", "tags": ["Hungarian", "Hearty"]},
            {"name": "Pierogi", "category": "Main Course", "type": "Vegetarian", "difficulty": "Hard", "emoji": "🥟", "description": "Polish dumplings with potato.", "tags": ["Polish", "Comfort"]},
            {"name": "Tiramisu", "category": "Dessert", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🍰", "description": "Italian coffee dessert.", "tags": ["Italian", "Dessert"]},
            {"name": "Croque Monsieur", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🥪", "description": "French grilled ham and cheese.", "tags": ["French", "Sandwich"]},
            {"name": "Tapas", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍢", "description": "Spanish small plates.", "tags": ["Spanish", "Appetizer"]},
            {"name": "Risotto", "category": "Rice", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🍚", "description": "Italian creamy rice dish.", "tags": ["Italian", "Creamy"]},
            {"name": "Sauerbraten", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Hard", "emoji": "🥩", "description": "German pot roast.", "tags": ["German", "Braised"]},
            {"name": "Bouillabaisse", "category": "Soup", "type": "Non-Vegetarian", "difficulty": "Hard", "emoji": "🐟", "description": "French fish stew.", "tags": ["French", "Seafood"]},
            {"name": "Stroganoff", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍄", "description": "Russian beef in sour cream sauce.", "tags": ["Russian", "Creamy"]},
            {"name": "Fondue", "category": "Main Course", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🫕", "description": "Swiss melted cheese dish.", "tags": ["Swiss", "Cheese"]},
            {"name": "Baklava", "category": "Dessert", "type": "Vegetarian", "difficulty": "Hard", "emoji": "🥐", "description": "Turkish layered pastry with nuts.", "tags": ["Turkish", "Sweet"]},
            {"name": "Pesto Pasta", "category": "Main Course", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍝", "description": "Pasta with basil sauce.", "tags": ["Italian", "Fresh"]},
            {"name": "Crepes", "category": "Dessert", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥞", "description": "French thin pancakes.", "tags": ["French", "Versatile"]},
            {"name": "Gazpacho", "category": "Soup", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥣", "description": "Spanish cold tomato soup.", "tags": ["Spanish", "Cold"]},
        ]
    },
    "british": {
        "start_id": 281,
        "recipes": [
            {"name": "Fish and Chips", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🐟", "description": "Battered fried fish with potato chips.", "tags": ["Fried", "Classic"]},
            {"name": "Shepherd's Pie", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🥧", "description": "Meat pie with mashed potato topping.", "tags": ["Comfort", "Baked"]},
            {"name": "Beef Wellington", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Hard", "emoji": "🥩", "description": "Beef wrapped in pastry.", "tags": ["Elegant", "Baked"]},
            {"name": "Full English Breakfast", "category": "Breakfast", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍳", "description": "Complete breakfast with eggs, bacon, beans.", "tags": ["Hearty", "Traditional"]},
            {"name": "Bangers and Mash", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🌭", "description": "Sausages with mashed potatoes.", "tags": ["Comfort", "Simple"]},
            {"name": "Yorkshire Pudding", "category": "Side Dish", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🥐", "description": "Baked batter pudding.", "tags": ["Baked", "Side"]},
            {"name": "Cornish Pasty", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Hard", "emoji": "🥟", "description": "Pastry filled with meat and vegetables.", "tags": ["Pastry", "Portable"]},
            {"name": "Toad in the Hole", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🌭", "description": "Sausages in Yorkshire pudding batter.", "tags": ["Baked", "Comfort"]},
            {"name": "Scotch Egg", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🥚", "description": "Boiled egg wrapped in sausage meat.", "tags": ["Fried", "Portable"]},
            {"name": "Bubble and Squeak", "category": "Side Dish", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥔", "description": "Fried leftover vegetables.", "tags": ["Simple", "Comfort"]},
            {"name": "Cottage Pie", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🥧", "description": "Beef pie with mashed potato.", "tags": ["Comfort", "Baked"]},
            {"name": "Ploughman's Lunch", "category": "Snack", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🧀", "description": "Cheese, bread, and pickles.", "tags": ["Cold", "Simple"]},
            {"name": "Eton Mess", "category": "Dessert", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍓", "description": "Meringue with cream and strawberries.", "tags": ["Dessert", "Sweet"]},
            {"name": "Sticky Toffee Pudding", "category": "Dessert", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🍮", "description": "Moist cake with toffee sauce.", "tags": ["Dessert", "Sweet"]},
            {"name": "Steak and Kidney Pie", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Hard", "emoji": "🥧", "description": "Meat pie with rich gravy.", "tags": ["Traditional", "Hearty"]},
            {"name": "Scones", "category": "Snack", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥐", "description": "Baked pastry for afternoon tea.", "tags": ["Tea", "Baked"]},
            {"name": "Victoria Sponge", "category": "Dessert", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍰", "description": "Layered cake with jam and cream.", "tags": ["Dessert", "Classic"]},
            {"name": "Black Pudding", "category": "Breakfast", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "⚫", "description": "Blood sausage.", "tags": ["Traditional", "Breakfast"]},
            {"name": "Lancashire Hotpot", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍲", "description": "Lamb stew with potato topping.", "tags": ["Stew", "Comfort"]},
            {"name": "Apple Crumble", "category": "Dessert", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍎", "description": "Baked apple with crumb topping.", "tags": ["Dessert", "Baked"]},
        ]
    },
    "american": {
        "start_id": 301,
        "recipes": [
            {"name": "Hamburger", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍔", "description": "Beef patty in a bun.", "tags": ["Classic", "Fast Food"]},
            {"name": "Hot Dog", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🌭", "description": "Sausage in a bun.", "tags": ["Street Food", "Simple"]},
            {"name": "BBQ Ribs", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍖", "description": "Grilled ribs with BBQ sauce.", "tags": ["BBQ", "Smoky"]},
            {"name": "Mac and Cheese", "category": "Side Dish", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🧀", "description": "Macaroni pasta with cheese sauce.", "tags": ["Comfort", "Cheesy"]},
            {"name": "Fried Chicken", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍗", "description": "Crispy fried chicken pieces.", "tags": ["Fried", "Southern"]},
            {"name": "Buffalo Wings", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍗", "description": "Spicy chicken wings.", "tags": ["Spicy", "Sports Food"]},
            {"name": "Philly Cheesesteak", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🥪", "description": "Beef sandwich with cheese.", "tags": ["Sandwich", "Cheesy"]},
            {"name": "Clam Chowder", "category": "Soup", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🥣", "description": "Creamy soup with clams.", "tags": ["Soup", "Seafood"]},
            {"name": "Jambalaya", "category": "Rice", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🍚", "description": "Cajun rice with meat and seafood.", "tags": ["Cajun", "Spicy"]},
            {"name": "Gumbo", "category": "Soup", "type": "Non-Vegetarian", "difficulty": "Hard", "emoji": "🍲", "description": "Louisiana stew with okra.", "tags": ["Cajun", "Hearty"]},
            {"name": "Chicken and Waffles", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Medium", "emoji": "🧇", "description": "Fried chicken with waffles.", "tags": ["Sweet", "Savory"]},
            {"name": "Corn Dog", "category": "Snack", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🌽", "description": "Hot dog in cornmeal batter.", "tags": ["Fried", "Fair Food"]},
            {"name": "Cobb Salad", "category": "Side Dish", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🥗", "description": "Salad with chicken, bacon, and egg.", "tags": ["Salad", "Healthy"]},
            {"name": "Meatloaf", "category": "Main Course", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🥩", "description": "Baked ground beef loaf.", "tags": ["Comfort", "Baked"]},
            {"name": "Biscuits and Gravy", "category": "Breakfast", "type": "Non-Vegetarian", "difficulty": "Easy", "emoji": "🍞", "description": "Biscuits with sausage gravy.", "tags": ["Breakfast", "Southern"]},
            {"name": "Pancakes", "category": "Breakfast", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🥞", "description": "Fluffy breakfast pancakes.", "tags": ["Breakfast", "Sweet"]},
            {"name": "Apple Pie", "category": "Dessert", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🥧", "description": "Classic baked apple pie.", "tags": ["Dessert", "Classic"]},
            {"name": "Brownies", "category": "Dessert", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍫", "description": "Chocolate fudge squares.", "tags": ["Dessert", "Chocolate"]},
            {"name": "Cheesecake", "category": "Dessert", "type": "Vegetarian", "difficulty": "Medium", "emoji": "🍰", "description": "Cream cheese cake.", "tags": ["Dessert", "Creamy"]},
            {"name": "S'mores", "category": "Dessert", "type": "Vegetarian", "difficulty": "Easy", "emoji": "🍫", "description": "Toasted marshmallow with chocolate.", "tags": ["Dessert", "Campfire"]},
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
