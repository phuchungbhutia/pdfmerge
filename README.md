# 📎 PDF Merge Tool
[![GitHub stars](https://img.shields.io/github/stars/phuchungbhutia/pdfmerge)](https://github.com/phuchungbhutia/pdfmerge/stargazers) [![License](https://img.shields.io/github/license/phuchungbhutia/pdfmerge)](https://github.com/phuchungbhutia/pdfmerge/blob/main/LICENSE) [![Workflow Status](https://img.shields.io/github/workflow/status/phuchungbhutia/pdfmerge/Update%20Prompt%20Indexes)](https://github.com/phuchungbhutia/pdfmerge/actions) [![Contributors](https://img.shields.io/github/contributors/phuchungbhutia/pdfmerge)](https://github.com/phuchungbhutia/pdfmerge/graphs/contributors) [![Last Updated](https://img.shields.io/github/last-commit/phuchungbhutia/pdfmerge/main?label=Last%20Updated)](https://github.com/phuchungbhutia/pdfmerge/commits/main)

A simple Python script to merge all PDFs in a folder into one combined file using `PyPDF2`.

## Repository Stats

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=phuchungbhutia&show_icons=true&theme=radical)

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
