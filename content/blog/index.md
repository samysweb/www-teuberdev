---
title: "Blog"
# Homepage
type: landing

sections:
  # A section to display blog posts
  - block: collection
    id: publications
    content:
      title: Pittsburgh
      subtitle: 
      text: Blog about my time in Pittsburgh (in German)
      # Display content from the `content/post/` folder
      filters:
        folders:
          - post
        category: "pittsburgh"
    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: 2
      # Choose your content listing view - here we use the `showcase` view
      view: article-grid
      # For the Showcase view, do you want to flip alternate rows?
      flip_alt_rows: true
  # A section to display blog posts
  - block: collection
    id: publications
    content:
      title: Blog Post Archive
      subtitle: 
      text: "This blog post represents a collection of blog posts I have written in various blogs and on various platforms since the year 2011. I now keep those blog posts here as a sort of *thought archive* and might extend them with further thoughts as I go along. I have put these blog posts here *as is* -- without any (sometimes badly needed) spell checks, censorship or commentary. Current opinions may (significantly) deviate from the opinions expressed here."
      # Display content from the `content/post/` folder
      filters:
        folders:
          - post
        category: "Archive"
    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: 2
      # Choose your content listing view - here we use the `showcase` view
      view: article-grid
      # For the Showcase view, do you want to flip alternate rows?
      flip_alt_rows: true
---
