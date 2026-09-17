import os
import sys

# Add the project root to sys.path so we can import from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import tensorflow as tf

from src.preprocessing.data_pipeline import get_datasets
from src.models.cnn_model import build_model
import matplotlib.pyplot as plt

def plot_history(history, save_path="results/training_history.png"):
    """Saves the training accuracy and loss curves."""
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(len(acc))
    plt.figure(figsize=(12, 5))
    
    # Accuracy plot
    plt.subplot(1, 2, 1)
    plt.plot(epochs, acc, 'b', label='Training Accuracy')
    plt.plot(epochs, val_acc, 'r', label='Validation Accuracy')
    plt.title('Training and Validation Accuracy')
    plt.legend()
    
    # Loss plot
    plt.subplot(1, 2, 2)
    plt.plot(epochs, loss, 'b', label='Training Loss')
    plt.plot(epochs, val_loss, 'r', label='Validation Loss')
    plt.title('Training and Validation Loss')
    plt.legend()
    
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    print(f"Training history chart saved to {save_path}")

def main():
    dataset_path = 'dataset/archive (2)/PlantVillage'
    if not os.path.exists(dataset_path):
        print(f"Dataset not found at {dataset_path}. Please check your paths.")
        return

    # 1. Load Data Pipeline
    train_dataset, val_dataset, classes = get_datasets(dataset_path, batch_size=8)  # Reduced batch size to prevent OOM
    print(f"Detected {len(classes)} classes.")

    # 2. Build Model
    model = build_model(input_shape=(256, 256, 3), num_classes=len(classes))
    
    # 3. Define Callbacks
    # EarlyStopping: Stop training if validation loss doesn't improve for 3 epochs
    early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
    
    # ModelCheckpoint: Save the best model dynamically
    os.makedirs('models', exist_ok=True)
    checkpoint = tf.keras.callbacks.ModelCheckpoint('models/best_cnn_model.keras', monitor='val_accuracy', save_best_only=True)

    # 4. Train the Model
    print("Starting Model Training...")
    history = model.fit(
        train_dataset,
        validation_data=val_dataset,
        epochs=10, # Kept relatively small for demonstration
        callbacks=[early_stop, checkpoint]
    )

    # 5. Evaluate and Save Results
    print("Training complete! Generating charts...")
    plot_history(history)
    
    # Save the final model just in case
    model.save('models/final_cnn_model.keras')
    print("Models saved successfully in the /models directory.")

if __name__ == "__main__":
    main()
