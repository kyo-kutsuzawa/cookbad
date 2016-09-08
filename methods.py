#!/usr/bin/env python
# -*- coding:utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        methods
# Purpose:     調理処理や，画像処理をまとめる
#
# Author:      kyo
#
# Created:     2016-09-04
# Copyright:   (c) kyo 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import cv2  # 変更
import numpy as np  # 変更

#========================================================================#
#--- 以下，「[food]を[minute]分焼く」という調理に対応する処理のモック ---#
#========================================================================#

# 調理処理の例
def yaku_func(self):
    """「焼く」に対応する調理処理のモック。
    食材画像への加工処理を呼び出したり，エトセトラする。
    ここでは ps = [焼く食材(Ingredient)，焼く時間(int)] とする。
    """
    food = self.ps[0]
    minute = self.ps[1]

    food.image = yaku_img(food.image, minute)   # 食材画像を焼かれた画像に更新
    food.name = '焼き' + food.name              # 'じゃがいも' → '焼きじゃがいも'
    food.history.append(self.name)              # 食材の調理履歴に'焼く'を追加する


# 画像処理関数の例
# 画像処理担当の人は，ここの処理を好きなライブラリで作ってもらいたいです。
def yaku_img(img, minute):
    # 変更
    """「焼く」に対応する画像処理のモック。
    基本的には，引数に画像をとって，加工処理した新しい画像を返す構造。
    今回は，第2引数に調理時間をとる。
    """
    # 処理……
    gamma = 1.0 / minute

    lookUpTable = np.zeros((256, 1), dtype = 'uint8')

    for i in range(256):
        lookUpTable[i][0] = 255 * pow(float(i) / 255, 1.0 / gamma)

    new_img = cv2.LUT(img, lookUpTable)

    #new_img = '{}_minutes baked '.format(minute) + img # スタブなので，画像の代わりに文字列を加工していく
    return new_img

#========================================================================#
#---          「[food]を[minute]分焼く」の処理例ここまで              ---#
#========================================================================#


if __name__ == '__main__':
    pass
