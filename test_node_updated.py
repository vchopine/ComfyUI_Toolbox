"""
Test script for the Model & Aspect Ratio Selector Node
This script simulates the functionality of the node to verify its behavior
"""

from model_aspect_ratio_node import ModelAspectRatioSelector

def test_node():
    # Create an instance of the node
    node = ModelAspectRatioSelector()
    
    # Test different model types and aspect ratios
    test_cases = [
        ("SDXL", "1:1 (Square)", 1024),
        ("SD", "16:9 (Landscape)", 768),
        ("SD1.5", "9:16 (Portrait)", 768),
        ("FLEX", "4:3 (Landscape)", 1024),
        ("SD3", "3:4 (Portrait)", 1024),
        ("Playground", "21:9 (Ultrawide)", 1024),
    ]
    
    print("Testing Model & Aspect Ratio Selector Node (Updated Version):")
    print("-" * 60)
    
    for model_type, aspect_ratio, base_resolution in test_cases:
        width, height, resolution_text = node.calculate_resolution(model_type, aspect_ratio, base_resolution)
        
        print(f"Model: {model_type}, Aspect Ratio: {aspect_ratio}, Base Resolution: {base_resolution}")
        print(f"Width: {width}, Height: {height}")
        print(f"Resolution Text: {resolution_text}")
        print("-" * 60)
    
    # Test custom base resolution
    width, height, resolution_text = node.calculate_resolution("SDXL", "16:9 (Landscape)", 1536)
    print(f"Model: SDXL, Aspect Ratio: 16:9 (Landscape), Base Resolution: 1536")
    print(f"Width: {width}, Height: {height}")
    print(f"Resolution Text: {resolution_text}")
    print("-" * 60)

if __name__ == "__main__":
    test_node()
