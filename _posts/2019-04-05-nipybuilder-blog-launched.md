---
title: "NiPy Builder Blog Launched"
date: 2019-04-05
---

 [NiPyBuilder site](\https://vancun.github.io/nipybuilder) was launched. The site is hosted by [GitHub Pages](https://pages.github.com/) with [Jekyll](https://jekyllrb.com/). Site includes also [NiPyBuilder Blog](https://vancun.github.io/nipybuilder/blog/). 

 GitHub Pages could be built from following sources:

 * `gh-pages` branch
 * `master` branch
 * `master` branch `/docs` folder

 [NiPyBuilder](https://vancun.github.io/nipybuilder) site uses the `gh-pages` branch as source for the GitHub pages.

 ## Setting Up Jekyll Locally

 ### Step 1: Install Ruby

 (Based on <https://help.github.com/en/articles/setting-up-your-github-pages-site-locally-with-jekyll)

 1. [Install Ruby](https://www.ruby-lang.org/en/downloads/)

 2. Install Bundler:

 ```bash
 $ gem install bundler
 # Installs the Bundler gem
 ```

 Step 2: Prepare Pages Directory

 1. Initialize git repository 

 ```bash
 $ git init nipybuilder-pages
 # git creates folder nipybuilder-pages
 
 $ cd nipybuilder-pages
 
 # Connect local repository to the remote github repository
 $ git remote add origin https://github.com/vancun/nipybuilder
 
 # Create GitHub Pages branch
 $ git checkout -b gh-pages
 
 # Pull remote repository
 $ git pull
 ```

 2. Create `.gitignore` file with following content:

 ```
 _site
 Gemfile.lock
 ```

 3. Commit and push:

 ```bash
 $ git add .
 $ git commit -m "Repository initialized."
 $ git push origin -u gh-pages
 ```

### Step 3: Prepare Jekyll

1. Create a file `Gemfile` with following content:

   ```
   source 'https://rubygems.org'
   gem 'github-pages', group: :jekyll_plugins
   ```

2. Install Jekyll and other dependencies:

   ```bash
   $ bundle install
   # ... 
   ```

### Step 4. Create Site Templates

(based on <http://jmcglone.com/guides/github-pages/)

1. Create file `_config.yaml`

   ```
   name: NiPy Builder
   markdown: kramdown
   permalink: /blog/:year/:month/:day/:title
   ```

2. Create file `index.html`

3. Create directory `_layouts` and place `default.html` and `post.html` files inside.

4. Create directory `css` and place file `main.css` inside.

5. Create directory `blog` and put some posts inside.

### Step 5. Preview Site

1. Start Jekyll server:

   ```bash
   $ bundle exec jekyll serve --baseurl '//nipybuilder'
   ```

2. Open a web browser and navigate to `http://localhost:4000/nipybuilder`

### Step 6. Update GitHub Repository

``` bash
$ git add .
$ git commit -m "Initial site version"
$ git push -u origin
```

### Step 7. Browse the Site

1. Open web browser and navigate to [`https://vancun.github.io/nipybuilder/`](https://vancun.github.io/nipybuilder/)



## Hints / Lessons Learned

1. Links should use `relative_url` filter. E.g.:

   ```html
   <link rel="stylesheet" type="text/css" href="{{ '/css/main.css'  | relative_url }}"
   ```

2. Jekyll server should be started with `--baseurl` option:

   ```bash
   $ bundle exec jekyll serve --baseurl '//nipybuilder'
   ```

## Resources

* [GitHub Pages](https://pages.github.com/)
* [Configuring a Publishing Source for GitHub Pages](https://help.github.com/en/articles/configuring-a-publishing-source-for-github-pages)
* [Jekyll](https://jekyllrb.com/)
* [Creating and Hosting a Personal Site on GitHub](http://jmcglone.com/guides/github-pages/)

