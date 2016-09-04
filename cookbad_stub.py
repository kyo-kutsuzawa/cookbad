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

def main():
    # Ingredientクラスの実体として，じゃがいもオブジェクトを生成する。
    # スタブなので，食材画像の代わりに文字列を加工していく
    potato = recipi.Ingredient('じゃがいも', 'potato_image')

    # 調理前のジャガイモを表示する
    print('調理前')
    print('名前:', potato.name)
    print('画像:', potato.image)
    print('履歴:', potato.history)

    # CookingMethodクラスの実体として，焼くオブジェクトを生成する。
    # ここでは，上で生成したじゃがいもを3分焼く。
    yaku = recipi.CookingMethod('焼く', methods.yaku_func, '[food]を[minute]分焼きます。')
    yaku.ps = [potato, 3]
    yaku()                  # 焼く処理を実行する。

    # 調理後のジャガイモを表示する
    print('\n調理後')
    print('名前:', potato.name)
    print('画像:', potato.image)
    print('履歴:', potato.history)

    return


#==========================================#
#--- 以下の関数はまだ実装していないです ---#
#==========================================#

def generate_recipi(ingredients):
    recipi = Recipi()
    cooking = generate_cookings(recipi)


def generate_ingredients():
    """レシピの材料一覧を生成する。
    """
    pass


def add_cooking(recipi, foods):
    """与えられたレシピに，次の調理手順を追加する。
    """
    pass


def load_ingredients():
    """ファイルからすべての食材リストを生成する。
    """
    with open('ingredients.dat') as f:
        pass


def load_cookingmethods():
    """ファイルからすべての調理法のリストを生成する。
    """
    with open('ingredients.dat') as f:
        pass


if __name__ == '__main__':
    main()
