"""
Model and Aspect Ratio Selector Node for ComfyUI
This node provides dropdown selectors for model types and aspect ratios,
and outputs width and height as integers for connecting to other nodes.
"""

from .model_aspect_ratio_node import ModelAspectRatioSelector

NODE_CLASS_MAPPINGS = {
    "ModelAspectRatioSelector": ModelAspectRatioSelector
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ModelAspectRatioSelector": "Model & Aspect Ratio Selector"
}
