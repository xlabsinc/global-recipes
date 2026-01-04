import json
import os
from collections import defaultdict

# Get all recipe files
recipe_files = sorted([f for f in os.listdir('/Users/B1V6/tmp20') if f.startswith('recipes-') and f.endswith('.json')])

# Track recipes by ID, name, and ingredients
recipes_by_id = {}
recipes_by_name = defaultdict(list)
recipes_by_ingredients = defaultdict(list)

all_recipes = []
total_recipes = 0

print("=" * 80)
print("CHECKING FOR DUPLICATE RECIPES")
print("=" * 80)

# Load all recipes
for filename in recipe_files:
    filepath = f'/Users/B1V6/tmp20/{filename}'
    with open(filepath, 'r') as f:
        recipes = json.load(f)
        
    print(f"\n{filename}: {len(recipes)} recipes")
    
    for recipe in recipes:
        recipe_id = recipe.get('id')
        recipe_name = recipe.get('name', '').lower().strip()
        ingredients_key = '|'.join(sorted([ing.lower().strip() for ing in recipe.get('ingredients', [])]))
        
        # Track by ID
        if recipe_id in recipes_by_id:
            print(f"  ⚠️  DUPLICATE ID: {recipe_id} - {recipe['name']} (also in {recipes_by_id[recipe_id]['file']})")
        else:
            recipes_by_id[recipe_id] = {'recipe': recipe, 'file': filename}
        
        # Track by name
        recipes_by_name[recipe_name].append({'recipe': recipe, 'file': filename})
        
        # Track by ingredients (exact match)
        recipes_by_ingredients[ingredients_key].append({'recipe': recipe, 'file': filename})
        
        all_recipes.append({'recipe': recipe, 'file': filename})
        total_recipes += 1

print("\n" + "=" * 80)
print("DUPLICATE ANALYSIS")
print("=" * 80)

# Check for duplicate names
duplicate_names = {name: items for name, items in recipes_by_name.items() if len(items) > 1}
if duplicate_names:
    print(f"\n⚠️  Found {len(duplicate_names)} recipes with duplicate names:")
    for name, items in sorted(duplicate_names.items()):
        print(f"\n  '{name.title()}':")
        for item in items:
            print(f"    - ID {item['recipe']['id']} in {item['file']}")
else:
    print("\n✓ No duplicate recipe names found")

# Check for duplicate ingredients (exact match)
duplicate_ingredients = {key: items for key, items in recipes_by_ingredients.items() if len(items) > 1}
if duplicate_ingredients:
    print(f"\n⚠️  Found {len(duplicate_ingredients)} recipes with identical ingredients:")
    for items in duplicate_ingredients.values():
        if len(items) > 1:
            print(f"\n  Recipes:")
            for item in items:
                print(f"    - {item['recipe']['name']} (ID {item['recipe']['id']}) in {item['file']}")
else:
    print("\n✓ No recipes with identical ingredients found")

# Summary
print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"Total files: {len(recipe_files)}")
print(f"Total recipes: {total_recipes}")
print(f"Unique IDs: {len(recipes_by_id)}")
print(f"Unique names: {len(recipes_by_name)}")

# Check ID ranges
print("\n" + "=" * 80)
print("ID RANGES")
print("=" * 80)
ids = sorted(recipes_by_id.keys())
print(f"ID range: {min(ids)} to {max(ids)}")

# Check for gaps
gaps = []
for i in range(min(ids), max(ids)):
    if i not in recipes_by_id:
        gaps.append(i)

if gaps:
    print(f"⚠️  Missing IDs: {gaps}")
else:
    print("✓ No gaps in ID sequence")

print("\n" + "=" * 80)
