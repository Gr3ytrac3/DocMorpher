import os
from docx import Document
from PIL import Image
from pdf2docx import Converter
import fitz  # PyMuPDF


def convert_document(input_path, output_format, output_dir):
    filename, _ = os.path.splitext(os.path.basename(input_path))
    output_file = os.path.join(output_dir, f"{filename}.{output_format}")

    try:
        if output_format == "txt":
            doc = Document(input_path)
            with open(output_file, "w", encoding="utf-8") as f:
                for para in doc.paragraphs:
                    f.write(para.text + "\n")

        elif output_format == "docx":
            if input_path.lower().endswith(".pdf"):
                print(f"[INFO] Start to convert {input_path}")
                cv = Converter(input_path)
                cv.convert(output_file)
                cv.close()
            else:
                print("[!] DOCX conversion only supports PDF as input for now.")

        elif output_format == "pdf":
            print("[!] PDF conversion from DOCX not yet implemented.")

        else:
            print(f"[!] Conversion to {output_format} is not supported yet.")

        print(f"[+] Saved converted document: {output_file}")

    except Exception as e:
        # Attempt to fix 'pixmap must be grayscale or rgb' issue
        if "pixmap must be grayscale or rgb" in str(e):
            print("[!] Attempting fix: Converting pages to RGB pixmaps...")
            try:
                doc = fitz.open(input_path)
                for i, page in enumerate(doc):
                    pix = page.get_pixmap()
                    if pix.colorspace.n != 3:
                        pix = fitz.Pixmap(fitz.csRGB, pix)
                    img_path = os.path.join(output_dir, f"{filename}_page{i+1}.png")
                    pix.save(img_path)
                print("[+] Saved pages as PNGs due to conversion error.")
            except Exception as ex:
                print(f"[X] Fallback image conversion also failed: {ex}")
        else:
            print(f"[!] Error converting PDF to {output_format}: {e}")




def convert_image(input_path, output_format, output_dir):
    filename, _ = os.path.splitext(os.path.basename(input_path))
    output_file = os.path.join(output_dir, f"{filename}.{output_format}")

    img = Image.open(input_path)
    img.save(output_file)

    print(f"[+] Saved converted image: {output_file}")
