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

import cv2
import numpy as np
import recipi


#========================================================================#
#--- 以下，「[food]を[minute]分焼く」という調理に対応する処理のモック ---#
#========================================================================#

# 調理処理の例
def yaku_func(self, food):
    """「焼く」に対応する調理処理のモック。
    食材画像への加工処理を呼び出したり，エトセトラする。
    ここでは ps = [焼く食材(Ingredient)，焼く時間(int)] とする。
    """
    import random
    minute = random.randint(5, 60)

    food.image = yaku_img(food.image, minute)   # 食材画像を焼かれた画像に更新
    food.name = '焼き' + food.name              # 'じゃがいも' → '焼きじゃがいも'
    food.history.append(self.name)              # 食材の調理履歴に'焼く'を追加する
    self.describe = self.describe.format(minute)


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
    if gamma > 1:
        gamma = 1

    lookUpTable = np.zeros((256, 1), dtype = 'uint8')

    for i in range(256):
        lookUpTable[i][0] = 255 * pow(float(i) / 255, 1.0 / gamma)

    new_img = cv2.LUT(img, lookUpTable)

    #new_img = '{}_minutes baked '.format(minute) + img # スタブなので，画像の代わりに文字列を加工していく
    return new_img

#========================================================================#
#---          「[food]を[minute]分焼く」の処理例ここまで              ---#
#========================================================================#


def niru_func(self, food):
    minute = 1

    food.image = niru_img(food.image, minute)
    food.name = '煮' + food.name
    food.history.append(self.name)
    self.describe = self.describe.format(minute)

def niru_img(img, minute):
    gamma = 2.0 / minute
    if gamma > 1:
        gamma = 1
    if gamma <= 1:
        gamma = 0.1

    lookUpTable = np.zeros((256, 1), dtype = 'uint8')

    for i in range(256):
        lookUpTable[i][0] = 255 * pow(float(i) / 255, 1.0 / gamma)

    new_img = cv2.LUT(img, lookUpTable)

    return new_img


def moru_func(self, food):
    food.image = moru_img(food.image, 3)
    food.name = food.name + '盛り'
    food.history.append(self.name)

def moru_img(img, minute):
    # imgはアルファチャンネル付きで
    src = img
    dst = cv2.imread('osara_1.png')
    expansion = 0.9 # 拡大率 任意に変えてください
    
    dh, dw = dst.shape[:2]
    h, w = src.shape[:2]
    if dw / dh < w / h:
        rh = int( dw * h / w * expansion )
        rw = int( dw * expansion )
    if dw / dh >= w / h:
        rh = int( dh * expansion )
        rw = int( dh * w / h * expansion )
    src = cv2.resize(src, ( rw, rh ))
    # なんとかしてお皿の画像サイズに収まるようにimgを拡大or縮小する + そのままだと大きすぎて皿に収まらないので拡大率を指定して縮小する
    
    mask = src[:,:,3]
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    mask = mask / 255.0
    
    src = src[:,:,:3]
    
    x = int( ( dw - rw ) / 2.0 )
    y = int( ( dh - rh ) / 2.0 )
    
    #print("dw : " + str(dw))
    #print("dh : " + str(dh))
    #print("w : " + str(w))
    #print("h : " + str(h))
    #print("rw : " + str(rw))
    #print("rh : " + str(rh))
    #print("x : " + str(x))
    #print("y : " + str(y))
    
    dst[y:y+rh:, x:x+rw] = ( 1.0 - mask ) * dst[y:y+rh:, x:x+rw]  # 透過率に応じて元の画像を暗くする。
    dst[y:y+rh:, x:x+rw] = src * mask + dst[y:y+rh:, x:x+rw]  # 貼り付ける方の画像に透過率をかけて加算。
    # センタリングをする
    
    return dst


def mix_func(self, food1, food2):
    newfood = recipi.Ingredient()

    newfood.image = mix_img(food1.image, food2.image)
    newfood.name = food1.name + food2.name
    newfood.history.append(self.name)
    cv2.imshow('New', newfood.image)

def mix_img(img1, img2):
    width = max(img1.shape[0], img2.shape[0])
    height = max(img1.shape[1], img2.shape[1])
    new_img = np.array([[[0,0,0,0]]*height]*width, dtype='uint8')

    mask = img2[:,:,3]  # アルファチャンネルだけ抜き出す。
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGRA)  # 4色分に増やす。
    mask = mask / 255.0  # 0-255だと使い勝手が悪いので、0.0-1.0に変更。

    new_img[0:img1.shape[0], 0:img1.shape[1]] = img1

    new_img[0:img2.shape[0], 0:img2.shape[1]] = (new_img[0:img2.shape[0], 0:img2.shape[1]] * (1 - mask)).astype('uint8')  # 透過率に応じて元の画像を暗くする。
    new_img[0:img2.shape[0], 0:img2.shape[1]] += (img2 * mask).astype('uint8')  # 貼り付ける方の画像に透過率をかけて加算。

    cv2.imwrite('out.png', new_img)
    return new_img


def test():
    onion = recipi.Ingredient('玉ねぎ', cv2.imread("./../img/cut_vegetable_onion.png", cv2.IMREAD_UNCHANGED))
    carrot = recipi.Ingredient('にんじん', cv2.imread("./../img/ninjin_carrot.png", cv2.IMREAD_UNCHANGED))
    #onion = recipi.Ingredient('玉ねぎ', cv2.imread("./../img/food_lettuce.png", cv2.IMREAD_UNCHANGED))
    #carrot = recipi.Ingredient('にんじん', cv2.imread("./../img/vegetable_tomato.png", cv2.IMREAD_UNCHANGED))

    # 調理前のジャガイモを表示する
    print('調理前')
    print('-'*10)
    print('名前:', onion.name)
    #cv2.imshow('Original', onion.image)
    print('履歴:', onion.history)
    print('-'*10)
    print('名前:', carrot.name)
    #cv2.imshow('Original', carrot.image)
    print('履歴:', carrot.history)
    print('-'*10)

    mix = recipi.CookingMethod('混ぜる', mix_func, '{0}と{1}を混ぜます。', 2)
    mix.ps = [onion, carrot]
    mix()

    # 調理後のジャガイモを表示する
    print('\n調理後')
    print('-'*10)
    print('名前:', onion.name)
    #cv2.imshow('After',onion.image)
    print('履歴:', onion.history)
    print('-'*10)

    cv2.waitKey()  # 変更


if __name__ == '__main__':
    test()
