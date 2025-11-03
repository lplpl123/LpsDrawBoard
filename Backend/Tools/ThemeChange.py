


def WidgetsThemeChange(colorFront, colorBack,
                       titleFrame, savedLabel, title,
                       menu):

    titleFrame.setStyleSheet(f"""
        background-color: rgb{colorFront}
        """)

    savedLabel.setStyleSheet("""
        QLabel{
        font-family: "微软雅黑";
        color: rgb""" + str(colorBack) + """
        }
        """)

    title.setStyleSheet("""
        QWidget{
        font-family: "微软雅黑";
        font-size: 20px;
        font-weight: bold;
        border: None;
        color: rgb""" + str(colorBack) + """
        }
        """)

    menu.setStyleSheet("""
        QMenu{
        font-family: "微软雅黑";
        font-size: 20px;
        font-weight: bold;
        border: None;
        color: rgb""" + str(colorBack) + """;
        background-color: rgb""" + str(colorFront) + """
        }
        QMenu::item:selected{color: rgb""" + str(colorFront) + """;
        background-color: rgb""" + str(colorBack) + """}
        """)