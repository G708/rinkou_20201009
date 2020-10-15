#!/usr/bin/env python3

import os, re, sys
import argparse
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# read tab file as a dataframe
def read_file(file_path, index_column):
    df = pd.read_csv(file_path, sep='\t', skiprows=6, index_col=index_column)

    return df

# extract label name froma file name
def label_set(file_paths):
    """
    Extract sample name from file_path.
    3 files are required.

    ex)
    20201009_nakato_sampledata/E024-Input.jaccard.csv -> E024
    """
    sample_names = []
    for i in file_paths:
        prefix = os.path.splitext(os.path.basename(i))[0]
        sample_name = re.findall("(.*).jaccard",prefix)
        print(sample_name)
        sample_names.append(sample_name[0])
        # sample_name[0]: without [0], It will be [['E024'], ['E058'], ['E096']]
    return sample_names # ['E024', 'E058', 'E096']

# plot and save function
def plot_by_col(df_list, col_name, label_list, out_name, x_min, x_max, y_min, y_max):
    """
    Plot results from 3 DataFrames.
    Save image as "Sample_names.Jaccard.pdf"
    x axis: 1-1000000, log
    y axis: 0-4
    """
    
    # color paltte
    color_palette = sns.color_palette(n_colors=len(df_list))
    
    #plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    for df, label, color in zip(df_list, label_list, color_palette):
        ax.plot(df[col_name], label=label, color=color)
    
#    ax.set_xscale("log") # x軸を対数軸にする
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.legend(loc='upper right')
    ax.set_title(col_name)

    plt.savefig(out_name)
    return fig

# calculate min and max axis value
def min_cal(df_list, col_name):
    min_list = []
    for df in range(len(df_list)):
        min_value = df[col_name].min()
        min_list.append(min_value)
    
    min_value = min_list.min()
    return min_value

def max_cal(df_list, col_name):
    max_list = []
    for df in range(len(df_list)):
        max_value = df[col_name].max()
        max_list.append(max_value)
    
    max_value = max_list.max()
    return max_value

# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="plot result of SSP files")
    parser.add_argument("input", help="file names", type=str, nargs='+')
    parser.add_argument("--col_x", help="column name of x axis value", type=str, default="Strand shift")
    parser.add_argument("--col_y", help="column name of x axis value", type=str, default="per control")
    parser.add_argument("--output", help="out put file path", type=str, default="plot.pdf")
    parser.add_argument("--x_min", help="minimun value of x axis", type=int)
    parser.add_argument("--x_max", help="maximun value of x axis", type=int)
    parser.add_argument("--y_min", help="minimun value of y axis", type=int)
    parser.add_argument("--y_max", help="maximun value of y axis", type=int)
    args = parser.parse_args()

    file_list = args.input
    col_x_name = args.col_x
    col_y_name = args.col_y
    output_path = args.output
    x_min_value = args.x_min
    x_max_value = args.x_max
    y_min_value = args.y_min
    y_max_value = args.y_max
    
    # read dataframe
    df_list = []
    for file in file_list:
        df = read_file(file, col_x_name)
        df_list.append(df)
    print("sample names: {}".format(file_list))
    
    # min and max value
    if (x_min_value == ''):
        x_min_value = min_cal(df_list, col_x_name)

    if (x_max_value == ''):
        x_max_value = max_cal(df_list, col_x_name)  

    if (y_min_value == ''):
        y_min_value = min_cal(df_list, col_y_name)
    
    if (y_max_value == ''):
        y_max_value = max_cal(df_list, col_y_name)        
    
    # label
    label_list = label_set(file_list)
    
    # plot
    plot_by_col(df_list, col_y_name, label_list, output_path, x_min_value, x_max_value, y_min_value , y_max_value )

    
    
    
