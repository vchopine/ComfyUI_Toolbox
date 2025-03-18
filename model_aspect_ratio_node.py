"""
Model and Aspect Ratio Selector Node for ComfyUI
This node provides dropdown selectors for model types and aspect ratios,
and outputs width and height as integers for connecting to other nodes.
It also displays the resolution in pixels directly on the node.
"""

class ModelAspectRatioSelector:
    """
    A ComfyUI node that provides dropdown selectors for model types and aspect ratios,
    and outputs width and height as integers.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model_type": (["SDXL", "SD", "SD1.5", "FLEX", "SD3", "Playground"], {"default": "SDXL"}),
                "aspect_ratio": ([
                    "1:1 (Square)", 
                    "16:9 (Landscape)", "9:16 (Portrait)",
                    "4:3 (Landscape)", "3:4 (Portrait)",
                    "3:2 (Landscape)", "2:3 (Portrait)",
                    "21:9 (Ultrawide)", "9:21 (Vertical Ultrawide)",
                    "2:1 (Landscape)", "1:2 (Portrait)"
                ], {"default": "1:1 (Square)"}),
                "custom_resolution": ("BOOLEAN", {"default": False}),
                "base_resolution": ("INT", {"default": 1024, "min": 512, "max": 4096, "step": 64}),
            }
        }
    
    RETURN_TYPES = ("INT", "INT", "STRING")
    RETURN_NAMES = ("width", "height", "resolution_text")
    FUNCTION = "calculate_resolution"
    CATEGORY = "utils"
    
    def calculate_resolution(self, model_type, aspect_ratio, custom_resolution, base_resolution):
        """
        Calculate width and height based on model type and aspect ratio.
        Also returns a formatted string showing the resolution.
        """
        # Extract the aspect ratio values
        if ":" in aspect_ratio:
            ratio_part = aspect_ratio.split(" ")[0]
            width_ratio, height_ratio = map(int, ratio_part.split(":"))
        else:
            # Default to 1:1 if format is unexpected
            width_ratio, height_ratio = 1, 1
        
        # Set optimal resolution based on model type if custom_resolution is False
        if not custom_resolution:
            if model_type == "SDXL":
                base = 1024  # SDXL optimal resolution
            elif model_type == "SD3":
                base = 2048  # SD3 optimal resolution
            elif model_type == "FLEX":
                base = 1024  # FLEX optimal resolution
            elif model_type == "Playground":
                base = 1024  # Playground optimal resolution
            else:  # SD, SD1.5, etc.
                base = 512  # SD/SD1.5 optimal resolution
        else:
            # Use user-specified base_resolution if custom_resolution is True
            base = base_resolution
        
        # Calculate width and height based on aspect ratio
        if width_ratio >= height_ratio:
            # Landscape or square
            width = base
            height = int((height_ratio / width_ratio) * width)
            # Make height divisible by 8
            height = (height // 8) * 8
        else:
            # Portrait
            height = base
            width = int((width_ratio / height_ratio) * height)
            # Make width divisible by 8
            width = (width // 8) * 8
        
        # Create resolution text for display
        model_res_text = f"{model_type} ({base}px)"
        resolution_text = f"{model_res_text} | {aspect_ratio} | {width}×{height}"
        
        return (width, height, resolution_text)
