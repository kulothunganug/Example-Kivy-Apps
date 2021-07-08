import traceback

from purp import PurpApp

try:
    PurpApp().run()
except Exception:
    error = traceback.format_exc()

    with open("ERROR.log", "w") as error_file:
        error_file.write(error)

    print(error)
