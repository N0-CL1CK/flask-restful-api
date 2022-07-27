from routes import main

if __name__ == '__main__':
    main.app.debug=True
    main.app.run(host="0.0.0.0", port=80)