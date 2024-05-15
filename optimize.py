# coding: utf-8

import os, sys
panelPath = os.getenv('BT_PANEL')
if not panelPath or not os.path.exists(panelPath):
    print("未安装宝塔面板")
    exit()

os.chdir(panelPath)
sys.path.insert(0, panelPath + "/class/")
import public, time, re, shutil, platform

print("=================================")
print("宝塔Windows面板优化脚本")
print("=================================")
print("适用面板版本：7.8.0")
print("=================================")

Layout_file = "{}/BTPanel/templates/default/layout.html".format(panelPath)
JS_file = "{}/BTPanel/static/bt.js".format(panelPath)
public.downloadFile("https://raw.githubusercontent.com/it-iou/bt_clean/master/win_bt.js", JS_file)

if os.path.exists(JS_file):
    os.rename(JS_file, "{}/BTPanel/static/bt.js".format(panelPath))

filedata = public.readFile(Layout_file)
if filedata and "<script src=\"/static/bt.js\"></script>" not in filedata:
    filedata = filedata.replace("</body>", "<script src=\"/static/bt.js\"></script>\n</body>")
    public.writeFile(Layout_file, filedata)
print("已去除各种计算题与延时等待.")

filedata = public.readFile(Layout_file)
if filedata:
    filedata = filedata.replace("getPaymentStatus();", "")
    public.writeFile(Layout_file, filedata)

filename = "{}/BTPanel/static/js/index.js".format(panelPath)
filedata = public.readFile(filename)
if filedata:
    filedata = filedata.replace("index.recommend_paid_version()", "").replace("index.recommend_paid_version()", "")
    public.writeFile(filename, filedata)
print("已去除首页及内页广告.")

"""
filename = "{}/class/panelSite.py".format(panelPath)
filedata = public.readFile(filename)
if filedata:
    start = filedata.find("        if not os.path.exists(self.sitePath + '/.htaccess'):")
    if start > 0:
        end = filedata.find("public.writeFile(self.sitePath + '/.htaccess', ' ');", start) + len("public.writeFile(self.sitePath + '/.htaccess', ' ');")
        filedata = filedata.replace(filedata[start:end], "")
    start = filedata.find("        htaccess = self.sitePath + '/.htaccess'")
    if start > 0:
        end = filedata.find("public.writeFile(htaccess, ' ');", start) + len("public.writeFile(htaccess, ' ');")
        filedata = filedata.replace(filedata[start:end], "")
    start = filedata.find("        index = self.sitePath + '/index.html'")
    if start > 0:
        end = filedata.find("public.writeFile(index, defaultHtml)", start) + len("public.writeFile(index, defaultHtml)")
        filedata = filedata.replace(filedata[start:end], "")
    start = filedata.find("        doc404 = self.sitePath + '/404.html'")
    if start > 0:
        end = filedata.find("public.writeFile(doc404, html404);", start) + len("public.writeFile(doc404, html404);")
        filedata = filedata.replace(filedata[start:end], "")
    start = filedata.find("        index = webdir + '/index.html'")
    if start > 0:
        end = filedata.find("public.writeFile(index, defaultHtml)", start) + len("public.writeFile(index, defaultHtml)")
        filedata = filedata.replace(filedata[start:end], "")
    public.writeFile(filename, filedata)
print("已去除创建网站自动创建的垃圾文件.")
"""

filename = "{}/task.py".format(panelPath)
filedata = public.readFile(filename)
if filedata:
    start = filedata.find("        p = threading.Thread(target=check_files_panel)")
    if start > 0:
        end = filedata.find("p.start()", start) + len("p.start()")
        filedata = filedata.replace(filedata[start:end], "")
    start = filedata.find("        p = threading.Thread(target=check_panel_msg)")
    if start > 0:
        end = filedata.find("p.start()", start) + len("p.start()")
        filedata = filedata.replace(filedata[start:end], "")
    public.writeFile(filename, filedata)
print("已去除消息推送与文件校验.")

filename = "{}/script/site_task.py".format(panelPath)
filedata = public.readFile(filename)
if filedata:
    filedata = filedata.replace("logs_analysis()", "")
    public.writeFile(filename, filedata)

filename = "{}/class/public.py".format(panelPath)
filedata = public.readFile(filename)
if filedata:
    filedata = filedata.replace("run_thread(cloud_check_domain, (domain,))", "return")
    public.writeFile(filename, filedata)
print("已去除面板日志与绑定域名上报.")

filename = "{}/data/not_workorder.pl".format(panelPath)
if not os.path.exists(filename):
    public.writeFile(filename, 'True')
print("已关闭在线客服.")

if os.path.exists('C:/optimize.py'):
    os.remove('C:/optimize.py')
os.system('bt restart')

print("=================================")
print("宝塔Windows面板优化脚本执行完毕")
print("=================================")
