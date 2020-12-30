---
title: "Efficient unpacking of required software from CERNVM-FS"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin

date: "2019-02-01T00:00:00Z"
doi: "10.5281/zenodo.2574462"

# Schedule page publish date (NOT publication's date).
publishDate: "2019-02-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["4"]

# Publication name and optional abbreviated publication name.
publication: CERN Openlab Report
# publication_short: In *ICW*

abstract: |2-
    In recent times a tool for efficient unpacking of software work-flows from CernVM File System(CVMFS) into standalone images has become necessary.There are two types of use cases for such images: On the one hand they can be used to deliverHEP software to compute nodes which do not support the traditional CVMFS delivery architecture(in particular HPC compute nodes). On the other hand the images can be used for benchmarksin which the network connectivity should not influence the benchmark results.We present a new software utility which allows CVMFS-sourced image creation and synchroniza-tion.  The resulting standalone images can run HEP applications independently from an internetconnection. We further provide a methodology for automatically extracting the resource require-ments from a given software work-flow through file access tracing.In first experimental evaluations the new tool outperformed mechanisms traditionally used for thistask like rsync and provides finer grained unpack functionalities than uncvmfs.
# Summary. An optional shortened abstract.
summary: Report on my project as part of the CERN Openlab Summer Student Programme
tags: []

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://zenodo.org/record/2574462#.X-yyha4xmV5'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  #caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
  #focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
- cvmfs

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
#slides: example
---
