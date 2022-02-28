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
    with open(u.dt_string+'/report/assets/themes/Viridis.css','w') as f:
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
    with open(u.dt_string+'/report/assets/themes/Elegant.css','w') as f:
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
    with open(u.dt_string+'/report/assets/themes/Classic.css','w') as f:
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
    with open(u.dt_string+'/report/assets/themes/Nostalgy.css','w') as f:
        f.write(nostalgy)   

def generateReportCss():

    css = """

/* RESPONSIVE BUILDER */
@charset "UTF-8"; /* https://1linelayouts.glitch.me/ */ /* * 100%Responsive v0.0.1 * 100% full responsive css library * Licensed under MIT (url) */ body{margin:0px;font-size:12px} /* ScreenWidth */ .fullscreen{width:100%} .middlescreen{width:50%} .boxsizing{-webkit-box-sizing: border-box; /* Safari/Chrome, other WebKit */-moz-box-sizing: border-box;    /* Firefox, other Gecko */box-sizing: border-box;         /* Opera/IE 8+ */} .overflow-auto{overflow: auto} /* FontSize */ /* h1, h2, h3, h4, h5, h6 : 6vw, 4.255vh, 3vh, 2vh, 1.7vh, 1.2vh */ .h1-default{font-size:clamp(40px,6vw,70px)} .h2-default{font-size:clamp(32px,4.255vw,64px)} .h3-default{font-size:clamp(26px,3vw,48px)} .h4-default{font-size:clamp(20px,2vw,36px)} .h5-default{font-size:clamp(16px,1.7vw,18px)} .h6-default{font-size:clamp(14px,1.2vw,16px)} /* huge, big, medium, small, tiny : 5vh, 4vh, 3vh, 2vh, 1vh */ .p-tiny{font-size: clamp(0.1em, 1vw, 1em)} .p-small{font-size: clamp(0.5em, 1.5vw, 1.2em)} p, .p-medium{font-size: clamp(0.8em, 1.8vw, 1.4em)} .p-big{font-size:clamp(1.2em, 2.0vw, 2.2em)} .p-huge{font-size:clamp(1.4em, 2.4vw, 2.8em)} /* DIV & CONTAINER */ @media (max-width: 800px) { .row {-webkit-flex-direction: column;flex-direction: column} .column {width:100% !important} .p-small{font-size:4vw} } .header{text-align: center} .row{display: -webkit-flex;display: flex} .column{box-sizing:border-box} .column.middle{-webkit-flex: 2;-ms-flex: 2;flex: 2;box-sizing:border-box} .footer{text-align: center} .child-container{} .no-margin{margin:0px} .no-padding{padding:0px} .float-left{float:left} .float-right{float:right} .plateitem-left{display: grid;place-items: left} .placeitem-center{display: grid;place-items: center} .placeitem-right{display: grid;place-items: right} .text-left{text-align: left} .text-center{text-align: center} .text-right{text-align: rightsss} /* The Deconstructed Pancake */ .dec-pancake{ display: flex; flex-wrap: wrap; justify-content: center; } .dec-box-pancake{ flex: 1 1 150px; /*  Stretching: */ /* flex: 0 1 150px; /*  No stretching: */ */ margin: 5px; } /* RAM (Repeat, Auto, Minmax) */ .ram{ display: grid; grid-gap: 1rem; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); } /* Clamping post card */ .clamping-post { display: grid; place-items: center; } .clamping-post-card { width: clamp(23ch, 50%, 46ch); display: flex; flex-direction: column; padding: 1rem; } .clamping-post-img { height: 125px; width: 100%; } /* IMAGE */ .img-fullscreen{width: 100%;height: auto} .img-threequarters{width: 75%;height: auto} .img-middlescreen{width: 50%;height: auto} .img-onequarters{width: 25%;height: auto}

/* PICKCHECK STYLES  */
:root{
    --primaryColor : #A3F7B5;
    --secondaryColor : #2F9C95;
    --grayColor : #e9e9e9;
    --lightgrayColor : #F9F9F9;
    --debugColor : crimson;

/*
    100-80 = 5aff00
    80-60  = ffe500
    60-40  = ffa500
    40-20  = ff2500
    0-20   = 3b0900
*/

    --deg1 : 336deg;
    --size1 : 74px;
    --size2 : 55%;
}

.header{
    height:7vh;
    background-image:linear-gradient(var(--deg1),var(--primaryColor),var(--secondaryColor));
}
.gradient{
    background-image:linear-gradient(var(--deg1),var(--primaryColor),var(--secondaryColor));
}
.header>img{width:var(--size1);margin-top: 13px}

.debug{background: var(--debugColor)}
.text-center>img{width:var(--size2)}
.page{margin:4%}
.compareZone{width:94%;margin:0 auto}
ul{background:var(--lightgrayColor)}
.category{background:var(--grayColor);padding:1.4%}
.gradient>div>ul{background:transparent}
.gradient>div>.category{background:transparent}


.level{font-size:x-large;border-radius: 50px;border:2px solid;width: 90px;height: 90px;top: 24vh;position: absolute;}
.lbA{color:var(--levelA);border-color:var(--levelA)}
.lbB{color:var(--levelB);border-color:var(--levelB)}
.lbC{color:var(--levelC);border-color:var(--levelC)}
.lbD{color:var(--levelD);border-color:var(--levelD)}
.lbE{color:var(--levelE);border-color:var(--levelE)}

.bA{background:var(--levelA)}
.bB{background:var(--levelB)}
.bC{background:var(--levelC);color:#FFF}
.bD{background:var(--levelD);color:#FFF}
.bE{background:var(--levelE);color:#FFF}

.disregarded{background:#B7B7B7;color:#575757}

.cnt{background:black}

.tag{margin:2%;text-align: center;overflow:hidden}


/* Loading animation */
.load {
    background:linear-gradient(90deg,#fff,#b7b7b75A,#efefef);
    background-size:auto;
    background-size:360% 360%;
    animation:gradient-animation 2s ease infinite;
    height: 173px;
   }
   @keyframes gradient-animation {
    0% {
     background-position:0% 50%
    }
    50% {
     background-position:100% 50%
    }
    100% {
     background-position:0% 50%
    }
}

    """
    with open(u.dt_string+'/report/assets/report.css','w') as f:
        f.write(css)    