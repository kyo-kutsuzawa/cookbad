#-------------------------------------------------------------------------------
# Name:        Recipi
# Purpose:     レシピ関連のクラス
#
# Author:      kyo
#
# Created:     2016-09-04
# Copyright:   (c) kyo 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Recipi:
    """レシピ
    レシピ全体を表すクラス。
    食材一覧，完成までの調理手順，などをまとめたクラス。
    """
    def __init__(self):
        steps = []


class Ingredient:
    """食材
    ひとつの食材を表す。
    食材名，食材の画像，調理された履歴，などをまとめたクラス。
    """
    def __init__(self, name='', img=None):
        self.name = name    # 食材名（e.g., 'ジャガイモ'）
        self.image = img    # 食材画像
        self.history = []   # 調理履歴（e.g., 切られた→焼かれた→盛り付けられた）


class CookingMethod:
    """調理法
    ひとつの調理方法を表す。
    穴あきの説明文，説明文の穴に収まる語句，調理手順に対応する画像処理，などをまとめたクラス。
    """
    def __init__(self, name='', cookfunc=None, describe=''):
        self.name = name            # 調理法の名前（e.g., '焼く'）
        self.decribe = describe     # 調理説明の文字列（e.g., '[food]を[minute]分焼きます。'）
        self.cookfunc = cookfunc    # 調理法に対応する処理の関数
        self.ps = []                # 調理説明の穴に入る語句（e.g., [ジャガイモ, 2]）

    def __call__(self):
        return self.cookfunc(self)


if __name__ == '__main__':
    pass
