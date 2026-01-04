# 🎯 Features Guide - Global Recipe Collection v2.1

## Quick Feature Overview

### 1. 🪟 Floating Windows with Smart Z-Index

**What it does:** Draggable, resizable recipe cards that always stay on top when you interact with them.

**How to use:**
```
1. Click any recipe card to open it as a floating window
2. Drag the header to move it around
3. Card automatically comes to front when dragging
4. Click any card to bring it to front
5. Drag bottom-right corner to resize
```

**Z-Index behavior:**
- New cards open on top
- Dragging brings card to front instantly
- Clicking any card brings it to front
- Proper stacking order maintained

**Perfect for:**
- Comparing multiple recipes side-by-side
- Keeping reference recipes visible while browsing
- Organizing your cooking workflow

---

### 2. 📁 Multiple File Upload

**What it does:** Load multiple JSON recipe files at once instead of one at a time.

**How to use:**
```
1. Click "📁 Load Recipe Files (Multiple)" button
2. In file dialog, select multiple files:
   - Windows: Hold Ctrl + Click files
   - Mac: Hold Cmd + Click files
3. Click "Open"
4. See success message: "✓ Added X recipes from Y file(s)"
```

**Visual feedback:**
- Status message appears in green
- Loaded files section appears below
- Recipe count updates
- Category filters regenerate

---

### 2. 🗂️ File Management UI

**What it shows:**
```
Loaded Files:
┌──────────────────────────────────────┐
│ recipes-1.json [10] ×                │
│ recipes-2.json [10] ×                │
│ my-recipes.json [5] ×                │
└──────────────────────────────────────┘
```

**Components:**
- **Filename** - Name of the loaded JSON file
- **[Count]** - Number of recipes in blue badge
- **×** - Red remove button

**Location:** Below the "Load Recipe Files" button in the Controls section

---

### 3. 🗑️ Remove/Unload Files

**What it does:** Completely removes a file and all its recipes from memory.

**How to use:**
```
1. Find the file in "Loaded Files:" section
2. Click the red × button on the right
3. Confirm removal in dialog box
4. File disappears immediately
```

**What happens:**
- ✓ File removed from memory
- ✓ All recipes from that file removed
- ✓ Recipe count updates
- ✓ Category filters regenerate (if categories change)
- ✓ Search results update
- ✓ Display refreshes

**Can you remove built-in files?** YES! You can remove any file including the default recipes-1.json through recipes-5.json.

---

### 4. 🔍 Real-Time Search

**How it works:**
```
Type: "coc"
See: Coconut Chutney, recipes with coconut...

Type: "chicken"
See: Chicken Chettinad, Hyderabadi Biryani, Chicken Curry...

Type: "easy"
See: All recipes tagged as "Easy"
```

**Searches in:**
- Recipe names
- Ingredients lists
- Descriptions
- Tags
- Categories

**No need to press Enter** - results update instantly as you type!

---

### 5. 📚 Multi-Recipe Viewing

**What it does:** View multiple recipes at the same time with full details.

**How it works:**

**Step 1 - Expand first recipe:**
```
Click: Masala Dosa card
Result: Card expands showing full ingredients & instructions
```

**Step 2 - Expand second recipe:**
```
Click: Idli card
Result: Idli also expands, Masala Dosa stays expanded
```

**Step 3 - Minimize any recipe:**
```
Click: Minimize button (−) on Masala Dosa
Result: Only Masala Dosa collapses, Idli stays expanded
```

**Visual layout:**
```
┌────────────────────────────────────────┐
│ Normal recipe cards (3 columns)        │
│  [Card]  [Card]  [Card]                │
│  [Card]  [Card]  [Card]                │
└────────────────────────────────────────┘

After clicking first card:
┌────────────────────────────────────────┐
│ Expanded Recipe 1 (full width)   [−]   │
│  Ingredients    │  Instructions         │
│  - Item 1       │  1. Step one          │
│  - Item 2       │  2. Step two          │
└────────────────────────────────────────┘
│ Normal recipe cards continue below...  │
│  [Card]  [Card]  [Card]                │
└────────────────────────────────────────┘

After clicking second card:
┌────────────────────────────────────────┐
│ Expanded Recipe 1 (full width)   [−]   │
│  Ingredients    │  Instructions         │
└────────────────────────────────────────┘
│ Normal cards...                        │
│  [Card]  [Card]                        │
└────────────────────────────────────────┘
│ Expanded Recipe 2 (full width)   [−]   │
│  Ingredients    │  Instructions         │
└────────────────────────────────────────┘
```

**Perfect for:**
- Comparing ingredients between recipes
- Planning multiple dishes for a meal
- Learning multiple recipes at once
- Printing multiple recipes

---

### 6. 🏷️ Category Filters

**What they do:** Show only recipes from selected category.

**Available categories** (auto-generated from loaded recipes):
- All (default)
- Breakfast
- Curry
- Dessert
- Main Course
- Rice
- Side Dish
- Snack
- Soup
- Bread

**How to use:**
```
1. Click any category button
2. See only recipes from that category
3. Search still works within selected category
4. Click "All" to see everything again
```

**Dynamic updates:**
- Categories appear/disappear as files are loaded/removed
- If you remove all "Soup" recipes, "Soup" button disappears
- Always sorted alphabetically (except "All" first)

---

## 🎨 Visual Reference

### Status Messages

**Success:**
```
✓ Loaded 50 recipes from 5 files
```
Green text, appears for 5 seconds

**Error:**
```
❌ Error parsing custom-file.json
```
Red text, appears for 5 seconds

**Info:**
```
✓ Removed recipes-3.json
```
Green text, appears for 5 seconds

---

### Recipe Card States

**Normal (Collapsed):**
```
┌─────────────────────┐
│ 🥞 Masala Dosa      │
│ Breakfast           │
├─────────────────────┤
│ ⏱️ 50 min 👥 4      │
│ Description...      │
│ [Veg] [Traditional] │
└─────────────────────┘
```

**Expanded:**
```
┌─────────────────────────────────────────────────┐
│ 🥞 Masala Dosa                             [−]  │
│ Breakfast                                       │
├─────────────────────────────────────────────────┤
│ ⏱️ 50 min 👥 4                                  │
│ Description...                                  │
│ [Veg] [Traditional]                             │
├──────────────────┬──────────────────────────────┤
│ 📝 Ingredients   │ 👨‍🍳 Instructions              │
│                  │                              │
│ ✓ 2 cups rice    │ ① Soak rice and dal...       │
│ ✓ 1/2 cup dal    │ ② Grind to batter...         │
│ ✓ 4 potatoes     │ ③ Ferment overnight...       │
│ ...              │ ...                          │
└──────────────────┴──────────────────────────────┘
```

---

### File Management Section

```
Loaded Files:
┌────────────────────────────────────────────────┐
│  recipes-1.json   [10]  ×                      │
│  recipes-2.json   [10]  ×                      │
│  recipes-3.json   [10]  ×                      │
│  my-custom.json   [25]  ×                      │
└────────────────────────────────────────────────┘
         ↑            ↑    ↑
      filename    count  remove
```

---

## 💡 Pro Tips

### Tip 1: Organize by Region
```
Load files:
- kerala-recipes.json
- tamil-nadu-recipes.json
- karnataka-recipes.json

Remove regions you're not interested in!
```

### Tip 2: Compare Similar Recipes
```
1. Search for "dosa"
2. Expand "Masala Dosa"
3. Expand "Plain Dosa"
4. Compare ingredients side-by-side
```

### Tip 3: Meal Planning
```
1. Filter by "Breakfast"
2. Expand 2-3 recipes
3. See what ingredients overlap
4. Plan shopping list
```

### Tip 4: Quick Access
```
1. Remove categories you don't cook
2. Keep only your favorites loaded
3. Faster browsing!
4. Re-load anytime
```

### Tip 5: Mobile Friendly
```
On mobile:
- Expanded recipes stack vertically
- Touch to expand
- Swipe to scroll
- Still works great!
```

---

## 🆘 Troubleshooting

### Q: Files not loading?
**A:** Check that JSON files are in the same folder as index.html

### Q: × button not working?
**A:** Make sure you click the × (not the filename)

### Q: Duplicate category buttons?
**A:** This is fixed in v2.0! Clear browser cache if you see it.

### Q: Can't select multiple files?
**A:** Make sure you hold Ctrl (Windows) or Cmd (Mac) while clicking

### Q: Recipe won't expand?
**A:** Click on the colored part or description, not the minimize button area

### Q: Lost default recipes?
**A:** Refresh page to reload built-in files

---

## 🎓 Advanced Usage

### Create Recipe Collections

**Example: Quick Weeknight Dinners**
```json
[
  {"id": 101, "name": "Quick Lemon Rice", ...},
  {"id": 102, "name": "15-Min Rasam", ...}
]
```
Save as `quick-dinners.json` and load it!

### Share Custom Recipes

1. Create your recipes in JSON format
2. Share the file with friends/family
3. They load it in their browser
4. Everyone has your recipes!

### Offline Recipe Book

1. Load all your favorite recipe files
2. Bookmark the page
3. Works offline after first load
4. Perfect for kitchen tablet!

---

## 📱 Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `/` or `Ctrl+F` | Focus search box |
| `Esc` | Clear search |
| `Click` | Expand recipe |
| `Click −` | Minimize recipe |

---

## 🎉 You're Ready!

All features are intuitive and easy to use. Just start exploring!

**Remember:**
- Load multiple files at once
- Remove files you don't need
- Expand multiple recipes
- Search as you type
- Enjoy cooking! 🍛

---

**Made with ❤️ for South Indian food lovers**
