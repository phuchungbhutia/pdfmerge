import os
import argparse
from PyPDF2 import PdfMerger

def merge_pdfs(input_folder=None, output_filename="merged_output.pdf"):
    """Merges all PDFs in the folder into a single PDF."""
    folder_path = input_folder or os.path.dirname(os.path.abspath(__file__))
    merger = PdfMerger()

    pdf_files = sorted([
        file for file in os.listdir(folder_path)
        if file.lower().endswith(".pdf") and file != output_filename
    ])

    if not pdf_files:
        print("No PDF files found in the folder.")
        return

    print("Merging the following PDFs:")
    for pdf in pdf_files:
        print(f" - {pdf}")
        merger.append(os.path.join(folder_path, pdf))

    output_path = os.path.join(folder_path, output_filename)
    merger.write(output_path)
    merger.close()

    print(f"\n✅ Merged PDF saved as: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge all PDFs in a folder into one file.")
    parser.add_argument("--folder", type=str, help="Path to the folder containing PDFs")
    parser.add_argument("--output", type=str, default="merged_output.pdf", help="Name of the output merged PDF file")
    args = parser.parse_args()

    merge_pdfs(args.folder, args.output)
