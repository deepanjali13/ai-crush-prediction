import tensorflow as tf
import numpy as np

# -------------------------------
# 1. Generate training data
# -------------------------------
# Features:
# [texts_first, reply_speed, emoji_usage, eye_contact, shares_personal]
# update dataset
X = np.array([
    [1, 9, 8, 9, 1],
    [1, 8, 7, 8, 1],
    [1, 7, 6, 7, 1],
    [1, 6, 6, 6, 1],
    [1, 5, 5, 5, 1],

    [0, 2, 1, 2, 0],
    [0, 3, 2, 3, 0],
    [0, 4, 2, 4, 0],
    [0, 1, 1, 1, 0],
    [0, 2, 3, 2, 0],

    [1, 8, 3, 6, 0],  # mixed signals
    [0, 6, 6, 5, 1],  # shy but interested
    [1, 4, 2, 3, 1],
    [0, 7, 7, 6, 0],
    [1, 6, 7, 5, 0],

    [1, 9, 9, 9, 1],
    [0, 5, 4, 5, 0],
    [1, 7, 8, 6, 1],
    [0, 3, 4, 3, 0],
    [1, 8, 6, 8, 1],

    [0, 4, 5, 4, 0],
    [1, 6, 4, 6, 1],
    [0, 2, 2, 3, 0],
    [1, 7, 7, 7, 1],
    [0, 5, 3, 4, 0],
])


# Labels:
# 1 = likes you
# 0 = does not
y = np.array([
    1, 1, 1, 1, 1,
    0, 0, 0, 0, 0,
    1, 1, 1, 0, 0,
    1, 0, 1, 0, 1,
    0, 1, 0, 1, 0
])


# -------------------------------
# 2. Build model
# -------------------------------
model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation="relu", input_shape=(5,)),
    tf.keras.layers.Dense(4, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])

# -------------------------------
# 3. Compile
# -------------------------------
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# -------------------------------
# 4. Train (REAL epochs)
# -------------------------------
model.fit(X, y, epochs=200, verbose=1)

# -------------------------------
# 5. Save model
# -------------------------------
model.save("crush_model.h5")

print("💖 Model trained and saved as crush_model.h5")
