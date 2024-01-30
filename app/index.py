from .app import app


if __name__ == "__main__":
  app.run(app, debug=True, port=5100)