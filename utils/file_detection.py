import os

def detect_file_type(file_path):
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    document_exts = ['.pdf', '.docx', '.txt', '.odt']
    image_exts = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']

    if ext in document_exts:
        return "document"
    elif ext in image_exts:
        return "image"
    else:
        return "unknown"
