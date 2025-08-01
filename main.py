"""
    这是一个示例插件
    Author: 君の名は

    Tips:
    若要在插件广场推送您的更新，请手动修改"plugin.json"的"version"版本号字段以被插件广场识别
"""
from PyQt5 import uic
import requests,time,json
from .ClassWidgets.base import PluginBase, SettingsBase  # 导入CW的基类


class Plugin(PluginBase):  # 插件类
    def __init__(self, cw_contexts, method):  # 初始化
        super().__init__(cw_contexts, method)  # 调用父类初始化方法
        
        self.method.register_widget(widget_code="almanac.ui", widget_name="黄历", widget_width=120)

    def execute(self):  # 自启动执行部分
        print('Plugin Executed!')
        

    def update(self, cw_contexts):  # 自动更新部分
        super().update(cw_contexts)  # 调用父类更新方法

        # 黄历小组件
        current_date=time.strftime("%Y-%m-%d",time.localtime()) # 获取当前时间,格式:YYYY-mm-dd
        datapack=requests.get("https://www.36jxs.com/api/Commonweal/almanac?sun="+current_date).content # 请求黄历数据
        almanac=json.loads(datapack.decode("utf-8"))["data"] # 解码数据并转换为json
        title=almanac["TianGanDiZhiYear"]+"年"+almanac["LMonth"]+almanac["LDay"] # 组件标题
        content="宜:"+almanac["Yi"]+"\n"+"忌:"+almanac["Ji"] # 组件内容
        self.method.change_widget_content(widget_code="almanac.ui", title=title, content=content) # 更新组件标题与内容
        



# 设置页（若无此需求，请删除此部分并将"__init__.py"中引用的本模块部分删除，并在"plugins.json"中把"settings"子块设为"false"）
class Settings(SettingsBase):
    def __init__(self, plugin_path, parent=None):
        super().__init__(plugin_path, parent)
        uic.loadUi(f'{self.PATH}/settings.ui', self)  # 加载设置界面
        """
        在这里写设置页面
        """
