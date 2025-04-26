import matplotlib.pyplot as plt

def plot_image(image, title="Original Image"):
    
    plt.figure(figsize=(6,6))
    plt.imshow(image, cmap='gray')  
    plt.title(title)
    plt.axis('off')
    plt.show()

def plot_processed_image(image, title="Processed Image"):
    
    plt.figure(figsize=(6,6))
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

def plot_histogram(image):
   
    plt.figure(figsize=(8,6))
    
    if image.ndim == 2:  
        plt.hist(image.ravel(), bins=256, color='black', alpha=0.7)
        plt.title('Grayscale Histogram')
        plt.xlabel('Pixel Intensity')
        plt.ylabel('Frequency')
    elif image.ndim == 3:  
        colors = ('red', 'green', 'blue')
        for i, color in enumerate(colors):
            plt.hist(image[:,:,i].ravel(), bins=256, color=color, alpha=0.5, label=f'{color.upper()} channel')
        plt.title('Color Image Histogram')
        plt.xlabel('Pixel Intensity')
        plt.ylabel('Frequency')
        plt.legend()
    else:
        print("Unsupported image format.")
        return

    plt.show()
