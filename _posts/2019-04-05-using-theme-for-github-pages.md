---
layout: post
title: "NiPy Builder Pages Use Themes"
date: 2019-04-05
---

Edit `Gemfile`, adding following line:
```
gem 'minima'
```

Install dependencies:
```bash
$ bundle install
```

Add line to `_config.yaml`:

```yaml
theme: minima
```

## (Optional) Convert gem-based theme to regular

Find where the theme was installed:

```
$ bundle show minima
C:/Ruby25-x64/lib/ruby/gems/2.5.0/gems/minima-2.5.0
```

1. Copy the content of the theme into the pages folder.
2. Rename file `index.html` to `index.md`.
3. Rename file `blog/index.html`  to `blog/index.md`
4. Remove `css` directory.
5. Modify file `index.md`:
   Change layout from `default` to `home`.



## References

* [Jekyll Themes](https://jekyllrb.com/docs/themes/)



