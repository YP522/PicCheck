from numpy import histogram_bin_edges
from generate.generateHTML import get_color_by_percentage, reverse_percentage
from generate.funcs.formatted import set_background_by_contast_color
from processing.compression import get_psnr, get_ssim, get_mse
from system import pck_S as s
from charts.css import column


def set_open_html_file(title, style):
    """
    This function returns a string that contains the opening html tags for the report
    
    :param title: The title of the report
    :param style: the name of the css file in the assets/themes folder
    :return: The open_html_file variable is being returned.
    """

    open_html_file = f'''
    <!-- PCK HTML REPORT -->
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
        <head>
            <meta charset="utf-8">
            <title>{title}</title>
            <link rel="stylesheet" href="assets/report.css">
            <link rel="stylesheet" href="assets/themes/{style}.css">  <!-- edit this line to change report css theme -->
            <link rel="icon" type="image/png" href="assets/favicon.png" />
            <link href="http://fonts.cdnfonts.com/css/montserrat" rel="stylesheet">
            <link rel="stylesheet" href="assets/charts.min.css">
        </head>
        <body>
            <div class="header fullscreen">
                <img src="assets/logo.png" alt="A free tool for compare 2 pictures">
            </div>
            <div class="page">    
    '''
    return open_html_file

def set_close_html_file():
    """
    This function closes the html file
    :return: The closing tags for the html file.
    """

    return '''
            </div>
        </body>
    </html>
    '''

def set_profile_of_picture(number, value):
    """
    It takes a number and a value and returns a string
    
    :param number: the number of the picture
    :param value: The percentage of similarity between the two images
    :return: A string with the html code for the profile of the picture.
    """

    profile_of_picture = f'''

                        <div class="text-center">
                            <img src="../data/img{number}.png" alt="A free tool for compare 2 pictures">
                            <h3>IMG {number}</h3>

                            <div class="level l{get_color_by_percentage(value)}">
                                <h4>{value}%</h4>
                            </div>
                        </div>

    '''
    return profile_of_picture

def set_start_compare_zone(title):
    """
    This function creates the start of the compare zone
    
    :param title: The title of the category
    :return: A string of HTML code that will be used to start a new compare zone.
    """

    start_compare_zone = f'''
                        <div class="compareZone">
                            <div>
                                <h2 class="category">{title}</h2>
                                <ul>
    '''

    return start_compare_zone

def set_wigdet_list_for_color_col(title, var1, var2, var3):
    """
    It takes three variables, a title, a color, and two percentages, and returns a string that contains
    a list item with a row that contains a column with the title, and a column with a row that contains
    three columns with the color, and the two percentages
    
    :param title: The title of the widget
    :param var1: The color of the text
    :param var2: the percentage of the color in the image
    :param var3: The percentage of the color in the image
    :return: A string of HTML code that will be used to create a list of items.
    """

    wigdet_list_for_color_col = f'''
                                        <li>
                                            <div class="row">
                                                <div class="column middlescreen">
                                                    {title}
                                                </div>
                                                <div class="column middlescreen">
                                                    <div class="row">
                                                        <div class="column middlescreen tag {set_background_by_contast_color(tuple(var1))}" style="color:rgb{tuple(var1)}">{var1}</div>
                                                        <div class="column middlescreen tag {get_color_by_percentage(var2)}">{var2} %</div>
                                                        <div class="column middlescreen tag {get_color_by_percentage(var3)}">{var3} %</div>
                                                    </div>
                                                </div>
                                
                                            </div>
                                        </li>
    '''
    return wigdet_list_for_color_col


def set_wigdet_list_for_compare(title, var1):
    """
    This function takes in a title and a percentage and returns a list item with the title and the
    percentage in a tag
    
    :param title: The title of the widget
    :param var1: The percentage of the first variable
    :return: A string of HTML code that will be used to create a list of widgets.
    """

    wigdet_list_for_compare = f'''
                                        <li>
                                            <div class="row">
                                                <div class="column middlescreen">
                                                    {title}
                                                </div>
                                                <div class="column middlescreen">
                                                    <div class="row">
                                                        <div class="column middlescreen tag "></div>
                                                        <div class="column middlescreen tag {get_color_by_percentage(var1)}">{var1}%</div>
                                                        <div class="column middlescreen tag {get_color_by_percentage(reverse_percentage(var1))}">{reverse_percentage(var1)}%</div>
                                                    </div>
                                                </div>

                                            </div>
                                        </li>
    '''
    return wigdet_list_for_compare


def set_wigdet_list_for_compression(title, var1, var2, var3):
    """
    It takes in three variables, and returns a string that contains HTML code for a list item
    
    :param title: The title of the widget
    :param var1: The percentage of the original size of the image
    :param var2: The percentage of the original size
    :param var3: The percentage of the original size of the image
    :return: A string of HTML code that will be used to create a list item for the compression widget.
    """

    wigdet_list_for_compression = f'''
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
    return wigdet_list_for_compression

def set_comparison_slider(img1,img2,width,height):
    """
    It takes two images, and returns a slider that compares them
    
    :param img1: the first image to compare
    :param img2: the image on the right
    :param width: width of the slider
    :param height: height of the slider
    :return: A string of HTML code that will be used to create a slider.
    """
    slider = f"""
        <h2 class="category">Image Comparison Slider</h2>
        <div class="row">

            <!-- slider container -->
            <div class="comparison_slider" style="width:{width}px;height:{height}px">

                <!-- image left -->
                <textarea readonly style="background: url('../data/img{img1}.png') no-repeat"></textarea>

                <!-- image right -->
                <textarea readonly style="background: url('../data/img{img2}.png') no-repeat"></textarea>

                <!--  -->
            </div>
            <!--  -->

        </div>    

    """
    return slider


def set_wigdet_for_structure_details(title,value):
    """
    This function takes in two arguments, a title and a value, and returns a string that contains a
    widget for the structure details page
    
    :param title: The title of the parameter
    :param value: The value of the parameter
    :return: A string of HTML code that will be used to display the structure details.
    """

    wigdet_for_structure_details = f'''
                                        <li>
                                            <div class="row">
                                                <div class="column middlescreen">
                                                    {title}
                                                </div>
                                                <div class="column middlescreen">
                                                    <div class="row">
                                                        <div class="column middlescreen tag">{value}</div>
                                                    </div>
                                                </div>

                                            </div>
                                        </li>
    '''
    return wigdet_for_structure_details


def set_structure_comparison_zone(image1,image2):
    """
    It takes two images as input and returns a string that contains the HTML code for the structure
    comparison zone
    
    :param image1: The first image to compare
    :param image2: The second image to compare to the first
    :return: the structure comparison zone.
    """
    structure_comparison_zone = f"""

        <h2 class="category">Image Structure Comparison</h2>

        <div class="compareZone">
            <div>
   
            <ul>
 
            {set_wigdet_for_structure_details("PSNR", get_psnr(s.scan(image1),s.scan(image2)))}

            {set_wigdet_for_structure_details("SSIM", get_ssim(s.scan(image1),s.scan(image2)))}

            {set_wigdet_for_structure_details("MSE", get_mse(s.scan(image1),s.scan(image2)))}                        
            </div>           
            </ul>             
        </div>

    """
    return structure_comparison_zone


def set_widget_for_image_details(title,value):
    """
    It takes in a title and a value and returns a widget for the image details
    
    :param title: The title of the image detail
    :param value: The value of the tag
    :return: A string of HTML code that will be used to display the image details.
    """

    widget_for_image_details = f"""
    
                        <li>
                            <div class="row">
                                <div class="column middlescreen">{title}</div>
                                <div class="column middlescreen">
                                <div class="row">
                                    <div class="column middlescreen tag ">{value}</div>
                                </div>
                                </div>
                            </div>
                        </li>

    """
    return widget_for_image_details

def set_details_comparison_zone(image):
    """
    This function creates a comparison zone for the image details
    
    :param image: The image to be analyzed
    :return: A string of HTML code that will be used to display the image details.
    """

    details_comparison_zone = f"""
    
        <div class="column middlescreen">
        <div class="compareZone">
            <div>
                <h2 class="category">Image Details</h2>
                <ul>
                    <div>
                    <ul>
                        {set_widget_for_image_details("Entropy",image.entropy())}

                        {set_widget_for_image_details("EXIF",image.getexif())}
                    </ul>
                    <br>
                    </div>
                </ul>
            </div>
        </div>
        </div>


    """

    return details_comparison_zone


def set_histogram_graphcss_graph(image):
    """
    It takes an image and returns a graph of the image's histogram.
    
    :param image: The image to be displayed
    :return: A string of HTML code that will be used to display the histogram of the image.
    """
    histogram_graphcss_graph = f"""
        <div class="column middlescreen">    
    """;

    histo = image.histogram()
    histo.insert(0, "image")

    chart = column(
    [
        ["image"],
        histo
    ],
        headers_in_first_row=True,
        headers_in_first_column=True,
    )
    
    histogram_graphcss_graph += chart
    histogram_graphcss_graph += """
        </div>""";

    return histogram_graphcss_graph