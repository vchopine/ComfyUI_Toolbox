"""
# Installation and Usage Guide for Model & Aspect Ratio Selector Node

This document provides detailed instructions on how to install and use the Model & Aspect Ratio Selector Node in ComfyUI.

## Installation

### Method 1: Manual Installation

1. Locate your ComfyUI custom_nodes directory:
   - Windows: `C:\path\to\ComfyUI\custom_nodes\`
   - Linux/macOS: `/path/to/ComfyUI/custom_nodes/`

2. Create a new directory for this node:
   ```
   mkdir -p /path/to/ComfyUI/custom_nodes/ComfyUI-ModelAspectRatioSelector
   ```

3. Copy the following files to the new directory:
   - `model_aspect_ratio_node.py`
   - `__init__.py`
   - `README.md`

4. Restart ComfyUI if it's already running.

### Method 2: Git Installation

1. Navigate to your ComfyUI custom_nodes directory:
   ```
   cd /path/to/ComfyUI/custom_nodes/
   ```

2. Clone the repository:
   ```
   git clone https://github.com/yourusername/ComfyUI-ModelAspectRatioSelector
   ```

3. Restart ComfyUI if it's already running.

## Usage Guide

### Adding the Node to Your Workflow

1. In ComfyUI, right-click on the canvas to open the node menu.
2. Type "Model" or "Aspect" in the search box.
3. Select "Model & Aspect Ratio Selector" from the results.
4. The node will be added to your canvas.

### Configuring the Node

The node has three input parameters:

1. **Model Type**: Select the AI model you're using from the dropdown:
   - SDXL
   - SD
   - SD1.5
   - FLEX
   - SD3
   - Playground

2. **Aspect Ratio**: Select your desired aspect ratio from the dropdown:
   - 1:1 (Square)
   - 16:9 (Landscape)
   - 9:16 (Portrait)
   - 4:3 (Landscape)
   - 3:4 (Portrait)
   - 3:2 (Landscape)
   - 2:3 (Portrait)
   - 21:9 (Ultrawide)
   - 9:21 (Vertical Ultrawide)
   - 2:1 (Landscape)
   - 1:2 (Portrait)

3. **Base Resolution**: Set the base resolution value (default is 1024).
   - For SDXL, FLEX, SD3, and Playground models, the default is 1024.
   - For SD and SD1.5 models, the maximum is capped at 768.

### Node Outputs

The node provides three outputs:

1. **Width**: Integer value for the calculated width (in pixels).
2. **Height**: Integer value for the calculated height (in pixels).
3. **Resolution Text**: A formatted string showing the model, aspect ratio, and resolution (e.g., "SDXL | 16:9 (Landscape) | 1536×864").

### Connecting to Other Nodes

#### Example 1: Basic Image Generation

1. Connect the **Width** and **Height** outputs to the corresponding inputs of an "Empty Latent Image" node.
2. Connect the Empty Latent Image to a KSampler node.
3. Connect the KSampler to a VAE Decode node.
4. Connect the VAE Decode to a Save Image node.

#### Example 2: Using Resolution Text

1. Connect the **Resolution Text** output to a "Text" node for display.
2. Alternatively, connect it to the "filename_prefix" input of a Save Image node to include the resolution information in the saved filename.

## Resolution Calculation Logic

The node calculates width and height based on:

1. The selected model type (which influences the base resolution)
2. The selected aspect ratio
3. The user-specified base resolution parameter

All dimensions are made divisible by 8 to ensure compatibility with most AI models.

### Examples:

- SDXL + 1:1 (Square) + Base 1024 = 1024×1024
- SD + 16:9 (Landscape) + Base 768 = 768×432
- SD1.5 + 9:16 (Portrait) + Base 768 = 432×768
- FLEX + 4:3 (Landscape) + Base 1024 = 1024×768
- SD3 + 3:4 (Portrait) + Base 1024 = 768×1024
- SDXL + 16:9 (Landscape) + Base 1536 = 1536×864

## Troubleshooting

If the node doesn't appear in ComfyUI:
1. Verify that the files are in the correct location.
2. Check the ComfyUI console for any error messages.
3. Restart ComfyUI completely.

If the node appears but doesn't function correctly:
1. Ensure you're using a compatible version of ComfyUI.
2. Check that the node's outputs are properly connected to other nodes.
"""
