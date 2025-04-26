from skimage.transform import resize
import numpy as np

def resize_image(image, target_shape):
   
    resized = resize(image, target_shape, anti_aliasing=True)
    resized = np.clip(resized, 0, 1)  
    print(f"Image resized to {target_shape}")
    return resized
