from app import electoral_app
from app.api.v2.models.db_conn import Database

app = electoral_app()

if __name__ == "__main__":
    app.run(debug=True)
