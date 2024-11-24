from PyQt5.QtWidgets import QFrame, QHBoxLayout, QPushButton, QLabel, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize, QPropertyAnimation, QEasingCurve, QRect, QPoint

class Clut_Bar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(40)
        self.setStyleSheet("""
            QFrame {
                background-color: #202020;
                color: white;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
            }
            QPushButton {
                border: none;
                background-color: transparent;
                color: white;
                padding: 5px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #3a3a3a;
            }
        """)

        # 初始化动画和状态
        self._is_maximized = False
        self._normal_geometry = None
        self.animation = QPropertyAnimation(self.window(), b"geometry")
        self.animation.setEasingCurve(QEasingCurve.OutCubic)  # 使用更平滑的曲线
        self.animation.setDuration(100)  # 增加动画持续时间以提高流畅性
        
        # 获取屏幕尺寸
        self.screen = QDesktopWidget().availableGeometry()

        layout = QHBoxLayout()
        layout.setContentsMargins(10, 0, 0, 0)
        self.title = QLabel("ClutUI | Ver0.0.1 | 感谢体验 | 测试框架 非软件")
        self.title.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(self.title)

        self.min_button = QPushButton()
        self.min_button.setIcon(QIcon("assets/icons/mini.png"))
        
        self.max_button = QPushButton()
        self.max_button.setIcon(QIcon("assets/icons/max3.png"))
        
        self.close_button = QPushButton()
        self.close_button.setIcon(QIcon("assets/icons/close2.png"))
        
        for btn in [self.min_button, self.max_button, self.close_button]:
            btn.setFixedSize(QSize(40, 30))
            layout.addWidget(btn)

        self.setLayout(layout)
        self.start_pos = None
        
        self.min_button.clicked.connect(self.window().showMinimized)
        self.max_button.clicked.connect(self.toggle_maximize_animation)
        self.close_button.clicked.connect(self.window().close)
        
    def toggle_maximize_animation(self):
        """切换最大化状态的动画"""
        if self.animation.state() == QPropertyAnimation.Running:
            return
            
        if not self._is_maximized:
            self._maximize_window()
        else:
            self._restore_window()
            
        self.animation.start()
        
    def _maximize_window(self):
        """最大化窗口"""
        self._normal_geometry = self.window().geometry()
        self.animation.setStartValue(self._normal_geometry)
        self.animation.setEndValue(self.screen)
        self._is_maximized = True
        self.max_button.setIcon(QIcon("assets/icons/restore.png"))  # 更改为还原图标

    def _restore_window(self):
        """还原窗口"""
        self.animation.setStartValue(self.window().geometry())
        self.animation.setEndValue(self._normal_geometry)
        self._is_maximized = False
        self.max_button.setIcon(QIcon("assets/icons/max3.png"))  # 更改为最大化图标
            
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_pos = event.globalPos() - self.window().frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.start_pos:
            if not self._is_maximized:
                self.window().move(event.globalPos() - self.start_pos)
            else:
                self._restore_and_move(event)
            event.accept()

    def _restore_and_move(self, event):
        """在最大化状态下还原并移动窗口"""
        self.toggle_maximize_animation()
        ratio = event.globalPos().x() / self.screen.width()
        new_x = int(self._normal_geometry.width() * ratio)
        self.start_pos = QPoint(new_x, event.pos().y())

    def mouseReleaseEvent(self, event):
        self.start_pos = None
        
    def mouseDoubleClickEvent(self, event):
        """双击标题栏切换最大化状态"""
        if event.button() == Qt.LeftButton:
            self.toggle_maximize_animation()