from flask import Flask, request

def createApp():
    app = Flask("SmartRoute")

    @app.route('/getRoute')
    def getRoute():
        """
        Obtain the shortest route from the first node
        to the second, and return the longitude.
        """
        return 'hi'

    return app

flaskapp = createApp()
flaskapp.run(host='0.0.0.0',port=8000)