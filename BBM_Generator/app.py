from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import os
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import matplotlib.patches as patches

app = Flask(__name__)

import os

DOWNLOAD_FOLDER = os.path.join(app.root_path, 'download')

@app.route('/')
def index():
    return render_template('input.html')

@app.route('/build_another_bbm')
def build_another_bbm():
    # Get list of all .png files in the download folder
    png_files = [f for f in os.listdir(DOWNLOAD_FOLDER) if f.endswith('.png')]
    
    # Delete the .png files
    for png_file in png_files:
        file_path = os.path.join(DOWNLOAD_FOLDER, png_file)
        if os.path.exists(file_path):
            os.remove(file_path)

    return redirect(url_for('index'))  # Redirect back to the main page

@app.route('/visualize', methods=['POST'])
def visualize():
    model_name = request.form['model_name']
    num_inputs = int(request.form['num_inputs'])
    num_outputs = int(request.form['num_outputs'])
    return render_template('visualize.html', model_name=model_name, num_inputs=num_inputs, num_outputs=num_outputs)

@app.route('/show_BBM', methods=['POST'])
def show_BBM():
    model_name = request.form['model_name']
    num_inputs = int(request.form['num_inputs'])
    num_outputs = int(request.form['num_outputs'])
    inputs = [request.form[f'input_{i+1}'] for i in range(num_inputs)]
    outputs = [request.form[f'output_{i+1}'] for i in range(num_outputs)]

    image_path = generate_black_box(model_name, inputs, outputs)
    image_url = url_for('download_file', filename=f'{model_name}.png', _external=True)

    return render_template("show_BBM.html", image_url=image_url, model_name=model_name)


@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(DOWNLOAD_FOLDER,filename)

def generate_black_box(model_name, input_labels, output_labels):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Draw a rectangle for the black box
    box = patches.Rectangle((0.3, 0.4), 0.4, 0.2, facecolor='grey', edgecolor='black')
    ax.add_patch(box)

    # Add model name and "Black Box Model" text inside the box using a newline
    plt.text(0.5, 0.5, f"{model_name}\nBlack Box Model", color='white', weight='bold', ha='center', va='center', fontsize=10)

    # Spacing and arrow length for inputs
    input_spacing = 0.2 / (len(input_labels) + 1)
    arrow_length_input = 0.14  # Slightly shortened to butt against the black box

    # Plot input arrows and labels
    for i, label in enumerate(input_labels):
        y_pos = 0.4 + (i+1)*input_spacing
        plt.arrow(0.15, y_pos, arrow_length_input, 0, head_width=0.02, head_length=0.02, fc='blue', ec='blue')
        plt.text(0.14, y_pos, label, ha='right', va='center', color='black', fontsize=10)

    # Spacing and arrow length for outputs
    output_spacing = 0.2 / (len(output_labels) + 1)
    arrow_length_output = 0.15

    # Plot output arrows and labels
    for i, label in enumerate(output_labels):
        y_pos = 0.4 + (i+1)*output_spacing
        plt.arrow(0.7, y_pos, arrow_length_output, 0, head_width=0.02, head_length=0.02, fc='red', ec='red')
        plt.text(0.87, y_pos, label, ha='left', va='center', color='black', fontsize=10)

    ax.axis('off')  # Turn off the axis
    plt.tight_layout()

    # Save the image
    import os

    DOWNLOAD_FOLDER = os.path.join(app.root_path, 'download')
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)
    image_path = os.path.join(DOWNLOAD_FOLDER, f"{model_name}.png")
    plt.savefig(image_path)

    # Close the plot to free up memory
    plt.close(fig)

    return image_path



if __name__ == '__main__':
    app.run(debug=True)
