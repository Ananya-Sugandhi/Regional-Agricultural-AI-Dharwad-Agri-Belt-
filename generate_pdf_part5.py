from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)
        self.cell(0, 10, "REGIONAL AGRICULTURAL AI - Phase 1", border=False, align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("helvetica", "I", 12)
        self.cell(0, 10, "Part 5: Model Training and Optimization", border=False, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDF()
pdf.add_page()
pdf.set_font("helvetica", size=11)

content = """
1. The Training Process
Training is where the actual "Machine Learning" happens. The untrained CNN from Part 4 is fed the images provided by the Data Pipeline from Part 3. The model makes a guess, checks its error using the Sparse Categorical Crossentropy loss function, and then uses the Adam optimizer to adjust its weights.

2. Epochs and Callbacks
- Epoch: One full pass of the entire training dataset through the model. We set the training to run for up to 10 epochs.
- Early Stopping: Training for too many epochs leads to overfitting. We used the EarlyStopping callback to monitor the validation loss. If the validation loss stops improving for 3 consecutive epochs, the training halts automatically, saving time and preventing overfitting.
- Model Checkpoint: We used the ModelCheckpoint callback to automatically save the model (as a .keras file) whenever it achieves a new highest validation accuracy.

3. Monitoring Performance (Loss & Accuracy)
- Training Accuracy: How well the model identifies the images it has trained on.
- Validation Accuracy: How well the model identifies unseen images (from the val folder). This is the true metric of success.
- If Training Accuracy is 99% but Validation Accuracy is 60%, the model is overfitting. Our data augmentation and dropout layers were explicitly added to minimize this gap.

4. Saving Artifacts
After training, the best model weights are saved in the `models/` folder. We also plot the loss and accuracy curves over the epochs using matplotlib and save this graph into the `results/` folder for analysis.

5. Viva & Interview Questions
Q: Why do we monitor validation accuracy instead of just training accuracy?
A: A model can easily memorize the training data (reaching 100% training accuracy). Validation accuracy proves that the model has actually learned the general patterns of the disease and can apply them to new, unseen leaves.

Q: What does the Adam optimizer do?
A: It updates the weights of the neural network iteratively based on the calculated error. It is highly popular because it dynamically adapts the learning rate for each parameter, making training faster and more stable.

Q: What is a .keras file?
A: It is a file format used by TensorFlow to save the entire model architecture, weights, and training configuration in one package, allowing us to load it later for inference without retraining.

6. Implementation Status
Model Training: COMPLETED.
The model was successfully compiled, trained using early stopping, and the optimal weights were saved to disk.
"""

content = content.replace("—", "-").replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
content = content.encode('ascii', 'ignore').decode('ascii')

pdf.write(5, content)

pdf.output("05_Model_Training.pdf")
print("Part 5 PDF generated successfully: 05_Model_Training.pdf")
