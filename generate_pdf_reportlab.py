from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

doc = SimpleDocTemplate("01_Environment_and_Project_Setup.pdf", pagesize=letter)
styles = getSampleStyleSheet()
styleN = styles["Normal"]
styleH1 = styles["Heading1"]
styleH2 = styles["Heading2"]

story = []

story.append(Paragraph("REGIONAL AGRICULTURAL AI - Phase 1", styleH1))
story.append(Paragraph("Part 1: Environment and Project Setup", styleH2))
story.append(Spacer(1, 12))

content = [
    ("1. Project Introduction", styleH2),
    ("The Regional Agricultural AI project aims to build an AI-based crop leaf disease detection system that analyzes a crop leaf image and identifies the disease with a confidence score.", styleN),
    ("Phase 1 focuses on the Core Machine Learning Disease Prediction System, isolating the model development from web applications, APIs, and deployments (which will follow in later phases).", styleN),
    
    ("2. Part Objective: Environment and Project Setup", styleH2),
    ("The goal of this part is to create a robust, reproducible Machine Learning project environment. A clean environment prevents dependency conflicts, ensures that code runs smoothly on different machines, and creates a logical structure for all scripts and data.", styleN),
    
    ("3. Project Setup Concepts", styleH2),
    ("- Python Version: We are using Python 3, which is the standard for ML development due to its rich ecosystem.", styleN),
    ("- Virtual Environment (venv): An isolated environment that contains its own Python executable and installed packages. It prevents global packages from interfering with project-specific dependencies.", styleN),
    ("- pip: Python's package installer, used to download and install libraries from the Python Package Index (PyPI).", styleN),
    ("- requirements.txt: A file listing all the packages required to run the project. This makes the project reproducible; anyone can run `pip install -r requirements.txt` to replicate the environment.", styleN),
    ("- Jupyter Notebook: An interactive computational environment used for data exploration, visualization, and step-by-step experimentation.", styleN),
    ("- VS Code: A powerful source-code editor where the final Python scripts will be developed.", styleN),
    ("- GPU vs CPU / CUDA: Deep learning models (like CNNs) train much faster on a GPU. CUDA is a parallel computing platform by NVIDIA that enables TensorFlow/Keras to leverage the GPU for rapid matrix operations. If no GPU is available, the CPU is used (which is much slower).", styleN),

    ("4. Project Architecture", styleH2),
    ("The workspace has been organized as follows:", styleN),
    ("- regional-agricultural-ai/", styleN),
    ("  - dataset/ (Original and processed datasets)", styleN),
    ("  - notebooks/ (Jupyter notebooks)", styleN),
    ("  - src/ (Source code)", styleN),
    ("    - data/ (Data ingestion)", styleN),
    ("    - preprocessing/ (Cleaning and transforms)", styleN),
    ("    - models/ (Architectures)", styleN),
    ("    - training/ (Training loops)", styleN),
    ("    - evaluation/ (Metrics)", styleN),
    ("    - inference/ (Prediction scripts)", styleN),
    ("  - models/ (Saved models)", styleN),
    ("  - results/ (Training logs)", styleN),
    ("  - reports/ (Generated docs)", styleN),
    ("  - requirements.txt (Dependencies)", styleN),

    ("5. Technologies & Packages", styleH2),
    ("- numpy: Fundamental package for scientific computing. Required for multi-dimensional arrays (tensors).", styleN),
    ("- pandas: Data manipulation and analysis tool. Required for handling tabular data.", styleN),
    ("- matplotlib & seaborn: Plotting libraries. Required for generating graphs.", styleN),
    ("- opencv-python: Open Source Computer Vision Library. Required for fast image reading, resizing.", styleN),
    ("- Pillow: Python Imaging Library. Required as a secondary image processing tool.", styleN),
    ("- scikit-learn: Machine learning library. Required for creating train/validation/test splits, calculating metrics.", styleN),
    ("- tensorflow & keras: The core deep learning framework. (Note: Awaits Python 3.11/3.12 or conda environment).", styleN),
    ("- tqdm: A smart progress meter. Required for showing progress bars.", styleN),
    ("- jupyter & notebook: Required to run .ipynb files for exploratory data analysis.", styleN),

    ("6. Code Explanation (Setup)", styleH2),
    ("Command: python -m venv venv", styleN),
    ("Explanation: Creates a folder named 'venv' containing the isolated Python environment.", styleN),
    ("Command: .\\venv\\Scripts\\activate", styleN),
    ("Explanation: Activates the environment so that subsequent commands use the isolated pip and Python.", styleN),
    ("Command: pip install -r requirements.txt", styleN),
    ("Explanation: Installs all listed dependencies automatically.", styleN),

    ("7. Viva & Interview Questions", styleH2),
    ("Q: Why do we use a virtual environment?", styleN),
    ("A: To isolate project dependencies from the global system, ensuring reproducibility and preventing version conflicts.", styleN),
    ("Q: What happens if you don't use requirements.txt?", styleN),
    ("A: Another developer (or the examiner) won't know which packages and versions to install, potentially causing the code to crash.", styleN),
    ("Q: Why separate data processing code from model training code?", styleN),
    ("A: It makes the codebase modular, easier to test, debug, and maintain.", styleN),

    ("8. Implementation Status", styleH2),
    ("Environment and Project Setup: COMPLETED.", styleN),
    ("The dependencies are installed, folders are created, and this document proves the successful execution of Part 1.", styleN)
]

for text, style in content:
    story.append(Paragraph(text, style))
    if style == styleH2:
        story.append(Spacer(1, 6))
    else:
        story.append(Spacer(1, 3))

doc.build(story)
