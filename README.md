# 🌍 Global Recipe Collection

A beautiful, interactive web application featuring 420 authentic recipes from around the world. Search, explore, and cook delicious dishes from 16 different cuisines across Asia, Europe, Middle East, Africa, Australia, and the Americas.

**Live Demo:** [https://xlabsinc.github.io/global-recipes/](https://xlabsinc.github.io/global-recipes/)

**Repository:** [https://github.com/xlabsinc/global-recipes](https://github.com/xlabsinc/global-recipes)

![Recipes](https://img.shields.io/badge/Recipes-420-orange) ![Cuisines](https://img.shields.io/badge/Cuisines-16-blue) ![License-MIT](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- 🔍 **Real-time Search** - Search by recipe name, ingredients, or tags with instant results
- 🎯 **Smart Filtering** - Filter by category, type (veg/non-veg), and cuisine
- 📱 **Fully Responsive** - Works seamlessly on desktop, tablet, and mobile devices
- 🎨 **Apple-Inspired Design** - Clean, modern interface with beautiful gradients and smooth animations
- 🌈 **Multi-Recipe View** - View multiple recipes simultaneously with expandable/collapsible cards
- 📥 **Docking System** - Minimize recipes to a bottom dock for easy access
- 📂 **Custom Recipe Loading** - Upload your own recipe JSON files or load from URLs
- 🔗 **Remote Loading** - Load recipes from GitHub Gist or any remote URL
- 🌟 **No Dependencies** - Pure HTML, CSS, and JavaScript - no frameworks required
- 🚀 **Fast & Lightweight** - Loads instantly with no backend required

## 🌎 Cuisines Included

### Indian Subcontinent (160 recipes)
- **South Indian** (100 recipes) - Dosa, Idli, Sambar, Biryani, Pongal, Vada
- **North Indian** (50 recipes) - Butter Chicken, Paneer Tikka, Chole, Naan, Rajma
- **Other Regions** (10 recipes) - Dhokla, Pav Bhaji, Momos, Rasgulla

### East Asian (100 recipes)
- **Chinese** (20 recipes) - Kung Pao Chicken, Mapo Tofu, Peking Duck, Dim Sum
- **Vietnamese** (20 recipes) - Pho, Banh Mi, Spring Rolls, Bun Cha
- **Korean** (20 recipes) - Kimchi, Bibimbap, Bulgogi, Tteokbokki
- **Thai** (20 recipes) - Pad Thai, Tom Yum, Green Curry, Som Tam
- **Japanese** (20 recipes) - Sushi, Ramen, Tempura, Tonkatsu

### Western (60 recipes)
- **European** (20 recipes) - Pizza, Pasta Carbonara, Paella, Moussaka, Schnitzel
- **British** (20 recipes) - Fish and Chips, Shepherd's Pie, Beef Wellington
- **American** (20 recipes) - Hamburger, BBQ Ribs, Mac and Cheese, Apple Pie

### Middle Eastern & Other (100 recipes)
- **Iranian** (20 recipes) - Ghormeh Sabzi, Tahdig, Fesenjan, Kabab Koobideh
- **Middle Eastern** (20 recipes) - Hummus, Falafel, Shawarma, Tabbouleh
- **Australian** (20 recipes) - Meat Pie, Lamington, Pavlova, Barramundi
- **African** (20 recipes) - Jollof Rice, Injera, Bobotie, Peri-Peri Chicken

## 🚀 Quick Start

### Option 1: Visit the Live Site

Simply go to [https://xlabsinc.github.io/global-recipes/](https://xlabsinc.github.io/global-recipes/) to start browsing recipes immediately!

### Option 2: Fork and Deploy Your Own

1. Fork this repository on GitHub
2. Go to your fork's Settings > Pages
3. Select "main" branch as source
4. Your site will be live at `https://YOUR-USERNAME.github.io/global-recipes/`

### Option 3: Run Locally

```bash
# Clone the repository
git clone https://github.com/xlabsinc/global-recipes.git

# Navigate to the directory
cd global-recipes

# Open in browser (or use a local server)
open index.html
# OR with Python
python -m http.server 8000
# OR with Node.js
npx serve
```

Then visit `http://localhost:8000` in your browser.

## 📖 Setting Up GitHub Pages

If you want to host your own copy or contribute to this project, here's how to set up GitHub Pages:

### For Contributors (Forking)

1. **Fork the Repository**
   - Go to [https://github.com/xlabsinc/global-recipes](https://github.com/xlabsinc/global-recipes)
   - Click the "Fork" button in the top-right corner
   - This creates a copy in your GitHub account

2. **Enable GitHub Pages on Your Fork**
   - Go to your forked repository
   - Click "Settings" (top-right)
   - Scroll down to "Pages" in the left sidebar
   - Under "Source", select "main" branch
   - Keep "/" (root) as the folder
   - Click "Save"

3. **Access Your Site**
   - Wait 1-2 minutes for deployment
   - Your site will be live at: `https://YOUR-USERNAME.github.io/global-recipes/`

4. **Make Changes**
   - Edit files in your fork
   - Commit and push changes
   - GitHub Pages automatically redeploys (1-2 minutes)

### For Organization Members (Direct Access)

If you have write access to the xlabsinc organization:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/xlabsinc/global-recipes.git
   cd global-recipes
   ```

2. **Make Your Changes**
   - Edit files as needed
   - Test locally before pushing

3. **Commit and Push**
   ```bash
   git add .
   git commit -m "Description of your changes"
   git push origin main
   ```

4. **Automatic Deployment**
   - GitHub Pages automatically rebuilds
   - Changes appear at [https://xlabsinc.github.io/global-recipes/](https://xlabsinc.github.io/global-recipes/) within 1-2 minutes

### Troubleshooting GitHub Pages

**Issue: Site not loading**
- Verify GitHub Pages is enabled in Settings > Pages
- Ensure "main" branch is selected as source
- Wait 2-3 minutes after enabling
- Check that index.html is in the root directory

**Issue: Recipes not showing**
- Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
- Check browser console (F12) for errors
- Verify all files in `recipes/` folder are uploaded
- Ensure file paths use `recipes/` prefix

**Issue: 404 Error**
- Double-check the URL format: `https://username.github.io/global-recipes/`
- Ensure repository name is exactly "global-recipes"
- Wait a few minutes for DNS propagation

For more detailed setup instructions, see [SETUP.md](SETUP.md).

## 📁 Project Structure

```
global-recipes/
├── index.html                    # Main application (single HTML file)
├── recipes/                      # Recipe data folder
│   ├── recipes-south-01.json     # South Indian recipes (10 files)
│   ├── recipes-north-01.json     # North Indian recipes (5 files)
│   ├── recipes-other-01.json     # Other Indian recipes (1 file)
│   ├── recipes-chinese-01.json   # Chinese recipes (2 files)
│   ├── recipes-vietnamese-01.json # Vietnamese recipes (2 files)
│   ├── recipes-korean-01.json    # Korean recipes (2 files)
│   ├── recipes-thai-01.json      # Thai recipes (2 files)
│   ├── recipes-japanese-01.json  # Japanese recipes (2 files)
│   ├── recipes-european-01.json  # European recipes (2 files)
│   ├── recipes-british-01.json   # British recipes (2 files)
│   ├── recipes-american-01.json  # American recipes (2 files)
│   ├── recipes-iranian-01.json   # Iranian recipes (2 files)
│   ├── recipes-middleeastern-01.json # Middle Eastern (2 files)
│   ├── recipes-australian-01.json # Australian recipes (2 files)
│   └── recipes-african-01.json   # African recipes (2 files)
├── README.md                     # This file
├── SETUP.md                      # Deployment guide
├── CONTRIBUTING.md               # Contribution guidelines
├── PROMPT_HISTORY.md             # Development history
├── MASTER_PROMPT.md              # Complete project specification
└── LICENSE                       # MIT License
```

## 📝 Recipe Data Format

Each recipe follows this JSON structure:

```json
{
  "id": 1,
  "name": "Recipe Name",
  "category": "Breakfast|Main Course|Curry|Rice|Snack|Dessert|Side Dish|Soup|Bread",
  "type": "Vegetarian|Non-Vegetarian",
  "difficulty": "Easy|Medium|Hard",
  "prepTime": 15,
  "cookTime": 20,
  "servings": 4,
  "emoji": "🍛",
  "description": "Brief description of the dish",
  "ingredients": [
    "2 cups flour",
    "1 cup water",
    "Salt to taste"
  ],
  "instructions": [
    "Step 1: Do this",
    "Step 2: Do that",
    "Step 3: Serve hot"
  ],
  "tags": ["Quick", "Easy", "Popular"]
}
```

## 🎨 Design & User Experience

### Apple-Inspired Design
- **San Francisco Font System** - Native Apple font stack for crisp text
- **Blue Color Palette** - Clean blue gradients (#0071e3, #00c6ff, #0072ff)
- **Smart Contrast** - Light card headers on blue background for excellent visibility
- **Smooth Animations** - Subtle transitions throughout the interface

### Advanced Features
- **Collapsible Sections** - Keep interface clean with collapsible loaded files
- **Docking System** - Minimize recipes to bottom dock for multi-recipe reference
- **Multi-Recipe View** - Compare multiple recipes side by side
- **Smart Search** - Real-time filtering across names, ingredients, and tags

## 🔧 Customization

### Loading Custom Recipes

**Option 1: Via UI (easiest)**
1. Click "📁 Load Recipes" button
2. Choose "Load from Computer" and select JSON file(s)
3. Or choose "Load from URL" and paste a GitHub Gist or raw file URL

**Option 2: From Remote URL**
Edit the `BASE_URL` constant in `index.html`:

```javascript
// For GitHub repository:
const BASE_URL = 'https://raw.githubusercontent.com/username/repo/main/';

// For GitHub Gist:
const BASE_URL = 'https://gist.githubusercontent.com/username/gist-id/raw/';

// For local files (default):
const BASE_URL = '';
```

### Adding More Recipe Files

1. Create JSON file following the format above
2. Place it in the `recipes/` folder
3. Update the `jsonFiles` array in `index.html`:

```javascript
const jsonFiles = [
    // ... existing files ...
    'recipes/your-custom-file.json'  // Add here
];
```

### Modifying Colors

All CSS is in `index.html`. Key color variables:
- Background: `linear-gradient(135deg, #00c6ff 0%, #0072ff 100%)`
- Active buttons: `#0071e3`
- Card headers (normal): `linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%)`
- Card headers (expanded): `linear-gradient(135deg, #0071e3 0%, #005bb5 100%)`

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Add More Recipes** - Submit authentic recipes from any cuisine
2. **Improve UI/UX** - Suggest design improvements
3. **Fix Bugs** - Report or fix issues
4. **Add Features** - Recipe ratings, nutrition info, meal planning, etc.
5. **Translations** - Add support for multiple languages

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📚 Documentation

- **[SETUP.md](SETUP.md)** - Detailed deployment and configuration guide
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute recipes and code
- **[PROMPT_HISTORY.md](PROMPT_HISTORY.md)** - Complete development history
- **[MASTER_PROMPT.md](MASTER_PROMPT.md)** - Full project specification

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by culinary traditions from around the world
- Thanks to all home cooks and chefs who preserve authentic recipes
- Special thanks to the open-source community
- Design inspired by Apple's clean aesthetic

## 🗺️ Roadmap

- [ ] Recipe images and photos
- [ ] User ratings and reviews
- [ ] Favorites/bookmarking with localStorage
- [ ] Print-friendly recipe cards
- [ ] Meal planning calendar
- [ ] Shopping list generator
- [ ] Nutritional information calculator
- [ ] Cooking timer integration
- [ ] Video tutorials links
- [ ] Multi-language support
- [ ] Recipe scaling (adjust servings)
- [ ] Unit conversion (metric/imperial)

## 📊 Statistics

- **Total Recipes:** 420
- **Total Files:** 40 JSON files
- **Cuisines:** 16 different cuisines
- **Recipe Types:** ~70% Vegetarian, ~30% Non-Vegetarian
- **Difficulty Mix:** ~50% Easy, ~35% Medium, ~15% Hard

---

**Made with ❤️ for food lovers around the world**

*If you enjoy this project, please consider giving it a ⭐ star on GitHub!*
