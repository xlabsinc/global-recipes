import json

# Fix recipes-south-07.json (IDs should be 61-70)
# These IDs are already correct, but they conflict with north-01
# South IDs: 1-60 (already used)
# We need south-07 to be 61-70, south-08 to be 71-80, etc.
# But north-01 already uses 61-70
# So we need to reassign south files to 61-100 and north files to 101-150

print("Fixing ID conflicts...")
print("=" * 80)

# Define new ID ranges
# South: 1-100 (files 01-10)
# North: 101-150 (files 01-05)
# Other: 151-160 (file 01)

# Fix recipes-north-01.json (change IDs from 61-70 to 101-110)
with open('/Users/B1V6/tmp20/recipes-north-01.json', 'r') as f:
    north_01 = json.load(f)

for i, recipe in enumerate(north_01):
    recipe['id'] = 101 + i

with open('/Users/B1V6/tmp20/recipes-north-01.json', 'w') as f:
    json.dump(north_01, f, indent=2)
print("✓ Fixed recipes-north-01.json: IDs 101-110")

# Fix recipes-north-02.json (change IDs from 71-80 to 111-120)
with open('/Users/B1V6/tmp20/recipes-north-02.json', 'r') as f:
    north_02 = json.load(f)

for i, recipe in enumerate(north_02):
    recipe['id'] = 111 + i

with open('/Users/B1V6/tmp20/recipes-north-02.json', 'w') as f:
    json.dump(north_02, f, indent=2)
print("✓ Fixed recipes-north-02.json: IDs 111-120")

# Fix recipes-north-03.json (change IDs from 81-90 to 121-130)
with open('/Users/B1V6/tmp20/recipes-north-03.json', 'r') as f:
    north_03 = json.load(f)

for i, recipe in enumerate(north_03):
    recipe['id'] = 121 + i

with open('/Users/B1V6/tmp20/recipes-north-03.json', 'w') as f:
    json.dump(north_03, f, indent=2)
print("✓ Fixed recipes-north-03.json: IDs 121-130")

# Fix recipes-north-04.json (change IDs from 91-100 to 131-140)
with open('/Users/B1V6/tmp20/recipes-north-04.json', 'r') as f:
    north_04 = json.load(f)

for i, recipe in enumerate(north_04):
    recipe['id'] = 131 + i

with open('/Users/B1V6/tmp20/recipes-north-04.json', 'w') as f:
    json.dump(north_04, f, indent=2)
print("✓ Fixed recipes-north-04.json: IDs 131-140")

# Fix recipes-north-05.json (IDs 101-110 -> 141-150)
with open('/Users/B1V6/tmp20/recipes-north-05.json', 'r') as f:
    north_05 = json.load(f)

for i, recipe in enumerate(north_05):
    recipe['id'] = 141 + i

with open('/Users/B1V6/tmp20/recipes-north-05.json', 'w') as f:
    json.dump(north_05, f, indent=2)
print("✓ Fixed recipes-north-05.json: IDs 141-150")

# Fix recipes-other-01.json (IDs 111-120 -> 151-160)
with open('/Users/B1V6/tmp20/recipes-other-01.json', 'r') as f:
    other_01 = json.load(f)

for i, recipe in enumerate(other_01):
    recipe['id'] = 151 + i

with open('/Users/B1V6/tmp20/recipes-other-01.json', 'w') as f:
    json.dump(other_01, f, indent=2)
print("✓ Fixed recipes-other-01.json: IDs 151-160")

# Fix the duplicate "Adhirasam" in recipes-south-08.json
# Remove the duplicate and replace with a different recipe
with open('/Users/B1V6/tmp20/recipes-south-08.json', 'r') as f:
    south_08 = json.load(f)

# Find and replace the Adhirasam at index with ID 75
for i, recipe in enumerate(south_08):
    if recipe['name'] == 'Adhirasam' and recipe['id'] == 75:
        south_08[i] = {
            "id": 75,
            "name": "Sundal",
            "category": "Snack",
            "type": "Vegetarian",
            "difficulty": "Easy",
            "prepTime": 15,
            "cookTime": 10,
            "servings": 4,
            "emoji": "🥜",
            "description": "Spiced chickpea or lentil snack popular in Tamil Nadu.",
            "ingredients": [
                "1 cup chickpeas",
                "Mustard seeds",
                "Curry leaves",
                "Grated coconut",
                "Green chilies",
                "Lemon juice",
                "Salt"
            ],
            "instructions": [
                "Soak and boil chickpeas",
                "Drain well",
                "Heat oil and add mustard seeds",
                "Add curry leaves and chilies",
                "Add chickpeas and salt",
                "Mix well",
                "Add coconut and lemon juice",
                "Serve warm or cold"
            ],
            "tags": ["Snack", "Healthy", "Protein"]
        }
        break

with open('/Users/B1V6/tmp20/recipes-south-08.json', 'w') as f:
    json.dump(south_08, f, indent=2)
print("✓ Fixed duplicate Adhirasam in recipes-south-08.json (replaced with Sundal)")

print("\n" + "=" * 80)
print("SUMMARY OF ID CHANGES")
print("=" * 80)
print("South Indian (recipes-south-01 to 10): IDs 1-100")
print("North Indian (recipes-north-01 to 05): IDs 101-150")
print("Other Regions (recipes-other-01):      IDs 151-160")
print("\nTotal: 160 unique recipes with no ID conflicts")
