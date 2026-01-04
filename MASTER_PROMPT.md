# Master Prompt - Global Recipe Collection Web Application

This is a comprehensive single prompt that can be used to recreate the entire Global Recipe Collection project from scratch (420 recipes from around the world).

---

## Complete Project Prompt

```
Create a complete recipe collection web application with the following specifications:

## PROJECT OVERVIEW
Build a single-page HTML application for browsing and managing cooking recipes,
similar to https://xlabsinc.github.io/cocktails/ but for global cuisines. The
application should be self-contained (all CSS/JavaScript embedded), feature an
Apple-inspired design aesthetic, and be ready for GitHub Pages deployment.

## RECIPE DATA
Create 420 recipes from around the world across 40 JSON files organized in a recipes/ folder:

### File Structure & Naming:
**All files should be placed in a recipes/ subfolder**

**Indian Recipes (16 files, 160 recipes):**
- recipes/recipes-south-01.json through recipes/recipes-south-10.json (100 South Indian recipes)
- recipes/recipes-north-01.json through recipes/recipes-north-05.json (50 North Indian recipes)
- recipes/recipes-other-01.json (10 other regional Indian recipes)

**Asian Recipes (12 files, 120 recipes):**
- recipes/recipes-chinese-01.json, recipes/recipes-chinese-02.json (20 Chinese recipes)
- recipes/recipes-vietnamese-01.json, recipes/recipes-vietnamese-02.json (20 Vietnamese recipes)
- recipes/recipes-korean-01.json, recipes/recipes-korean-02.json (20 Korean recipes)
- recipes/recipes-thai-01.json, recipes/recipes-thai-02.json (20 Thai recipes)
- recipes/recipes-japanese-01.json, recipes/recipes-japanese-02.json (20 Japanese recipes)

**Western Recipes (6 files, 60 recipes):**
- recipes/recipes-european-01.json, recipes/recipes-european-02.json (20 European recipes)
- recipes/recipes-british-01.json, recipes/recipes-british-02.json (20 British recipes)
- recipes/recipes-american-01.json, recipes/recipes-american-02.json (20 American recipes)

**Middle Eastern & Other (6 files, 80 recipes):**
- recipes/recipes-iranian-01.json, recipes/recipes-iranian-02.json (20 Iranian recipes)
- recipes/recipes-middleeastern-01.json, recipes/recipes-middleeastern-02.json (20 Middle Eastern recipes)
- recipes/recipes-australian-01.json, recipes/recipes-australian-02.json (20 Australian recipes)
- recipes/recipes-african-01.json, recipes/recipes-african-02.json (20 African recipes)

### ID Assignment:
**Indian Recipes:**
- South Indian: IDs 1-100 (10 recipes per file)
- North Indian: IDs 101-150 (10 recipes per file)
- Other regions: IDs 151-160 (10 recipes in file)

**Asian Recipes:**
- Chinese: IDs 161-180 (10 recipes per file)
- Vietnamese: IDs 181-200 (10 recipes per file)
- Korean: IDs 201-220 (10 recipes per file)
- Thai: IDs 221-240 (10 recipes per file)
- Japanese: IDs 241-260 (10 recipes per file)

**Western Recipes:**
- European: IDs 261-280 (10 recipes per file)
- British: IDs 281-300 (10 recipes per file)
- American: IDs 301-320 (10 recipes per file)

**Middle Eastern & Other:**
- Iranian: IDs 321-340 (10 recipes per file)
- Middle Eastern: IDs 341-360 (10 recipes per file)
- Australian: IDs 361-380 (10 recipes per file)
- African: IDs 381-400 (10 recipes per file)

### JSON Structure:
Each recipe must include:
{
  "id": 1,
  "name": "Recipe Name",
  "category": "Breakfast|Main Course|Curry|Rice|Snack|Dessert|Side Dish|Soup|Bread",
  "type": "Vegetarian|Non-Vegetarian",
  "difficulty": "Easy|Medium|Hard",
  "prepTime": 15,  // minutes
  "cookTime": 20,  // minutes
  "servings": 4,
  "emoji": "🍛",
  "description": "Brief description of the dish",
  "ingredients": ["2 cups flour", "1 cup water", "Salt to taste"],
  "instructions": ["Step 1", "Step 2", "Step 3"],
  "tags": ["Quick", "Easy", "Popular"]
}

### Recipe Requirements:
- All 420 recipes must be unique (no duplicates by name or ID)
- Include authentic dishes from each cuisine
- South Indian: Masala Dosa, Idli, Sambar, Vada, Pongal, etc.
- North Indian: Butter Chicken, Paneer, Chole, Parathas, etc.
- Other Indian: Dhokla, Pav Bhaji, Rasgulla, Momos, etc.
- Chinese: Kung Pao Chicken, Mapo Tofu, Peking Duck, Dim Sum, etc.
- Vietnamese: Pho, Banh Mi, Spring Rolls, Bun Cha, etc.
- Korean: Kimchi, Bibimbap, Bulgogi, Japchae, etc.
- Thai: Pad Thai, Tom Yum, Green Curry, Som Tam, etc.
- Japanese: Sushi, Ramen, Tempura, Tonkatsu, etc.
- European: Pizza, Pasta, Paella, Moussaka, Schnitzel, etc.
- British: Fish and Chips, Shepherd's Pie, Beef Wellington, etc.
- American: Hamburger, BBQ Ribs, Mac and Cheese, Fried Chicken, etc.
- Iranian: Ghormeh Sabzi, Tahdig, Fesenjan, Kabab Koobideh, etc.
- Middle Eastern: Hummus, Falafel, Shawarma, Tabbouleh, etc.
- Australian: Meat Pie, Lamington, Pavlova, Barramundi, etc.
- African: Jollof Rice, Injera, Bobotie, Peri-Peri Chicken, etc.
- Mix of vegetarian (~70%) and non-vegetarian (~30%)
- Mix of difficulty levels (Easy ~50%, Medium ~35%, Hard ~15%)
- Use two-digit file numbering for proper sorting

## HTML APPLICATION FEATURES

### Core Functionality:
1. **Auto-load recipes on start:**
   - Load all 40 JSON files automatically
   - Support loading from local files OR remote URL
   - Include BASE_URL configuration constant:
     ```javascript
     const BASE_URL = '';  // Empty for local, or set to remote URL
     ```

2. **Search & Filter:**
   - Real-time search across recipe names, ingredients, categories, tags
   - Category filter buttons (All, Breakfast, Curry, Rice, etc.)
   - Type dropdown filter (All Types, Vegetarian, Non-Vegetarian)
   - Exact type matching (searching "Veg" should NOT match "Non-Vegetarian")
   - Display limit: Show 30 recipes initially
   - Show "Showing X of Y recipes" counter

3. **Recipe Display:**
   - Display recipes as cards in a grid layout
   - Each card shows: emoji, name, category, prep+cook time, servings, difficulty
   - Click card to expand in place and show full recipe
   - Expanded view shows ingredients list and numbered instructions
   - Support viewing multiple recipes simultaneously

4. **Recipe Management:**
   - Minimize button (−) on expanded cards
   - Minimized recipes go to fixed dock at bottom of screen
   - Close button (×) to dismiss recipes completely
   - Restore button (↑) in dock to bring back minimized recipes
   - Dock shows recipe name with emoji in horizontal scroll
   - Blue border highlight for currently viewing recipes

5. **File Management:**
   - Load additional JSON files from computer (multiple selection)
   - Load recipes from remote URL (GitHub Gist, raw URLs, etc.)
   - Single-line expandable loader:
     - Button: "📁 Load Recipes"
     - Expands to show two options: "Load from Computer" and "Load from URL"
   - Display loaded files with recipe count in collapsible section
   - Loaded files section collapsed by default on page load
   - Remove button (×) for each loaded file
   - Prevent duplicate category filter buttons

6. **Help System:**
   - Button: "❓ Help"
   - Expands to show complete JSON structure guide
   - Include example recipe with all fields
   - List required vs optional fields
   - Provide tips (validate at jsonlint.com, use GitHub Gist for sharing)

### User Interface Design:
**Apple-Inspired Design Aesthetic:**
- San Francisco font system (-apple-system, BlinkMacSystemFont)
- Clean, minimal interface with subtle shadows
- Blue color palette inspired by Apple (#0071e3, #00c6ff, #0072ff)
- Light/white card colors for contrast against blue background
- Smooth animations and transitions

- **Header:**
  - Title: "🌍 Global Recipe Collection"
  - Subtitle: "Discover 400+ authentic recipes from around the world"
  - Blue gradient background (#00c6ff to #0072ff)

- **Search Bar:**
  - Large search input with icon
  - Placeholder: "Search by recipe name or ingredient..."
  - White background, rounded corners

- **Controls Section:**
  - Type filter dropdown at top
  - Category filter buttons (pill-shaped, active state in Apple blue #0071e3)
  - Single-line loader buttons (Load Recipes, Help)
  - Expandable sections for loader and help
  - Collapsible loaded files section (collapsed by default)

- **Recipe Cards:**
  - White background, rounded corners, shadow
  - Hover effect: lift up slightly with blue shadow
  - Expanded: full width, two-column layout (ingredients | instructions)
  - Card header colors:
    - Normal state: Light gray gradient (#f8f9fa to #e9ecef) with dark text (#1d3557)
    - Expanded state: Blue gradient (#0071e3 to #005bb5) with white text
  - Ingredient checkmarks in Apple blue (#0071e3)
  - Step numbers in Apple blue circles
  - Action buttons adapt to header color (blue tint on light, white on blue)

- **Docked Area:**
  - Fixed at bottom of screen
  - White background with blue top border (#0071e3)
  - Horizontal scrolling for multiple cards
  - Blue gradient for docked cards
  - Show when recipes are docked, hide when empty

### Technical Requirements:
1. **Single HTML File:**
   - All CSS embedded in <style> tag
   - All JavaScript embedded in <script> tag
   - No external dependencies (no jQuery, no frameworks)
   - Pure vanilla JavaScript

2. **JavaScript Features:**
   - ES6+ syntax (async/await, arrow functions, template literals)
   - Fetch API for loading files
   - Maps for tracking loaded files and docked cards
   - Real-time filtering with input event listeners
   - Dynamic DOM manipulation

3. **CSS Features:**
   - CSS Grid for recipe layout
   - Flexbox for components
   - Smooth transitions and animations
   - Responsive design (mobile-friendly)
   - Media queries for breakpoints (@768px, @968px)

4. **State Management:**
   - `recipes` array - all loaded recipes
   - `filteredRecipes` array - current filtered view
   - `loadedFiles` Map - tracks loaded files
   - `dockedCards` Map - tracks minimized recipes
   - `currentFilter` - active category
   - `currentTypeFilter` - active type filter

5. **Key Functions to Implement:**
   - `loadRecipes()` - Load built-in files with BASE_URL support
   - `loadFromURL()` - Load from remote URL
   - `filterRecipes()` - Apply search and filters
   - `displayRecipes()` - Render recipe cards
   - `expandRecipe(id)` - Show full recipe
   - `dockRecipe(id)` - Minimize to dock
   - `closeRecipe(id)` - Dismiss recipe
   - `restoreRecipe(id)` - Restore from dock
   - `setupFilters()` - Generate category buttons (clear first to prevent duplicates)
   - `updateFileList()` - Show loaded files
   - `removeFile(filename)` - Unload file
   - `toggleLoader()` - Show/hide loader section
   - `toggleHelp()` - Show/hide help section
   - `toggleLoadedFiles()` - Show/hide loaded files list

## DOCUMENTATION

Create the following documentation files:

1. **README.md:**
   - Project title and description
   - Features list
   - Live demo link placeholder
   - Screenshot placeholder
   - Recipe JSON structure
   - How to add recipes
   - Contributing guidelines
   - License (MIT)

2. **SETUP.md:**
   - GitHub Pages deployment instructions
   - Local development setup
   - BASE_URL configuration guide
   - Deployment options (local, GitHub, Gist, CDN)

3. **CONTRIBUTING.md:**
   - How to contribute recipes
   - JSON validation requirements
   - Pull request guidelines
   - Recipe guidelines (authentic, accurate measurements)

4. **VERSION_6_FINAL.md:**
   - Complete feature list
   - File structure
   - ID assignment strategy
   - Deployment options with examples
   - Validation report
   - Technical details

## VALIDATION REQUIREMENTS

Before completing, validate:
- ✓ All 420 recipe IDs are unique (1-400, no gaps)
- ✓ No duplicate recipe names
- ✓ All files use two-digit numbering (01-10, not 1-10)
- ✓ All JSON files are valid and loadable
- ✓ Search and filters work correctly
- ✓ Minimize/restore/close functions work
- ✓ File loading works (local and URL)
- ✓ Mobile responsive
- ✓ No console errors
- ✓ Category buttons don't duplicate when loading files
- ✓ Loaded files section collapsed by default
- ✓ Apple-style colors applied throughout

## DEPLOYMENT CONFIGURATION

Include clear instructions for BASE_URL:

```javascript
// For local files (default):
const BASE_URL = '';

// For GitHub repository:
const BASE_URL = 'https://raw.githubusercontent.com/username/repo/main/';

// For GitHub Gist:
const BASE_URL = 'https://gist.githubusercontent.com/username/gist-id/raw/';

// For custom server:
const BASE_URL = 'https://cdn.example.com/recipes/';
```

## DELIVERABLES

1. **index.html** (~45KB)
   - Complete single-page application
   - All CSS and JavaScript embedded
   - BASE_URL configuration at line ~954
   - Apple-style design aesthetic
   - Ready for GitHub Pages

2. **40 JSON files** (~600KB total)
   - recipes-south-01.json through recipes-south-10.json
   - recipes-north-01.json through recipes-north-05.json
   - recipes-other-01.json
   - recipes-chinese-01.json, recipes-chinese-02.json
   - recipes-vietnamese-01.json, recipes-vietnamese-02.json
   - recipes-korean-01.json, recipes-korean-02.json
   - recipes-thai-01.json, recipes-thai-02.json
   - recipes-japanese-01.json, recipes-japanese-02.json
   - recipes-european-01.json, recipes-european-02.json
   - recipes-british-01.json, recipes-british-02.json
   - recipes-american-01.json, recipes-american-02.json
   - recipes-iranian-01.json, recipes-iranian-02.json
   - recipes-middleeastern-01.json, recipes-middleeastern-02.json
   - recipes-australian-01.json, recipes-australian-02.json
   - recipes-african-01.json, recipes-african-02.json
   - All with unique IDs (1-400) and authentic recipes

3. **Documentation files:**
   - README.md
   - SETUP.md
   - CONTRIBUTING.md
   - VERSION_6_FINAL.md (160 recipes milestone)
   - VERSION_7_GLOBAL.md (420 recipes expansion)
   - PROMPT_HISTORY.md (this conversation)
   - MASTER_PROMPT.md (this document)

4. **Validation:**
   - No duplicate IDs
   - No duplicate recipes
   - All files properly named
   - All features working

## TESTING CHECKLIST

Before considering complete, test:
- [ ] Open index.html in browser
- [ ] Verify all 420 recipes load from 40 files
- [ ] Test search with various terms
- [ ] Test all category filters
- [ ] Test type filter (Veg/Non-Veg)
- [ ] Expand multiple recipes simultaneously
- [ ] Minimize recipes to dock
- [ ] Restore from dock
- [ ] Close recipes
- [ ] Load custom JSON file
- [ ] Load from URL
- [ ] Remove loaded file
- [ ] View help section
- [ ] Toggle loaded files section (should be collapsed by default)
- [ ] Verify Apple-style colors (blue gradients)
- [ ] Test on mobile device
- [ ] Verify no console errors

## OPTIONAL ENHANCEMENTS

Future improvements to consider:
- Recipe images
- Favorites/bookmarking (localStorage)
- Print-friendly views
- Recipe ratings
- Nutrition information
- Meal planning feature
- Shopping list generator
- Cooking timer integration
- Social sharing
- Export recipes to PDF

## SUCCESS CRITERIA

The project is complete when:
1. All 420 unique recipes are created and validated
2. HTML application has all specified features working
3. Apple-style design aesthetic is applied throughout
4. Loaded files section is collapsible and collapsed by default
5. Documentation is comprehensive and clear
6. BASE_URL configuration works for local and remote
7. No duplicates (IDs or recipes) exist
8. File naming follows two-digit convention
9. Mobile responsive and error-free
10. Ready for immediate GitHub Pages deployment

---

## EXAMPLE REPOSITORY STRUCTURE

```
global-recipes/
├── index.html
├── recipes/
│   ├── recipes-south-01.json through recipes-south-10.json (10 files)
│   ├── recipes-north-01.json through recipes-north-05.json (5 files)
│   ├── recipes-other-01.json
│   ├── recipes-chinese-01.json, recipes-chinese-02.json
│   ├── recipes-vietnamese-01.json, recipes-vietnamese-02.json
│   ├── recipes-korean-01.json, recipes-korean-02.json
│   ├── recipes-thai-01.json, recipes-thai-02.json
│   ├── recipes-japanese-01.json, recipes-japanese-02.json
│   ├── recipes-european-01.json, recipes-european-02.json
│   ├── recipes-british-01.json, recipes-british-02.json
│   ├── recipes-american-01.json, recipes-american-02.json
│   ├── recipes-iranian-01.json, recipes-iranian-02.json
│   ├── recipes-middleeastern-01.json, recipes-middleeastern-02.json
│   ├── recipes-australian-01.json, recipes-australian-02.json
│   └── recipes-african-01.json, recipes-african-02.json
├── README.md
├── SETUP.md
├── CONTRIBUTING.md
├── VERSION_6_FINAL.md
├── VERSION_7_GLOBAL.md
├── PROMPT_HISTORY.md
├── MASTER_PROMPT.md
└── LICENSE
```

## TARGET HOSTING

Primary: GitHub Pages
- Repository name: global-recipes (or world-recipe-collection)
- URL: https://username.github.io/global-recipes/
- Branch: main
- Directory: / (root)

## ESTIMATED METRICS

- Total recipes: 420
- Total files: 40 JSON + 1 HTML + 7 docs = 48 files
- Total size: ~650KB
- Load time: <3 seconds
- Browser support: Modern browsers (Chrome, Firefox, Safari, Edge)
- Mobile support: Yes (responsive design)
- Design: Apple-inspired aesthetic

---

## NOTES FOR IMPLEMENTATION

1. **Start with data:** Create all 420 recipes first, ensuring uniqueness
2. **Organize files:** Place all recipe JSON files in a recipes/ subfolder
3. **Build incrementally:** Start with basic viewing, add features progressively
4. **Test frequently:** After each feature, test in browser
5. **Validate data:** Run duplicate checks before finalizing
6. **Document as you go:** Write docs while features are fresh
7. **Think deployment:** Consider both local and remote loading from start
8. **Apply design consistently:** Use Apple-style colors throughout
9. **Maintain contrast:** Ensure light card headers contrast with blue background
10. **Default states:** Set loaded files to collapsed on initial load

This prompt encapsulates the entire Global Recipe Collection project and can be
used to recreate it with any AI assistant or development team.
```

---

**End of Master Prompt**
