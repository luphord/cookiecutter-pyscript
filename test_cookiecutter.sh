#!/bin/sh

echo 'executing cookiecutter in temp dir...'
tmp_dir=$(mktemp -d -t XXXXXXXXXX)
cookiecutter -o $tmp_dir --no-input . project_name='My Awesome Test Project'
project_dir=$tmp_dir/$(ls $tmp_dir)

echo
echo 'starting a repo in newly created project...'
cd $project_dir
git init
git add .
git commit -m "initial commit"

echo
echo 'setting up a dev environment...'
make venv
. .venv/bin/activate

echo
echo 'reformatting code...'
make format

echo
echo 'runing linter and tests...'
make lint test

echo
echo 'preparing a release...'
bumpversion minor
make dist

echo
echo 'trying a test run of cli...'
make cli

echo 
echo 'printing README...'
cat $project_dir/README.md

echo 
echo "project dir is $project_dir"