from app import create_app
import os
app = create_app()

if __name__ == '__main__':
    
    h=os.getenv("HOST","127.0.0.1" )
    if(os.getenv("FLASK_ENV")=="development"):
        app.run(host=h,debug=True)
    else:
        app.run(host=h,debug=True)