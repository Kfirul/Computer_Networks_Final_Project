#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[ ]:


# create data frame
def create_df(path):
    df= pd.read_csv(path)
    df = df.drop(['No.'] , axis=1)
    df['Delay'] = pd.to_numeric(df['Time']).diff()
    return df


# In[2]:


#  A function that generates a graph displaying packets by their times compared to their respective lengths.
def create_packet_length_bar_graph(data, xlabel, ylabel, title, color='black'):
    # Convert 'Time' column to numeric (seconds)
    data['Time'] = pd.to_numeric(data['Time'])

    # Extract the "Length" column and calculate the Ethernet payload lengths
    data_length = data['Length'] 

    # Create the bar graph
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    plt.bar(data['Time'], data_length, color=color)  # Use 'Time' column for x-axis
    plt.xlabel(xlabel)  # Set x-axis label
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()


# In[3]:


#  A function that generates a graph displaying packets sent at Groups withe threshold compared to their respective lengths.
def create_group_packet_bar_graph(data, xlabel, ylabel, title,threshold):

    # Group the data by delay intervals and sum the packet lengths
    data_grouped = data.groupby(data['Delay'].gt(threshold).cumsum())['Length'].sum()

    # Create the bar graph
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    data_grouped.plot(kind='bar', x=data_grouped.index, y=data_grouped.values)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()


# In[4]:


# Create pdf graph
def generate_and_plot_pdf_with_exponential_fit(df, bins=10):

    df_cleaned = df.dropna(subset=['Delay'])
    
    counts, bin_edges = np.histogram(df_cleaned['Delay'], bins=bins, density=True)
    
    # Convert counts to probabilities
    pdf = counts / sum(counts)
    
    plt.figure(figsize=(10, 6))
    
    # Plotting the outline of the histogram using plt.step
    plt.step(bin_edges[:-1], pdf, where='post', color='blue', lw=2, label='PDF')
    
    # Estimate lambda (rate parameter) from the data
    lambd = 1. / np.mean(df['Delay'])
    
    # Compute the bin width from the first two bin edges
    bin_width = bin_edges[1] - bin_edges[0]
    
    # Adjust the scale_factor with respect to bin_width
    scale_factor = max(pdf) / (lambd * np.exp(-lambd * bin_edges[np.argmax(pdf)]))
    
    # Create x values for the fitted exponential curve
    x = np.linspace(0, max(bin_edges), 500)
    
    # Calculate exponential distribution values using the estimated lambda
    y = scale_factor * lambd * np.exp(-lambd * x)
    
    plt.plot(x, y, color='red', lw=2, label='Fitted Exponential Distribution')
    
    plt.xlabel('Inter-Arrival Time')
    plt.ylabel('Density')
    plt.title('PDF of Inter-Arrival Time and Fitted Exponential Distribution')
    plt.legend()
    plt.grid(True)
    
    plt.show()


# In[5]:


# create ccdf graph
def plot_ccdf(dataframes, labels, big_threshold=0.7):
    fig, ax = plt.subplots(figsize=(10, 6))
    for df, label in zip(dataframes, labels):
        # Sort and normalize the data
        sorted_vals = np.sort(df['Length'])
        normalized_vals = sorted_vals / max(sorted_vals)

        # Compute CDF and then CCDF
        cdf = np.arange(1, len(sorted_vals) + 1) / len(sorted_vals)
        ccdf = 1 - cdf
        
        plt.plot(normalized_vals, ccdf, label=label)
    
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('Normalized Message Sizes')
    plt.ylabel('CCDF')
    plt.title('CCDF of Packets Size Distribution')
    plt.legend(loc="lower left")
    plt.show()
    return fig

