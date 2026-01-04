# Quick Setup Guide for GitHub Pages

Follow these simple steps to host your Global Recipe Collection on GitHub Pages:

## 🌟 Official Deployment

**Live Site:** [https://xlabsinc.github.io/global-recipes/](https://xlabsinc.github.io/global-recipes/)

**Repository:** [https://github.com/xlabsinc/global-recipes](https://github.com/xlabsinc/global-recipes)

This is the official deployment of the Global Recipe Collection. If you want to contribute or deploy your own copy, follow the instructions below.

---

## 📋 For Contributors: Fork and Deploy

### Step 1: Fork the Repository

1. Go to [https://github.com/xlabsinc/global-recipes](https://github.com/xlabsinc/global-recipes)
2. Click the "Fork" button in the top right
3. This creates a copy in your GitHub account at `https://github.com/YOUR-USERNAME/global-recipes`

### Step 2: Enable GitHub Pages

1. Go to your forked repository settings
2. Click "Settings" (top right)
3. Scroll down to "Pages" in the left sidebar
4. Under "Source", select "main" branch
5. Keep "/" (root) as the folder
6. Click "Save"
7. Wait 1-2 minutes for deployment

### Step 3: Access Your Site

Your site will be live at:
```
https://YOUR-USERNAME.github.io/global-recipes/
```

---

## 🔧 For Organization Members: Direct Deployment

If you have write access to xlabsinc/global-recipes:

### Step 1: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/xlabsinc/global-recipes.git

# Navigate to the directory
cd global-recipes
```

### Step 2: Make Changes

Edit files as needed and test locally:

```bash
# Test with Python
python3 -m http.server 8000

# Or with Node.js
npx serve
```

### Step 3: Commit and Push

```bash
# Add your changes
git add .

# Commit with a descriptive message
git commit -m "Your change description"

# Push to main branch
git push origin main
```

### Step 4: Automatic Deployment

- GitHub Pages automatically rebuilds from the main branch
- Changes appear at [https://xlabsinc.github.io/global-recipes/](https://xlabsinc.github.io/global-recipes/)
- Deployment takes 1-2 minutes

---

## 🆕 Creating a New Deployment from Scratch

If you want to create a completely new repository (not forked):

### Step 1: Create Repository

1. Go to [GitHub](https://github.com) and log in
2. Click "+" icon > "New repository"
3. Name it (e.g., `my-recipes`)
4. Set to "Public"
5. Click "Create repository"

### Step 2: Upload Files

**Option A: GitHub Web Interface**

1. Click "uploading an existing file"
2. Upload `index.html`
3. Create `recipes/` folder and upload all 40 JSON files
4. Upload documentation files (README.md, etc.)
5. Commit changes

**Option B: Git Command Line**

```bash
# Navigate to project folder
cd /path/to/global-recipes

# Initialize git (if not already)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Global Recipe Collection"

# Add your remote repository
git remote add origin https://github.com/YOUR-USERNAME/my-recipes.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages

Same as Step 2 in "For Contributors" section above.

---## Configuration Options

### Option 1: Local Files (Default - Recommended)

The default setup loads recipes from the `recipes/` folder. This is the simplest and most reliable option.

**No changes needed** - Just deploy and it works!

### Option 2: Remote Loading (Advanced)

If you want to host recipes separately (e.g., in a Gist or different repo):

1. Open `index.html`
2. Find the `BASE_URL` constant (around line 967)
3. Update it to your remote URL:

```javascript
// For GitHub raw files:
const BASE_URL = 'https://raw.githubusercontent.com/username/repo/main/recipes/';

// For GitHub Gist:
const BASE_URL = 'https://gist.githubusercontent.com/username/gist-id/raw/';

// For local files (default):
const BASE_URL = '';
```

**Note:** When using remote URLs, ensure:
- The URL ends with a `/`
- The path includes the `recipes/` folder if needed
- CORS is enabled on the remote server

## Customization

### Change Repository Name

If you want a different URL, you can rename the repository:
- Go to Settings > General > Repository name
- Your new URL will be: `https://YOUR-USERNAME.github.io/NEW-NAME/`

### Custom Domain

You can add a custom domain:
1. Go to Settings > Pages > Custom domain
2. Enter your domain (e.g., `recipes.yourdomain.com`)
3. Follow GitHub's instructions for DNS configuration

### Update Branding

Edit `index.html` to customize:
- Title (line 6): Change "Global Recipe Collection"
- Header (line 707): Change the main title
- Subtitle (line 708): Change the description
- Colors: Update CSS gradients and colors (lines 17-600)

## Testing Locally

Before pushing, test locally:

```bash
# Using Python 3
python3 -m http.server 8000

# Using Python 2
python -m SimpleHTTPServer 8000

# Using Node.js
npx serve

# Or simply open index.html in your browser (some features may not work)
```

Then visit: `http://localhost:8000`

**Important:** Use a local server for testing, as some browsers restrict loading local JSON files.

## Troubleshooting

### Recipes not loading

**Problem:** Blank page or no recipes showing

**Solutions:**
1. Check browser console (F12) for errors
2. Verify all JSON files are in the `recipes/` folder
3. Ensure `index.html` has correct file paths (should be `recipes/recipes-*.json`)
4. Wait a few minutes after deployment
5. Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)

### 404 Error

**Problem:** Page not found

**Solutions:**
1. Verify GitHub Pages is enabled in Settings > Pages
2. Ensure the source is set to "main" branch
3. Wait 1-2 minutes for initial deployment
4. Check that `index.html` is in the root directory

### Styling issues

**Problem:** Colors or layout look wrong

**Solutions:**
1. Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
2. Try a different browser
3. Check browser console for CSS errors
4. Verify the entire `index.html` file uploaded correctly

### JSON Parsing Errors

**Problem:** "Invalid JSON" errors in console

**Solutions:**
1. Validate JSON files at [jsonlint.com](https://jsonlint.com)
2. Check for missing commas, quotes, or brackets
3. Ensure UTF-8 encoding (no special characters issues)

## Updating Your Site

Whenever you want to update recipes or the site:

```bash
# Make your changes to the files

# Add and commit
git add .
git commit -m "Add new recipes" # or describe your changes

# Push to GitHub
git push
```

GitHub Pages will automatically redeploy within 1-2 minutes.

### Adding New Recipes

1. Create/edit JSON files in the `recipes/` folder
2. Follow the recipe format (see README.md)
3. Update `index.html` if adding new files (add to `jsonFiles` array)
4. Commit and push changes

## Advanced Configuration

### BASE_URL Examples

**Local Files (Default):**
```javascript
const BASE_URL = '';
```
Recipes load from: `recipes/recipes-south-01.json`

**GitHub Repository:**
```javascript
const BASE_URL = 'https://raw.githubusercontent.com/user/repo/main/';
```
Recipes load from: `https://raw.githubusercontent.com/user/repo/main/recipes/recipes-south-01.json`

**GitHub Gist:**
```javascript
const BASE_URL = 'https://gist.githubusercontent.com/user/gist-id/raw/';
```
Recipes load from: `https://gist.githubusercontent.com/user/gist-id/raw/recipes/recipes-south-01.json`

### Performance Tips

1. **Optimize JSON files:** Remove unnecessary whitespace
2. **Use a CDN:** Consider using jsDelivr for faster loading
3. **Enable caching:** GitHub Pages has built-in caching
4. **Minimize images:** If adding recipe images, compress them first

## Need Help?

- Check the [README.md](README.md) for detailed documentation
- See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines
- Review [PROMPT_HISTORY.md](PROMPT_HISTORY.md) for development history
- Check [MASTER_PROMPT.md](MASTER_PROMPT.md) for full specifications
- Open an issue on GitHub if you encounter problems

## Deployment Checklist

Before going live, verify:

- [ ] All 40 JSON files are in the `recipes/` folder
- [ ] `index.html` is in the root directory
- [ ] File paths in `index.html` use `recipes/` prefix
- [ ] README.md is updated with your information
- [ ] Test locally with a server (not just opening file)
- [ ] All recipes load correctly in local testing
- [ ] Search and filters work properly
- [ ] Mobile view looks good (responsive design)
- [ ] No console errors in browser dev tools

---

**Congratulations! Your Global Recipe Collection is now live! 🎉🌍**

Enjoy sharing 420 recipes from around the world!
