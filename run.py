from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    h = os.getenv("HOST", "0.0.0.0")
    p = int(os.getenv("PORT", 5000))
    app.run(host=h, port=p, debug=False)
