#-*-coding:utf-8-*-
import math

class Complex:

    #コンストラクタ
    def __init__(self,re,im):
        self.re = re #実部
        self.im = im #虚部
     
    #文字列化
    def __str__(self):
        if self.im >0:
            return str(self.re) + "+" + str(self.im) + "i"
        elif self.im <0:
            return str(self.re) + str(self.im) + "i"
        else:
            return str(self.re)
    
    #絶対値を求めるメソッド
    def get_abs(self):
        return self.re*self.re+self.im*self.im
    
    #偏角を求めるメソッド
    def get_arg(self):
        if self.re == 0:
            if self.im == 0:
                return null
            elif self.im > 0:
                return 3.1415926535*0.5
	    else:
	    	return -3.1415926535*0.5
        else:
            return math.atan2(self.im, self.re)

        
    # + のオーバーロード
    def __add__(self,other):
        return Complex(self.re+other.re, self.im+other.im)
    
    # - のオーバーロード
    def __sub__(self,other):
        return Complex(self.re-other.re, self.im-other.im)
    
    # * のオーバーロード
    def __mul__(self,other):
        return Complex(self.re*other.re-self.im*other.im, self.re*other.im+self.im*other.re)
#テスト
if __name__ == '__main__':
	a =Complex(1,-2) #インスタンス生成
	print a #文字列化
	print a.get_abs() #絶対値の取得
	print a.get_arg() #偏角の取得
	b = Complex(5,3)
	print a+b # +演算子
	print a-b # -演算子
	print a*b # *演算子
