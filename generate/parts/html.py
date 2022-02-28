from generate.generateHTML import *

def reversePercentage(percentage):
    return 100-percentage

def setBackgroundByContastColor(color):
    if color >  (200, 200, 200) :
        return "cnt"
    else: return ""

def getColorByPercentage(percentage):
    if percentage >=0 and percentage<20:
        return "bE"
    elif percentage>=20 and percentage<40:
        return "bD"
    elif percentage>=40 and percentage<60:
        return "bC"
    elif percentage>=60 and percentage<80:
        return "bB"                
    elif percentage>=80:
        return "bA"
    else:
        return ""

def setWigdetListForColorCol(title,var1,var2,var3):

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


def setWigdetListForCompare(title,var1):

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


def setWigdetListForCompression(title,var1,var2,var3):

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