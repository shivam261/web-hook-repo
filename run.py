from app import create_app
import os
app = create_app()

if __name__ == '__main__':
    h=os.getenv("HOST","127.0.0.1" )
    app.run(host=h,debug=True)