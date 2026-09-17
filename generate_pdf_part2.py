from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)
        self.cell(0, 10, "REGIONAL AGRICULTURAL AI - Phase 1", border=False, align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("helvetica", "I", 12)
        self.cell(0, 10, "Part 2: Data Collection and Exploratory Data Analysis", border=False, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDF()
pdf.add_page()
pdf.set_font("helvetica", size=11)

content = """
1. Data Collection
We have successfully integrated the PlantVillage dataset into our workspace. The dataset contains healthy and diseased crop leaf images separated into training and validation sets. 

2. Exploratory Data Analysis (EDA)
Before training a Deep Learning model, we must understand the data we are feeding it. Through our EDA notebook, we analyzed the following:

- Class Distribution: The dataset contains 38 distinct classes of crop-disease combinations. We observed the number of images per class to identify any class imbalance. Class imbalance occurs when some diseases have significantly more images than others, which can cause the model to be biased toward the majority class.
- Image Dimensions: We verified that images have consistent dimensions (often 256x256 pixels). Knowing the input size is crucial for designing the first layer of our Convolutional Neural Network (CNN).
- Visual Inspection: We plotted random sample images to visually confirm the leaf features. Some leaves have visible spots (e.g., Early Blight), while others appear normal (Healthy).

3. Handling Class Imbalance
If we find severe class imbalance, we can handle it by:
- Data Augmentation: Artificially generating new images for minority classes by rotating, flipping, or zooming existing images.
- Class Weights: Telling the loss function to penalize misclassifications of the minority classes more heavily.

4. Setup for Preprocessing
The images are currently in standard JPG format. In the next part, we will build a data pipeline to read these images from disk, resize them, normalize pixel values (scaling from 0-255 to 0.0-1.0), and feed them to the model in batches.

5. Viva & Interview Questions
Q: What is Exploratory Data Analysis (EDA) in Deep Learning?
A: It involves analyzing the dataset visually and statistically (e.g., checking class distribution, image sizes, and data corruption) to inform the preprocessing and model design steps.

Q: What is Data Leakage?
A: Data leakage occurs when information from the validation/test set accidentally leaks into the training process, causing the model to look falsely accurate. By keeping our train and val folders strictly separated, we prevent this.

Q: Why do we normalize image pixels?
A: Neural networks converge much faster when input values are small and have a similar scale. Dividing pixel values by 255.0 scales them to the [0, 1] range.

6. Implementation Status
Data Collection and EDA: COMPLETED.
The dataset is in place, and we have explored its characteristics.
"""

content = content.replace("—", "-").replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
content = content.encode('ascii', 'ignore').decode('ascii')

pdf.write(5, content)

pdf.output("02_Data_Collection_and_EDA.pdf")
print("Part 2 PDF generated successfully: 02_Data_Collection_and_EDA.pdf")
