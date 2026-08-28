import subprocess
import shutil


class Automation:

    def open_app(self, command):

        try:

            subprocess.Popen([command],shell=True)

            print("NOVA: Opening Application...")
        except:
            print("I couldn't open that application.")



