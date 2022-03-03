from system import utils as u


def generateDefaultThemes():
    viridis = """
        :root{

            --levelA : #D0E11D;
            --levelB : #48C16E;
            --levelC : #20908D;
            --levelD : #365B8D;
            --levelE : #481B6E;

        }
    """
    with open(u.dt_string+'/report/assets/themes/Viridis.css', 'w') as f:
        f.write(viridis)

    elegant = """
        :root{

            --levelA : #A6E1FA;
            --levelB : #0E6BA8;
            --levelC : #0A2472;
            --levelD : #001C55;
            --levelE : #00072D;

        }
    """
    with open(u.dt_string+'/report/assets/themes/Elegant.css', 'w') as f:
        f.write(elegant)

    classic = """
        :root{

            --levelA : #90BE6D;
            --levelB : #F9C74F;
            --levelC : #F8961E;
            --levelD : #F3722C;
            --levelE : #F94144;

        }
    """
    with open(u.dt_string+'/report/assets/themes/Classic.css', 'w') as f:
        f.write(classic)

    nostalgy = """
        :root{

            --levelA : #FAAE7B;
            --levelB : #CC8B79;
            --levelC : #9F6976;
            --levelD : #714674;
            --levelE : #432371;

        }
    """
    with open(u.dt_string+'/report/assets/themes/Nostalgy.css', 'w') as f:
        f.write(nostalgy)


def generateReportCss():

    css = """

        body{margin:0;font-size:12px}.fullscreen{width:100%}.middlescreen{width:50%}
        .p-medium,p{font-size:clamp(.8em, 1.8vw, 1.4em)}@media (max-width:800px){.row{-webkit-flex-direction:column;flex-direction:column}
        .column{width:100%!important}}.header{text-align:center}.row{display:-webkit-flex;display:flex}
        .column{box-sizing:border-box}.column.middle{-webkit-flex:2;-ms-flex:2;flex:2;box-sizing:border-box}.text-center{text-align:center}
        :root{--primaryColor:#A3F7B5;--secondaryColor:#2F9C95;--grayColor:#e9e9e9;--lightgrayColor:#F9F9F9;--deg1:336deg;--size1:74px;--size2:55%}
        .header{height:7vh;background-image:linear-gradient(var(--deg1),var(--primaryColor),var(--secondaryColor))}.header>img{width:var(--size1);margin-top:13px}
        .text-center>img{width:var(--size2)}.page{margin:4%}.compareZone{width:94%;margin:0 auto}ul{background:var(--lightgrayColor)}
        .category{background:var(--grayColor);padding:1.4%}.level{font-size:x-large;border-radius:50px;border:2px solid;width:90px;height:90px;top:24vh;position:absolute}
        .lbA{color:var(--levelA);border-color:var(--levelA)}.lbB{color:var(--levelB);border-color:var(--levelB)}.lbC{color:var(--levelC);border-color:var(--levelC)}.lbD{color:var(--levelD);border-color:var(--levelD)}.lbE{color:var(--levelE);border-color:var(--levelE)}
        .bA{background:var(--levelA)}.bB{background:var(--levelB)}.bC{background:var(--levelC);color:#fff}.bD{background:var(--levelD);color:#fff}.bE{background:var(--levelE);color:#fff}
        .disregarded{background:#b7b7b7;color:#575757}.cnt{background:#000}.tag{margin:2%;text-align:center;overflow:hidden}


    """
    with open(u.dt_string+'/report/assets/report.css', 'w') as f:
        f.write(css)
