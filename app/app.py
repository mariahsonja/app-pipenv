from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def page():
        return 'Hello, Earth!'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=8080)
