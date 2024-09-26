---
title: "Research"
# Homepage
type: landing

sections:
  # A section to display blog posts
  - block: collection
    id: publications
    content:
      title: Publications
      subtitle: 
      text: 
      # Display content from the `content/post/` folder
      filters:
        folders:
          - publication
    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: 1
      # Choose your content listing view - here we use the `showcase` view
      view: citation
      # For the Showcase view, do you want to flip alternate rows?
      flip_alt_rows: true
  # A section to display blog posts
  - block: collection
    id: projects
    content:
      title: Study Projects
      subtitle: 
      text: Projects from Bachelor's and Master's (2015-2022).
      # Display content from the `content/post/` folder
      filters:
        folders:
          - project
    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: 2
      # Choose your content listing view - here we use the `showcase` view
      view: article-grid
      # For the Showcase view, do you want to flip alternate rows?
      flip_alt_rows: true
---
