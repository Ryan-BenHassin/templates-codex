#TODO
#!/bin/bash

# Root directory
ROOT_DIR="."

# Iterate over each file in the directory and subdirectories
find "$ROOT_DIR" -type f | while read -r file; do
    # Prepend #TODO to the first line of each file
    sed -i '' '1s/^/#TODO\n/' "$file"
done

echo "Prepending done for all files."
