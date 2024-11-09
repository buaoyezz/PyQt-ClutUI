# PyQt-ClutUI

<p align="center">
    <img src="assets/icons/logo.png" alt="ClutUI Logo" width="200"/>
</p>

<p align="center">
    <strong>一个基于PyQt5的现代化UI框架</strong>
</p>

<p align="center">
    <a href="#特性">特性</a> •
    <a href="#运行">运行</a> •
    <a href="#快速开始">快速开始</a> •
    <a href="#贡献">贡献</a> •
    <a href="#许可证">许可证</a> •
    <a href="#END">结语</a> 
</p>

## 特性

- 🎨 现代化设计风格
- 🚀 丰富的预置组件
- 📦 易于集成和使用
- 🛠 高度可定制
- 💡 智能的通知系统
- 🎯 无边框窗口支持
- 🌈 动画效果支持
  - 窗口最大化/还原动画
  - 侧边栏展开/收缩动画
  - 页面切换滑动动画
  - 通知弹出/消失动画
- 🎭 丰富的组件库
  - ClutButton - 现代化按钮组件
    ```python
    # ClutButton - 现代化按钮组件
    from assets.utils.clut_button import ClutButton
    
    # 创建一个基础按钮
    button = ClutButton("点击我")
    # 创建一个主要按钮
    primary_button = ClutButton("主要按钮", primary=True)
    ```
  - ClutCard - 卡片容器组件
    ```python
    from assets.utils.clut_card import ClutCard
    
    # 创建一个卡片
    card = ClutCard()
    card.set_title("卡片标题")
    card.set_content("这是卡片内容")
    ```
  - ClutImageCard - 图片卡片组件
    ```python
    from assets.utils.clut_image_card import ClutImageCard
    
    # 创建一个图片卡片
    image_card = ClutImageCard("图片路径", "卡片标题", "卡片描述")
    ```
  - ClutLineEdit - 输入框组件
    ```python
    from assets.utils.clut_button import ClutLineEdit
    
    # 创建一个输入框
    input_box = ClutLineEdit()
    input_box.setPlaceholderText("请输入内容...")
    ```
  - ClutMessageBox - 消息对话框组件
    ```python
    from assets.utils.message_box import ClutMessageBox
    
    # 创建并显示一个消息框
    msg_box = ClutMessageBox(title="提示", text="这是一条消息", buttons=["确定", "取消"])
    result = msg_box.exec_()
    ```
  - OverlayNotification - 通知提示组件
    ```python
    from assets.utils.notification import OverlayNotification
    
    # 创建通知组件
    notification = OverlayNotification()
    # 显示一条3秒后自动关闭的消息
    notification.show_message("这是一条通知消息")
    ```
  - Clut_Bar - 自定义标题栏组件
    ```python
    from assets.utils.titlebar import Clut_Bar
    
    # 创建自定义标题栏
    title_bar = Clut_Bar()
    # 设置窗口标题
    title_bar.title.setText("我的应用")
    ```

## | 运行

1. 克隆仓库:
   ```bash
   git clone https://github.com/buaoyezz/PyQt-ClutUI.git
   ```

2. 安装依赖:
   ```bash
   pip install PyQt5
   ```

3. 运行示例:
    直接运行ClutUI_Main.py
    或
    ```bash
    python ClutUI_Main.py
    ```

## 快速开始

1. 导入需要的组件
2. 创建组件实例
3. 设置组件属性
4. 将组件添加到布局中

## 贡献

-欢迎提交 Issue 和 Pull Request!

## 许可证

- 本项目采用 GPL-3.0 许可证
- 更多信息请参阅 LICENSE 文件

## END

- 感谢您的使用和支持！
- 本框架仍在开发中，欢迎提出建议和贡献！
- 喜欢的话请给个Star吧！
- 代码写的不好，见谅
