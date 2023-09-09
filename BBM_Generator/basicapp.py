import matplotlib.pyplot as plt
import matplotlib.patches as patches

def visualize_blackbox(input_labels, output_labels):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Draw a rectangle for the black box (making it longer in width than in height)
    box = patches.Rectangle((0.3, 0.4), 0.4, 0.2, facecolor='grey', edgecolor='black')
    ax.add_patch(box)

    # Add "Black Box Model" text
    plt.text(0.5, 0.5, 'Black Box Model', color='white', weight='bold',
             ha='center', va='center', fontsize=12)

    # Calculate the positions for input labels
    input_positions = [(0.2, 0.45), (0.2, 0.5), (0.2, 0.55)]

    # Plot input arrows and labels
    for i, (label, (x, y)) in enumerate(zip(input_labels, input_positions)):
        plt.arrow(x, y, 0.08, 0, head_width=0.02, head_length=0.02, fc='blue', ec='blue')
        plt.text(x - 0.15, y, label, ha='center', va='center', color='black', fontsize=10)

    # Calculate the space between output arrows
    total_space = 0.2
    space_per_arrow = total_space / (len(output_labels) + 1)

    # Plot output arrows and labels
    for i, label in enumerate(output_labels, 1):
        y_pos = 0.4 + i*space_per_arrow
        plt.arrow(0.7, y_pos, 0.1, 0, head_width=0.02, head_length=0.02, fc='red', ec='red')
        plt.text(0.85, y_pos, label, ha='center', va='center', color='black', fontsize=10)

    ax.axis('off')  # Turn off the axis
    plt.tight_layout()
    plt.show()

# Example Usage:
input_labels = ["Input 1", "Input 2", "Input 3"]
output_labels = ["Output 1", "Output 2"]
visualize_blackbox(input_labels, output_labels)
