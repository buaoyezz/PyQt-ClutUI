from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QHBoxLayout, 
                            QFrame, QSpacerItem, QSizePolicy)
from assets.utils.clut_button import ClutLineEdit, ClutButton
from assets.utils.message_box import ClutMessageBox
from assets.utils.clut_card import ClutCard
from assets.utils.clut_image_card import ClutImageCard

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        # 主布局
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)  # 增加页面边距
        layout.setSpacing(24)  # 增加组件间距
        
        # 欢迎区域
        welcome_container = QFrame()
        welcome_container.setObjectName("welcomeContainer")
        welcome_layout = QVBoxLayout(welcome_container)
        welcome_layout.setContentsMargins(0, 0, 0, 0)
        welcome_layout.setSpacing(8)
        
        welcome_label = QLabel("ClutUI - PyQt5")
        welcome_label.setStyleSheet("""
            QLabel {
                font-size: 32px;
                font-weight: bold;
                color: #ffffff;
            }
        """)
        
        sub_title = QLabel("感谢体验ClutUI | 欢迎使用 希望给你带来不一样的体验")
        sub_title.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: rgba(255, 255, 255, 0.7);
            }
        """)
        
        welcome_layout.addWidget(welcome_label)
        welcome_layout.addWidget(sub_title)
        layout.addWidget(welcome_container)
        
        # 搜索区域
        search_container = QFrame()
        search_container.setObjectName("searchContainer")
        search_layout = QHBoxLayout(search_container)
        search_layout.setContentsMargins(0, 0, 0, 0)
        search_layout.setSpacing(16)
        
        self.search_input = ClutLineEdit()
        self.search_input.setPlaceholderText("搜索感兴趣的内容...")
        self.search_input.setMinimumHeight(40)  # 增加输入框高度
        
        search_button = ClutButton("搜索", primary=True)
        search_button.setMinimumWidth(100)
        search_button.clicked.connect(self.on_search)
        
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_button)
        layout.addWidget(search_container)
        
        # 分隔
        layout.addSpacing(32)
        
        # 按钮区域
        actions_container = QFrame()
        actions_container.setObjectName("actionsContainer")
        actions_layout = QHBoxLayout(actions_container)
        actions_layout.setContentsMargins(0, 0, 0, 0)
        actions_layout.setSpacing(16)
        
        # 左
        left_buttons = QHBoxLayout()
        left_buttons.setSpacing(12)
        
        self.primary_button = ClutButton("发布新帖", primary=True)
        self.secondary_button = ClutButton("浏览", primary=False)
        
        left_buttons.addWidget(self.primary_button)
        left_buttons.addWidget(self.secondary_button)
        
        # 右
        right_buttons = QHBoxLayout()
        right_buttons.setSpacing(12)
        
        example_button = ClutButton("帮助", primary=False)
        example_button.clicked.connect(self.show_example_message_box)
        
        right_buttons.addWidget(example_button)
        
        # 弹性空间
        actions_layout.addLayout(left_buttons)
        actions_layout.addStretch()
        actions_layout.addLayout(right_buttons)
        
        layout.addWidget(actions_container)
        
        # 弹性空间
        layout.addStretch()
        
        # 卡片
        card = ClutCard(
            title="ClutUI Card", 
            msg="This is a ClutUI 's Card\n这是ClutUI的卡片"
        )
        layout.addWidget(card)
        
        # 图片在上方
        # card1 = ClutImageCard(
        #     title="图片卡片",
        #     msg="点击图片可以跳转",
        #     image_url="assets/icons/play.png",
        #     image_mode=0,
        #     image_clickConnect=self.on_image_click
        # )
        # layout.addWidget(card1)
        
        # 图片在左侧
        # card2 = ClutImageCard(
        #     title="左侧图片布局",
        #     msg="图片显示在左侧，文字在右侧",
        #     image_url="path/to/image.jpg",
        #     image_mode=1
        # )
        # layout.addWidget(card2)
        
        # 图片作为背景
        # card3 = ClutImageCard(
        #     title="背景图片布局",
        #     msg="文字覆盖在图片上，带渐变遮罩",
        #     image_url="path/to/image.jpg",
        #     image_mode=2
        # )
        # layout.addWidget(card3)
        
        self.setLayout(layout)
        
        self.setStyleSheet("""
            QFrame#welcomeContainer, QFrame#searchContainer, QFrame#actionsContainer {
                background: rgba(255, 255, 255, 0.03);
                border-radius: 12px;
                padding: 24px;
            }
        """)
        
    def on_search(self):
        print("搜索按钮被点击")

    def show_example_message_box(self):
        ClutMessageBox.show_message(
            self,
            title="帮助信息",
            text="欢迎ClutUI\n\nI Will Tell You How To Use It!",
            buttons=["我知道了"]
        )
        
    def on_image_click(self):
        print("点击了一下图片~")