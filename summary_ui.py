# summary_ui.py
def show_summary(input_file, file_type, selected_formats, output_dir):
    print("\n┌──[Process Summary]")
    print(f"│ Input File     : {input_file}")
    print(f"│ Detected Type  : {file_type.capitalize()}")
    print(f"│ Output Formats : {', '.join(selected_formats)}")
    print(f"│ Output Path    : {output_dir}")
    print("└" + "─" * 40)
