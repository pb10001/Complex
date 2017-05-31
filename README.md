# Complex　
##### Pythonの複素数クラス。Python2.7.11で動作確認済
##### ※調べたらPythonで普通に複素数使えるらしい。
## インポート
##### 作業ディレクトリにComplex.pyを置く。
```
from Complex import Complex
```
## インスタンスの生成
##### 引数は2つ。
```
re = 1
im = -1
a  = Complex(re,im)
```
## 文字列
##### printを使うと(re)+(im)iの形で出力する。
```
print a
```
##### 出力は1-1i
## メソッド
##### get_abs() 絶対値を返す。
##### get_arg() 偏角をradで返す。
```
print a.get_abs()
print a.get_arg()
```
##### 出力はそれぞれ2,-0.78539...
## 演算子オーバーロード
##### +,-,*が使える。
```
b = Complex(4,2)
print a + b
print a - b
print a * b
```
##### 出力は5+1i,-3-3i,6-2i
