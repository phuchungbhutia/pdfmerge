# 📎 PDF Merge Tool

A simple Python script to merge all PDFs in a folder into one combined file using `PyPDF2`.

## 🚀 Features

- Automatically detects all `.pdf` files in a folder
- Merges them in sorted order
- Accepts optional folder and output filename via command-line arguments

## 🧰 Requirements

- Python 3.7+
- PyPDF2

```bash
pip install PyPDF2
```
## 🛠 Usage
```bash
python pdfmerge.py
```

# Optional:
```bash
python pdfmerge.py --folder "path/to/pdfs" --output "merged.pdf"
```