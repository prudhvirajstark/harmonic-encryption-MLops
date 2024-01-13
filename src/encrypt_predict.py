from seal import EncryptionParameters, KeyGenerator, Encryptor, Decryptor, Evaluator, Ciphertext
import numpy as np
from sklearn.metrics import accuracy_score

model = None  # Load your trained model here

params = EncryptionParameters(scheme_type=2)
params.set_poly_modulus("1x^4096 + 1")
params.set_coeff_modulus([2 ** i for i in range(40, 62, 4)])
params.set_plain_modulus(1 << 8)

keygen = KeyGenerator(params)
public_key = keygen.public_key()
secret_key = keygen.secret_key()

encryptor = Encryptor(params, public_key)
decryptor = Decryptor(params, secret_key)
evaluator = Evaluator(params)


y_pred_encrypted = [Ciphertext() for _ in range(len(X_test_encrypted))]
for i in range(len(X_test_encrypted)):
    model_input = X_test_encrypted[i]
    evaluator.multiply_plain(model_input, model.coef_[0], y_pred_encrypted[i])

y_pred_decrypted = np.array([decryptor.decrypt(y) for y in y_pred_encrypted])
y_pred_final = (y_pred_decrypted > 0.5).astype(int)

accuracy_homomorphic = accuracy_score(y_test, y_pred_final)
print(f"Accuracy of homomorphically encrypted model: {accuracy_homomorphic}")
