#!/bin/bash
INPUT=$1

git switch main
git fetch origin --tags
git tag --list


MAJOR=$(echo $INPUT | cut -d '/' -f2 | cut -d '.' -f1)
MINOR=$(echo $INPUT | cut -d '/' -f2 | cut -d '.' -f2)
Version=$(git describe --tags | grep $MAJOR.$MINOR)
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

echo $Version



