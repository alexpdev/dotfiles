example = """
QPushButton::menu-indicator {
    image: url(myindicator.png);
    subcontrol-position: right center;
    subcontrol-origin: padding;
    left: -2px;
}"""

lineedit = """
QLineEdit { color: red }

QLineEdit { color: red }
QLineEdit[readOnly="true"] { color: gray }

QLineEdit { color: red }
QLineEdit[readOnly="true"] { color: gray }

QLineEdit { color: red }
QLineEdit[readOnly="true"] { color: gray }
QLineEdit {
    border: 2px solid gray;
    border-radius: 10px;
    padding: 0 8px;
    background: yellow;
    selection-background-color: darkgray;
}

QLineEdit[echoMode="2"] {
    lineedit-password-character: 9679;
}
QLineEdit:read-only {
    background: lightblue;
}"""

dialog = """
QDialog QLineEdit { color: brown }
"""

textedit = """
QTextEdit, QListView {
    background-color: white;
    background-image: url(draft.png);
    background-attachment: scroll;
}

QTextEdit, QListView {
    background-color: white;
    background-image: url(draft.png);
    background-attachment: fixed;
}
"""

checkbox = """
QCheckBox {
    spacing: 5px;
}

QCheckBox::indicator {
    width: 13px;
    height: 13px;
}

QCheckBox::indicator:unchecked {
    image: url(:/images/checkbox_unchecked.png);
}

QCheckBox::indicator:unchecked:hover {
    image: url(:/images/checkbox_unchecked_hover.png);
}

QCheckBox::indicator:unchecked:pressed {
    image: url(:/images/checkbox_unchecked_pressed.png);
}

QCheckBox::indicator:checked {
    image: url(:/images/checkbox_checked.png);
}

QCheckBox::indicator:checked:hover {
    image: url(:/images/checkbox_checked_hover.png);
}

QCheckBox::indicator:checked:pressed {
    image: url(:/images/checkbox_checked_pressed.png);
}

QCheckBox::indicator:indeterminate:hover {
    image: url(:/images/checkbox_indeterminate_hover.png);
}

QCheckBox::indicator:indeterminate:pressed {
    image: url(:/images/checkbox_indeterminate_pressed.png);
}
"""

combobox = """
QComboBox {
    border: 1px solid gray;
    border-radius: 3px;
    padding: 1px 18px 1px 3px;
    min-width: 6em;
}

QComboBox:editable {
    background: white;
}

QComboBox:!editable, QComboBox::drop-down:editable {
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
}

QComboBox:!editable:on, QComboBox::drop-down:editable:on {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,
                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);
}

QComboBox:on {
    padding-top: 3px;
    padding-left: 4px;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;
    border-left-width: 1px;
    border-left-color: darkgray;
    border-left-style: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow {
    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);
}

QComboBox::down-arrow:on {
    top: 1px;
    left: 1px;
}

QComboBox QAbstractItemView {
    border: 2px solid darkgray;
    selection-background-color: lightgray;
}"""

dockwidget = """
QDockWidget {
    border: 1px solid lightgray;
    titlebar-close-icon: url(close.png);
    titlebar-normal-icon: url(undock.png);
}

QDockWidget::title {
    text-align: left;
    background: lightgray;
    padding-left: 5px;
}

QDockWidget::close-button, QDockWidget::float-button {
    border: 1px solid transparent;
    background: darkgray;
    padding: 0px;
}

QDockWidget::close-button:hover, QDockWidget::float-button:hover {
    background: gray;
}

QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {
    padding: 1px -1px -1px 1px;
}

QDockWidget {
    border: 1px solid lightgray;
    titlebar-close-icon: url(close.png);
    titlebar-normal-icon: url(float.png);
}

QDockWidget::title {
    text-align: left;
    background: lightgray;
    padding-left: 35px;
}

QDockWidget::close-button, QDockWidget::float-button {
    background: darkgray;
    padding: 0px;
    icon-size: 14px;
}

QDockWidget::close-button:hover, QDockWidget::float-button:hover {
    background: gray;
}

QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {
    padding: 1px -1px -1px 1px;
}

QDockWidget::close-button {
    subcontrol-position: top left;
    subcontrol-origin: margin;
    position: absolute;
    top: 0px; left: 0px; bottom: 0px;
    width: 14px;
}

QDockWidget::float-button {
    subcontrol-position: top left;
    subcontrol-origin: margin;
    position: absolute;
    top: 0px; left: 16px; bottom: 0px;
    width: 14px;
}"""

qframe = """
QFrame, QLabel, QToolTip {
    border: 2px solid green;
    border-radius: 4px;
    padding: 2px;
    background-image: url(images/welcome.png);
}"""

groupbox = """
QGroupBox {
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);
    border: 2px solid gray;
    border-radius: 5px;
    margin-top: 1ex;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding: 0 3px;
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #FF0ECE, stop: 1 #FFFFFF);
}

QGroupBox::indicator {
    width: 13px;
    height: 13px;
}

QGroupBox::indicator:unchecked {
    image: url(:/images/checkbox_unchecked.png);
}"""

headerview="""
QHeaderView::section {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                      stop:0 #616161, stop: 0.5 #505050,
                                      stop: 0.6 #434343, stop:1 #656565);
    color: white;
    padding-left: 4px;
    border: 1px solid #6c6c6c;
}

QHeaderView::section:checked
{
    background-color: red;
}

QHeaderView::down-arrow {
    image: url(down_arrow.png);
}

QHeaderView::up-arrow {
    image: url(up_arrow.png);
}"""

listview = """
QListView {
    alternate-background-color: yellow;
}
QListView {
    show-decoration-selected: 1;
}

QListView::item:alternate {
    background: #EEEEEE;
}

QListView::item:selected {
    border: 1px solid #6a6ea9;
}

QListView::item:selected:!active {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #ABAFE5, stop: 1 #8588B2);
}

QListView::item:selected:active {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #6a6ea9, stop: 1 #888dd9);
}

QListView::item:hover {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #FAFBFE, stop: 1 #DCDEF1);
}"""

mainwindow = """
QMainWindow::separator {
    background: yellow;
    width: 10px;
    height: 10px;
}

QMainWindow::separator:hover {
    background: red;
}"""

menu = """
QMenu {
    background-color: #ABABAB;
    border: 1px solid black;
}

QMenu::item {

        if you want menu color and menu item color to be different */
    background-color: transparent;
}

QMenu::item:selected {
    background-color: #654321;
}

QMenu {
    background-color: white;
    margin: 2px;
}

QMenu::item {
    padding: 2px 25px 2px 20px;
    border: 1px solid transparent;
}

QMenu::item:selected {
    border-color: darkblue;
    background: rgba(100, 100, 100, 150);
}

QMenu::icon:checked {
    background: gray;
    border: 1px inset gray;
    position: absolute;
    top: 1px;
    right: 1px;
    bottom: 1px;
    left: 1px;
}

QMenu::separator {
    height: 2px;
    background: lightblue;
    margin-left: 10px;
    margin-right: 5px;
}

QMenu::indicator {
    width: 13px;
    height: 13px;
}


QMenu::indicator:non-exclusive:unchecked {
    image: url(:/images/checkbox_unchecked.png);
}

QMenu::indicator:non-exclusive:unchecked:selected {
    image: url(:/images/checkbox_unchecked_hover.png);
}

QMenu::indicator:non-exclusive:checked {
    image: url(:/images/checkbox_checked.png);
}

QMenu::indicator:non-exclusive:checked:selected {
    image: url(:/images/checkbox_checked_hover.png);
}


QMenu::indicator:exclusive:unchecked {
    image: url(:/images/radiobutton_unchecked.png);
}

QMenu::indicator:exclusive:unchecked:selected {
    image: url(:/images/radiobutton_unchecked_hover.png);
}

QMenu::indicator:exclusive:checked {
    image: url(:/images/radiobutton_checked.png);
}

QMenu::indicator:exclusive:checked:selected {
    image: url(:/images/radiobutton_checked_hover.png);
}"""


menubar = """
QMenuBar {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                      stop:0 lightgray, stop:1 darkgray);
    spacing: 3px;
}

QMenuBar::item {
    padding: 1px 4px;
    background: transparent;
    border-radius: 4px;
}

QMenuBar::item:selected {
    background: #a8a8a8;
}

QMenuBar::item:pressed {
    background: #888888;
}"""

progressbar="""
QProgressBar {
    border: 2px solid grey;
    border-radius: 5px;
}

QProgressBar::chunk {
    background-color: #05B8CC;
    width: 20px;
}
QProgressBar {
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center;
}

QProgressBar::chunk {
    background-color: #CD96CD;
    width: 10px;
    margin: 0.5px;
}"""

pushbutton = """
QPushButton {
    border: 2px solid #8f8f91;
    border-radius: 6px;
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #f6f7fa, stop: 1 #dadbde);
    min-width: 80px;
}

QPushButton:pressed {
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #dadbde, stop: 1 #f6f7fa);
}

QPushButton:flat {
    border: none;
}

QPushButton:default {
    border-color: navy;
}

QPushButton:open {
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #dadbde, stop: 1 #f6f7fa);
}

QPushButton::menu-indicator {
    image: url(menu_indicator.png);
    subcontrol-origin: padding;
    subcontrol-position: bottom right;
}

QPushButton::menu-indicator:pressed, QPushButton::menu-indicator:open {
    position: relative;
    top: 2px; left: 2px;
}"""

radiobutton = """
QRadioButton::indicator {
    width: 13px;
    height: 13px;
}

QRadioButton::indicator::unchecked {
    image: url(:/images/radiobutton_unchecked.png);
}

QRadioButton::indicator:unchecked:hover {
    image: url(:/images/radiobutton_unchecked_hover.png);
}

QRadioButton::indicator:unchecked:pressed {
    image: url(:/images/radiobutton_unchecked_pressed.png);
}

QRadioButton::indicator::checked {
    image: url(:/images/radiobutton_checked.png);
}

QRadioButton::indicator:checked:hover {
    image: url(:/images/radiobutton_checked_hover.png);
}

QRadioButton::indicator:checked:pressed {
    image: url(:/images/radiobutton_checked_pressed.png);
}"""

scrollbar = """
QScrollBar:horizontal {
    border: 2px solid grey;
    background: #32CC99;
    height: 15px;
    margin: 0px 20px 0 20px;
}

QScrollBar::handle:horizontal {
    background: white;
    min-width: 20px;
}

QScrollBar::add-line:horizontal {
    border: 2px solid grey;
    background: #32CC99;
    width: 20px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal {
    border: 2px solid grey;
    background: #32CC99;
    width: 20px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
    border: 2px solid grey;
    width: 3px;
    height: 3px;
    background: white;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}

QScrollBar:horizontal {
    border: 2px solid green;
    background: cyan;
    height: 15px;
    margin: 0px 40px 0 0px;
}

QScrollBar::handle:horizontal {
    background: gray;
    min-width: 20px;
}

QScrollBar::add-line:horizontal {
    background: blue;
    width: 16px;
    subcontrol-position: right;
    subcontrol-origin: margin;
    border: 2px solid black;
}

QScrollBar::sub-line:horizontal {
    background: magenta;
    width: 16px;
    subcontrol-position: top right;
    subcontrol-origin: margin;
    border: 2px solid black;
    position: absolute;
    right: 20px;
}

QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
    width: 3px;
    height: 3px;
    background: pink;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}

QScrollBar:vertical {
     border: 2px solid grey;
     background: #32CC99;
     width: 15px;
     margin: 22px 0 22px 0;
}

QScrollBar::handle:vertical {
     background: white;
     min-height: 20px;
}

QScrollBar::add-line:vertical {
     border: 2px solid grey;
     background: #32CC99;
     height: 20px;
     subcontrol-position: bottom;
     subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical {
     border: 2px solid grey;
     background: #32CC99;
     height: 20px;
     subcontrol-position: top;
     subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
     border: 2px solid grey;
     width: 3px;
     height: 3px;
     background: white;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
     background: none;
}"""

sizegrip = """
QSizeGrip {
    image: url(:/images/sizegrip.png);
    width: 16px;
    height: 16px;
}"""

slider = """
QSlider::groove:horizontal {
    border: 1px solid #999999;
    height: 8px;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);
    margin: 2px 0;
}

QSlider::handle:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
    border: 1px solid #5c5c5c;
    width: 18px;
    margin: -2px 0;
    border-radius: 3px;
}

QSlider::groove:vertical {
    background: red;
    position: absolute;
    left: 4px; right: 4px;
}

QSlider::handle:vertical {
    height: 10px;
    background: green;
    margin: 0 -4px;
}

QSlider::add-page:vertical {
    background: white;
}

QSlider::sub-page:vertical {
    background: pink;
}"""

spinbox = """
QSpinBox {
    padding-right: 15px;
    border-image: url(:/images/frame.png) 4;
    border-width: 3;
}

QSpinBox::up-button {
    subcontrol-origin: border;
    subcontrol-position: top right;
    width: 16px;
    border-image: url(:/images/spinup.png) 1;
    border-width: 1px;
}

QSpinBox::up-button:hover {
    border-image: url(:/images/spinup_hover.png) 1;
}

QSpinBox::up-button:pressed {
    border-image: url(:/images/spinup_pressed.png) 1;
}

QSpinBox::up-arrow {
    image: url(:/images/up_arrow.png);
    width: 7px;
    height: 7px;
}

QSpinBox::up-arrow:disabled, QSpinBox::up-arrow:off {
   image: url(:/images/up_arrow_disabled.png);
}

QSpinBox::down-button {
    subcontrol-origin: border;
    subcontrol-position: bottom right;
    width: 16px;
    border-image: url(:/images/spindown.png) 1;
    border-width: 1px;
    border-top-width: 0;
}

QSpinBox::down-button:hover {
    border-image: url(:/images/spindown_hover.png) 1;
}

QSpinBox::down-button:pressed {
    border-image: url(:/images/spindown_pressed.png) 1;
}

QSpinBox::down-arrow {
    image: url(:/images/down_arrow.png);
    width: 7px;
    height: 7px;
}

QSpinBox::down-arrow:disabled,
QSpinBox::down-arrow:off {
   image: url(:/images/down_arrow_disabled.png);
}"""

splitter = """
QSplitter::handle {
    image: url(images/splitter.png);
}

QSplitter::handle:horizontal {
    width: 2px;
}

QSplitter::handle:vertical {
    height: 2px;
}

QSplitter::handle:pressed {
    url(images/splitter_pressed.png);
}"""

statusbar = """
QStatusBar {
    background: brown;
}

QStatusBar::item {
    border: 1px solid red;
    border-radius: 3px;
}

QStatusBar QLabel {
    border: 3px solid white;
}"""

tabwidget = """
QTabWidget::pane {
    border-top: 2px solid #C2C7CB;
}

QTabWidget::tab-bar {
    left: 5px;
}"""

tabbar = """
QTabBar::tab {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
    border: 2px solid #C4C4C3;
    border-bottom-color: #C2C7CB;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    min-width: 8ex;
    padding: 2px;
}

QTabBar::tab:selected, QTabBar::tab:hover {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,
                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);
}

QTabBar::tab:selected {
    border-color: #9B9B9B;
    border-bottom-color: #C2C7CB;
}

QTabBar::tab:!selected {
    margin-top: 2px;
}

QTabWidget::pane {
    border-top: 2px solid #C2C7CB;
}

QTabWidget::tab-bar {
    left: 5px;
}

QTabBar::tab {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
    border: 2px solid #C4C4C3;
    border-bottom-color: #C2C7CB;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    min-width: 8ex;
    padding: 2px;
}

QTabBar::tab:selected, QTabBar::tab:hover {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,
                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);
}

QTabBar::tab:selected {
    border-color: #9B9B9B;
    border-bottom-color: #C2C7CB;
}

QTabBar::tab:!selected {
    margin-top: 2px;
}

QTabBar::tab:selected {
    margin-left: -4px;
    margin-right: -4px;
}

QTabBar::tab:first:selected {
    margin-left: 0;
}

QTabBar::tab:last:selected {
    margin-right: 0;
}

QTabBar::tab:only-one {
    margin: 0;
}

QTabWidget::pane {
    border-top: 2px solid #C2C7CB;
    position: absolute;
    top: -0.5em;
}

QTabWidget::tab-bar {
    alignment: center;
}

QTabBar::tab {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
    border: 2px solid #C4C4C3;
    border-bottom-color: #C2C7CB;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    min-width: 8ex;
    padding: 2px;
}

QTabBar::tab:selected, QTabBar::tab:hover {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,
                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);
}

QTabBar::tab:selected {
    border-color: #9B9B9B;
    border-bottom-color: #C2C7CB;
}

QTabBar::tear {
    image: url(tear_indicator.png);
}

QTabBar::scroller {
    width: 20px;
}

QTabBar QToolButton {
    border-image: url(scrollbutton.png) 2;
    border-width: 2px;
}

QTabBar QToolButton::right-arrow {
    image: url(rightarrow.png);
}

QTabBar QToolButton::left-arrow {
    image: url(leftarrow.png);
}

QTabBar::close-button {
    image: url(close.png)
    subcontrol-position: left;
}

QTabBar::close-button:hover {
    image: url(close-hover.png)
}"""


tableview="""
QTableView {
    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5,
                                stop: 0 #FF92BB, stop: 1 white);
}

QTableView QTableCornerButton::section {
    background: red;
    border: 2px outset red;
}

QTableView::indicator:unchecked {
    background-color: #d7d6d5
}"""

ToolBar= """QToolBar {
    background: red;
    spacing: 3px;
}

QToolBar::handle {
    image: url(handle.png);
}"""

ToolBox= """QToolBox::tab {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
    border-radius: 5px;
    color: darkgray;
}

QToolBox::tab:selected {
    font: italic;
    color: white;
}"""

ToolButton= """QToolButton {
    border: 2px solid #8f8f91;
    border-radius: 6px;
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #f6f7fa, stop: 1 #dadbde);
}

QToolButton[popupMode="1"] {
    padding-right: 20px;
}

QToolButton:pressed {
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #dadbde, stop: 1 #f6f7fa);
}

QToolButton::menu-button {
    border: 2px solid gray;
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
    width: 16px;
}

QToolButton::menu-arrow {
    image: url(downarrow.png);
}

QToolButton::menu-arrow:open {
    top: 1px; left: 1px;
}"""

ToolTip= """QToolTip {
    border: 2px solid darkkhaki;
    padding: 5px;
    border-radius: 3px;
    opacity: 200;
}"""

TreeView= """QTreeView {
    alternate-background-color: yellow;
}

QTreeView {
    show-decoration-selected: 1;
}

QTreeView::item {
     border: 1px solid #d9d9d9;
    border-top-color: transparent;
    border-bottom-color: transparent;
}

QTreeView::item:hover {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #e7effd, stop: 1 #cbdaf1);
    border: 1px solid #bfcde4;
}

QTreeView::item:selected {
    border: 1px solid #567dbc;
}

QTreeView::item:selected:active{
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #6ea1f1, stop: 1 #567dbc);
}

QTreeView::item:selected:!active {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #6b9be8, stop: 1 #577fbf);
}

QTreeView::branch {
        background: palette(base);
}

QTreeView::branch:has-siblings:!adjoins-item {
        background: cyan;
}

QTreeView::branch:has-siblings:adjoins-item {
        background: red;
}

QTreeView::branch:!has-children:!has-siblings:adjoins-item {
        background: blue;
}

QTreeView::branch:closed:has-children:has-siblings {
        background: pink;
}

QTreeView::branch:has-children:!has-siblings:closed {
        background: gray;
}

QTreeView::branch:open:has-children:has-siblings {
        background: magenta;
}

QTreeView::branch:open:has-children:!has-siblings {
        background: green;
}

QTreeView::branch:has-siblings:!adjoins-item {
    border-image: url(vline.png) 0;
}

QTreeView::branch:has-siblings:adjoins-item {
    border-image: url(branch-more.png) 0;
}

QTreeView::branch:!has-children:!has-siblings:adjoins-item {
    border-image: url(branch-end.png) 0;
}

QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings {
        border-image: none;
        image: url(branch-closed.png);
}

QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings  {
        border-image: none;
        image: url(branch-open.png);
}
"""
