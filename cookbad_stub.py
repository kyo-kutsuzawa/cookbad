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
    method.ps = random.sample(rcp.ingredients, method.n_ps)
    method()

    rcp.steps.append(method)


ingredients_list = []
def load_ingredients():
    """ファイルからすべての食材リストを生成する。
    """
    #potato = recipi.Ingredient('じゃがいも', cv2.imread("img/cut_vegetable_potato.png", cv2.IMREAD_UNCHANGED))
    potato = recipi.Ingredient('じゃがいも', 'ジャガ')
    niku = recipi.Ingredient('牛肉', 'うし')
    tamanegi = recipi.Ingredient('玉ねぎ', '卑怯')
    ninjin = recipi.Ingredient('にんじん', 'キャロット')
    iwasi = recipi.Ingredient('鰯', 'いわいわ')

    ingredients_list.append(potato)
    ingredients_list.append(niku)
    ingredients_list.append(tamanegi)
    ingredients_list.append(ninjin)
    ingredients_list.append(iwasi)

    with open('ingredients.dat') as f:
        pass


cooking_methods_list = []
def load_cookingmethods():
    """ファイルからすべての調理法のリストを生成する。
    """
    yaku = recipi.CookingMethod('bake', methods.yaku_func, '{0}を{{}}分焼く。', 1)
    niru = recipi.CookingMethod('niru', methods.niru_func, '{0}を{{}}分煮る。', 1)
    moru = recipi.CookingMethod('moru', methods.moru_func, '{0}を皿に盛り付ける。', 1)
    maze = recipi.CookingMethod('mix', methods.mix_func, '{0}と{1}を混ぜる。', 2)

    cooking_methods_list.append(yaku)
    cooking_methods_list.append(niru)
    cooking_methods_list.append(moru)
    cooking_methods_list.append(maze)

    with open('ingredients.dat') as f:
        pass


if __name__ == '__main__':
    main()
