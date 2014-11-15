import os
from posts import app, database

def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    database.Base.metadata.create_all(database.engine)
    run()

