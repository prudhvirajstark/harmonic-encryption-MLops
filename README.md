# homomorphic-encryption-MLops

This repository demonstrates a simple example of securing a machine learning model using homomorphic encryption.

- The example involves training a basic machine learning model for predicting outcomes, and then integrating homomorphic encryption to make predictions on encrypted data. 

## Instructions

1. **Run the Training Script:**
   - Navigate to the `src` directory.
   - Execute `python train_ml_model.py` to train a simple machine learning model.

2. **Load the Trained Model:**
   - Load your own trained machine learning model.
   - Modify `encrypt_predict.py` accordingly, replacing the placeholder `model = None` with your loaded model.

3. **Run the Homomorphic Encryption Script:**
   - Execute `python encrypt_predict.py` to make predictions on encrypted data using homomorphic encryption.

Adjust the code as needed for your specific model and data. The folder structure and dependencies are provided for easy setup.

## Folder Structure

```plaintext
homomorphic_ml_example/
|-- src/
|   |-- train_ml_model.py
|   |-- encrypt_predict.py
|-- requirements.txt

```
