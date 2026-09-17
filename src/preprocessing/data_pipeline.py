import os
import tensorflow as tf
from tensorflow.keras import layers

def get_datasets(dataset_dir, batch_size=32, img_size=(256, 256)):
    """
    Loads images from the directory and creates training and validation datasets.
    """
    train_dir = os.path.join(dataset_dir, 'train')
    val_dir = os.path.join(dataset_dir, 'val')
    
    print("Loading training data...")
    train_ds = tf.keras.utils.image_dataset_from_directory(
        train_dir,
        seed=123,
        image_size=img_size,
        batch_size=batch_size
    )
    
    print("Loading validation data...")
    val_ds = tf.keras.utils.image_dataset_from_directory(
        val_dir,
        seed=123,
        image_size=img_size,
        batch_size=batch_size
    )
    
    # Get class names
    class_names = train_ds.class_names
    
    # -----------------------------------
    # Data Augmentation & Normalization Layers
    # -----------------------------------
    data_augmentation = tf.keras.Sequential([
        layers.RandomFlip("horizontal_and_vertical"),
        layers.RandomRotation(0.2),
        layers.RandomZoom(0.2),
    ])
    
    normalization_layer = layers.Rescaling(1./255)
    
    # -----------------------------------
    # Optimize datasets for performance
    # -----------------------------------
    AUTOTUNE = tf.data.AUTOTUNE
    
    # Apply augmentation and normalization to the training dataset
    train_ds = train_ds.map(lambda x, y: (data_augmentation(x, training=True), y), num_parallel_calls=AUTOTUNE)
    train_ds = train_ds.map(lambda x, y: (normalization_layer(x), y), num_parallel_calls=AUTOTUNE)
    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    
    # Only apply normalization to validation dataset (NO augmentation!)
    val_ds = val_ds.map(lambda x, y: (normalization_layer(x), y), num_parallel_calls=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
    
    return train_ds, val_ds, class_names

if __name__ == "__main__":
    # Test the pipeline
    # Check possible paths based on where the script is executed
    dataset_path = '../../dataset/archive (2)/PlantVillage'
    if not os.path.exists(dataset_path):
        dataset_path = 'dataset/archive (2)/PlantVillage'
        
    if os.path.exists(dataset_path):
        train_dataset, val_dataset, classes = get_datasets(dataset_path)
        print(f"Successfully loaded pipeline with {len(classes)} classes.")
        
        for image_batch, labels_batch in train_dataset.take(1):
            print(f"Batch shape: {image_batch.shape}")
            print(f"Label shape: {labels_batch.shape}")
            print(f"Max pixel value in batch: {tf.reduce_max(image_batch).numpy():.2f}")
    else:
        print(f"Dataset directory not found at {dataset_path}. Please check paths.")
