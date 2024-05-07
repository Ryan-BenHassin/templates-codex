```
from PIL import Image, ImageFilter, ImageEnhance
import cv2
import numpy as np

class ImageProcessor:
 def __init__(self, image_path):
 self.image_path = image_path
 self.image = Image.open(image_path)
 self.cv_image = cv2.imread(image_path)

 def apply_filter(self, filter_type):
 if filter_type == 'blur':
 return self.image.filter(ImageFilter.BLUR)
 elif filter_type == 'contour':
 return self.image.filter(ImageFilter.CONTOUR)
 elif filter_type == 'detail':
 return self.image.filter(ImageFilter.DETAIL)
 elif filter_type == 'edge_enhance':
 return self.image.filter(ImageFilter.EDGE_ENHANCE)
 elif filter_type == 'edge_enhance_more':
 return self.image.filter(ImageFilter.EDGE_ENHANCE_MORE)
 elif filter_type == 'emboss':
 return self.image.filter(ImageFilter.EMBOSS)
 elif filter_type == 'find_edges':
 return self.image.filter(ImageFilter.FIND_EDGES)
 elif filter_type == 'sharpen':
 return self.image.filter(ImageFilter.SHARPEN)
 elif filter_type == 'smooth':
 return self.image.filter(ImageFilter.SMOOTH)
 elif filter_type == 'smooth_more':
 return self.image.filter(ImageFilter.SMOOTH_MORE)

 def adjust_brightness(self, factor):
 enhancer = ImageEnhance.Brightness(self.image)
 return enhancer.enhance(factor)

 def adjust_contrast(self, factor):
 enhancer = ImageEnhance.Contrast(self.image)
 return enhancer.enhance(factor)

 def adjust_color_balance(self, factor):
 enhancer = ImageEnhance.Color(self.image)
 return enhancer.enhance(factor)

 def adjust_sharpness(self, factor):
 enhancer = ImageEnhance.Sharpness(self.image)
 return enhancer.enhance(factor)

 def convert_to_grayscale(self):
 return cv2.cvtColor(self.cv_image, cv2.COLOR_BGR2GRAY)

 def save_image(self, image, path):
 image.save(path)

# Example usage
processor = ImageProcessor('input.jpg')
filtered_image = processor.apply_filter('blur')
processor.save_image(filtered_image, 'output.jpg')
```
