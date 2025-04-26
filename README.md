# 📄 DocMorpher

> **DocMorpher** is a simple, fast, and beginner-friendly **CLI tool** that converts **documents** (PDF, DOCX, TXT, ODT) and **images** (JPG, PNG, BMP, GIF) into various formats easily.  
> Designed for learners, and anyone needing flexible document handling on Linux.
> ![Process Diagram](https://github.com/Gr3ytrac3/DocMorpher/blob/90cc6ace7a54ac406b98318485141a7cfb80355e/Screenshot_2025-04-26_06_08_43.png)

---

## 📜 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Process Flow Diagram](#process-flow-diagram)
- [Supported Formats](#supported-formats)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## 🚀 Features
- Detects file type (Document or Image) automatically.
- Supports multiple conversion formats.
- Process summary displayed before conversion.
- Simple and elegant CLI interface.
- Designed to run smoothly on **Linux** environments like **Kali Linux**.
- Modular and beginner-friendly codebase.

---

## 🛠️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/docmorpher.git

# 2. Navigate into the project
cd docmorpher

# 3. (Optional but recommended) Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# 4. Install the dependencies
pip install -r requirements.txt
```

### Required Libraries:
- `python-docx`
- `Pillow`
- `PyMuPDF (fitz)`

Install manually if needed:

```bash
pip install python-docx Pillow PyMuPDF
```

---

## 🧩 Usage

```bash
python main.py
```

You will be prompted to:
- Enter the input file path.
- Choose the desired output format(s).
- Specify the output directory.

✅ Sit back and let **DocMorpher** handle the conversion!

---

## 📈 Process Flow Diagram

Here’s a simple view of how **DocMorpher** works:

> ![Process Diagram](https://github.com/Gr3ytrac3/DocMorpher/blob/24309fbb7aa26872c3705cbb3706fea3f3157853/Screenshot_2025-04-26_14_26_26.png)
> ![Process Diagram](https://github.com/Gr3ytrac3/DocMorpher/blob/24309fbb7aa26872c3705cbb3706fea3f3157853/Screenshot_2025-04-26_14_26_56.png)
> ![Process Diagram](https://github.com/Gr3ytrac3/DocMorpher/blob/24309fbb7aa26872c3705cbb3706fea3f3157853/Screenshot_2025-04-26_14_27_00.png)

---

## 🧾 Supported Formats

| Input Type | Formats to Convert Into |
|:-----------|:-------------------------|
| Document   | PDF, DOCX, TXT, ODT        |
| Image      | JPG, PNG, BMP, GIF         |

---

## 📂 Project Structure

```
docmorpher/
│
├── main.py                 # Main execution file
├── banner.py                # Banner display
├── utils/
│   ├── file_detection.py    # Detects file type
│   ├── directory_helper.py  # Validates output directory
├── engine/
│   ├── conversion_engine.py # Handles file conversions
├── venv/                    # (Optional) Virtual Environment
├── requirements.txt         # Project dependencies
└── README.md                # This file
```

---

## 🤝 Contributing

We welcome contributions!

1. Fork this repo 🍴
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Create a pull request ✅

---

## 🪪 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute it as you wish.

---

> Built with ❤️ by **Gr3ytrac3** (CyberDevHQ)

---

# ✅ Quick Start Command

```bash
git clone https://github.com/yourusername/docmorpher.git && cd docmorpher && python3 main.py
```

---
