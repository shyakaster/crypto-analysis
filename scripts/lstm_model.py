import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import numpy as np

class CryptoLSTMModel:
    """
    LSTM model for cryptocurrency analysis.
    
    This model is designed for time series forecasting or regression tasks.
    """

    def __init__(self, input_shape, output_units=1, lstm_units=50, dropout_rate=0.2):
        """
        Initialize the LSTM model.

        Args:
            input_shape (tuple): Shape of the input data (timesteps, features).
            output_units (int): Number of output units. Default is 1.
            lstm_units (int): Number of units in each LSTM layer. Default is 50.
            dropout_rate (float): Dropout rate to prevent overfitting. Default is 0.2.
        """
        self.input_shape = input_shape
        self.output_units = output_units
        self.lstm_units = lstm_units
        self.dropout_rate = dropout_rate
        self.model = self.build_model()

    def build_model(self):
        """
        Build and compile the LSTM model.

        Returns:
            model (tf.keras.Model): Compiled LSTM model.
        """
        model = Sequential()
        # First LSTM layer returns sequences for stacking another LSTM
        model.add(LSTM(self.lstm_units, input_shape=self.input_shape, return_sequences=True))
        model.add(Dropout(self.dropout_rate))
        # Second LSTM layer for further sequence processing
        model.add(LSTM(self.lstm_units))
        model.add(Dropout(self.dropout_rate))
        # Dense layer for output
        model.add(Dense(self.output_units, activation='linear'))

        # Compile the model
        model.compile(optimizer='adam', loss='mse')
        return model

    def train(self, X_train, y_train, epochs=50, batch_size=32, validation_data=None):
        """
        Train the LSTM model.

        Args:
            X_train (array-like): Training input data.
            y_train (array-like): Training target data.
            epochs (int): Number of training epochs.
            batch_size (int): Batch size.
            validation_data (tuple): Tuple of (X_val, y_val) for validation.
        
        Returns:
            history: Training history.
        """
        history = self.model.fit(
            X_train, 
            y_train,
            epochs=epochs,
            batch_size=batch_size,
            validation_data=validation_data
        )
        return history

    def predict(self, X):
        """
        Generate predictions using the trained model.

        Args:
            X (array-like): Input data.
        
        Returns:
            Predictions from the model.
        """
        return self.model.predict(X)
        
if __name__ == "__main__":
    # Example usage:
    # Assuming you have prepared your time series data as X_train and y_train.

    # Define parameters
    time_steps = 60  # e.g., number of past days to look at
    features = 5     # e.g., open, high, low, close, volume
    input_shape = (time_steps, features)

    # Initialize the model
    model = CryptoLSTMModel(input_shape=input_shape, output_units=1, lstm_units=50, dropout_rate=0.2)

    # Dummy data for demonstration (replace with your data)
    X_train = np.random.rand(1000, time_steps, features)  # 1000 samples
    y_train = np.random.rand(1000, 1)

    # Train the model
    history = model.train(X_train, y_train, epochs=10, batch_size=32)

    # Generate predictions on dummy test data
    X_test = np.random.rand(10, time_steps, features)
    predictions = model.predict(X_test)
    print(predictions)