import numpy as np
import scipy as sp
import matplotlib as mpl

# Check if these packages are installed
try:
    import numpy
    import scipy
    import matplotlib
    print("All required packages are installed.")
except ImportError as e:    print(f"Error: {e}. Please install the required packages.")