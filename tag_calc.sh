#!/bin/bash
Version=$(git describe --tags | cut -d '-' -f1 | awk -F. -v OFS=. '{$NF += 1 ; print }')
if [ "${Version}" = "" ];then
    Version="1.0.1"
else
    Version=$(git describe --tags | cut -d '-' -f1 | awk -F. -v OFS=. '{$NF += 1 ; print }')
fi
echo $Version