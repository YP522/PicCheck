from generate.generateHTML import *
from generate.funcs.formatted import *


def setWigdetListForColorCol(title, var1, var2, var3):

    WigdetListForColorCol = f'''
        <li>
            <div class="row">
                <div class="column middlescreen">
                    {title}
                </div>
                <div class="column middlescreen">
                    <div class="row">
                        <div class="column middlescreen tag {setBackgroundByContastColor(tuple(var1))}" style="color:rgb{tuple(var1)}">{var1}</div>
                        <div class="column middlescreen tag {getColorByPercentage(var2)}">{var2} %</div>
                        <div class="column middlescreen tag {getColorByPercentage(var3)}">{var3} %</div>
                    </div>
                </div>

            </div>
        </li>
    '''
    return WigdetListForColorCol


def setWigdetListForCompare(title, var1):

    WigdetListForCompare = f'''
        <li>
            <div class="row">
                <div class="column middlescreen">
                    {title}
                </div>
                <div class="column middlescreen">
                    <div class="row">
                        <div class="column middlescreen tag "></div>
                        <div class="column middlescreen tag {getColorByPercentage(var1)}">{var1}%</div>
                        <div class="column middlescreen tag {getColorByPercentage(reversePercentage(var1))}">{reversePercentage(var1)}%</div>
                    </div>
                </div>

            </div>
        </li>
    '''
    return WigdetListForCompare


def setWigdetListForCompression(title, var1, var2, var3):

    WigdetListForCompression = f'''
        <li>
            <div class="row">
                <div class="column middlescreen">
                    {title}
                </div>
                <div class="column middlescreen">
                    <div class="row">
                        <div class="column middlescreen tag">{var1} %</div>
                        <div class="column middlescreen tag {getColorByPercentage(var2)}">{var2} %</div>
                        <div class="column middlescreen tag {getColorByPercentage(var3)}">{var3} %</div>
                    </div>
                </div>

            </div>
        </li>
    '''
    return WigdetListForCompression
