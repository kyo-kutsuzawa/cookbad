# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        cookbad_stub
# Purpose:     mock of cookbad.
#
# Author:      kyo
#
# Created:     2016-09-03
# Copyright:   (c) kyo 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import recipi
import methods

import cv2  # 変更
import numpy as np  # 変更


def main():
    import random

    load_cookingmethods()
    load_ingredients()

    rcp = recipi.Recipi()
    rcp.ingredients = generate_ingredients(random.randint(1, 5))

    print('材料：')
    for i in rcp.ingredients:
        print(' '*4 + i.name)
    print()

    for i in range(10):
        add_cooking(rcp)

    print('レシピ：')
    for s in rcp.steps:
        print(' '*4 + s.describe)


def web():
    import random
    import copy

    load_cookingmethods()
    load_ingredients()

    rcp = recipi.Recipi()
    rcp.ingredients = generate_ingredients(random.randint(3, 10))
    materials = copy.deepcopy(rcp.ingredients)

    for i in range(random.randint(3, 5)):
        add_cooking(rcp)

    # 最後に，すべてを皿に盛る
    method = recipi.CookingMethod('moru', methods.moru_func, '皿に盛る。', 0)
    method(rcp)
    rcp.steps.append(method)

    cv2.imwrite('out.png', rcp.ingredients[0].image)

    return rcp, materials


def test():
    # Ingredientクラスの実体として，じゃがいもオブジェクトを生成する。
    # スタブなので，食材画像の代わりに文字列を加工していく
    #potato = recipi.Ingredient('じゃがいも', cv2.imread("img/cut_vegetable_potato.png", cv2.IMREAD_UNCHANGED))
    potato = recipi.Ingredient('じゃがいも', cv2.imread("cut_vegetable_onion.png", cv2.IMREAD_UNCHANGED))

    # 調理前のジャガイモを表示する
    print('調理前')
    print('名前:', potato.name)
    #print('画像:', potato.image)  # 変更
    cv2.imshow('Original',potato.image)  # 変更
    print('履歴:', potato.history)

    # CookingMethodクラスの実体として，焼くオブジェクトを生成する。
    # ここでは，上で生成したじゃがいもを3分焼1:18 2016/09/08く。
    yaku = recipi.CookingMethod('焼く', methods.yaku_func, '[food]を[minute]分焼きます。')
    yaku.ps = [potato, 3]
    yaku()                  # 焼く処理を実行する。

    # 調理後のジャガイモを表示する
    print('\n調理後')
    print('名前:', potato.name)
    #print('画像:', potato.image)  # 変更
    cv2.imshow('After',potato.image)  # 変更
    print('履歴:', potato.history)

    cv2.waitKey()  # 変更

    return


#==========================================#
#--- 以下の関数はまだ実装していないです ---#
#==========================================#

def generate_recipi(ingredients):
    rcp = Recipi()
    cooking = generate_cookings(rcp)


def generate_ingredients(n_materials):
    """レシピの材料一覧を生成する。
    """
    import random
    import copy

    if n_materials <= len(ingredients_list):
        return copy.deepcopy(random.sample(ingredients_list, n_materials))
    else:
        return copy.deepcopy(random.sample(ingredients_list, len(ingredients_list)))


def add_cooking(rcp):
    """与えられたレシピに，次の調理手順を追加する。
    """
    import random
    import copy

    method = copy.deepcopy(random.choice(cooking_methods_list))
    if method.n_ps <= len(rcp.ingredients):
        method.ps = random.sample(rcp.ingredients, method.n_ps)
        method(rcp)
        rcp.steps.append(method)


ingredients_list = []
def load_ingredients():
    """ファイルからすべての食材リストを生成する。
    """
    import csv
    #potato = recipi.Ingredient('じゃがいも', cv2.imread("img/cut_vegetable_potato.png", cv2.IMREAD_UNCHANGED))

    with open('ingredients.dat', 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            if len(row) == 2:
                ingredients_list.append(recipi.Ingredient(row[0], cv2.imread('img\\'+row[1], cv2.IMREAD_UNCHANGED)))


cooking_methods_list = []
def load_cookingmethods():
    """ファイルからすべての調理法のリストを生成する。
    """
    import csv

    with open('cooking_methods.dat', 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            if len(row) == 3:
                cooking_methods_list.append(recipi.CookingMethod('_', getattr(methods, row[1]), row[0], int(row[2])))


if __name__ == '__main__':
    main()
