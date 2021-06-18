import os
from dotenv import load_dotenv

from app import app

load_dotenv()


PORT = os.getenv('PORT')
HOST_BACK = os.getenv('HOST_BACK')


if __name__ == '__main__':
    app.run(debug=True,port=PORT,host=HOST_BACK)