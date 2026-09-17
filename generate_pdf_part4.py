from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)
        self.cell(0, 10, "REGIONAL AGRICULTURAL AI - Phase 1", border=False, align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("helvetica", "I", 12)
        self.cell(0, 10, "Part 4: Model Architecture", border=False, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDF()
pdf.add_page()
pdf.set_font("helvetica", size=11)

content = """
1. Introduction to the AI Brain
The core of our disease detection system is a Convolutional Neural Network (CNN). CNNs are the industry standard for image classification because they can automatically learn spatial hierarchies of features (like edges, textures, and specific disease spots) directly from the raw pixel data.

2. Custom CNN Architecture
We designed a sequential CNN model with the following structure:
- Convolutional Layers: These act as feature extractors. We used multiple layers with increasing filters (32, 64, 128) to detect more complex patterns as we go deeper into the network.
- Activation Functions (ReLU): After each convolution, we apply a ReLU (Rectified Linear Unit) activation to introduce non-linearity, allowing the model to learn complex, real-world data.
- MaxPooling Layers: These layers downsample the image, reducing its spatial dimensions. This drastically cuts down the computational power required and makes the model robust to small shifts in the image.
- Flattening: Once the image is reduced to a deep feature map, we flatten it into a 1D vector so it can be fed into traditional dense layers.
- Dense (Fully Connected) Layers: These layers interpret the extracted features and make the final decision.
- Output Layer: A dense layer with 38 neurons (one for each disease class) using the Softmax activation function. Softmax converts the raw outputs into probabilities that sum up to 100%.

3. Compiling the Model
Before training, the model needs to be compiled with a strategy:
- Optimizer (Adam): The algorithm that updates the network weights. Adam is fast and adapts the learning rate during training.
- Loss Function (Sparse Categorical Crossentropy): Measures how far the model's predictions are from the actual labels. Our goal is to minimize this loss.
- Metrics: We track Accuracy (the percentage of correctly classified images) to evaluate our progress.

4. Implementation
The complete architecture is coded in `src/models/cnn_model.py`. We wrote a function `build_model(input_shape, num_classes)` which generates and compiles the model dynamically.

5. Viva & Interview Questions
Q: Why do we use Convolutional layers instead of normal Dense layers for images?
A: Dense layers treat every pixel independently, losing the spatial structure of the image (like how pixels form a spot). Convolutional layers slide a filter across the image, preserving the spatial relationships and drastically reducing the number of parameters.

Q: What is the purpose of the Softmax function?
A: Softmax converts the final output scores of the network into normalized probabilities. For example, it tells us the model is 95% confident the leaf has Early Blight and 5% confident it is Healthy.

6. Implementation Status
Model Architecture: COMPLETED.
The untrained model is built and ready to be compiled and trained with our dataset.
"""

content = content.replace("—", "-").replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
content = content.encode('ascii', 'ignore').decode('ascii')

pdf.write(5, content)

pdf.output("04_Model_Architecture.pdf")
print("Part 4 PDF generated successfully: 04_Model_Architecture.pdf")
