#!/bin/bash

mkdir subjects;
cp -a d01/ d02/ guidelines.md subjects/;
cd subjects;
mv guidelines.md guidelines.txt
rm -r d*/ex*/ref;

