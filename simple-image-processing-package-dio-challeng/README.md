image_processing_package/
│
├── README.md
├── requirements.txt
├── setup.py          
│
├── simple_image_processing/
│   │
│   ├── processing/
│   │   ├── __init__.py
│   │   ├── combination.py
│   │   └── transformation.py
│   │
│   └── tools/
│       ├── __init__.py
│       ├── io.py
│       └── plot.py


# simple_image_processing

Description. 
The package package_name is used to:
	- Processing: 
		- Histogram Matching.
		- Structural Similarity
		- Resize Image
	- Tools:
		- Read Image
		- Save Image
		- Plot Image
		- Plot Result
		- Plot Histogram  
	- This package provides simple tool to help new users get to know Python's capability of processing images.

## Installation

```bash
pip install simple_image_processing
```

## Usage

```python
from simple_image_processing import transformation
transformation.resize_image()
```

## Author
DanMV18

## License
[MIT] MIT Licence