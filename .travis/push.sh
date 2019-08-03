#!/bin/sh

set -e
set -x

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
  git init
  git remote add origin https://${GITHUB_TOKEN}@github.com/samysweb/www-teuberdev.git > /dev/null 2>&1
  git pull origin page
}

commit_website_files() {
  git add .
  git commit -am "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git push --quiet --set-upstream origin page
}

mkdir /opt/publish && cd /opt/publish
setup_git
cp -R /opt/page/* .
commit_website_files
upload_files