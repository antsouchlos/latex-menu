import argparse
import qrcode
import qrcode.image.svg


def main():
    # Parse arguments

    parser = argparse.ArgumentParser()
    parser.add_argument("--text", help="Text to encode in QR code")
    parser.add_argument("--output", help="Output filename (SVG file)")
    parser.add_argument(
        "--color", help="Color of the QR code (e.g., #FFFFFF)", default="#FFFFFF")

    args = parser.parse_args()

    # Generate QR code

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(args.text)
    qr.make(fit=True)

    # The stroke is needed to eliminate dark lines betwen the squares
    some_args = {"stroke-width": ".1",
                 "fill": args.color, "stroke": args.color}

    img = qr.make_image(
        image_factory=qrcode.image.svg.SvgImage, **some_args)
    img.save(args.output)


if __name__ == "__main__":
    main()
