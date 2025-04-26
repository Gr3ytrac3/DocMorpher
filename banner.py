from rich.console import Console
from pyfiglet import figlet_format
from termcolor import cprint
from rich.panel import Panel
console = Console()


def show_banner():
    cprint(figlet_format("DocMorpher", font="slant"), "cyan")
    cprint("Author     : Cyberdev", "green")
    cprint("Version    : 1.0.0", "yellow")
    cprint("GitHub     : Gr3ytrac3", "white")
    cprint("Tool       : Convert & Morph Docs Like a Pro 💼", "magenta")
    print("=" * 60)


    # Process section
    process_steps = """[bold cyan]
        1. Upload File 📂
        2. File Type Detection 🕵️
        3. Choose Output Format 🎯
        4. Select Output Location 🗂️
        5. Start Conversion 🚀
        6. Done! 🎉
        """
    console.print(Panel(process_steps, title="[bold magenta]Process Overview"))