import tensorflow as tf
from tensorflow.keras import layers, models

def build_model(input_shape=(256, 256, 3), num_classes=38):
    """
    Builds and compiles a Convolutional Neural Network for Leaf Disease Detection.
    
    Args:
        input_shape: The shape of the input images (height, width, channels).
        num_classes: The total number of classes (diseases).
        
    Returns:
        A compiled tf.keras Model.
    """
    model = models.Sequential()

    # 1st Convolutional Block
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(layers.MaxPooling2D((2, 2)))

    # 2nd Convolutional Block
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))

    # 3rd Convolutional Block
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    
    # 4th Convolutional Block
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))

    # Flattening Layer
    model.add(layers.Flatten())

    # Dense (Fully Connected) Classifier
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dropout(0.5)) # Dropout to prevent overfitting
    
    # Output Layer (Softmax for probabilities across 38 classes)
    model.add(layers.Dense(num_classes, activation='softmax'))

    # Compile the model
    model.compile(
        optimizer='adam',
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
        metrics=['accuracy']
    )

    return model

if __name__ == "__main__":
    # Test building the model
    print("Building model architecture...")
    model = build_model(input_shape=(256, 256, 3), num_classes=38)
    print("Model built successfully! Here is the summary:")
    model.summary()
