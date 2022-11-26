from numpy import histogram_bin_edges
from generate.generateHTML import get_color_by_percentage, reverse_percentage
from generate.funcs.formatted import set_background_by_contast_color
from processing.compression import get_psnr, get_ssim, get_mse
from system import pck_S as s
from charts.css import column

def tag(tag, attributes={}, content=""):
    attribute_string = " ".join(['{}="{}"'.format(key, value) for key, value in attributes.items()])
    
    if tag=="img" or tag=="link" or tag=="meta":
        return "<{tag} {attributes}>".format(tag=tag,attributes=attribute_string)
    elif tag=="!type":
        return "<!DOCTYPE {content}>".format(content=content)
    elif tag=="!--" :
        return "<!-- {content} -->".format(content=content)        
    
    return "<{tag} {attributes}>{content}</{tag}>".format(tag=tag, attributes=attribute_string, content=content)


def set_html(content):
    """
    It takes a string of HTML content and returns a string of HTML content
    
    :param content: The content of the HTML file
    :return: The html tag with the content of the head and body tags.
    """
    
    html = tag("!--",{},"PCK HTML REPORT")+tag("!type",{},"html")+tag(
        "html",
        {"lang":"en", "dir":"ltr"},
        content,
    )
    return html


def set_header(title,style):
    """
    This function returns a string that contains the opening html tags for the report
    
    :param title: The title of the report
    :param style: the name of the css file in the assets/themes folder
    :return: The open_html_file variable is being returned.
    """

    html = tag("head",{},
        tag("meta",{"charset":"utf-8"})+
        tag("title",{},title)+
        tag("link",{"rel":"stylesheet","href":"assets/report.css"})+
        tag("link",{"rel":"stylesheet","href":f"assets/themes/{style}.css"})+"  "+tag("!--",{},"edit this line to change report css theme")+
        tag("link",{"rel":"icon","type":"image/png","href":"assets/favicon.png"})+
        tag("link",{"href":"https://fonts.cdnfonts.com/css/montserrat","rel":"stylesheet"})+
        tag("link",{"rel":"stylesheet","href":"assets/charts.min.css"})
    )
    return html


def set_body(header,content):
    """
    > The function `set_body` takes two arguments, `header` and `content`, and returns a string that is
    the HTML for a body tag with the header and content inside it
    
    :param header: the header of the page
    :param content: the content of the page
    :return: The body tag with the header and content
    """

    return tag(
    "body", 
    {},
    header+content)
    

def set_profile_of_picture(number, value):
    """
    It takes a number and a value and returns a string
    
    :param number: the number of the picture
    :param value: The percentage of similarity between the two images
    :return: A string with the html code for the profile of the picture.
    """

    profile_of_picture = tag("div",{"class": "text-center"},
            tag("img",{"src":f"../data/img{number}.png","alt":"A free tool for compare 2 pictures"},"")+
            tag("h3",{},f"IMG {number}")+
            tag("div",{"class":f"level l{get_color_by_percentage(value)}"},tag("h4",{},f"{value}%"))
        )
    

    return profile_of_picture


def set_compare_zone(title, content):
    start_compare_zone = tag(
        "div",
        {"class":"compareZone"},
        tag(
            "div",
            {},
            tag(
                "h2",
                {"class":"category"},
                title
            )+content
        )
    )
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

    wigdet_list_for_color_col = tag(
        "li",
        {},
        tag(
            "div",
            {"class":"row"}, 
            tag("div", {"class":"column middlescreen"},title)+
            tag(
                "div",
                {"class":"column middlescreen"},
                tag(
                    "div",
                    {"class":"row"},
                        tag("div",{"class":f"column middlescreen tag {set_background_by_contast_color(tuple(var1))}", "style":f"color:rgb{tuple(var1)}"},var1)+
                        tag("div",{"class":f"column middlescreen tag {get_color_by_percentage(var2)}"},f"{var2} %")+
                        tag("div",{"class":f"column middlescreen tag {get_color_by_percentage(var3)}"},f"{var3} %")
                )
            )
        )
    )

    return wigdet_list_for_color_col


def set_wigdet_list_for_compare(title, var1):
    """
    This function takes in a title and a percentage and returns a list item with the title and the
    percentage in a tag
    
    :param title: The title of the widget
    :param var1: The percentage of the first variable
    :return: A string of HTML code that will be used to create a list of widgets.
    """

    wigdet_list_for_compare = tag("li",{},
                                tag("div",{"class":"row"},
                                    tag("div",{"class":"column middlescreen"},title)+tag("div",{"class":"column middlescreen"},
                                        tag("div",{"class":"row"},
                                            tag("div",{"class":"column middlescreen tag"},"")+
                                            tag("div",{"class":f"column middlescreen tag {get_color_by_percentage(var1)}"},f"{var1}%")+
                                            tag("div",{"class":f"column middlescreen tag {get_color_by_percentage(reverse_percentage(var1))}"},f"{reverse_percentage(var1)}%")
                                        ))
                                    )
                                )
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

    wigdet_list_for_compression = tag("li",{"class":"row"},
                                          tag("div",{"class":"column middlescreen"},title)+
                                          tag("div",{"class":"column middlescreen"},
                                              tag("div",{"class":"row"},
                                                  tag("div",{"class":"column middlescreen tag"},f"{var1} %")+
                                                  tag("div",{"class":f"column middlescreen tag {get_color_by_percentage(var2)}"},f"{var2} %")+
                                                  tag("div",{"class":f"column middlescreen tag {get_color_by_percentage(var3)}"},f"{var3} %")
                                              )
                                          )
                                      )

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

    slider = tag("h2",{"class":"category"},"Image Comparison Slider")+tag("div",{"class":"row"},
                tag("!--",{},"slider container")+
                tag("div",{"class":"comparison_slider", "style":f"width:{width}px;height:{height}px"},
                    tag("!--",{},"image left")+
                    tag("textarea",{"readonly":"","style":f"background: url('../data/img{img1}.png') no-repeat"},"")+
                    tag("!--",{},"image right")+
                    tag("textarea",{"readonly":"","style":f"background: url('../data/img{img2}.png') no-repeat"},"")
                )
             )
    return slider


def set_wigdet_for_structure_details(title,value):
    """
    This function takes in two arguments, a title and a value, and returns a string that contains a
    widget for the structure details page
    
    :param title: The title of the parameter
    :param value: The value of the parameter
    :return: A string of HTML code that will be used to display the structure details.
    """

    wigdet_for_structure_details = tag("li",{},tag("div",{"class":"row"},tag("div",{"class":"column middlescreen"},title)+tag("div",{"class":"column middlescreen"},tag("div",{"class":"row"},tag("div",{"class":"column middlescreen tag"},value)))))
    return wigdet_for_structure_details


def set_structure_comparison_zone(image1,image2):
    """
    It takes two images as input and returns a string that contains the HTML code for the structure
    comparison zone
    
    :param image1: The first image to compare
    :param image2: The second image to compare to the first
    :return: the structure comparison zone.
    """

    structure_comparison_zone = tag("h2",{"class":"category"},"Image Structure Comparison")+tag("div",{"class":"compareZone"},
        tag("div",{},tag("ul",{},
            set_wigdet_for_structure_details("PSNR", get_psnr(s.scan(image1),s.scan(image2)))+
            set_wigdet_for_structure_details("SSIM", get_ssim(s.scan(image1),s.scan(image2)))+
            set_wigdet_for_structure_details("MSE", get_mse(s.scan(image1),s.scan(image2))))
        )
    )

    return structure_comparison_zone


def set_widget_for_image_details(title,value):
    """
    It takes in a title and a value and returns a widget for the image details
    
    :param title: The title of the image detail
    :param value: The value of the tag
    :return: A string of HTML code that will be used to display the image details.
    """

    widget_for_image_details = tag("li",{},tag("div",{"class":"row"},tag("div",{"class":"column middlescreen"},title)+tag("div",{"class":"column middlescreen"},tag("div",{"class":"row"},tag("div",{"class":"column middlescreen tag"},value)))))

    return widget_for_image_details


def set_details_comparison_zone(image):
    """
    This function creates a comparison zone for the image details
    
    :param image: The image to be analyzed
    :return: A string of HTML code that will be used to display the image details.
    """

    details_comparison_zone = tag("div",{"class":"column middlescreen"},tag("div",{"class":"compareZone"},tag("div",{},tag("h2",{"class":"category"},"Image Details")+tag("ul",{},tag("div",{},tag("ul",{},set_widget_for_image_details("Entropy",image.entropy())+set_widget_for_image_details("EXIF",image.getexif())+tag("br",{},"")))))))

    return details_comparison_zone


def set_histogram_graphcss_graph(image):
    """
    It takes an image and returns a graph of the image's histogram.
    
    :param image: The image to be displayed
    :return: A string of HTML code that will be used to display the histogram of the image.
    """

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
    
    histogram_graphcss_graph = tag("div",{"class":"column middlescreen"},chart)

    return histogram_graphcss_graph


