from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)
        self.cell(0, 10, "REGIONAL AGRICULTURAL AI - Phase 1", border=False, align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("helvetica", "I", 12)
        self.cell(0, 10, "Part 1: Environment and Project Setup", border=False, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDF()
pdf.add_page()
pdf.set_font("helvetica", size=11)

content = """
1. Project Introduction
The Regional Agricultural AI project aims to build an AI-based crop leaf disease detection system that analyzes a crop leaf image and identifies the disease with a confidence score.

Phase 1 focuses on the Core Machine Learning Disease Prediction System, isolating the model development from web applications, APIs, and deployments (which will follow in later phases).

2. Part Objective: Environment and Project Setup
The goal of this part is to create a robust, reproducible Machine Learning project environment. A clean environment prevents dependency conflicts, ensures that code runs smoothly on different machines, and creates a logical structure for all scripts and data.

3. Project Setup Concepts
- Python Version: We are using Python 3, which is the standard for ML development due to its rich ecosystem.
- Virtual Environment (venv): An isolated environment that contains its own Python executable and installed packages. It prevents global packages from interfering with project-specific dependencies.
- pip: Python's package installer, used to download and install libraries from the Python Package Index (PyPI).
- requirements.txt: A file listing all the packages required to run the project. This makes the project reproducible; anyone can run `pip install -r requirements.txt` to replicate the environment.
- Jupyter Notebook: An interactive computational environment used for data exploration, visualization, and step-by-step experimentation.
- VS Code: A powerful source-code editor where the final Python scripts will be developed.
- GPU vs CPU / CUDA: Deep learning models (like CNNs) train much faster on a GPU. CUDA is a parallel computing platform by NVIDIA that enables TensorFlow/Keras to leverage the GPU for rapid matrix operations. If no GPU is available, the CPU is used (which is much slower).

4. Project Architecture
The workspace has been organized as follows:
- regional-agricultural-ai/
  - dataset/            (Original and processed datasets)
  - notebooks/          (Jupyter notebooks for experimentation)
  - src/                (Source code)
    - data/           (Scripts for data ingestion)
    - preprocessing/  (Scripts for image cleaning and transformation)
    - models/         (CNN and Transfer Learning model architectures)
    - training/       (Training and evaluation loops)
    - evaluation/     (Metrics and visualization scripts)
    - inference/      (Inference pipeline to test new images)
  - models/             (Saved trained models .keras)
  - results/            (Results from training logs, charts)
  - reports/            (Generated PDFs and documentation)
  - requirements.txt    (Project dependencies)
  - README.md           (Instructions on how to run)

5. Technologies & Packages
The following packages were carefully selected for Phase 1:

- numpy: Fundamental package for scientific computing. Required for multi-dimensional arrays (tensors). Example: Converting image pixels to an array.
- pandas: Data manipulation and analysis tool. Required for handling tabular data (e.g., dataset statistics, evaluation tables).
- matplotlib & seaborn: Plotting libraries. Required for generating graphs (e.g., loss curves, class distribution charts).
- opencv-python: Open Source Computer Vision Library. Required for fast image reading, resizing, and manipulation.
- Pillow: Python Imaging Library. Required as a secondary image processing tool, often used seamlessly with Keras.
- scikit-learn: Machine learning library. Required for creating train/validation/test splits, calculating metrics (confusion matrix, F1-score), and data preprocessing.
- tensorflow & keras: The core deep learning framework. Required for building, training, and exporting Convolutional Neural Networks (CNNs).
- tqdm: A smart progress meter. Required for showing progress bars during loops (e.g., processing thousands of images).
- jupyter & notebook: Required to run .ipynb files for exploratory data analysis and model prototyping.
- fpdf2: Required to generate PDF documentation dynamically through Python scripts.

6. Code Explanation (Setup)
Command: `python -m venv venv`
Explanation: Creates a folder named 'venv' containing the isolated Python environment.
Command (Windows): `.\\venv\\Scripts\\activate`
Explanation: Activates the environment so that subsequent commands use the isolated pip and Python.
Command: `pip install -r requirements.txt`
Explanation: Installs all listed dependencies automatically.

7. Viva & Interview Questions
Q: Why do we use a virtual environment?
A: To isolate project dependencies from the global system, ensuring reproducibility and preventing version conflicts between different projects.
Q: What happens if you don't use requirements.txt?
A: Another developer (or the examiner) won't know which packages and versions to install, potentially causing the code to crash due to missing or updated libraries.
Q: Why separate data processing code from model training code?
A: It makes the codebase modular, easier to test, debug, and maintain. For example, if we change the image size, we only update the preprocessing script without touching the model script.

8. Implementation Status
Environment and Project Setup: COMPLETED.
The dependencies are installed, folders are created, and this document proves the successful execution of Part 1.
"""

# Replace unicode dashes with standard hyphens and correct newlines
content = content.replace("—", "-").replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
content = content.encode('ascii', 'ignore').decode('ascii')

for line in content.split("\n"):
    pdf.multi_cell(0, 5, line)

pdf.output("01_Environment_and_Project_Setup.pdf")
