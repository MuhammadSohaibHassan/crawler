# File Finder Tool

A simple and enhanced command-line tool to search for files on your local system based on various criteria such as filename, extension, size, and more. This tool allows users to filter files, view their details (like size and path), and sort the results by different attributes.

## Features
- **Search by Filename**: Search for files based on their name (partial match supported).
- **Exact Filename Match**: Option to match the exact filename, ignoring extensions.
- **Search by File Extension**: Search for files with a specific extension.
- **File Size Filters**: Specify minimum and maximum file sizes (in KB) for your search.
- **Exact Size Match**: Match files by their exact size (in bytes).
- **Sort Results**: Sort the results by filename, size, or path.
- **Case Sensitivity**: Enable or disable case-sensitive filename matching.
- **Display File Details**: Option to display file size and path along with the filename.
  
## Installation
To use the file finder tool, follow these steps:

### Requirements:
- Python 3.x (Tested on version 3.8+)

### Steps to Run:
1. **Download or Clone the Repository:**
    - You can clone the repository using Git:
      ```
      git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
      ```
    - Alternatively, you can manually download the files as `.zip` from the GitHub interface.

2. **Install Required Packages:**
    - You’ll need to install the following Python packages:
      ```bash
      pip install colorama
      ```

3. **Running the Finder:**
    - After installation, you can run the `finder.py` script using the following command:
      ```bash
      python finder.py [OPTIONS]
      ```

    - Replace `[OPTIONS]` with the desired arguments as described below.

## Usage

### Arguments

- **`filename`**: Filename to search for (partial match allowed).
- **`file_extension`**: Optional file extension to search for (partial match allowed).
- **`-ef`, `--exact-filename`**: Match filename exactly (ignores extension).
- **`-ee`, `--exact-extension`**: Match extension exactly (ignores dot).
- **`-td`, `--target-dir`**: Target directory to search in (default: current working directory).
- **`-mins`, `--min-size`**: Minimum file size in KB.
- **`-maxs`, `--max-size`**: Maximum file size in KB.
- **`--size`**: Exact file size in bytes to match.
- **`-s`, `--show-size`**: Show file size in KB.
- **`-p`, `--show-path`**: Show file path.
- **`--sort`**: Sort results by `name`, `size`, or `path`.
- **`-cs`, `--case-sensitive`**: Enable case-sensitive filename matching.

### Example Commands:

- **Search for files with a specific name**:
  ```bash
  python finder.py "example" --target-dir /path/to/search --sort size

  
