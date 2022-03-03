from datetime import datetime


author  = "YP522"
email   = "yp@ypetit.web-edu.fr"
version = "0.0.0"
prefix  = "[PCK]"
line    = "#######################################################################################"
good    = "[√]"
bad     = "[X]"
errors  = ["File Not found", "Not the same size"]
xlsName = "PicCheck-PRO.xlsx"

slogan = "There is no one who was born under a bad star, there are only people who cannot read the sky | Dalaï Lama"

#                                   TIME                                      #
now = datetime.now()
day = now.strftime("%d:%m:%Y")
time = now.strftime("%H:%M:%S")
dt_string = "output/"+now.strftime("%d-%m-%Y-%H-%M-%S")

#                                   CMDS                                      #


def log(elt):
    return print(f"{prefix} {elt}")


credits = f"{prefix} Create by {author}"


help = f"""
{line}
                  PicChecK {version} » HELP | What can I do to help you ?
{line}

    - help    : Get help for execute commands of PicChecK               [PCK]
    - version : Get current version of PicChecK                         [PCK]
    - about   : What is PicCheck ?                                      [PCK]
    - credits : Get current authors of PicChecK                         [PCK]

    - run [img1] [img2] [output]: Get current version of PicChecK       [PCK]

{line}
"""

about = f"""
{line}
                  PicChecK {version} » About | What is PicCheck  ?
{line}

    PicCheck is a free python project for compare similiraty and difference
    between 2 pictures with the sames size.

    PCK gives a global report on the "3C" principle it has adopted

        P
        i
    1.  c o l l e c t           :   ColorAverage, ColorDominante, ColorOccurences
    2.  C o m p a r e           :   % ColorDiff, ColorGap, Delta-E,
        h
        e
    3.  c o m p r e s s i o n   :   Compression Ratio Level, DCT estimate value
        K

    The set of these 3 criteria will form a similarity/difference score
    expressed in percentage [0%-100%] / [100%-0%].

    OutPut :

        * HTML report with comparison details
        * XLSX with data pixel by pixel
        * TXT report synthesis of results

{line}

Credits : {credits}

"""
