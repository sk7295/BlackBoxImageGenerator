import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def get_user_data():
    # Ask for the model name first
    model_name = simpledialog.askstring("Model Name", "Enter the name of the black box model:")

    # Prompt user for number of inputs and outputs
    num_inputs = simpledialog.askinteger("Input", "Enter number of inputs:")
    num_outputs = simpledialog.askinteger("Output", "Enter number of outputs:")
    
    input_names = []
    for i in range(num_inputs):
        name = simpledialog.askstring("Input Name", f"Enter name for Input {i+1}/{num_inputs}:")
        input_names.append(name)

    output_names = []
    for i in range(num_outputs):
        name = simpledialog.askstring("Output Name", f"Enter name for Output {i+1}/{num_outputs}:")
        output_names.append(name)

    visualize_blackbox(model_name, input_names, output_names)


def visualize_blackbox(model_name, input_labels, output_labels):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Draw a rectangle for the black box
    box = patches.Rectangle((0.3, 0.4), 0.4, 0.2, facecolor='grey', edgecolor='black')
    ax.add_patch(box)

    # Add "Black Box Model" text
    plt.text(0.5, 0.5, f"{model_name}\nBlack Box Model", color='white', weight='bold',
             ha='center', va='center', fontsize=12)

    # Calculate the space between input and output arrows
    input_space_per_arrow = 0.2 / (len(input_labels) + 1)
    output_space_per_arrow = 0.2 / (len(output_labels) + 1)

    # Plot input arrows and labels (arrows as lines upon which text is written)
    for i, label in enumerate(input_labels, 1):
        y_pos = 0.4 + i*input_space_per_arrow
        plt.arrow(0.15, y_pos, 0.15, 0, fc='blue', ec='blue', head_length=0, head_width=0)
        plt.text(0.2, y_pos, label, ha='left', va='center', color='black', fontsize=10)

    # Plot output arrows and labels (arrows as lines upon which text is written)
    for i, label in enumerate(output_labels, 1):
        y_pos = 0.4 + i*output_space_per_arrow
        plt.arrow(0.7, y_pos, 0.15, 0, fc='red', ec='red', head_length=0, head_width=0)
        plt.text(0.75, y_pos, label, ha='left', va='center', color='black', fontsize=10)

    ax.axis('off')  # Turn off the axis
    plt.tight_layout()
    plt.show()


root = tk.Tk()
root.title("Black Box Model Visualizer")

# Create main frame
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

# Add a label and button to the main frame
label = tk.Label(frame, text="Black Box Model Visualizer", font=("Arial", 16))
label.grid(row=0, column=0, pady=20)
btn = tk.Button(frame, text="Enter Details", command=get_user_data)
btn.grid(row=1, column=0)

root.mainloop()
