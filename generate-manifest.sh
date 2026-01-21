#!/bin/bash
# Generates manifest.json for the gallery
cd /var/home/core/gallery
ls -1r walerie-art/*.png 2>/dev/null | sed 's|walerie-art/||' | \
  jq -R -s 'split("\n") | map(select(. != ""))' > manifest.json
echo "Generated manifest.json with $(jq length manifest.json) images"
