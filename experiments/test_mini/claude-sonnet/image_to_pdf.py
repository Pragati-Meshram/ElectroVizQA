from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def png_to_pdf(png_file_path, pdf_file_path):
    # Open the image file
    with Image.open(png_file_path) as img:
        # Create a PDF canvas
        c = canvas.Canvas(pdf_file_path, pagesize=letter)
        width, height = letter  # Use letter page size
        
        # Resize the image to fit the page if needed
        img_width, img_height = img.size
        aspect = img_width / img_height
        if img_width > width or img_height > height:
            if aspect > 1:  # Landscape orientation
                new_width = width
                new_height = width / aspect
            else:  # Portrait orientation
                new_width = height * aspect
                new_height = height
            img = img.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
        
        # Draw the image on the canvas
        c.drawImage(img, 0, 0, width=img.width, height=img.height)
        c.save()

# Example usage
png_file = 'example.png'
pdf_file = 'output.pdf'
png_to_pdf(png_file, pdf_file)
