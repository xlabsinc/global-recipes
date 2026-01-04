# Contributing to Global Recipe Collection

First off, thank you for considering contributing to the Global Recipe Collection! 🙏

**Repository:** [https://github.com/xlabsinc/global-recipes](https://github.com/xlabsinc/global-recipes)

**Live Site:** [https://xlabsinc.github.io/global-recipes/](https://xlabsinc.github.io/global-recipes/)

## How Can I Contribute?

### 🍽️ Adding New Recipes

1. Fork the repository
2. Create a new branch (`git checkout -b add-recipe-name`)
3. Add your recipe to the appropriate JSON file in the `recipes/` folder (or create a new one)
4. Follow the recipe format below
5. Test that it loads correctly
6. Submit a pull request

#### Recipe Format

```json
{
  "name": "Recipe Name",
  "category": "Breakfast|Main Course|Curry|Rice|Snack|Dessert|Side Dish|Soup|Bread",
  "type": "Vegetarian|Non-Vegetarian",
  "difficulty": "Easy|Medium|Hard",
  "prepTime": 20,
  "cookTime": 30,
  "servings": 4,
  "emoji": "🍛",
  "description": "Brief description of the dish and its cultural significance",
  "ingredients": [
    "2 cups ingredient with specific quantity",
    "1 tablespoon another ingredient",
    "Salt to taste"
  ],
  "instructions": [
    "Step 1: Detailed first step",
    "Step 2: Clear second step",
    "Step 3: Final step and serving suggestion"
  ],
  "tags": ["Quick", "Traditional", "Popular"]
}
```

**Important:** The `id` field is **optional** and will be auto-generated if not provided. You don't need to worry about assigning unique IDs - the system handles this automatically!

#### Where to Add Your Recipe

- **Indian recipes:** Add to existing files or create `recipes-other-02.json`
- **Asian recipes:** Add to existing cuisine files (Chinese, Vietnamese, Korean, Thai, Japanese)
- **Western recipes:** Add to European, British, or American files
- **Middle Eastern:** Add to Iranian or Middle Eastern files
- **Other cuisines:** Add to Australian, African, or create a new regional file
- **New cuisine:** Create `recipes-CUISINE-01.json` in the `recipes/` folder

### 🐛 Reporting Bugs

- Use the GitHub Issues tab
- Describe the bug clearly
- Include steps to reproduce
- Add screenshots if applicable
- Mention your browser/device
- Check browser console for errors

### 💡 Suggesting Features

- Check if the feature is already requested
- Open a new issue with the "enhancement" label
- Describe the feature and its benefits
- Provide examples or mockups if possible
- Consider technical feasibility

### 🎨 Improving UI/UX

- Fork the repository
- Make your changes to `index.html`
- Test on multiple devices/browsers (mobile, tablet, desktop)
- Ensure accessibility standards
- Submit a pull request with screenshots/recordings

### 📝 Improving Documentation

- Fix typos, grammar, or unclear instructions
- Add more examples
- Improve README structure
- Update outdated information
- Submit a pull request

## Recipe Guidelines

### Authenticity
- Recipes should be authentic to their stated cuisine
- Traditional family recipes are highly valued
- Regional variations are welcome
- Include cultural context when possible

### Quality Standards
- **Instructions:** Clear, detailed, and in logical order
- **Ingredients:** Accurate quantities with standard measurements
- **Timing:** Realistic prep and cook times
- **Servings:** Accurate portion information
- **Description:** Brief but informative (2-3 sentences)
- **Tips:** Include helpful cooking tips in instructions if applicable

### Categories

We organize recipes into these categories:
- **Breakfast** - Morning meals and brunch items
- **Main Course** - Primary dishes for lunch/dinner
- **Curry** - Saucy dishes with various proteins/vegetables
- **Rice** - Rice-based dishes
- **Snack** - Light bites and appetizers
- **Dessert** - Sweet treats and sweets
- **Side Dish** - Accompaniments and condiments
- **Soup** - Liquid-based dishes
- **Bread** - Flatbreads, buns, and baked goods

### Cuisines Currently Included

- Indian (South, North, Other regions)
- Chinese
- Vietnamese
- Korean
- Thai
- Japanese
- European
- British
- American
- Iranian
- Middle Eastern
- Australian
- African

**Want to add a new cuisine?** Open an issue first to discuss!

## File Organization

### Adding to Existing Files

1. Open the appropriate file in `recipes/` folder
2. Add your recipe to the JSON array
3. Validate JSON syntax at [jsonlint.com](https://jsonlint.com)
4. No need to assign an ID - it will be auto-generated!

### Creating New Files

1. Name format: `recipes-CUISINE-##.json` (use two-digit numbers)
2. Place in the `recipes/` folder
3. Update `index.html` to include the new file:
   ```javascript
   const jsonFiles = [
       // ... existing files ...
       'recipes/recipes-CUISINE-01.json'  // Add here
   ];
   ```

## Code Style

### HTML/CSS
- Use 4 spaces for indentation
- Use semantic HTML5 elements
- Keep CSS organized by component
- Follow the modern, clean design aesthetic
- Maintain color consistency (#667eea, #764ba2, #f5f7fa)

### JavaScript
- Use ES6+ syntax (const, let, arrow functions)
- Use descriptive variable names
- Add comments for complex logic
- Follow existing code patterns
- Test on multiple browsers (Chrome, Firefox, Safari, Edge)

### JSON
- Use 2-space indentation for recipe files
- Validate before committing
- Ensure proper UTF-8 encoding
- Keep files under 100KB when possible

## Pull Request Process

1. **Before submitting:**
   - Test your changes locally with a server (`python -m http.server`)
   - Validate all JSON files
   - Check for typos and formatting
   - Ensure no duplicate IDs
   - Test search and filters with your new recipes

2. **PR Description should include:**
   - What recipes/changes you're adding
   - Which cuisine/category
   - Any special notes
   - Screenshots if UI changes

3. **After submitting:**
   - Respond to review feedback
   - Make requested changes
   - Ensure CI/CD passes (if configured)

## Testing Checklist

Before submitting a PR, verify:

- [ ] JSON syntax is valid
- [ ] Recipe ID is unique
- [ ] All required fields are present
- [ ] Measurements are clear and accurate
- [ ] Recipe loads in the UI
- [ ] Search finds your recipe
- [ ] Filters work correctly
- [ ] No console errors
- [ ] Mobile view looks good

## Community Guidelines

### Be Respectful
- Welcome contributors from all backgrounds
- Respect different cooking traditions
- Be patient with newcomers
- Provide constructive feedback

### Share Knowledge
- Help others learn
- Share cooking tips and experiences
- Explain regional variations
- Celebrate culinary diversity

### Quality Over Quantity
- Focus on authentic, well-tested recipes
- Ensure accuracy of information
- Provide helpful context
- Take pride in your contributions

## Questions?

Feel free to:
- Open an issue with your question
- Tag maintainers for help
- Check existing issues and documentation
- Join discussions in pull requests

## Recognition

Contributors will be recognized in:
- GitHub contributors list
- Special thanks in releases
- Community spotlight (coming soon)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to preserving and sharing culinary traditions from around the world! 🌍❤️**

*Together, we're building the world's most comprehensive open-source recipe collection!*
