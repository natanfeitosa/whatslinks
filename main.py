"""Entry point file for WhatsLinks app

version: 0.1.0
"""

from src.app import App


if __name__ == '__main__':
    app = App()
    app.run()

# poetry run python main.py -m screen:phone_moto_g,portrait,scale=.5