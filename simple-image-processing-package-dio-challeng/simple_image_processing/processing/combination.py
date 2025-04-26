import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity as ssim

def find_difference(image1, image2):
    
    gray1 = rgb2gray(image1)
    gray2 = rgb2gray(image2)
    
    score, diff = ssim(gray1, gray2, full=True)
    diff = (1 - diff) 

    print(f"Structural Similarity Index: {score:.4f}")
    
    return diff

def combine_histograms(source_image, reference_image):
    
    matched = match_histograms(source_image, reference_image, channel_axis=-1)
    return matched
