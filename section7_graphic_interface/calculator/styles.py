# QSS - DOCUMENTATION
# https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html

# Theme installation
# pip install pyqtdarktheme
# Theme Documentation
# https://pyqtdarktheme.readthedocs.io/en/stable/how_to_use.html
import qdarktheme

from variables import PRIMARY_COLOR, DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR

qss = f"""
QPushButton[cssClass="specialButton"] {{
    color: #fff;
    background: "{PRIMARY_COLOR}";
}}
QPushButton[cssClass="specialButton"]:hover {{
    color: #fff;
    background: "{DARKER_PRIMARY_COLOR}";
}}
QPushButton[cssClass="specialButton"]:pressed {{
    color: #fff;
    background: "{DARKEST_PRIMARY_COLOR}";
}}
"""


def setupTheme():
    qdarktheme.setup_theme(
            theme='dark',
            corner_shape='rounded',  # Will make display have corner rounded
            custom_colors={
                "[dark]": {
                    "primary": f"{PRIMARY_COLOR}",
                },
                "[light]": {
                    "primary": f"{PRIMARY_COLOR}",
                },
            },
            additional_qss=qss
    )
