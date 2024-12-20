"""
Take a PDF file with the 4 pages. Reorder and merge them into a foldable
leaflet.
"""


import fitz
import argparse


def merge_two_pages(page1, page2, output_doc, margin_x_mm):
    # Calculate dimensions

    points_per_mm = 2.83465

    a4_width = 297 * points_per_mm
    a4_height = 210 * points_per_mm

    margin_x = margin_x_mm * points_per_mm
    margin_y = margin_x / a4_width * a4_height

    page1_rect = fitz.Rect(
        x0=margin_x, y0=margin_y, x1=a4_width/2, y1=a4_height-margin_y)
    page2_rect = fitz.Rect(
        x0=a4_width/2, y0=margin_y, x1=a4_width - margin_x, y1=a4_height-margin_y)

    # Merge pages

    new_page = output_doc.new_page(width=a4_width, height=a4_height)

    new_page.show_pdf_page(page1_rect, page1.parent,
                           page1.number, keep_proportion=False)
    new_page.show_pdf_page(page2_rect, page2.parent,
                           page2.number, keep_proportion=False)


def main():
    # Parse command line arguments

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="Path to the input PDF file", required=True)
    parser.add_argument("--output", help="Path to the output PDF file", required=True)
    parser.add_argument(
        "--margin-x", help="Margin in x-direction in mm", type=float, default=10)

    args = parser.parse_args()

    # Reorder and merge pages

    input_doc = fitz.open(args.input)
    output_doc = fitz.open()

    merge_two_pages(input_doc.load_page(3), input_doc.load_page(
        0), output_doc, args.margin_x)
    merge_two_pages(input_doc.load_page(1), input_doc.load_page(
        2), output_doc, args.margin_x)

    output_doc.save(args.output)


if __name__ == "__main__":
    main()
