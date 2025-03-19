#!/usr/bin/env python
import os
import sys

def find_string_in_file(file_path, search_string):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                if search_string in line:
                    print(f"Found in {file_path} at line {line_number}: {line.strip()}")
    except UnicodeDecodeError:
        # Skip binary files
        pass
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def search_directory(directory, search_string):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.sh', '.txt', '.md', '.yaml', '.yml', '.json')):
                file_path = os.path.join(root, file)
                find_string_in_file(file_path, search_string)

if __name__ == "__main__":
    # Search for taps_rezos in the current directory
    search_directory(".", "taps_rezos")