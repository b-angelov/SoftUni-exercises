import os


def zip_current_project():
    '''Place this file in the folder containing your project directory and run it.\n
            A project zip will be created, excluding __pycache__ directory, which occupies space.\n
            Suitable for Windows 10/11 and Unix based systems, supporting tar'''
    os.system(f"tar --exclude __pycache__ -acvf project.zip project")


if __name__ == "__main__":
    zip_current_project()