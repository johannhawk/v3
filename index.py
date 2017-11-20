from bottle import route, run, template, error, static_file

@error(404)
def error404(error):
    return "<h1>Error 404!</h1>"

@route('/static/<filename>')
def srever_static(filename):
    return static_file(filename, root="./static")

@route('/pic')
def pic():
    return '''
<!DOCTYPE html>
           <html>
                <head>
                <title>Pictures</title>
                 <link rel="stylesheet" type="text/css" href="/static/bare.css">
                </head>
                <style>

.caption { visibility: hidden; }
.caption:target { visibility: visible; }
</style>
        <body>
    
            <a href="Steve_Jobs">Steve Jobs</a><br><a href="bio">Biography</a>
            <br><a href="pic">Pictures</a><br><a href="x/error">Error 404</a>

           <hr>
           <h1>Pictures</h1>
           <a href=#capt0>
           <img src="/static/pic0.jpg" style="width:200px;height:400px;">
           </a>
           <div class=caption id=capt0>Stundum er lett ad angra folk og dyr</div>
           <hr>
           <a href=#capt1>
           <img src="/static/pic1.jpg">
           </a>
           <div class=caption id=capt1>Jardaber og vofflur</div>
           <hr>
           <a href=#capt2>
           <img src="/static/pic2.jpg">
           </a>
           <div class=caption id=capt2>mynd med engar utskyringar</div>
           <hr>
           <a href=#capt3>
           <img src="/static/pic3.png">
           </a>
           <div class=caption id=capt3>naestum dvi satt</div>
           <hr>
           <a href=#capt4>
           <img src="/static/pic4.png">
           </a>
           <div class=caption id=capt4>kotturin minn</div>
           
           <hr>
           <a href=#capt5>
           <img src="/static/pic5.png">
           </a>
           <div class=caption id=capt5>litur ut fyrir ad vera vietnam hermadur inni gong</div>
           <hr>
           <a href=#capt6>
           <img src="/static/pic6.png">
           </a>
           <div class=caption id=capt6>forrutinar brandari</div>
           <hr>
           <a href=#capt7>
           <img src="/static/pic7.gif" style="width:200px;height:300px;">
           </a>
           <div class=caption id=capt7>dessi mynd er i .gif format/div>
           <hr>
           <a href=#capt8>
           <img src="/static/pic8.png">
           </a>
           <div class=caption id=capt8>Always sunny in philadelpia</div>
           <hr>
           <a href=#capt9>
           <img src="/static/pic9.png" style="width:500px;height:300px;" >
           </a>
           <div class=caption id=capt9>engin er i midpunkt heimsins</div>

           </body>
           '''

@route('/<name:int>')
def i(name):
    if name == 1:
        return template('./static/1',name="Steve Jobs")
    elif name == 2:
        return template('./static/2',name="Steve Jobs")
    elif name == 3:
        return template('./static/p',name="Steve Jobs")

#hver undirsida a ad innihalda efnisyfirlit, mynd, texta og CSS

#nota dynamic route(route med eitt wildcard) til ad akvarda hvada undirsida er valin

#utfaerdu HTTP errors sidu ef smellt er a undirsidu sem er ekki til






run(host='localhost', port=8080)
