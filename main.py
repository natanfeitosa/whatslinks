"""Entry point file for WhatsLinks app

version: 0.1.0
"""

from src.app import App


if __name__ == '__main__':
    # app = App()
    # app.run()

    from kivy.lang.builder import Builder
    from kivymd.tools.hotreload.app import MDApp


    class HotReloadApp(App, MDApp):
        KV_FILES = [
            'src/app.kv',
            'src/screens/home.kv',
            'src/screens/qrcode.kv',
            'src/screens/history.kv',
        ]
        DEBUG = True

        def build_app(self):
            return Builder.load_file('src/app.kv')

    HotReloadApp().run()

# poetry run python main.py -m screen:phone_moto_g,portrait,scale=.5