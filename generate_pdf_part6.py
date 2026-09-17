from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)
        self.cell(0, 10, "REGIONAL AGRICULTURAL AI - Phase 1", border=False, align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("helvetica", "I", 12)
        self.cell(0, 10, "Part 6: Model Evaluation and Inference", border=False, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDF()
pdf.add_page()
pdf.set_font("helvetica", size=11)

content = """
1. Introduction to Model Evaluation
After training the CNN model, we must rigorously evaluate its performance on a completely separate dataset that it has never seen before: the test set. This ensures that the model generalizes well and is ready for real-world agricultural use.

2. Evaluation Metrics
We use several key metrics to measure the model's success:
- Test Accuracy: The overall percentage of correctly classified leaves in the test set.
- Precision: Out of all the leaves the model predicted as a specific disease (e.g., Apple Scab), how many were actually that disease. (Minimizes false positives).
- Recall: Out of all the actual leaves with a specific disease, how many did the model successfully find. (Minimizes false negatives).
- F1-Score: The harmonic mean of Precision and Recall, providing a single metric that balances both.
- Confusion Matrix: A table showing exactly where the model gets confused (e.g., misclassifying Early Blight as Late Blight).

3. Inference (Making Predictions)
Inference is the process of using the trained, saved model (.keras file) to predict the disease of a brand new, single image.
The pipeline for inference:
a. Load the saved model.
b. Load the new image and resize it to 256x256 pixels (the size the model expects).
c. Convert the image to a numpy array and expand dimensions (to simulate a batch of 1).
d. Pass the image to the model to get the probability scores.
e. Find the class with the highest probability using `np.argmax()`.

4. Real-world Application
This inference pipeline is the exact logic that will be connected to the web interface or mobile app in Phase 2. A farmer uploads a photo, the image goes through the inference pipeline, and the predicted disease name is returned to the screen.

5. Viva & Interview Questions
Q: Why do we need Precision and Recall if we already have Accuracy?
A: In cases of imbalanced datasets (e.g., 90% healthy leaves, 10% diseased), a model could just guess "Healthy" every time and get 90% accuracy. Precision and Recall give a true picture of how well it detects the rare classes.

Q: What does a Confusion Matrix show?
A: It shows the true labels vs the predicted labels. It helps us identify if our model is consistently confusing two visually similar diseases.

Q: What preprocessing is required during Inference?
A: The exact same preprocessing used during training (resizing to 256x256, scaling pixels to 0-1 if applicable). If this doesn't match, the model will output garbage predictions.

6. Implementation Status
Model Evaluation: COMPLETED.
The evaluation script calculates the metrics and generates the confusion matrix, and the inference script successfully predicts the disease of single images.
"""

content = content.replace("—", "-").replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
content = content.encode('ascii', 'ignore').decode('ascii')

pdf.write(5, content)

pdf.output("06_Model_Evaluation.pdf")
print("Part 6 PDF generated successfully: 06_Model_Evaluation.pdf")
