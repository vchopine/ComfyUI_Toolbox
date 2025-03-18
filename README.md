# Model & Aspect Ratio Selector Node for ComfyUI

This custom ComfyUI node provides dropdown selectors for model types and aspect ratios, and outputs width and height as integers for connecting to other nodes. It automatically sets the optimal resolution based on the selected model type and displays the resolution in pixels directly on the node.

## Features

- Dropdown selector for AI model types (SDXL, SD, SD1.5, FLEX, SD3, Playground)
- Automatic optimal resolution selection based on model type:
  - SD/SD1.5: 512×512
  - SDXL/FLEX/Playground: 1024×1024
  - SD3: 2048×2048
- Dropdown selector for popular aspect ratios in both landscape and portrait orientations
- Option to override with custom resolution if needed
- Outputs width and height as integers for connecting to other nodes
- Displays the selected model, base resolution, aspect ratio, and final dimensions in pixels

## Installation

1. Navigate to your ComfyUI custom_nodes directory:
   ```
   cd /path/to/ComfyUI/custom_nodes/
   ```

2. Create a new directory for this node:
   ```
   mkdir -p ComfyUI-ModelAspectRatioSelector
   ```
   
3. Copy the `model_aspect_ratio_node.py` and `__init__.py` files to this directory.

4. Restart ComfyUI if it's already running.

## Usage

1. In ComfyUI, right-click on the canvas and search for "Model & Aspect Ratio Selector".
2. Select your desired model type from the dropdown (SDXL, SD, SD1.5, FLEX, SD3, Playground).
3. Select your desired aspect ratio from the dropdown (1:1, 16:9, 9:16, etc.).
4. By default, the node will use the optimal resolution for the selected model type. If you want to use a custom resolution, set "custom_resolution" to True and adjust the "base_resolution" value.
5. Connect the width and height outputs to other nodes that require dimension inputs (like Empty Latent Image).

## Model-Specific Optimal Resolutions

The node automatically sets the optimal base resolution for each model type:

- **SD/SD1.5**: 512×512 (for 1:1 aspect ratio)
- **SDXL/FLEX/Playground**: 1024×1024 (for 1:1 aspect ratio)
- **SD3**: 2048×2048 (for 1:1 aspect ratio)

When using non-square aspect ratios, the node maintains the longer dimension at the base resolution and calculates the shorter dimension proportionally, ensuring all dimensions are divisible by 8.

## Example Workflow

1. Add the "Model & Aspect Ratio Selector" node to your workflow
2. Select "SDXL" as the model type and "16:9 (Landscape)" as the aspect ratio
3. The node will output width=1024, height=576
4. Connect these outputs to an Empty Latent Image node
5. Connect the resolution_text output to a Text node for display or to a Save Image node for filename prefixing

## Custom Resolution Option

If you need to use a resolution different from the model's optimal value:

1. Set "custom_resolution" to True
2. Adjust the "base_resolution" parameter to your desired value
3. The node will use this value as the base for calculating dimensions

## Troubleshooting

If the node doesn't appear in ComfyUI:
1. Verify that the files are in the correct location.
2. Check the ComfyUI console for any error messages.
3. Restart ComfyUI completely.

If the node appears but doesn't function correctly:
1. Ensure you're using a compatible version of ComfyUI.
2. Check that the node's outputs are properly connected to other nodes.

## License

This code is provided under the MIT License.
