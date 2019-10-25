from app import app
import os

def main(host='127.0.0.1', port=None):
    for port in range(5000, 5100):
        try:
            app.run(debug=True, host=host, port=port)
            break
        except OSError as e:
            if 'Address in use' in str(e):
                continue

if __name__ == "__main__":
    main()