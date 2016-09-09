# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:         module1
# Purpose:
#
# Author:       kyo
#
# Created:      20160909
# Copyright:    (c) kyo 2016
# Licence:      <your licence>
#-------------------------------------------------------------------------------

import cgi
from jinja2 import Environment, FileSystemLoader
import cookbad_stub
import recipi

def main():
    #テンプレートファイルを指定
    env = Environment(loader=FileSystemLoader('./', encoding='shift-jis'))
    tpl = env.get_template('./cgi-bin/test.html')

    f = cgi.FieldStorage()
    rcp, materials = cookbad_stub.web()

    materials_list = []
    for m in materials:
        materials_list.append({'name': m.name})

    steps_list = []
    for s in rcp.steps:
        steps_list.append({'dsc': s.describe})

    sample_list = []
    sample_list.append({'title':u"コンテンツtitle1", 'body':u"コンテンツbody1"})
    sample_list.append({'title':u"コンテンツtitle2", 'body':u"コンテンツbody2"})
    sample_list.append({'title':u"コンテンツtitle3", 'body':u"コンテンツbody3"})

    html = tpl.render({'title':'aaaaa', 'materials':materials_list, 'recipi':steps_list})

    #print('Content-type: text/html; charset=UTF-8\r\n')
    print('Content-type: text/html; charset=Shift-JIS\r\n')
    print(html)


if __name__ == '__main__':
    main()
