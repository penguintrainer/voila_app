import subprocess as sp

def main():
    command = "voila --enable_nbextention=True --autoreload=True .\app\notebook\main.ipynb"
    sp.run(command)

if __name__ == "__main__":
    main()