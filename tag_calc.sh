#!/bin/bash
echo "PART 1"
INPUT=$1

git tag --list
git switch main
git fetch origin --tags

MAJOR=$(echo $INPUT | cut -d '/' -f2 | cut -d '.' -f1)
MINOR=$(echo $INPUT | cut -d '/' -f2 | cut -d '.' -f2)
Version=$(git describe --tags | grep $MAJOR.$MINOR)
echo "PART 2"
if [ "${Version}" = "" ];then
Version="${MAJOR}.${MINOR}.1"
else

BDIKA=$(git tag --list | grep $MAJOR.$MINOR |  tail -n1)

MAJOR=$(echo $BDIKA | cut -d '/' -f2 | cut -d '.' -f1)
MINOR=$(echo $BDIKA | cut -d '/' -f2 | cut -d '.' -f2)
PATCH=$(echo $BDIKA | cut -d '/' -f2 | cut -d '.' -f3)

NEW_PATCH=`expr $PATCH + 1`
Version="${MAJOR}.${MINOR}.${NEW_PATCH}"

fi
echo "PART 1"
echo $Version



