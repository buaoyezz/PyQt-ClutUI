import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QHBoxLayout, 
                            QVBoxLayout, QListWidget, QFrame, QPushButton, QLabel, 
                            QStackedWidget, QTextEdit, QLineEdit, QMessageBox, QDesktopWidget, QWIDGETSIZE_MAX)
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtCore import Qt, QSize, QTimer, QPropertyAnimation, QEasingCurve, QRect
from assets.utils.style_loader import load_stylesheet
from assets.utils.titlebar import Clut_Bar
from assets.utils.page_manager import PageManager
from assets.utils.main_ui import setup_main_layout, setup_content_layout, setup_sidebar
from assets.utils.notification_manager import NotificationManager
from assets.utils.message_box import ClutMessageBox
from assets.utils.settings_manager import SettingsManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # 添加screen属性初始化
        self.screen = QDesktopWidget().availableGeometry()
        
        # 设置默认大小和最小大小，而不是固定大小
        self.setMinimumSize(1066, 577)  # 最小尺寸
        self.resize(1066, 577)  # 默认尺寸
        
        # 将窗口居中显示
        x = (self.screen.width() - 1066) // 2
        y = (self.screen.height() - 577) // 2
        self.move(x, y)
        
        # 初始化设置管理器
        self.settings_manager = SettingsManager()
        
        # 设置窗口初始大小
        self.restore_window_geometry()
        
        # 记录窗口状态
        self._is_maximized = False
        self._normal_geometry = None
        
        # 初始化动画
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setEasingCurve(QEasingCurve.OutCubic)  # 使用弹性曲线
        self.animation.setDuration(300)  # 动画持续时间
        
        self.notification_manager = NotificationManager()
        
        self.notification_manager.show_message(
            title="Welcome Use ClutUI", 
            msg="欢迎你的到来！"
        )


        main_layout = setup_main_layout()
        self.title_bar = Clut_Bar(self)
        main_layout.addWidget(self.title_bar)

        content_layout, scroll_area = setup_content_layout()
        
        # 设置页面管理器
        self.page_manager = PageManager()
        self.content_stack = self.page_manager.get_stack()
        
        # 设置侧边栏
        sidebar_widget = setup_sidebar(self.page_manager)
        
        content_layout.addWidget(sidebar_widget)
        
        # 将content_stack放入滚动区域
        scroll_area.setWidget(self.content_stack)
        content_layout.addWidget(scroll_area)
        
        main_layout.addLayout(content_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def toggle_maximize_animation(self):
        """切换最大化状态"""
        if not self._is_maximized:
            # 保存当前几何信息
            self._normal_geometry = self.geometry()
            # 直接使用系统最大化
            self.showMaximized()
            # 更新状态
            self._is_maximized = True
            self.title_bar.max_button.setText("❐")
        else:
            # 还原窗口
            self.showNormal()
            # 更新状态
            self._is_maximized = False
            self.title_bar.max_button.setText("□")
            # 恢复位置
            if self._normal_geometry:
                self.setGeometry(self._normal_geometry)

    def mouseDoubleClickEvent(self, event):
        """双击标题栏切换最大化状态"""
        if event.button() == Qt.LeftButton:
            self.toggle_maximize_animation()
            
    def restore_window_geometry(self):
        """恢复或设置窗口几何属性"""
        settings = self.settings_manager.settings["window"]
        screen = QDesktopWidget().availableGeometry()
        
        # 如果是首次运行或没有保存的设置
        if settings["width"] == 0 or settings["height"] == 0:
            recommended = self.settings_manager.get_recommended_size()
            self.setGeometry(
                recommended["x"],
                recommended["y"],
                recommended["width"],
                recommended["height"]
            )
        else:
            # 确保窗口位置在屏幕范围内
            x = max(0, min(settings["x"], screen.width() - settings["width"]))
            y = max(0, min(settings["y"], screen.height() - settings["height"]))
            
            # 使用保存的设置
            self.setGeometry(
                x, y,
                settings["width"],
                settings["height"]
            )
        
        # 如果设置为最大化，则最大化窗口
        if settings["is_maximized"]:
            QTimer.singleShot(100, lambda: self.title_bar.toggle_maximize_animation())
            
    def changeEvent(self, event):
        """窗口状态改变事件"""
        if hasattr(Qt, 'WindowStateChange'):
            state_change = Qt.WindowStateChange
        else:
            state_change = Qt.WindowState  # Qt6 中的新名称
            
        if event.type() == state_change:
            if self.windowState() == Qt.WindowMaximized and \
               not self._is_maximized:
                # 从正常状态到最大化
                event.accept()
                self.toggle_maximize_animation()
            elif self.windowState() == Qt.WindowNoState and \
                 self._is_maximized:
                # 从最大化到正常状态
                event.accept()
                self.toggle_maximize_animation()
        super().changeEvent(event)
        
    def save_window_geometry(self):
        """保存窗口几何属性"""
        if not self._is_maximized:
            geometry = self.geometry()
            print(f"保存窗口几何信息: {geometry.width()}x{geometry.height()}")  # 调试输出
            self.settings_manager.settings["window"].update({
                "width": geometry.width(),
                "height": geometry.height(),
                "x": geometry.x(),
                "y": geometry.y(),
            })
        self.settings_manager.settings["window"]["is_maximized"] = self._is_maximized
        self.settings_manager.save_settings()

    def closeEvent(self, event):
        """窗口关闭事件"""
        self.save_window_geometry()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QWidget {
            font-size: 14px;
            font-family: 'Microsoft YaHei', sans-serif;
        }
    """)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
