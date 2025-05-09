from banner import show_banner
from utils.file_detection import detect_file_type
from utils.directory_helper import validate_directory
from engine.conversion_engine import convert_document, convert_image
from summary_ui import show_summary

def main():
    show_banner()

    # 1. Get the file path from user
    input_file = input("\n[+] Enter the full path to the file you want to convert: ").strip()

    # 2. Detect the file type
    file_type = detect_file_type(input_file)
    if file_type == "unknown":
        print("[!] Unsupported file type. Exiting.")
        return

    print(f"[+] Detected file type: {file_type}")

    # 3. Show conversion options based on file type
    if file_type == "document":
        available_formats = ["pdf", "docx", "txt", "odt"]
    elif file_type == "image":
        available_formats = ["jpg", "png", "bmp", "gif"]
    else:
        print("[!] Error detecting file type. Exiting.")
        return

    print("\n[+] Available formats to convert to:")
    for idx, fmt in enumerate(available_formats, 1):
        print(f"{idx}. {fmt}")

    choices = input("\n[+] Enter the numbers of the format(s) you want (comma-separated, e.g., 1,3): ").split(",")

    selected_formats = []
    for choice in choices:
        try:
            selected_formats.append(available_formats[int(choice.strip()) - 1])
        except (IndexError, ValueError):
            print(f"[!] Invalid choice: {choice}")

    if not selected_formats:
        print("[!] No valid formats selected. Exiting.")
        return

    print(f"[+] You selected: {', '.join(selected_formats)}")

    # 4. Ask for output directory
    output_dir = input("\n[+] Enter the full path of the directory where you want to save the converted file(s): ").strip()
    if not validate_directory(output_dir):
        print("[!] Output directory invalid or does not exist. Exiting.")
        return

    print("\n[+] All inputs received successfully.")
    show_summary(input_file, file_type, selected_formats, output_dir)
    print("\n[*] Starting conversion...\n")


    for fmt in selected_formats:
        if file_type == "document":
            convert_document(input_file, fmt, output_dir)
        elif file_type == "image":
            convert_image(input_file, fmt, output_dir)

    print("\n[✔️] Conversion(s) completed successfully!")

if __name__ == "__main__":
    main()
