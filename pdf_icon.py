from PIL import Image, ImageDraw

def create_icon():
    # Create a 48x48 image with RGBA mode for transparency
    size = 48
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw circular background
    margin = 2
    draw.ellipse([margin, margin, size-margin, size-margin], fill='#2B2B2B')
    
    # Draw "PDF" text
    text_color = '#FFFFFF'
    draw.text((10, 15), "PDF", fill=text_color, font=None)
    
    # Draw arrow
    arrow_color = '#FF6B6B'
    points = [(35, 20), (40, 25), (35, 30)]
    draw.line(points, fill=arrow_color, width=2)
    
    # Save as PNG file
    try:
        img.save('pdf_reverser.png', 'PNG')
        print("Icon created successfully!")
        return True
    except Exception as e:
        print(f"Error creating icon: {str(e)}")
        return False

if __name__ == "__main__":
    create_icon() 