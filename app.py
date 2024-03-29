
from flask import Flask
from views.stores import store_blueprint
from views.alerts import alert_blueprint

app = Flask(__name__)

app.register_blueprint(store_blueprint, url_prefix="/items")
app.register_blueprint(alert_blueprint, url_prefix="/alerts")

if __name__ == "__main__":
    app.run(debug=True)
