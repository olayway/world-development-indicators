#!/bin/bash

given_folder="indicators"
output_file="output.md"

> "$output_file"

# Iterate over each subdirectory in the given folder
find "$given_folder" -mindepth 1 -maxdepth 1 -type d | while read subdir; do
  datapackage_file="$subdir/datapackage.json"

  # Check if datapackage.json exists
  if [ -f "$datapackage_file" ]; then
    # Extract the title value from datapackage.json
    title=$(jq -r '.title' "$datapackage_file")

    # Extract the subdirectory name
    dirname=$(basename "$subdir")

    # Append the formatted string to the output file
    echo "* [$title](https://datahub.io/core/world-development-indicators/$given_folder/$dirname)" >> "$output_file"
  fi
done
