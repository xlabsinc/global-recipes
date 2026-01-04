# Feature Specification - Version 13.0

This document outlines the comprehensive feature additions requested for the Global Recipe Collection application.

## Summary of Changes

### 1. Regional Tags (✅ COMPLETED)
- Added regional tags to all 420 recipes across 40 JSON files
- Tags include: 'South Indian', 'North Indian', 'Chinese', 'Vietnamese', 'Korean', 'Thai', 'Japanese', 'European', 'British', 'American', 'Iranian', 'Middle Eastern', 'African', 'Australian'
- Broader tags also added: 'Asian', 'Western', 'East Asian', 'Southeast Asian', 'Oceania', 'Persian', 'Arabic'

### 2. Tag Filter System (✅ COMPLETED)

**Replace Type Filter with Tag-Based Filter:**

#### UI Components:
- Remove the Type dropdown (`<select id="typeFilter">`)
- Add tag input field with autocomplete
- Display selected tags as removable chips/badges
- Show tag suggestions as user types

#### Functionality:
- Extract all unique tags from loaded recipes
- Provide autocomplete suggestions based on user input
- Allow multiple tag selection
- Filter recipes that match ANY selected tag (OR logic) or ALL selected tags (AND logic - decide which)
- Each tag chip should have an 'x' button to remove

#### HTML Structure:
```html
<div class="tag-filter-container">
    <span class="filter-label">Tags:</span>
    <div class="tag-input-wrapper">
        <div class="selected-tags" id="selectedTags">
            <!-- Selected tag chips appear here -->
        </div>
        <input type="text" id="tagInput" placeholder="Type to filter by tags..." autocomplete="off">
        <div class="tag-suggestions" id="tagSuggestions" style="display: none;">
            <!-- Suggestions appear here -->
        </div>
    </div>
</div>
```

#### CSS Additions:
```css
.tag-filter-container {
    margin-bottom: 15px;
}

.tag-input-wrapper {
    position: relative;
    background: white;
    border: 2px solid #e1e4e8;
    border-radius: 10px;
    padding: 8px;
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    align-items: center;
}

.selected-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
}

.tag-chip {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 4px 10px;
    border-radius: 15px;
    font-size: 0.85em;
    display: flex;
    align-items: center;
    gap: 6px;
}

.tag-chip-remove {
    cursor: pointer;
    font-weight: bold;
    opacity: 0.8;
}

.tag-chip-remove:hover {
    opacity: 1;
}

#tagInput {
    flex: 1;
    min-width: 150px;
    border: none;
    outline: none;
    font-size: 0.9em;
}

.tag-suggestions {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: white;
    border: 2px solid #667eea;
    border-top: none;
    border-radius: 0 0 10px 10px;
    max-height: 200px;
    overflow-y: auto;
    z-index: 1000;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.tag-suggestion-item {
    padding: 10px 15px;
    cursor: pointer;
    transition: background 0.2s;
}

.tag-suggestion-item:hover {
    background: #f8f9ff;
}

.tag-suggestion-item.highlight {
    background: #e8ecff;
}
```

#### JavaScript Functions:
```javascript
let selectedTags = [];
let allTags = new Set();

function extractAllTags() {
    allTags.clear();
    recipes.forEach(recipe => {
        if (recipe.tags) {
            recipe.tags.forEach(tag => allTags.add(tag));
        }
    });
}

function showTagSuggestions(input) {
    const value = input.toLowerCase();
    if (!value) {
        hideTagSuggestions();
        return;
    }

    const matches = Array.from(allTags)
        .filter(tag => tag.toLowerCase().includes(value) && !selectedTags.includes(tag))
        .slice(0, 10);

    if (matches.length === 0) {
        hideTagSuggestions();
        return;
    }

    const suggestionsEl = document.getElementById('tagSuggestions');
    suggestionsEl.innerHTML = matches.map(tag =>
        `<div class="tag-suggestion-item" onclick="addTag('${tag}')">${tag}</div>`
    ).join('');
    suggestionsEl.style.display = 'block';
}

function hideTagSuggestions() {
    document.getElementById('tagSuggestions').style.display = 'none';
}

function addTag(tag) {
    if (!selectedTags.includes(tag)) {
        selectedTags.push(tag);
        renderSelectedTags();
        filterRecipes();
    }
    document.getElementById('tagInput').value = '';
    hideTagSuggestions();
}

function removeTag(tag) {
    selectedTags = selectedTags.filter(t => t !== tag);
    renderSelectedTags();
    filterRecipes();
}

function renderSelectedTags() {
    const container = document.getElementById('selectedTags');
    container.innerHTML = selectedTags.map(tag => `
        <div class="tag-chip">
            <span>${tag}</span>
            <span class="tag-chip-remove" onclick="removeTag('${tag}')">×</span>
        </div>
    `).join('');
}

// Update filterRecipes() to include tag filtering
function filterRecipes() {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();

    filteredRecipes = recipes.filter(recipe => {
        const matchesCategory = currentFilter === 'All' || recipe.category === currentFilter;

        // Tag filtering
        const matchesTags = selectedTags.length === 0 ||
            selectedTags.some(tag => recipe.tags && recipe.tags.includes(tag));

        if (!searchTerm) return matchesCategory && matchesTags;

        const matchesSearch =
            recipe.name.toLowerCase().includes(searchTerm) ||
            recipe.description.toLowerCase().includes(searchTerm) ||
            recipe.ingredients.some(ing => ing.toLowerCase().includes(searchTerm)) ||
            recipe.tags.some(tag => tag.toLowerCase().includes(searchTerm)) ||
            recipe.category.toLowerCase().includes(searchTerm);

        return matchesCategory && matchesTags && matchesSearch;
    });

    displayRecipes(filteredRecipes.slice(0, itemsPerPage));
    updateStats();
}
```

### 3. Theme/Skin Selection (TODO)

**Add Color Scheme Selector in Top Left:**

#### Themes to Support:
1. **Light Mode (Default)** - Current colors
2. **Dark Mode** - Dark background with light text
3. **Blue Theme** - Original blue gradient theme
4. **Green Theme** - Nature-inspired green palette
5. **Orange Theme** - Warm orange palette

#### UI Components:
```html
<div class="theme-selector">
    <button class="theme-btn" onclick="toggleThemeMenu()">🎨 Theme</button>
    <div class="theme-menu" id="themeMenu" style="display: none;">
        <div class="theme-option" onclick="setTheme('light')">☀️ Light</div>
        <div class="theme-option" onclick="setTheme('dark')">🌙 Dark</div>
        <div class="theme-option" onclick="setTheme('blue')">💙 Blue</div>
        <div class="theme-option" onclick="setTheme('green')">💚 Green</div>
        <div class="theme-option" onclick="setTheme('orange')">🧡 Orange</div>
    </div>
</div>
```

#### Theme Definitions:
```javascript
const themes = {
    light: {
        bg: 'linear-gradient(135deg, #f5f7fa 0%, #e4e9f2 100%)',
        accent: '#667eea',
        accentGradient: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        cardBg: '#ffffff',
        text: '#2c3e50',
        textLight: '#495057'
    },
    dark: {
        bg: 'linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)',
        accent: '#667eea',
        accentGradient: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        cardBg: '#0f3460',
        text: '#e9ecef',
        textLight: '#cbd5e0'
    },
    blue: {
        bg: 'linear-gradient(135deg, #00c6ff 0%, #0072ff 100%)',
        accent: '#0071e3',
        accentGradient: 'linear-gradient(135deg, #0071e3 0%, #005bb5 100%)',
        cardBg: '#ffffff',
        text: '#2c3e50',
        textLight: '#495057'
    },
    green: {
        bg: 'linear-gradient(135deg, #d4fc79 0%, #96e6a1 100%)',
        accent: '#2d6a4f',
        accentGradient: 'linear-gradient(135deg, #52b788 0%, #2d6a4f 100%)',
        cardBg: '#ffffff',
        text: '#1b4332',
        textLight: #2d6a4f'
    },
    orange: {
        bg: 'linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)',
        accent: '#ff6b35',
        accentGradient: 'linear-gradient(135deg, #ff6b35 0%, #f7931e 100%)',
        cardBg: '#ffffff',
        text: '#6a0136',
        textLight: '#9a031e'
    }
};

function setTheme(themeName) {
    const theme = themes[themeName];
    document.body.style.background = theme.bg;
    // Apply theme to all elements using CSS custom properties
    document.documentElement.style.setProperty('--accent-color', theme.accent);
    document.documentElement.style.setProperty('--accent-gradient', theme.accentGradient);
    document.documentElement.style.setProperty('--card-bg', theme.cardBg);
    document.documentElement.style.setProperty('--text-color', theme.text);
    document.documentElement.style.setProperty('--text-light', theme.textLight);

    localStorage.setItem('selectedTheme', themeName);
    document.getElementById('themeMenu').style.display = 'none';
}

// Load saved theme on startup
window.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('selectedTheme') || 'light';
    setTheme(savedTheme);
});
```

### 4. Grid Layout Changes (✅ COMPLETED)

**Change Grid to 5 Items Per Row:**

```css
.recipe-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 20px;
    margin-bottom: 30px;
}

@media (max-width: 1400px) {
    .recipe-grid {
        grid-template-columns: repeat(4, 1fr);
    }
}

@media (max-width: 1100px) {
    .recipe-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}

@media (max-width: 968px) {
    .recipe-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 768px) {
    .recipe-grid {
        grid-template-columns: 1fr;
    }
}
```

### 5. Items Per Page Selector (✅ COMPLETED)

**Add Dropdown for Display Count:**

```html
<div class="display-controls">
    <span class="filter-label">Show:</span>
    <select id="itemsPerPageSelect" class="filter-select" onchange="changeItemsPerPage()">
        <option value="5">5 items</option>
        <option value="10" selected>10 items</option>
        <option value="20">20 items</option>
        <option value="30">30 items</option>
        <option value="all">All items</option>
    </select>
</div>
```

```javascript
let itemsPerPage = 10; // Changed from MAX_INITIAL_DISPLAY = 30

function changeItemsPerPage() {
    const select = document.getElementById('itemsPerPageSelect');
    const value = select.value;
    itemsPerPage = value === 'all' ? filteredRecipes.length : parseInt(value);
    displayRecipes(filteredRecipes.slice(0, itemsPerPage));
    updateStats();
}
```

### 6. Close Button on Cards (✅ COMPLETED)

**Add Close Button to Main Page Cards:**

```html
<!-- In createRecipeCard() function -->
<div class="recipe-header">
    <div class="recipe-header-left">
        <div class="recipe-name">${recipe.emoji} ${recipe.name}</div>
        <div class="recipe-category">${recipe.category}</div>
    </div>
    <div class="card-actions-mini">
        <button class="close-card-mini-btn" onclick="event.stopPropagation(); dismissCard('${recipe.id}')" title="Dismiss">×</button>
    </div>
</div>
```

```javascript
let dismissedCards = new Set();

function dismissCard(id) {
    dismissedCards.add(id);
    const card = document.getElementById(`recipe-${id}`);
    if (card) {
        card.style.display = 'none';
    }
}

// Update filterRecipes to exclude dismissed cards
function filterRecipes() {
    // ... existing filter logic ...
    filteredRecipes = filteredRecipes.filter(recipe => !dismissedCards.has(recipe.id));
    // ...
}
```

### 7. Clickable Card Names (✅ COMPLETED)

**Make Card Name Clickable:**

```javascript
// In createRecipeCard() function
card.querySelector('.recipe-name').addEventListener('click', (e) => {
    e.stopPropagation();
    expandRecipe(recipe.id);
});

// Also keep the click on recipe-body
card.querySelector('.recipe-body').addEventListener('click', () => {
    if (!card.classList.contains('expanded')) {
        expandRecipe(recipe.id);
    }
});
```

```css
.recipe-name {
    cursor: pointer;
    transition: color 0.2s;
}

.recipe-name:hover {
    color: #667eea;
}
```

### 8. Resizable Floating Cards (TODO)

**Make Expanded Cards Floating and Resizable:**

This is the most complex feature. When a recipe is expanded:
- It should become a floating modal/window
- It should be draggable
- It should be resizable
- Multiple cards can be expanded at once
- Cards should stack/overlap properly

```css
.recipe-card.floating {
    position: fixed;
    z-index: 1000;
    max-width: 800px;
    min-width: 400px;
    width: 60vw;
    height: 80vh;
    top: 10vh;
    left: 50%;
    transform: translateX(-50%);
    overflow: hidden;
    display: flex;
    flex-direction: column;
    resize: both;
    box-shadow: 0 10px 40px rgba(0,0,0,0.3);
}

.recipe-card.floating .recipe-header {
    cursor: move;
}

.recipe-card.floating .expanded-content {
    flex: 1;
    overflow-y: auto;
    display: block !important;
}

.resize-handle {
    position: absolute;
    bottom: 0;
    right: 0;
    width: 20px;
    height: 20px;
    cursor: nwse-resize;
    background: linear-gradient(135deg, transparent 50%, #667eea 50%);
}
```

```javascript
let floatingCards = [];
let zIndexCounter = 1000;

function expandRecipe(id) {
    const recipe = recipes.find(r => r.id === id);
    if (!recipe) return;

    // Create floating card
    const floatingCard = createFloatingCard(recipe);
    document.body.appendChild(floatingCard);
    floatingCards.push({ id, element: floatingCard });

    // Make draggable
    makeDraggable(floatingCard, floatingCard.querySelector('.recipe-header'));

    // Make resizable (if browser supports)
    if ('ResizeObserver' in window) {
        // Resizable via CSS resize property
    }
}

function createFloatingCard(recipe) {
    const card = document.createElement('div');
    card.className = 'recipe-card floating';
    card.id = `floating-recipe-${recipe.id}`;
    card.style.zIndex = ++zIndexCounter;

    // ... similar HTML structure as regular card but optimized for floating ...

    return card;
}

function makeDraggable(element, handle) {
    let pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;

    handle.onmousedown = dragMouseDown;

    function dragMouseDown(e) {
        e.preventDefault();
        element.style.zIndex = ++zIndexCounter;
        pos3 = e.clientX;
        pos4 = e.clientY;
        document.onmouseup = closeDragElement;
        document.onmousemove = elementDrag;
    }

    function elementDrag(e) {
        e.preventDefault();
        pos1 = pos3 - e.clientX;
        pos2 = pos4 - e.clientY;
        pos3 = e.clientX;
        pos4 = e.clientY;
        element.style.top = (element.offsetTop - pos2) + "px";
        element.style.left = (element.offsetLeft - pos1) + "px";
        element.style.transform = 'none';
    }

    function closeDragElement() {
        document.onmouseup = null;
        document.onmousemove = null;
    }
}

function closeFloatingCard(id) {
    const index = floatingCards.findIndex(c => c.id === id);
    if (index !== -1) {
        floatingCards[index].element.remove();
        floatingCards.splice(index, 1);
    }
}
```

### 9. File Checkboxes (✅ COMPLETED)

**Add Checkboxes to Loaded Files:**

```javascript
// Update updateFileList() function
function updateFileList() {
    const fileListEl = document.getElementById('fileList');
    const sectionEl = document.getElementById('loadedFilesSection');

    if (loadedFiles.size === 0) {
        sectionEl.style.display = 'none';
        return;
    }

    sectionEl.style.display = 'block';
    fileListEl.innerHTML = '';

    loadedFiles.forEach((fileData, filename) => {
        const fileTag = document.createElement('div');
        fileTag.className = 'file-tag';

        // Add checkbox
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = fileData.visible !== false; // default true
        checkbox.className = 'file-checkbox';
        checkbox.onchange = (e) => toggleFileVisibility(filename, e.target.checked);

        const nameSpan = document.createElement('span');
        nameSpan.textContent = filename;

        const countSpan = document.createElement('span');
        countSpan.className = 'recipe-count';
        countSpan.textContent = fileData.recipes.length;

        const removeBtn = document.createElement('button');
        removeBtn.className = 'remove-btn';
        removeBtn.textContent = '×';
        removeBtn.title = `Remove ${filename}`;
        removeBtn.onclick = (e) => {
            e.stopPropagation();
            if (confirm(`Remove ${filename} and its ${fileData.recipes.length} recipes?`)) {
                removeFile(filename);
            }
        };

        fileTag.appendChild(checkbox);
        fileTag.appendChild(nameSpan);
        fileTag.appendChild(countSpan);
        fileTag.appendChild(removeBtn);
        fileListEl.appendChild(fileTag);
    });
}

function toggleFileVisibility(filename, visible) {
    const fileData = loadedFiles.get(filename);
    if (fileData) {
        fileData.visible = visible;
        filterRecipes();
    }
}

// Update filterRecipes to respect file visibility
function filterRecipes() {
    // Get only recipes from visible files
    let visibleRecipes = [];
    loadedFiles.forEach((fileData, filename) => {
        if (fileData.visible !== false) {
            visibleRecipes = visibleRecipes.concat(fileData.recipes);
        }
    });

    recipes = visibleRecipes;

    // ... rest of filtering logic ...
}
```

```css
.file-checkbox {
    width: 18px;
    height: 18px;
    cursor: pointer;
    accent-color: #667eea;
}

.file-tag {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #e8f4f8;
    border: 1px solid rgba(0, 114, 255, 0.2);
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 0.85em;
    color: #005bb5;
}
```

## Implementation Priority

1. ✅ Regional tags - COMPLETED
2. ✅ Tag filter system - COMPLETED
3. ✅ Items per page selector - COMPLETED
4. ✅ Change default to 10 - COMPLETED
5. ✅ Close button on cards - COMPLETED
6. ✅ Clickable card names - COMPLETED
7. ✅ File checkboxes - COMPLETED
8. ✅ Grid layout to 5 per row - COMPLETED
9. ⏳ Theme selection - DEFERRED (LOW PRIORITY)
10. ⏳ Floating resizable cards - DEFERRED (COMPLEX)

## Estimated Complexity

- **Simple (< 50 lines):** Grid layout, close buttons, clickable names, items per page
- **Medium (50-150 lines):** Tag filter, file checkboxes, theme selection
- **Complex (150+ lines):** Floating resizable cards

## Notes

- Store theme preference in localStorage
- Store dismissed cards in localStorage (optional)
- File visibility state should be tracked in loadedFiles Map
- Floating cards need careful z-index management
- Consider mobile responsiveness for all new features
