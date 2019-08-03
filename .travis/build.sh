#!/bin/sh

set -e
set -x

mkdir /opt/page
git clone --recurse-submodules https://github.com/samysweb/www-teuberdev.git /opt/app
echo Build started on `date`
cd /opt/app
hugo --theme introduction
cp -R public/* /opt/page