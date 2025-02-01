# PyQt-ClutUI
-已停更，请使用ClutUI-Nextgen

<p align="center">
    <img src="src/clutui/assets/icons/logo.png" alt="ClutUI Logo" width="500"/>
</p>

<p align="center">
    <strong>✨ 一个基于PyQt5的现代化UI框架 ✨</strong>
</p>

<p align="center">
    <a href="#安装" style="text-decoration:none; color:#007BFF; font-weight:bold;">🔧 安装</a> •
    <a href="#快速开始" style="text-decoration:none; color:#007BFF; font-weight:bold;">🚀 快速开始</a> •
    <a href="#贡献" style="text-decoration:none; color:#007BFF; font-weight:bold;">🌟 贡献</a> •
    <a href="#许可证" style="text-decoration:none; color:#007BFF; font-weight:bold;">📜 许可证</a> •
    <a href="#其他" style="text-decoration:none; color:#007BFF; font-weight:bold;">📚 其他</a> •
    <a href="#END" style="text-decoration:none; color:#007BFF; font-weight:bold;">💬 结语</a> 
</p>

## 🔧 安装
+ ClutUI现在已经支持pip安装，已上传PyPi
1. 使用pip安装:
   ```bash
   pip install clutui
   ```

2. 或者克隆仓库:
   ```bash
   git clone https://github.com/buaoyezz/PyQt-ClutUI.git
   ```

3. 安装必要依赖:
   ```cmd
   pip install PyQt5
   ```
>或者使用本地安装
   ```bash
   pip install PyQt5-5.15.9-cp312-cp312-win_amd64.whl
   ```
## 🍞 编译项目
 - 项目由PyPi于twine库进行上传
    ```bash
    pip install twine
    python -m twine upload dist/*
    ```

 - 编译语句
   ```bash
   python -m build
   ```
 - 需要类似如下的完善的项目结构
    ```bash
    ClutUI/
      ├── src/
      │   └── clutui/
      │       ├── __init__.py
      │       ├── main.py  (示例主文件(ClutMain.py))
      │       └── assets/
      │           └── utils/
      │               ├── __init__.py
      │               ├── style_loader.py
      │               ├── titlebar.py
      │               └── ...
      ├── tests/
      ├── pyproject.toml
      ├── setup.cfg
      ├── README.md
      └── LICENSE
    ```
  - `__init__.py`文件内必须完整导入所有组件
    ```python
        from .assets.utils.titlebar import Clut_Bar
        from .assets.utils.style_loader import load_stylesheet
        from .assets.utils.page_manager import PageManager
        from .assets.utils.main_ui import (
            setup_main_layout,
            setup_content_layout,
            setup_sidebar
        )
        from .assets.utils.notification_manager import NotificationManager
        from .assets.utils.message_box import ClutMessageBox
        from .assets.utils.settings_manager import SettingsManager
        from .assets.utils.overlay_notification import OverlayNotification
        from .assets.utils.clut_image_card import ClutImageCard
        from .assets.utils.clut_card import ClutCard
        from .assets.utils.clut_button import ClutButton
        # 页面组件导入
        from .assets.pages.home import HomePage
        from .assets.pages.about import AboutPage
    ```
    然后在all中正确写入
    ```python
    __all__ = [
        # 主窗口
        "MainWindow",
        
        # 工具类
        "Clut_Bar",
        "load_stylesheet",
        "PageManager",
        "setup_main_layout",
        "setup_content_layout", 
        "setup_sidebar",
        "NotificationManager",
        "ClutMessageBox",
        "SettingsManager",
        "OverlayNotification",
        "ClutImageCard",
        "ClutCard",
        "ClutButton",
        
        # 页面组件
        "HomePage",
        "AboutPage"
    ] 
    ```
  - ***注意不要忘记作者和版本号参数**
  - 其他文件`setup.cfg`和`pyproject.toml`请自行调整配置
  - `setup.cfg`包含[metadata][options.packages.find]和[options]三个部分，请自行调整<br>其中`options.packages.find`如下:
    ```conf
    [options.packages.find]
    where = src 
    ```
  - `pyproject.toml`包含<br>+ [tool.setuptools.package-data]<br>+ [tool.setuptools.packages.find]<br>+ [tool.setuptools]<br>+ [project.urls]<br>+ [project]<br>+ [build-system]
  + 请注意不要遗漏,自行调整
## 🚀 快速开始

1. 导入需要的组件
2. 创建组件实例
3. 设置组件属性
4. 将组件添加到布局中
5. 运行应用程序并查看效果

## 🌟 贡献

- 欢迎提交 Issue 和 Pull Request!
- 请确保您的代码符合项目的编码规范
- 提交前请运行所有测试用例

## 📜 许可证

- 本项目采用 GPL-3.0 许可证
- 更多信息请参阅 LICENSE 文件

## 📚 其他

- 本项目使用PyQt5开发，请确保安装PyQt5
- 本项目为PyQt5的UI框架，不是UI库
- 本项目的使用实战示例请参考[ClutCommitCanvas](https://github.com/buaoyezz/ClutCommitCanvas)完全由ClutUI为框架开发
- 本项目仍在开发中，欢迎提出建议和贡献！
- 项目开源，请遵守GPL-3.0协议
- 如有任何问题，请通过GitHub Issue与我们联系

## 💬 END

- 感谢您的使用和支持！
- 本框架仍在开发中，欢迎提出建议和贡献！
- 喜欢的话请给个Star吧！⭐️
- 期待您的反馈和改进建议！
