from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)
        self.cell(0, 10, "REGIONAL AGRICULTURAL AI - Phase 1", border=False, align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("helvetica", "I", 12)
        self.cell(0, 10, "Part 3: Data Preprocessing and Augmentation", border=False, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDF()
pdf.add_page()
pdf.set_font("helvetica", size=11)

content = """
1. Data Preprocessing Pipeline
Before feeding the images to a Neural Network, we must transform raw image files into numerical tensors that the model can process efficiently. We built a data pipeline to automate this.

2. Key Preprocessing Steps
- Resizing: Images come in different sizes, but a Neural Network requires fixed-size inputs. We resize all images to 256x256 pixels.
- Batching: Instead of loading thousands of images into RAM at once (which would crash the system), we load them in batches (e.g., 32 images at a time).
- Normalization: Image pixel values range from 0 to 255. We scale them down to the range [0.0, 1.0] by dividing by 255. This helps the network learn faster and more stably.

3. Data Augmentation
To prevent the model from overfitting (memorizing the exact training images) and to handle class imbalance, we applied Data Augmentation. 
Augmentation artificially creates new training examples by applying random transformations to existing images:
- Random Flip: Flips the leaf horizontally or vertically.
- Random Rotation: Rotates the leaf slightly.
- Random Zoom: Zooms in on different parts of the leaf.
Because of these transformations, the model rarely sees the exact same image twice during training, which forces it to learn the actual patterns of the disease rather than the background.

4. Prefetching and Caching
To maximize GPU/CPU utilization, we use `AUTOTUNE` to prefetch batches. While the model is training on Batch 1, the CPU is already loading and preprocessing Batch 2 in the background. This drastically reduces training time.

5. Code Implementation
The logic for creating the training and validation pipelines was written in `src/preprocessing/data_pipeline.py` using TensorFlow's image utilities.

6. Viva & Interview Questions
Q: Why do we apply Data Augmentation only to the training set and not the validation set?
A: Augmentation is used to teach the model to generalize better. The validation set is meant to test the model on real, unaltered images, so we never distort validation data.

Q: What is overfitting and how does augmentation help?
A: Overfitting happens when a model performs exceptionally well on training data but poorly on unseen data. Augmentation adds noise and variation, making the training data harder to memorize, thus improving generalization.

Q: Why do we process data in batches instead of all at once?
A: To manage memory efficiently. A dataset of 50,000 images would consume too much RAM, but processing 32 images at a time requires very little memory.

7. Implementation Status
Data Preprocessing and Augmentation: COMPLETED.
The input pipeline is ready to feed tensors into our future deep learning model.
"""

content = content.replace("—", "-").replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
content = content.encode('ascii', 'ignore').decode('ascii')

pdf.write(5, content)

pdf.output("03_Data_Preprocessing_and_Augmentation.pdf")
print("Part 3 PDF generated successfully: 03_Data_Preprocessing_and_Augmentation.pdf")
