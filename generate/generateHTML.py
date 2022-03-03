from PIL import Image

from generate.funcs.formatted import aroundValue, cleanList, reversePercentage, getPercentageBetween, getColorByPercentage
from generate.generateCSS import generateDefaultThemes, generateReportCss
from generate.parts.favicon import generateFavIcon
from generate.parts.html import setWigdetListForColorCol, setWigdetListForCompare, setWigdetListForCompression
from generate.parts.logo import generateLogo

from processing.collect import getColorOccurences, getColorAverage,getColorDominante
from processing.compare import getColorDifferences, getDiff
from processing.compression import getCompressionLevel

from system import utils as u

page_title = "My report"


def generateHTML(nor_img1, nor_img2):

    gra_img1 = Image.open(f"{u.dt_string}/data/gra_img1.png").convert('RGB')
    gra_img2 = Image.open(f"{u.dt_string}/data/gra_img2.png").convert('RGB')

    # revoir nomination des variables images

    col_nor_occ = aroundValue(getColorOccurences(nor_img1, nor_img2)[1])
    col_nor_avg_img_1 = getColorAverage(nor_img1, nor_img2)[0]
    col_nor_avg_img_2 = getColorAverage(nor_img1, nor_img2)[1]
    for_col_nor_avg_img_1 = cleanList(col_nor_avg_img_1)
    for_col_nor_avg_img_2 = cleanList(col_nor_avg_img_2)
    pc_col_avg = getDiff(col_nor_avg_img_1, col_nor_avg_img_2, 0)
    col_nor_dom_img_1 = cleanList(getColorDominante(nor_img1, nor_img2)[0])
    col_nor_dom_img_2 = cleanList(getColorDominante(nor_img1, nor_img2)[1])
    for_col_nor_dom_img_1 = cleanList(col_nor_dom_img_1)
    for_col_nor_dom_img_2 = cleanList(col_nor_dom_img_2)
    pc_col_dom = getDiff(col_nor_dom_img_1, col_nor_dom_img_2, 0)

    col_gra_occ = aroundValue(getColorOccurences(gra_img1, gra_img1)[1])
    col_gra_avg_img_1 = getColorAverage(gra_img1, gra_img1)[0]
    col_gra_avg_img_2 = getColorAverage(gra_img1, gra_img2)[1]
    for_col_gra_avg_img_1 = cleanList(col_gra_avg_img_1)
    for_col_gra_avg_img_2 = cleanList(col_gra_avg_img_2)
    pc_gra_col_avg = getDiff(col_gra_avg_img_1, col_gra_avg_img_2, 0)
    col_gra_dom_img_1 = cleanList(getColorDominante(gra_img1, gra_img2)[0])
    col_gra_dom_img_2 = cleanList(getColorDominante(gra_img1, gra_img2)[1])
    for_col_gra_dom_img_1 = cleanList(col_gra_dom_img_1)
    for_col_gra_dom_img_2 = cleanList(col_gra_dom_img_2)
    pc_gra_col_dom = getDiff(col_gra_dom_img_1, col_gra_dom_img_2, 0)

    com_nor_dif_img_1 = aroundValue(getColorDifferences(nor_img1, nor_img2)/(nor_img1.width*nor_img1.height)*100)
    com_nor_dif_img_2 = aroundValue(getColorDifferences(nor_img1, nor_img2)/(nor_img1.width*nor_img1.height)*100)

    com_gra_dif_img_1 = aroundValue(getColorDifferences(gra_img1, gra_img2)/(gra_img1.width*gra_img1.height)*100)
    com_gra_dif_img_2 = aroundValue(getColorDifferences(gra_img1, gra_img2)/(gra_img1.width*gra_img1.height)*100)

    cmp_nor_lvl_img_1 = aroundValue(getCompressionLevel(nor_img1, "img1"))
    cmp_nor_lvl_img_2 = aroundValue(getCompressionLevel(nor_img2, "img2"))

    cmp_gra_lvl_img_1 = aroundValue(getCompressionLevel(gra_img1, "gra_img1"))
    cmp_gra_lvl_img_2 = aroundValue(getCompressionLevel(gra_img2, "gra_img2"))

    lvl_img1 = aroundValue(
        col_nor_occ
        + reversePercentage(pc_col_avg)
        + reversePercentage(pc_col_dom)
        + col_gra_occ
        + reversePercentage(pc_gra_col_avg)
        + reversePercentage(pc_gra_col_dom)
        + com_nor_dif_img_1
        + com_gra_dif_img_1
        + aroundValue(reversePercentage(getPercentageBetween(cmp_nor_lvl_img_2, cmp_nor_lvl_img_1)))
        + aroundValue(reversePercentage(getPercentageBetween(cmp_gra_lvl_img_2, cmp_gra_lvl_img_1)))
        )/10

    lvl_img2 = reversePercentage(aroundValue(lvl_img1))

    html = f'''
    <!-- PCK HTML REPORT -->
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
        <head>
            <meta charset="utf-8">
            <title>{page_title}</title>
            <link rel="stylesheet" href="assets/report.css">
            <link rel="stylesheet" href="assets/themes/Viridis.css">  <!-- edit this line to change report css theme -->
            <link rel="icon" type="image/png" href="assets/favicon.png" />
        </head>
        <body>
            <div class="header fullscreen">
                <img src="assets/logo.png" alt="A free tool for compare 2 pictures">
            </div>
            <div class="page">
                <div class="row">
                    <div class="column middlescreen">
                        <div class="text-center">
                            <img src="../data/img1.png" alt="A free tool for compare 2 pictures">
                            <h3>IMG 1</h3>

                            <div class="level l{getColorByPercentage(lvl_img1)}">
                                <h4>{lvl_img1}%</h4>
                            </div>
                        </div>

                        <div class="compareZone">
                            <div>
                                <h2 class="category">ColorCollect</h2>
                                <ul>
                                    <li>

                                        Normal

                                        <ul>

                                            {setWigdetListForColorCol("ColorOccurences","",col_nor_occ,reversePercentage(col_nor_occ))}

                                            {setWigdetListForColorCol("ColorAverage",for_col_nor_avg_img_1,reversePercentage(pc_col_avg),pc_col_avg)}

                                            {setWigdetListForColorCol("ColorDominante",for_col_nor_dom_img_1,reversePercentage(pc_col_dom),pc_col_dom)}

                                        </ul>

                                    <br>

                                    <li>

                                        GrayScale

                                        <ul>

                                            {setWigdetListForColorCol("ColorOccurences","",col_gra_occ,reversePercentage(col_gra_occ))}

                                            {setWigdetListForColorCol("ColorAverage",for_col_gra_avg_img_1,reversePercentage(pc_gra_col_avg),pc_gra_col_avg)}

                                            {setWigdetListForColorCol("ColorDominante",for_col_gra_dom_img_1,reversePercentage(pc_gra_col_dom),pc_gra_col_dom)}

                                        </ul>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <div class="compareZone">
                            <div>
                                <h2 class="category">ColorCompare</h2>
                                <ul>
                                    <li>

                                        Normal

                                        <ul>

                                            {setWigdetListForCompare("ColorDifference",com_nor_dif_img_1)}

                                        </ul>

                                    <br>

                                    <li>

                                        GrayScale

                                        <ul>

                                            {setWigdetListForCompare("ColorDifference",com_gra_dif_img_1)}

                                        </ul>

                                    </li>
                                </ul>
                            </div>
                        </div>

                        <div class="compareZone">
                            <div>
                                <h2 class="category">Compression</h2>
                                <ul>
                                    <li>

                                        Normal

                                        <ul>

                                            {setWigdetListForCompression("COMPRESSION LEVEL",cmp_nor_lvl_img_1,aroundValue(reversePercentage(getPercentageBetween(cmp_nor_lvl_img_2,cmp_nor_lvl_img_1))),aroundValue(getPercentageBetween(cmp_nor_lvl_img_2,cmp_nor_lvl_img_1)))}

                                        </ul>


                                    <br>

                                    <li>

                                        GrayScale

                                        <ul>

                                            {setWigdetListForCompression("COMPRESSION LEVEL",cmp_gra_lvl_img_1,aroundValue(reversePercentage(getPercentageBetween(cmp_gra_lvl_img_2,cmp_gra_lvl_img_1))),aroundValue(getPercentageBetween(cmp_gra_lvl_img_2,cmp_gra_lvl_img_1)))}

                                        </ul>

                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="column middlescreen">
                        <div class="text-center">
                            <img src="../data/img2.png" alt="A free tool for compare 2 pictures">
                            <h3>IMG 2</h3>
                            <div class="level l{getColorByPercentage(lvl_img2)}">
                                <h4>{lvl_img2}%</h4>
                            </div>
                        </div>

                        <div class="compareZone">
                            <div>
                                <h2 class="category">ColorCollect</h2>
                                <ul>
                                    <li>

                                        Normal

                                        <ul>


                                            {setWigdetListForColorCol("ColorOccurences","",col_nor_occ,reversePercentage(col_nor_occ))}

                                            {setWigdetListForColorCol("ColorAverage",for_col_nor_avg_img_2,reversePercentage(pc_col_avg),pc_col_avg)}

                                            {setWigdetListForColorCol("ColorDominante",for_col_nor_dom_img_2,reversePercentage(pc_col_dom),pc_col_dom)}


                                        </ul>


                                    <br>

                                    <li>

                                        GrayScale

                                        <ul>

                                            {setWigdetListForColorCol("ColorOccurences","",col_gra_occ,reversePercentage(col_gra_occ))}

                                            {setWigdetListForColorCol("ColorAverage",for_col_gra_avg_img_2,reversePercentage(pc_gra_col_avg),pc_gra_col_avg)}

                                            {setWigdetListForColorCol("ColorDominante",for_col_gra_dom_img_2,reversePercentage(pc_gra_col_dom),pc_gra_col_dom)}

                                        </ul>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <div class="compareZone">
                            <div>
                                <h2 class="category">ColorCompare</h2>
                                <ul>
                                    <li>

                                        Normal

                                        <ul>

                                            {setWigdetListForCompare("ColorDifference",com_nor_dif_img_2)}

                                        </ul>


                                    <br>

                                    <li>

                                        GrayScale

                                        <ul>

                                            {setWigdetListForCompare("ColorDifference",com_gra_dif_img_2)}

                                        </ul>

                                    </li>
                                </ul>
                            </div>
                        </div>

                        <div class="compareZone">
                            <div>
                                <h2 class="category">Compression</h2>
                                <ul>
                                    <li>

                                        Normal

                                        <ul>

                                            {setWigdetListForCompression("COMPRESSION LEVEL", cmp_nor_lvl_img_2, aroundValue(reversePercentage(getPercentageBetween(cmp_nor_lvl_img_2, cmp_nor_lvl_img_1))), aroundValue(getPercentageBetween(cmp_nor_lvl_img_2, cmp_nor_lvl_img_1)))}

                                        </ul>

                                    <br>

                                    <li>

                                        GrayScale

                                        <ul>

                                            {setWigdetListForCompression("COMPRESSION LEVEL",cmp_gra_lvl_img_2,aroundValue(reversePercentage(getPercentageBetween(cmp_gra_lvl_img_2,cmp_gra_lvl_img_1))),aroundValue(getPercentageBetween(cmp_gra_lvl_img_2,cmp_gra_lvl_img_1)))}

                                        </ul>

                                    </li>
                                </ul>
                            </div>
                        </div>

                    </div>

                </div>
            </div>
        </body>
    </html>

    '''

    with open(u.dt_string+'/report/report.html', 'w') as f:
        f.write(html)
    generateFavIcon(16, tuple(for_col_nor_avg_img_2), tuple(for_col_nor_avg_img_1))
    generateLogo()
    generateReportCss()
    generateDefaultThemes()
