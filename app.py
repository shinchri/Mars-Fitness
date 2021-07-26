from flask import Flask, render_template, request, Response, flash, redirect, url_for, abort

def create_app(test_config=None):

    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('pages/home.html')

    return app

app = create_app()

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

if __name__ == '__main__':
    app.run()