import json
#SŁUŻY DO TWORZRZNIA POWTARZALNYCH STORNEK
# Load data from the JSON file
with open('news.json', 'r', encoding='utf-8') as file:
    news_data = json.load(file)
for index, news_item in enumerate(news_data):
    # Create the HTML content dynamically
    html_content = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Buduję Domy Pasywne</title>
        <link rel="shortcut icon" type="image/x-icon" href="../img/bdpwhite.png"/>
        <link rel="stylesheet" href="../css/styles.css">
        <link href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap" rel="stylesheet">
    </head>
    <body>

        <header>
            <a href="../../index.html"><img src="../img/bdpwhite.png" alt="Logo"></a>
            <nav>
            <a href="../../news.html">Aktualności</a>
            <div class="dropdown">
                <button class="dropbtn">Firma</button>
                <div class="dropdown-content">
                    <a href="../../dlaczego-my.html">DLACZEGO MY?</a>
                    <a href="../../media-o-nas.html">MEDIA O NAS</a>
                    <a href="../../nowy-ekspert.html">NOWY EKSPERT</a>
                </div>
            </div>
            <div class="dropdown">
                <button class="dropbtn">Nasza oferta</button>
                <div class="dropdown-content">
                    <a href="../../budowa-domow-niskoenergetycznych-i-pasywnych.html">BUDOWA DOMÓW NISKOENERGETYCZNYCH I PASYWNYCH</a>
                    <a href="../../audyty-energetyczne-domow-przed-budowa.html">AUDYTY ENERGETYCZNE DOMÓW PRZED BUDOWĄ</a>
                </div>
            </div>
            <div class="dropdown">
                <button class="dropbtn">Przykładowe budowy</button>
                <div class="dropdown-content">
                    <a href="#service1">DOM JEDNORODZINNY W KRUSZYNIE</a>
                    <a href="#service2">DOM JEDNORODZINNY W OLIMPINIE</a>
                    <a href="#service3">DOM JEDNORODZINNY W ŁOCHOWIE</a>
                    <a href="#service3">DOM JEDNORODZINNY W POPOWIE</a>
                    <a href="#service3">BUDOWA NAJWIĘKSZEGO DOMU PASYWNEGO W POLSCE</a>
                    <a href="#service3">DOM JEDNORODZINNY W MUROWAŃCU</a>
                </div>
            </div>
            <div class="dropdown">
                <button class="dropbtn">Dom pasywny w szczegółach</button>
                <div class="dropdown-content">
                    <a href="../../plyta-fundamentowa.html">PASYWNA PŁYTA FUNDAMENTOWA</a>
                    <a href="../../plyta-grzewcza.html">AKUMULACYJNA PŁYTA GRZEWCZA</a>
                    <a href="../../cieply-montaz-okien.html">"CIEPŁY" MONTAŻ OKIEN"</a>
                    <a href="../../wiezba-prefabrykowana.html">WIĘŹBA PREFABRYKOWANA</a>
                    <a href="../../system-bso.html">SYSTEM BSO</a>
                    <a href="../../wentylacja-mechaniczna.html">WENTYLACJA MECHANICZNA</a>
                    <a href="../../ocieplenie-stropodachu.html">OCIEPLENIE STROPODACHU</a>
                    <a href="../../termowizja.html">TERMOWIZJA</a>
                    <a href="../../test-szczelnosci.html">TEST SZCZELNOŚCI (BLOWER DOOR)</a>
                </div>
            </div>
            <a href="#contact">Kontakt</a>
        </nav>
         <div class="callus">
            <p>Chcesz się dowiedzieć więcej?</p>
            <p>Zadzwoń: 790 210 215</p>
        </div>
        </header>

        <section id="news" class="news-section">
    '''

    # Loop through each news item and add it to the HTML content

    html_content += f'''
        <div class="news-title">
            <h1>{news_item["title"]}</h1>
        </div>
        <div class="news" id="news-container">
            <div class="news-item-only">
                <img src="{news_item["image_news"]}" alt="{news_item["title"]}">
                <p style="font-size: 19px;">&#x23F0;</p>
                <div class="news-content">
                    <h3>{news_item["date"]}</h3>
                    <p>{news_item["description"]}</p>
                </div>
            </div>
        </div>

        <div class="wave-shape-contact2"></div>
        <div class="wave-shape-news"></div>
    '''
    # Complete the HTML content
    html_content += '''
        </section>
        <footer>
        <div class="footer-content">
            <div class="wave-shape-footer"></div>
            <div class="footer-section-img">
                <a href="../../index.html"><img src="../img/bdpwhite.png" alt="Logo"></a>
            </div>
            <div class="footer-section">
                <a href="../../news.html">Aktualności</a>
                <a href="../../dlaczego-my.html">Dlaczego My?</a>
                <a href="../../media-o-nas.html">Media o nas</a>
                <a href="../../nowy-ekspert.html">Nowy ekspert</a>
                <a href="../../budowa-domow-niskoenergetycznych-i-pasywnych.html">Budowa domów niskoenergetycznych i pasywnych</a>
                <a href="../../audyty-energetyczne-domow-przed-budowa.html">Audyty energetyczne domów przed budową</a>
                <a href="../../index.html#contact">Kontakt</a>
            </div>
            <div class="footer-section">
                <h3>Oberwuj nas!</h3>
                <a href="https://www.facebook.com/Buduje-Domy-Pasywne-531664133565053/" target="_blank">Facebook</a>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 Buduję Domy Pasywne</p>
        </div>
    </footer>
    </body>
    </html>
    '''

    # Write the generated HTML content to a new HTML file
    with open('news' + str((index + 1)) + '.html', 'w', encoding='utf-8') as output_file:
        output_file.write(html_content)

print("HTML pages generated successfully.")
