"""
Test script for the updated Model & Aspect Ratio Selector Node
This script tests the node with optimal model-specific resolutions
"""

from model_aspect_ratio_node import ModelAspectRatioSelector

def test_node():
    # Create an instance of the node
    node = ModelAspectRatioSelector()
    
    print("Testing with optimal model resolutions (custom_resolution=False):")
    print("-" * 70)
    
    # Test all model types with default optimal resolutions
    for model in ['SDXL', 'SD', 'SD1.5', 'FLEX', 'SD3', 'Playground']:
        width, height, res_text = node.calculate_resolution(model, '1:1 (Square)', False, 1024)
        print(f"{model}: {width}x{height} - {res_text}")
    
    print("\nTesting with custom resolution (custom_resolution=True):")
    print("-" * 70)
    
    # Test with custom resolution
    for model in ['SDXL', 'SD', 'SD1.5']:
        width, height, res_text = node.calculate_resolution(model, '1:1 (Square)', True, 1536)
        print(f"{model} (custom 1536px): {width}x{height} - {res_text}")
    
    print("\nTesting different aspect ratios with SD3:")
    print("-" * 70)
    
    # Test different aspect ratios with SD3
    aspect_ratios = [
        "1:1 (Square)", 
        "16:9 (Landscape)", "9:16 (Portrait)",
        "4:3 (Landscape)", "3:4 (Portrait)"
    ]
    
    for ratio in aspect_ratios:
        width, height, res_text = node.calculate_resolution('SD3', ratio, False, 1024)
        print(f"SD3 with {ratio}: {width}x{height} - {res_text}")

if __name__ == "__main__":
    test_node()
