---
title: "Efficient unpacking of required software from CVMFS"
summary: CERN Openlab Summer Student Internship
tags:
- Other
- Student
date: "2018-08-31T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: Photo by rawpixel on Unsplash
  focal_point: Smart

links:
- icon: github
  icon_pack: fab
  name: GitHub
  url: https://github.com/cvmfs/cvmfs/tree/devel/cvmfs/shrinkwrap
- icon: graduation-cap
  icon_pack: fas
  name: Publication
  url: /publication/cvmfs/
url_code: ""
url_pdf: ""
url_slides: "https://indico.cern.ch/event/727274/contributions/3100407/attachments/1700394/2738250/Lightning_talk.pdf"
url_video: "https://cds.cern.ch/record/2634204"

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides: example
---

The CernVM File System (CVMFS) is a distributed global scale network file system that is broadly used for software delivery in the High Energy Physics (HEP) community (especially at CERN). It is mainly optimized for typical software package workloads which consist of many relatively small files. While exact user numbers are unknown due to its proxy hierarchy it is estimated that CERN’s CVMFS installation is used to access software distributions on some 64k nodes in 160 sites of the Worldwide Large Computing Grid (WLCG). CVMFS can therefore be considered the main software distribution system inside the HEP community around CERN. In recent years there has been growing interest in using High Performance Computing (HPC) installations for HEP calculations. However, deploying HEP software to HPC resources like Cori, NERSC(USA) still poses a big challenge to the current CVMFS delivery architecture. Three of the main challenges for bringing HEP software to HPC resources are limited access to internet from the compute nodes inside the HPC center, lack of a local hard disk which could be used for file caching and the lack of system access necessary to use technologies like FUSE.
While there are some ways of avoiding the need for an active internet connection or the needfor a local hard disk, the task of HEP software deployment becomes notoriously difficult once the underlying system does not allow mounting through FUSE. Due to these circumstancesthere has been a growing interest in exporting software stored in CVMFS into stand-alone software images. Another reason for the development of the export utility has been a growing interest in building benchmark containers for system evaluations. In these cases, it is desirable to have a container of minimal size which runs exactly the same workflow on every system without relying on external factors like the internet connection for its execution. The export utility therefore perfectly fits this use case with its ability to export previously examined workflows into standalone images.The presented software utility (cvmfs_shrinkwrap) allows the export of software stacks from CVMFS into standalone images. The software functionality represents a superset of the uncvmfs utility, which is currently used in HEP for exporting images from CVMFS repositories, since it allows the export of repository subsets (instead of an entire repository). The utility currently permits exports to POSIX folders but also to tarballs, SquashFS images or even Docker Images stored in OCI registries through a POSIX export followed by a packaging step which produces the desired image format. Just like uncvmfs the cvmfs_shrinkwrap utility uses file deduplication by hardlinking for the image building to minimize storage needs for the resulting read-only images.