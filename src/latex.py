import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

def render_latex_to_image(latex_code):
    fig, ax = plt.subplots()
    ax.text(0.5, 0.5, f"${latex_code}$", fontsize=20, ha='center', va='center')
    ax.axis('off')  # Turn off axes
    
    # Save figure as an image
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.1)
    buf.seek(0)

    # Use Pillow to open the image
    image = Image.open(buf)
    return image