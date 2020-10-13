#!/usr/bin/env python3

import os, re, sys
import argparse
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def read_file(file_path):
    df = pd.read_csv(file_path, sep='\t', skiprows=6, index_col='Strand shift')

    return df

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

def plot_by_col(df1,df2,df3,col_name,label):
    """
    Plot results from 3 DataFrames.
    Save image as "Sample_names.Jaccard.pdf"
    x axis: 0-1000000, log
    y axis: 0-4
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(df1[col_name], label=label[0], color="red")
    ax.plot(df2[col_name], label=label[1], color="blue")
    ax.plot(df3[col_name], label=label[2], color="green")
    ax.set_xscale("log") # x軸を対数軸にする
    ax.set_xlim(0,1000000)
    ax.set_ylim(0,4)
    ax.legend(loc='upper right')
    ax.set_title(col_name)
    save_name = "_".join(label) +".Jaccard.pdf"
    plt.savefig(save_name)
    return fig

# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="plot result of 3 SSP files")
    parser.add_argument("file1", help="1st file path", type=str)
    parser.add_argument("file2", help="2nd file path", type=str)
    parser.add_argument("file3", help="3rd file path", type=str)


    args = parser.parse_args()

    filename1 = args.file1
    filename2 = args.file2
    filename3 = args.file3

    label_list = label_set([filename1,filename2,filename3])

    df1 = read_file(filename1)
    df2 = read_file(filename2)
    df3 = read_file(filename3)
    print("sample names: {}".format(label_list))
    plot_by_col(df1,df2,df3,"per control",label_list)
