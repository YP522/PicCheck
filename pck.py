# _________________________________________________________________________________________________________________________________ #
#                                                                                                                                   #
#        ________    ___      ________                  ________      ___  ___      _______       ________      ___  ___            #
#       |\   __  \  |\  \    |\   ____\                |\   ____\    |\  \|\  \    |\  ___ \     |\   ____\    |\  \|\  \           #
#       \ \  \|\  \ \ \  \   \ \  \___|                \ \  \___|    \ \  \\\  \   \ \   __/|    \ \  \___|    \ \  \/  /|_         #
#        \ \   ____\ \ \  \   \ \  \        T U r E s   \ \  \        \ \   __  \   \ \  \_|/__   \ \  \        \ \   ___  \        #
#         \ \  \___|  \ \  \   \ \  \____    t u R e S   \ \  \____    \ \  \ \  \   \ \  \_|\ \   \ \  \____    \ \  \\ \  \       #
#          \ \__\      \ \__\   \ \_______\               \ \_______\   \ \__\ \__\   \ \_______\   \ \_______\   \ \__\\ \__\      #
#           \|__|       \|__|    \|_______|                \|_______|    \|__|\|__|    \|_______|    \|_______|    \|__| \|__|      #
#                                                                                                                                   #
# _________________________________________________________________________________________________________________________________ #

from system import utils as u
import system.pck_S as s
import typer
#####################################################################################################################################

class main():

    # Start Script
    app = typer.Typer()

    # Open help
    @app.command()
    def help():
        typer.echo(u.help)

    # Get the current version
    @app.command()
    def version():
        typer.echo(f"{u.prefix} PicChecK version : {u.version}")

    # Learn more about PicChecK
    @app.command()
    def about():
        typer.echo(u.about)

    # Learn more about PicChecK
    @app.command()
    def credits():
        typer.echo(u.credits)

    # Start the 3C execution between 2 selected pictures
    @app.command()
    def run(img1: str, img2: str):
        s.run(img1,img2)

    # init app
    if __name__ == "__main__":
        app()