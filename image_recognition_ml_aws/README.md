# Image Recognition with Machine Learning and AWS

This project demonstrates image recognition using a Convolutional Neural Network (CNN) trained on the CIFAR-10 dataset. The model is built with TensorFlow and can classify images into 10 categories.

## Features
1. Train a CNN on the CIFAR-10 dataset.
2. Predict new images using the trained model.
3. Integrate with AWS S3 for image storage.

### Instructions

1. **Training the model:**
   Run `train.py` to train the CNN model on the CIFAR-10 dataset. The model will be saved as `image_recognition_model.h5`.

2. **Predicting new images:**
   Use `predict.py` to classify a new image:
   ```bash
   python predict.py --image path_to_image
   ```

3. **AWS S3 Integration:**
   Upload images to S3 using the `aws_s3.py` script:
   ```python
   upload_to_s3('path_to_image', 'your_bucket_name')
   ```

### Dependencies
Install the required dependencies with:
```bash
pip install -r requirements.txt
```
