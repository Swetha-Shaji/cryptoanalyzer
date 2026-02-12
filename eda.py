"""
EDA (Exploratory Data Analysis) Module
Handles visualization of historical price data
"""

import matplotlib.pyplot as plt
import pandas as pd


def plot_historical_price(df_original, save_path=None):
    """
    Plot historical Bitcoin closing price over time.
    
    Args:
        df_original (pd.DataFrame): Original dataframe with 'Date' and 'Close' columns
        save_path (str): Path to save the plot image
    
    Returns:
        matplotlib.figure.Figure: Matplotlib figure object
    """
    fig, ax = plt.subplots(figsize=(14, 6))
    
    ax.plot(df_original['Date'], df_original['Close'], linewidth=1.5, color='#1f77b4')
    ax.fill_between(df_original['Date'], df_original['Close'], alpha=0.3, color='#1f77b4')
    
    ax.set_title('Bitcoin Historical Price (2010-2024)', fontsize=16, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Price (USD)', fontsize=12)
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    if save_path:
        fig.savefig(save_path, dpi=100, bbox_inches='tight')
        print(f"Historical plot saved to {save_path}")
    
    return fig


def plot_price_statistics(df_original, save_path=None):
    """
    Create a subplot showing price statistics and distribution.
    
    Args:
        df_original (pd.DataFrame): Original dataframe with price columns
        save_path (str): Path to save the plot image
    
    Returns:
        matplotlib.figure.Figure: Matplotlib figure object
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Price over time
    axes[0, 0].plot(df_original['Date'], df_original['Close'], linewidth=1, color='#1f77b4')
    axes[0, 0].set_title('Close Price Over Time', fontweight='bold')
    axes[0, 0].set_xlabel('Date')
    axes[0, 0].set_ylabel('Price (USD)')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Price distribution
    axes[0, 1].hist(df_original['Close'], bins=50, color='#ff7f0e', edgecolor='black', alpha=0.7)
    axes[0, 1].set_title('Price Distribution', fontweight='bold')
    axes[0, 1].set_xlabel('Price (USD)')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].grid(True, alpha=0.3, axis='y')
    
    # Daily returns
    daily_returns = df_original['Close'].pct_change() * 100
    axes[1, 0].plot(df_original['Date'], daily_returns, linewidth=0.5, color='#2ca02c')
    axes[1, 0].set_title('Daily Returns (%)', fontweight='bold')
    axes[1, 0].set_xlabel('Date')
    axes[1, 0].set_ylabel('Return (%)')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Volume
    axes[1, 1].bar(df_original['Date'], df_original['Volume'], color='#d62728', alpha=0.6, width=1)
    axes[1, 1].set_title('Trading Volume', fontweight='bold')
    axes[1, 1].set_xlabel('Date')
    axes[1, 1].set_ylabel('Volume')
    axes[1, 1].grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    
    if save_path:
        fig.savefig(save_path, dpi=100, bbox_inches='tight')
        print(f"Statistics plot saved to {save_path}")
    
    return fig


def print_data_summary(df_original):
    """
    Print summary statistics of the dataset.
    
    Args:
        df_original (pd.DataFrame): Original dataframe with price data
    """
    print("=" * 60)
    print("DATA SUMMARY")
    print("=" * 60)
    print(f"Date range: {df_original['Date'].min()} to {df_original['Date'].max()}")
    print(f"Total trading days: {len(df_original)}")
    print(f"\nClose Price Statistics:")
    print(f"  Min: ${df_original['Close'].min():.2f}")
    print(f"  Max: ${df_original['Close'].max():.2f}")
    print(f"  Mean: ${df_original['Close'].mean():.2f}")
    print(f"  Median: ${df_original['Close'].median():.2f}")
    print(f"  Std Dev: ${df_original['Close'].std():.2f}")
    print(f"\nVolume Statistics:")
    print(f"  Mean: {df_original['Volume'].mean():.0f}")
    print(f"  Max: {df_original['Volume'].max():.0f}")
    print("=" * 60)
    print()
