import os
import argparse
from pathlib import Path
import fnmatch
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def find_files(filename, extension, exact_filename, exact_extension, target_dir, min_size, max_size, size, show_size, show_path, sort_by, case_sensitive):
    matched_files = []

    try:
        target_path = Path(target_dir).resolve()
        if not target_path.is_dir():
            raise NotADirectoryError(f"Target directory '{target_dir}' does not exist or is not accessible.")

        for file_path in target_path.rglob('*'):
            try:
                if not file_path.is_file():
                    continue

                # Get filename without extension
                file_name_without_ext = file_path.stem  # Get filename without extension

                # Adjust filename matching for case-sensitivity
                compare_filename = file_name_without_ext if case_sensitive else file_name_without_ext.lower()
                compare_search_filename = filename if case_sensitive else filename.lower()

                # Match filename (ignores extension)
                if exact_filename:
                    if compare_filename != compare_search_filename:
                        continue
                else:
                    if filename and compare_search_filename not in compare_filename:
                        continue

                # Match extension (ignores dot)
                file_ext = file_path.suffix.lstrip('.').lower()  # Remove dot and convert to lowercase
                extension = extension.lstrip('.').lower()  # Remove dot and convert to lowercase
                
                if exact_extension:
                    if file_ext != extension:
                        continue
                else:
                    if extension and not fnmatch.fnmatch(file_ext, f"*{extension}*"):
                        continue

                # File size filters
                file_size_bytes = file_path.stat().st_size  # Size in bytes
                if size and file_size_bytes != size:
                    continue
                if (min_size and file_size_bytes < min_size * 1024) or (max_size and file_size_bytes > max_size * 1024):
                    continue

                # Collect file details
                file_info = {
                    "name": file_path.name,
                    "size_bytes": file_size_bytes if show_size else None,
                    "path": str(file_path) if show_path else None
                }
                matched_files.append(file_info)
            except (PermissionError, FileNotFoundError):
                # Skip files we cannot access
                continue

    except Exception as e:
        print(Fore.RED + f"Error: {e}")
        return []

    # Sort results if needed, handle missing sort fields gracefully
    if sort_by:
        if sort_by == "size":
            matched_files.sort(key=lambda x: x["size_bytes"])
        else:
            matched_files.sort(key=lambda x: x.get(sort_by, ""))

    return matched_files

def display_results(results, show_size, show_path):
    if not results:
        print(Fore.YELLOW + "No files found matching the criteria.")
        return

    for idx, file_info in enumerate(results, start=1):
        output = f"{Fore.CYAN}{idx}. File: {file_info['name']}"
        if show_size and file_info['size_bytes'] is not None:
            output += f"{Fore.GREEN}, Size: {file_info['size_bytes'] / 1024:.2f} KB"  # Showing size in KB for display
        if show_path and file_info['path'] is not None:
            output += f"{Fore.YELLOW}, Path: {file_info['path']}"
        print(output)

def main():
    parser = argparse.ArgumentParser(description="Enhanced command-line file crawler.")
    parser.add_argument("filename", help="Filename to search for (partial match allowed).")
    parser.add_argument("file_extension", nargs="?", default="", help="Optional file extension to search for (partial match allowed).")
    parser.add_argument("-ef", "--exact-filename", action="store_true", help="Match filename exactly (ignores extension).")
    parser.add_argument("-ee", "--exact-extension", action="store_true", help="Match extension exactly (ignores dot).")
    parser.add_argument("-td", "--target-dir", default=os.getcwd(), help="Target directory to search in.")
    parser.add_argument("-mins", "--min-size", type=int, help="Minimum file size in KB.")
    parser.add_argument("-maxs", "--max-size", type=int, help="Maximum file size in KB.")
    parser.add_argument("--size", type=int, help="Exact size in bytes to match.")
    parser.add_argument("-s", "--show-size", action="store_true", help="Show file size in KB.")
    parser.add_argument("-p", "--show-path", action="store_true", help="Show file path.")
    parser.add_argument("--sort", choices=['name', 'size', 'path'], help="Sort results by name, size, or path.")
    parser.add_argument("-cs", "--case-sensitive", action="store_true", help="Enable case-sensitive filename matching.")

    args = parser.parse_args()

    results = find_files(
        args.filename,
        args.file_extension,
        args.exact_filename,
        args.exact_extension,
        args.target_dir,
        args.min_size,
        args.max_size,
        args.size,
        args.show_size,
        args.show_path,
        args.sort,
        args.case_sensitive
    )

    display_results(results, args.show_size, args.show_path)

if __name__ == "__main__":
    main()
