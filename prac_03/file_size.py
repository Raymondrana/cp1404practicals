def count_lines(filename: str) -> int:
    #Opens a file and counts the number of lines it contains.
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return len(lines)


def main():
    filename = input("Enter filename: ").strip()

    # Loop continues as long as filename is not an empty string
    while filename:
        try:
            line_count = count_lines(filename)
            print(f"{filename} has {line_count} lines.")
        except FileNotFoundError:
            print(f"ERROR: {filename} does not exist.")
        except PermissionError:
            print(f"ERROR: Permission denied to read {filename}.")

        # Prompt again for the next iteration
        filename = input("Enter filename: ").strip()

main()
