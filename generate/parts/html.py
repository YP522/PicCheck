from generate.generateHTML import *
from generate.funcs.formatted import *


def set_open_html_file(title, style):

    openHtmlFile = f'''
    <!-- PCK HTML REPORT -->
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
        <head>
            <meta charset="utf-8">
            <title>{title}</title>
            <link rel="stylesheet" href="assets/report.css">
            <link rel="stylesheet" href="assets/themes/{style}.css">  <!-- edit this line to change report css theme -->
            <link rel="icon" type="image/png" href="assets/favicon.png" />
        </head>
        <body>
            <div class="header fullscreen">
                <img src="assets/logo.png" alt="A free tool for compare 2 pictures">
            </div>
            <div class="page">    
    '''
    return openHtmlFile

def set_close_html_file():

    return '''
            </div>
        </body>
    </html>
    '''

def set_profile_of_picture(number, value):

    profileOfPicture = f'''

                        <div class="text-center">
                            <img src="../data/img{number}.png" alt="A free tool for compare 2 pictures">
                            <h3>IMG {number}</h3>

                            <div class="level l{get_color_by_percentage(value)}">
                                <h4>{value}%</h4>
                            </div>
                        </div>

    '''
    return profileOfPicture

def set_start_compare_zone(title):

    startCompareZone = f'''
                        <div class="compareZone">
                            <div>
                                <h2 class="category">{title}</h2>
                                <ul>
    '''

    return startCompareZone

def set_wigdet_list_for_color_col(title, var1, var2, var3):

    WigdetListForColorCol = f'''
                                        <li>
                                            <div class="row">
                                                <div class="column middlescreen">
                                                    {title}
                                                </div>
                                                <div class="column middlescreen">
                                                    <div class="row">
                                                        <div class="column middlescreen tag {set_Background_By_Contast_Color(tuple(var1))}" style="color:rgb{tuple(var1)}">{var1}</div>
                                                        <div class="column middlescreen tag {get_color_by_percentage(var2)}">{var2} %</div>
                                                        <div class="column middlescreen tag {get_color_by_percentage(var3)}">{var3} %</div>
                                                    </div>
                                                </div>
                                
                                            </div>
                                        </li>
    '''
    return WigdetListForColorCol


def set_wigdet_list_for_compare(title, var1):

    WigdetListForCompare = f'''
                                        <li>
                                            <div class="row">
                                                <div class="column middlescreen">
                                                    {title}
                                                </div>
                                                <div class="column middlescreen">
                                                    <div class="row">
                                                        <div class="column middlescreen tag "></div>
                                                        <div class="column middlescreen tag {get_color_by_percentage(var1)}">{var1}%</div>
                                                        <div class="column middlescreen tag {get_color_by_percentage(reversePercentage(var1))}">{reversePercentage(var1)}%</div>
                                                    </div>
                                                </div>

                                            </div>
                                        </li>
    '''
    return WigdetListForCompare


def set_wigdet_list_for_compression(title, var1, var2, var3):

    WigdetListForCompression = f'''
                                        <li>
                                            <div class="row">
                                                <div class="column middlescreen">
                                                    {title}
                                                </div>
                                                <div class="column middlescreen">
                                                    <div class="row">
                                                        <div class="column middlescreen tag">{var1} %</div>
                                                        <div class="column middlescreen tag {get_color_by_percentage(var2)}">{var2} %</div>
                                                        <div class="column middlescreen tag {get_color_by_percentage(var3)}">{var3} %</div>
                                                    </div>
                                                </div>

                                            </div>
                                        </li>
    '''
    return WigdetListForCompression

