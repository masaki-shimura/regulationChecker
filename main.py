import PySimpleGUI as sg

is_loop = True
layout = [[sg.Text('【 アプリケーションの説明 】')],
          [sg.Text(' 各種リソースが任意のレギュレーション通りになっているか確認する為のツールです')],
          [sg.Button('アプリ終了')]]

window = sg.Window('Regulation Checker', layout)


def initialize():
    """初期化処理"""
    sg.theme('LightGrey4')
    print('初期化処理が呼ばれました')


def finalize():
    """終了処理"""
    print('終了処理が呼ばれました')
    window.close()


def update(is_loop=True):
    """更新処理"""
    print('更新処理が呼ばれました')
    while is_loop:
        event, values = window.read()
        # 終了処理
        if event == sg.WIN_CLOSED or event == 'アプリ終了':
            break


initialize()
update(is_loop)
finalize()
