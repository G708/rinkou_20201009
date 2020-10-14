# rinkou_20201009
#### 課題1~4 ->  20201009_Oba.ipynb  

#### 課題5 ->  plot20201009.py  
```
python plot20201009.py file1 file2 file3
```
3つのデータを同じグラフにプロットし、３つのファイル名を結合した名前でグラフを保存する。

#### 発展課題  ->  plot_add20201009.py  
```
python plot_add20201009.py data_dir
```
指定したデータディレクトリの中のファイルから一つづつグラフを作成する。E119-H3K4me3.jaccard.csvとなっているファイルのChIP名ごとに新しいディレクトリを作成して、ChIP名ごとに作図したグラフを保存する。


実行例
python3 plot20201009.py  \
20201009_nakato_testdata/E100-H3K27ac.jaccard.csv \
20201009_nakato_testdata/E100-H3K36me3.jaccard.csv \
20201009_nakato_testdata/E100-H3K4me3.jaccard.csv

python3 plot20201009_makino.py \
20201009_nakato_testdata/E100-H3K27ac.jaccard.csv \
20201009_nakato_testdata/E100-H3K36me3.jaccard.csv \
20201009_nakato_testdata/E100-H3K4me3.jaccard.csv \
20201009_nakato_testdata/E100-H3K9me3.jaccard.csv \
--output "E100_per_control.pdf" \
--x_min -500 --x_max 2000

python3 plot_add20201009.py 20201009_nakato_testdata_partial

