from PIL import Image

from generate.funcs.formatted import around_value, cleanList, reversePercentage, get_percentage_between, get_color_by_percentage
from generate.generateCSS import generate_default_themes, generate_report_css
from generate.generateTXT import generate_txt
from generate.parts.favicon import generate_fav_icon
from generate.parts.html import set_profile_of_picture, set_wigdet_list_for_color_col, set_wigdet_list_for_compare, set_wigdet_list_for_compression, set_close_html_file, set_open_html_file, set_start_compare_zone
from generate.parts.logo import generate_logo

from processing.collect import get_color_occurences, get_color_average,get_color_dominante
from processing.compare import get_color_differences, get_diff
from processing.compression import get_compression_level

from system import utils as u

page_title = "My report"


def generate_html(nor_img1, nor_img2):

    gra_img1 = Image.open(f"{u.dt_string}/data/gra_img1.png").convert('RGB')
    gra_img2 = Image.open(f"{u.dt_string}/data/gra_img2.png").convert('RGB')

    # revoir nomination des variables images

    col_nor_occ = around_value(get_color_occurences(nor_img1, nor_img2)[1])
    col_nor_avg_img_1 = get_color_average(nor_img1, nor_img2)[0]
    col_nor_avg_img_2 = get_color_average(nor_img1, nor_img2)[1]
    for_col_nor_avg_img_1 = cleanList(col_nor_avg_img_1)
    for_col_nor_avg_img_2 = cleanList(col_nor_avg_img_2)
    pc_col_avg = get_diff(col_nor_avg_img_1, col_nor_avg_img_2, 0)
    col_nor_dom_img_1 = cleanList(get_color_dominante(nor_img1, nor_img2)[0])
    col_nor_dom_img_2 = cleanList(get_color_dominante(nor_img1, nor_img2)[1])
    for_col_nor_dom_img_1 = cleanList(col_nor_dom_img_1)
    for_col_nor_dom_img_2 = cleanList(col_nor_dom_img_2)
    pc_col_dom = get_diff(col_nor_dom_img_1, col_nor_dom_img_2, 0)

    col_gra_occ = around_value(get_color_occurences(gra_img1, gra_img2)[1])
    col_gra_avg_img_1 = get_color_average(gra_img1, gra_img2)[0]
    col_gra_avg_img_2 = get_color_average(gra_img1, gra_img2)[1]
    for_col_gra_avg_img_1 = cleanList(col_gra_avg_img_1)
    for_col_gra_avg_img_2 = cleanList(col_gra_avg_img_2)
    pc_gra_col_avg = get_diff(col_gra_avg_img_1, col_gra_avg_img_2, 0)
    col_gra_dom_img_1 = cleanList(get_color_dominante(gra_img1, gra_img2)[0])
    col_gra_dom_img_2 = cleanList(get_color_dominante(gra_img1, gra_img2)[1])
    for_col_gra_dom_img_1 = cleanList(col_gra_dom_img_1)
    for_col_gra_dom_img_2 = cleanList(col_gra_dom_img_2)
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
        + reversePercentage(pc_col_avg)
        + reversePercentage(pc_col_dom)
        + col_gra_occ
        + reversePercentage(pc_gra_col_avg)
        + reversePercentage(pc_gra_col_dom)
        + com_nor_dif_img_1
        + com_gra_dif_img_1
        + around_value(reversePercentage(get_percentage_between(cmp_nor_lvl_img_2, cmp_nor_lvl_img_1)))
        + around_value(reversePercentage(get_percentage_between(cmp_gra_lvl_img_2, cmp_gra_lvl_img_1)))
        )/10

    lvl_img2 = reversePercentage(around_value(lvl_img1))

    html = f'''
        {set_open_html_file(page_title,"Viridis")}
                <div class="row">
                    <div class="column middlescreen">
                    {set_profile_of_picture("1",lvl_img1)}

                        {set_start_compare_zone("ColorCollect")}
                                <li>

                                    Normal

                                    <ul>

                                        {set_wigdet_list_for_color_col("ColorOccurences","",col_nor_occ,reversePercentage(col_nor_occ))}

                                        {set_wigdet_list_for_color_col("ColorAverage",for_col_nor_avg_img_1,reversePercentage(pc_col_avg),pc_col_avg)}

                                        {set_wigdet_list_for_color_col("ColorDominante",for_col_nor_dom_img_1,reversePercentage(pc_col_dom),pc_col_dom)}

                                    </ul>

                                    <br>

                                <li>

                                    GrayScale

                                    <ul>

                                        {set_wigdet_list_for_color_col("ColorOccurences","",col_gra_occ,reversePercentage(col_gra_occ))}

                                        {set_wigdet_list_for_color_col("ColorAverage",for_col_gra_avg_img_1,reversePercentage(pc_gra_col_avg),pc_gra_col_avg)}

                                        {set_wigdet_list_for_color_col("ColorDominante",for_col_gra_dom_img_1,reversePercentage(pc_gra_col_dom),pc_gra_col_dom)}

                                    </ul>
                                </li>
                            </ul>
                        </div>
                    </div>
                        {set_start_compare_zone("ColorCompare")}
                                    <li>

                                        Normal

                                        <ul>

                                            {set_wigdet_list_for_compare("ColorDifference",com_nor_dif_img_1)}

                                        </ul>

                                    <br>

                                    <li>

                                        GrayScale

                                        <ul>

                                            {set_wigdet_list_for_compare("ColorDifference",com_gra_dif_img_1)}

                                        </ul>

                                    </li>
                                </ul>
                            </div>
                        </div>

                        {set_start_compare_zone("Compression")}
                                    <li>

                                        Normal

                                        <ul>

                                            {set_wigdet_list_for_compression("COMPRESSION LEVEL",cmp_nor_lvl_img_1,around_value(reversePercentage(get_percentage_between(cmp_nor_lvl_img_2,cmp_nor_lvl_img_1))),around_value(get_percentage_between(cmp_nor_lvl_img_2,cmp_nor_lvl_img_1)))}

                                        </ul>


                                    <br>

                                    <li>

                                        GrayScale

                                        <ul>

                                            {set_wigdet_list_for_compression("COMPRESSION LEVEL",cmp_gra_lvl_img_1,around_value(reversePercentage(get_percentage_between(cmp_gra_lvl_img_2,cmp_gra_lvl_img_1))),around_value(get_percentage_between(cmp_gra_lvl_img_2,cmp_gra_lvl_img_1)))}

                                        </ul>

                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="column middlescreen">
                        {set_profile_of_picture("2",lvl_img2)}

                        {set_start_compare_zone("ColorCollect")}
                                    <li>

                                        Normal

                                        <ul>


                                            {set_wigdet_list_for_color_col("ColorOccurences","",col_nor_occ,reversePercentage(col_nor_occ))}

                                            {set_wigdet_list_for_color_col("ColorAverage",for_col_nor_avg_img_2,reversePercentage(pc_col_avg),pc_col_avg)}

                                            {set_wigdet_list_for_color_col("ColorDominante",for_col_nor_dom_img_2,reversePercentage(pc_col_dom),pc_col_dom)}


                                        </ul>


                                    <br>

                                    <li>

                                        GrayScale

                                        <ul>

                                            {set_wigdet_list_for_color_col("ColorOccurences","",col_gra_occ,reversePercentage(col_gra_occ))}

                                            {set_wigdet_list_for_color_col("ColorAverage",for_col_gra_avg_img_2,reversePercentage(pc_gra_col_avg),pc_gra_col_avg)}

                                            {set_wigdet_list_for_color_col("ColorDominante",for_col_gra_dom_img_2,reversePercentage(pc_gra_col_dom),pc_gra_col_dom)}

                                        </ul>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        {set_start_compare_zone("ColorCompare")}
                                    <li>

                                        Normal

                                        <ul>

                                            {set_wigdet_list_for_compare("ColorDifference",com_nor_dif_img_2)}

                                        </ul>


                                    <br>

                                    <li>

                                        GrayScale

                                        <ul>

                                            {set_wigdet_list_for_compare("ColorDifference",com_gra_dif_img_2)}

                                        </ul>

                                    </li>
                                </ul>
                            </div>
                        </div>

                        {set_start_compare_zone("Compression")}
                                    <li>

                                        Normal

                                        <ul>

                                            {set_wigdet_list_for_compression("COMPRESSION LEVEL", cmp_nor_lvl_img_2, around_value(reversePercentage(get_percentage_between(cmp_nor_lvl_img_2, cmp_nor_lvl_img_1))), around_value(get_percentage_between(cmp_nor_lvl_img_2, cmp_nor_lvl_img_1)))}

                                        </ul>

                                    <br>

                                    <li>

                                        GrayScale

                                        <ul>

                                            {set_wigdet_list_for_compression("COMPRESSION LEVEL",cmp_gra_lvl_img_2,around_value(reversePercentage(get_percentage_between(cmp_gra_lvl_img_2,cmp_gra_lvl_img_1))),around_value(get_percentage_between(cmp_gra_lvl_img_2,cmp_gra_lvl_img_1)))}

                                        </ul>

                                    </li>
                                </ul>
                            </div>
                        </div>

                    </div>

                </div>
         {set_close_html_file()}

    '''

    with open(u.dt_string+'/report/report.html', 'w') as f:
        f.write(html)
    generate_fav_icon(16, tuple(for_col_nor_avg_img_2), tuple(for_col_nor_avg_img_1))
    generate_logo()
    generate_report_css()
    generate_default_themes()
