from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from assets.utils.clut_card import ClutCard
from assets.utils.clut_image_card import ClutImageCard
import webbrowser
from PyQt5.QtCore import QTimer
from assets.utils.notification_manager import NotificationManager
from functools import partial

class AboutPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.notifications_shown = False  # 标记是否已显示过通知

    def showEvent(self, event):
        super().showEvent(event)
        if not self.notifications_shown:
            # 延迟一小段时间后显示通知
            QTimer.singleShot(100, self._show_about_notifications)
            self.notifications_shown = True

    def _show_about_notifications(self):
        from assets.utils.notification_manager import NotificationManager
        notification = NotificationManager()
        
        notification.show_message(
            title="开源仓库",
            msg="在 GitHub 上查看 Clut UI 的项目主页",
            duration=3000
        )
        notification.show_message(
            title="开源许可证",
            msg="本项目遵循 GPLv3.0 许可证供非商业使用",
            duration=3000
        )
        notification.show_message(
            title="版权声明",
            msg="PyQt-ClutUI 版权所有 © 2024 by ZZBuAoYe",
            duration=3000
        )
        notification.show_message(
            title="Tips",
            msg="点击可跳转至GitHub仓库",
            duration=3000,
            icon="assets/icons/tips.png"
        )

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)
        self.notification_manager = NotificationManager()
        
        # 标题
        title = QLabel("| 关于")
        title.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: white;
            }
        """)
        layout.addWidget(title)

        # Logo 部分使用 ClutImageCard
        logo_card = ClutImageCard(
            title="PyQt-ClutUI",
            msg="基于 PyQt5 的现代化 UI 组件库 | 作者: ZZBuAoYe",
            image_url="assets/icons/logo.png",
            image_mode=1  # 图片左侧模式1
        )
        layout.addWidget(logo_card)
        self.notification_manager.show_message(
            title="Logo加载完成",
            msg="Logo已成功加载显示"
        )
        github_card = ClutCard(
            title="开源仓库",
            msg="在 GitHub 上查看 Clut UI 的项目主页[GitHub]"
        )
        github_card.mousePressEvent = partial(
            self.open_url, 
            "https://github.com/ZZBuAoYe/PyQt-ClutUI"
        )
        layout.addWidget(github_card)

        # 许可证
        license_card = ClutCard(
            title="开源许可证",
            msg="本项目遵循 GPLv3.0 许可证供非商业使用"
        )
        license_card.mousePressEvent = partial(
            self.open_url,
            "https://github.com/ZZBuAoYe/PyQt-ClutUI/blob/main/LICENSE"
        )
        layout.addWidget(license_card)

        # 新增版权信息卡片
        copyright_card = ClutCard(
            title="本框架版权声明",
            msg="PyQt-ClutUI 版权所有 © 2024 by ZZBuAoYe\n保留所有权利"
        )
        layout.addWidget(copyright_card)
        pyqt_card = ClutCard(
            title="第三方资源",
            msg="本框架基于PyQt5开发完成 | PyQt5 的版权所有 © 2024 Riverbank Computing Limited"
        )
        layout.addWidget(pyqt_card)

        layout.addStretch()

    def open_url(self, url, event):
        if event.button() == Qt.LeftButton:
            webbrowser.open(url)
            self.notification_manager.show_message(
                title="正在跳转",
                msg="正在打开外部链接..."
            )