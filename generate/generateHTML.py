from PIL import Image

from generate.funcs.formatted import around_value, clean_list, reverse_percentage, get_percentage_between, get_color_by_percentage
from generate.generateCSS import generate_default_themes, generate_report_css
from generate.generateTXT import generate_txt
from generate.parts.favicon import generate_fav_icon
from generate.parts.html import set_body, set_details_comparison_zone, set_html, set_profile_of_picture, set_wigdet_list_for_color_col, set_compare_zone, set_header, set_comparison_slider, set_structure_comparison_zone, set_histogram_graphcss_graph, set_wigdet_list_for_compare, set_wigdet_list_for_compression, tag
from generate.parts.logo import generate_logo

from processing.collect import get_color_occurences, get_color_average,get_color_dominante
from processing.compare import get_color_differences, get_diff
from processing.compression import get_compression_level

from system import utils as u

page_title = "My report"


def generate_html(nor_img1, nor_img2):
    """
    It generates the html file that will be used to display the report
    
    :param nor_img1: The first image to compare
    :param nor_img2: The image to compare to
    """

    gra_img1 = Image.open(f"{u.dt_string}/data/gra_img1.png").convert('RGB')
    gra_img2 = Image.open(f"{u.dt_string}/data/gra_img2.png").convert('RGB')

    # revoir nomination des variables images

    col_nor_occ = around_value(get_color_occurences(nor_img1, nor_img2)[1])
    col_nor_avg_img_1 = get_color_average(nor_img1, nor_img2)[0]
    col_nor_avg_img_2 = get_color_average(nor_img1, nor_img2)[1]
    for_col_nor_avg_img_1 = clean_list(col_nor_avg_img_1)
    for_col_nor_avg_img_2 = clean_list(col_nor_avg_img_2)
    pc_col_avg = get_diff(col_nor_avg_img_1, col_nor_avg_img_2, 0)
    col_nor_dom_img_1 = clean_list(get_color_dominante(nor_img1, nor_img2)[0])
    col_nor_dom_img_2 = clean_list(get_color_dominante(nor_img1, nor_img2)[1])
    for_col_nor_dom_img_1 = clean_list(col_nor_dom_img_1)
    for_col_nor_dom_img_2 = clean_list(col_nor_dom_img_2)
    pc_col_dom = get_diff(col_nor_dom_img_1, col_nor_dom_img_2, 0)

    col_gra_occ = around_value(get_color_occurences(gra_img1, gra_img2)[1])
    col_gra_avg_img_1 = get_color_average(gra_img1, gra_img2)[0]
    col_gra_avg_img_2 = get_color_average(gra_img1, gra_img2)[1]
    for_col_gra_avg_img_1 = clean_list(col_gra_avg_img_1)
    for_col_gra_avg_img_2 = clean_list(col_gra_avg_img_2)
    pc_gra_col_avg = get_diff(col_gra_avg_img_1, col_gra_avg_img_2, 0)
    col_gra_dom_img_1 = clean_list(get_color_dominante(gra_img1, gra_img2)[0])
    col_gra_dom_img_2 = clean_list(get_color_dominante(gra_img1, gra_img2)[1])
    for_col_gra_dom_img_1 = clean_list(col_gra_dom_img_1)
    for_col_gra_dom_img_2 = clean_list(col_gra_dom_img_2)
    pc_gra_col_dom = get_diff(col_gra_dom_img_1, col_gra_dom_img_2, 0)

    com_nor_dif_img_1 = around_value(get_color_differences(nor_img1, nor_img2)/(nor_img1.width*nor_img1.height)*100)
    com_nor_dif_img_2 = around_value(get_color_differences(nor_img1, nor_img2)/(nor_img1.width*nor_img1.height)*100)

    com_gra_dif_img_1 = around_value(get_color_differences(gra_img1, gra_img2)/(gra_img1.width*gra_img1.height)*100)
    com_gra_dif_img_2 = around_value(get_color_differences(gra_img1, gra_img2)/(gra_img1.width*gra_img1.height)*100)

    cmp_nor_lvl_img_1 = around_value(get_compression_level(nor_img1, "img1"))
    cmp_nor_lvl_img_2 = around_value(get_compression_level(nor_img2, "img2"))

    cmp_gra_lvl_img_1 = around_value(get_compression_level(gra_img1, "gra_img1"))
    cmp_gra_lvl_img_2 = around_value(get_compression_level(gra_img2, "gra_img2"))

    lvl_img1 = around_value(
        col_nor_occ
        + reverse_percentage(pc_col_avg)
        + reverse_percentage(pc_col_dom)
        + col_gra_occ
        + reverse_percentage(pc_gra_col_avg)
        + reverse_percentage(pc_gra_col_dom)
        + com_nor_dif_img_1
        + com_gra_dif_img_1
        + around_value(reverse_percentage(get_percentage_between(cmp_nor_lvl_img_2, cmp_nor_lvl_img_1)))
        + around_value(reverse_percentage(get_percentage_between(cmp_gra_lvl_img_2, cmp_gra_lvl_img_1)))
        )/10

    lvl_img2 = reverse_percentage(around_value(lvl_img1))

    header = tag(
        "div",
        {"class":"header fullscreen"},
        tag("img",{"src":"assets/logo.png","alt":"A free tool for compare 2 pictures"})
    )

    html = set_html(
    set_header("My report","Viridis")+
    set_body(
        header,
        tag("div",{"class": "page"},
            tag("div",{"class": "row"},
                tag("div",{"class":"column middlescreen"},
                set_profile_of_picture("1",lvl_img1)+
                set_compare_zone("ColorCollect",
                    tag("ul",{},
                        tag("li",{},"Normal"+
                            tag("ul",{},
                                set_wigdet_list_for_color_col("ColorOccurences","",col_nor_occ,reverse_percentage(col_nor_occ))+
                                set_wigdet_list_for_color_col("ColorAverage",for_col_nor_avg_img_1,reverse_percentage(pc_col_avg),pc_col_avg)+
                                set_wigdet_list_for_color_col("ColorDominante",for_col_nor_dom_img_1,reverse_percentage(pc_col_dom),pc_col_dom)
                                )
                            )+
                        tag("br",{},"")+
                        tag("li",{},"GrayScale"+
                            tag("ul",{},
                                set_wigdet_list_for_color_col("ColorOccurences","",col_gra_occ,reverse_percentage(col_gra_occ))+
                                set_wigdet_list_for_color_col("ColorAverage",for_col_gra_avg_img_1,reverse_percentage(pc_gra_col_avg),pc_gra_col_avg)+
                                set_wigdet_list_for_color_col("ColorDominante",for_col_gra_dom_img_1,reverse_percentage(pc_gra_col_dom),pc_gra_col_dom)
                                )
                            )
                        )
                    )+
                set_compare_zone("ColorCompare",
                    tag("ul",{},
                        tag("li",{},"Normal"+            
                            tag("ul",{},
                                    set_wigdet_list_for_compare("ColorDifference",com_nor_dif_img_1)
                                    )
                                )+
                            tag("br",{},"")+
                            tag("li",{},"GrayScale"+
                                tag("ul",{},
                                    set_wigdet_list_for_compare("ColorDifference",com_gra_dif_img_1)
                                    )
                                )
                            )
                        )+
                set_compare_zone("Compression",
                    tag("ul",{},
                        tag("li",{},"Normal"+            
                            tag("ul",{},
                                    set_wigdet_list_for_compression("COMPRESSION LEVEL",cmp_nor_lvl_img_1,around_value(reverse_percentage(get_percentage_between(cmp_nor_lvl_img_2,cmp_nor_lvl_img_1))),around_value(get_percentage_between(cmp_nor_lvl_img_2,cmp_nor_lvl_img_1)))
                                    )
                                )+
                            tag("br",{},"")+
                            tag("li",{},"GrayScale"+
                                tag("ul",{},
                                    set_wigdet_list_for_compression("COMPRESSION LEVEL",cmp_gra_lvl_img_1,around_value(reverse_percentage(get_percentage_between(cmp_gra_lvl_img_2,cmp_gra_lvl_img_1))),around_value(get_percentage_between(cmp_gra_lvl_img_2,cmp_gra_lvl_img_1)))
                                    )
                                )
                            )
                        ))+tag("div",{"class":"column middlescreen"},
                set_profile_of_picture("2",lvl_img2)+
                set_compare_zone("ColorCollect",
                    tag("ul",{},
                        tag("li",{},"Normal"+
                            tag("ul",{},
                                set_wigdet_list_for_color_col("ColorOccurences","",col_nor_occ,reverse_percentage(col_nor_occ))+
                                set_wigdet_list_for_color_col("ColorAverage",for_col_nor_avg_img_2,reverse_percentage(pc_col_avg),pc_col_avg)+
                                set_wigdet_list_for_color_col("ColorDominante",for_col_nor_dom_img_2,reverse_percentage(pc_col_dom),pc_col_dom)
                                )
                            )+
                        tag("br",{},"")+
                        tag("li",{},"GrayScale"+
                            tag("ul",{},
                                set_wigdet_list_for_color_col("ColorOccurences","",col_gra_occ,reverse_percentage(col_gra_occ))+
                                set_wigdet_list_for_color_col("ColorAverage",for_col_gra_avg_img_2,reverse_percentage(pc_gra_col_avg),pc_gra_col_avg)+
                                set_wigdet_list_for_color_col("ColorDominante",for_col_gra_dom_img_2,reverse_percentage(pc_gra_col_dom),pc_gra_col_dom)
                                )
                            )
                        )
                    )+
                set_compare_zone("ColorCompare",
                    tag("ul",{},
                        tag("li",{},"Normal"+            
                            tag("ul",{},
                                    set_wigdet_list_for_compare("ColorDifference",com_nor_dif_img_2)
                                    )
                                )+
                            tag("br",{},"")+
                            tag("li",{},"GrayScale"+
                                tag("ul",{},
                                    set_wigdet_list_for_compare("ColorDifference",com_gra_dif_img_2)
                                    )
                                )
                            )
                        )+
                set_compare_zone("Compression",
                    tag("ul",{},
                        tag("li",{},"Normal"+            
                            tag("ul",{},
                                    set_wigdet_list_for_compression("COMPRESSION LEVEL",cmp_nor_lvl_img_2,around_value(reverse_percentage(get_percentage_between(cmp_nor_lvl_img_2,cmp_nor_lvl_img_1))),around_value(get_percentage_between(cmp_nor_lvl_img_2,cmp_nor_lvl_img_1)))
                                    )
                                )+
                            tag("br",{},"")+
                            tag("li",{},"GrayScale"+
                                tag("ul",{},
                                    set_wigdet_list_for_compression("COMPRESSION LEVEL",cmp_gra_lvl_img_2,around_value(reverse_percentage(get_percentage_between(cmp_gra_lvl_img_2,cmp_gra_lvl_img_1))),around_value(get_percentage_between(cmp_gra_lvl_img_2,cmp_gra_lvl_img_1)))
                                    )
                                )
                            )
                        )      
                    )               
                )+
                set_comparison_slider("2","1",nor_img1.width, nor_img1.height)+
                set_structure_comparison_zone(nor_img1,nor_img2)+
                tag("div",
                {"class":"row"},
                    set_details_comparison_zone(nor_img1)+
                    set_details_comparison_zone(nor_img2)
                )+
                tag("h2",{"class":"category"},"Image Histogram")+
                tag("div",{"class":"row"},set_histogram_graphcss_graph(nor_img1)+set_histogram_graphcss_graph(nor_img2))
            )
        )
   
    )
    

    with open(u.dt_string+'/report/report.html', 'w') as f:
        f.write(html)
    generate_fav_icon(16, tuple(for_col_nor_avg_img_2), tuple(for_col_nor_avg_img_1))
    generate_logo()
    generate_report_css()
    generate_default_themes()
