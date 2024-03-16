import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import matplotlib.pyplot as plt

# Carga el modelo preentrenado
model = load_model("keras_Model.h5", compile=False)

# Carga las etiquetas de las clases
class_names = [line.strip() for line in open("labels.txt", "r")]

# Función para reconocer una imagen
def reconocer_imagen(imagen_path):
    # Carga la imagen y la convierte a RGB
    img = image.load_img(imagen_path, target_size=(224, 224), grayscale=False, color_mode="rgb")
    # Convierte la imagen en un array de numpy
    x = image.img_to_array(img)
    # Agrega un eje adicional al principio de la forma del array
    x = np.expand_dims(x, axis=0)
    # Normaliza los valores de la imagen
    x = x / 255.0
    # Realiza la predicción con el modelo
    preds = model.predict(x)
    # Encuentra el índice de la clase con la mayor probabilidad
    index = np.argmax(preds)
    # Obtiene el nombre de la clase y la probabilidad asociada
    class_name = class_names[index]
    confidence_score = preds[0][index]
    # Imprime el resultado
    print(f"La imagen pertenece a la clase '{class_name}' con una confianza de {confidence_score * 100:.2f}%.")
    # Muestra la imagen con una etiqueta en la parte inferior
    plt.imshow(img)
    plt.xlabel(f"{class_name} ({confidence_score * 100:.2f}%)")
    plt.show()

# Ejemplo de uso
reconocer_imagen("imagen.jpg")