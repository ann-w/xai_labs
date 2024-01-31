# Move these functions to a seperate python file

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def plot_histograms(df: pd.DataFrame):
    """Plot histograms for all numeric features."""
    df.hist(bins=15, figsize=(10, 8))
    plt.suptitle("Histograms of Features")
    plt.show()


def plot_boxplots(df: pd.DataFrame):
    """Plot compact boxplots for numeric features in a 3x3 grid."""
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    n = len(numeric_columns)
    n_cols = 3
    n_rows = n // n_cols + (n % n_cols > 0)
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(10, n_rows * 3))
    fig.suptitle('Box Plots of Features', fontsize=10)

    for i, column in enumerate(numeric_columns):
        ax = axes.flatten()[i]
        sns.boxplot(x=df[column], ax=ax)
        ax.set_title(f'{column}', fontsize=10)
        ax.set_xlabel('')

    # Hide any empty subplot areas if the number of numeric columns isn't a multiple of 3
    for j in range(i + 1, n_rows * n_cols):
        axes.flatten()[j].set_visible(False)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


def plot_pairplot(df: pd.DataFrame):
    """Plot pairplot to visualize relationships between features."""
    sns.pairplot(df)
    plt.suptitle("Pairplot of Features")
    plt.show()



def plot_correlation_heatmap(df: pd.DataFrame):
    """Plot a correlation heatmap of the features."""
    plt.figure(figsize=(8, 6))
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
    plt.title("Correlation Heatmap")
    plt.show()

