from dotenv import load_dotenv
load_dotenv()

from App import Create_App

App = Create_App()

if __name__ == "__main__":
    App.run(debug=True, port=5007)  