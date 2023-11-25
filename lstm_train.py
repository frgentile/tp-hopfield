#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    print("Hello World!")
    
    # Load and preprocess the data
    df = pd.read_csv('data/SBUX.csv', index_col='Date', parse_dates=True)

    print(df.head(5))

    plt.style.use('ggplot')
    df['Volume'].plot(label='CLOSE', title='Star Bucks Stock Volume')
    plt.show()

    # Define your LSTM model

    # Compile the model

    # Train the model

    # Evaluate the model

    # Save the model


# Call the main function if running as a standalone script
if __name__ == "__main__":
    main()

