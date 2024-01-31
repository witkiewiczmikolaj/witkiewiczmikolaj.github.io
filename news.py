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
                    <a href="#service1">DLACZEGO MY?</a>
                    <a href="#service2">MEDIA O NAS</a>
                    <a href="#service3">NOWY EKSPERT</a>
                </div>
            </div>
            <div class="dropdown">
                <button class="dropbtn">Nasza oferta</button>
                <div class="dropdown-content">
                    <a href="#service1">BUDOWA DOMÓW NISKOENERGETYCZNYCH I PASYWNYCH</a>
                    <a href="#service2">AUDYTY ENERGETYCZNE DOMÓW PRZED BUDOWĄ</a>
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
                    <a href="#service1">PASYWNA PŁYTA FUNDAMENTOWA</a>
                    <a href="#service2">AKUMULACYJNA PŁYTA GRZEWCZA</a>
                    <a href="#service3">"CIEPŁY" MONTAŻ OKIEN"</a>
                    <a href="#service3">WIĘŹBA PREFABRYKOWANA</a>
                    <a href="#service3">SYSTEM BSO</a>
                    <a href="#service3">WENTYLACJA MECHANICZNA</a>
                    <a href="#service3">OCIEPLENIE STROPODACHU</a>
                    <a href="#service3">TERMOWIZJA</a>
                    <a href="#service3">TEST SZCZELNOŚCI (BLOWER DOOR)</a>
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
                <img src="../img/bdpwhite.png" alt="Logo">
            </div>
            <div class="footer-section">
                <a href="#" target="_blank">Aktualności</a>
                <a href="#" target="_blank">Dlaczego My?</a>
                <a href="#" target="_blank">Media o nas</a>
                <a href="#" target="_blank">Nowy ekspert</a>
                <a href="#" target="_blank">Budowa domów niskoenergetycznych i pasywnych</a>
                <a href="#" target="_blank">Audyty energetyczne domów przed budową</a>
            </div>
            <div class="footer-section">
                <h3>Oberwuj nas!</h3>
                <a href="#" target="_blank">Facebook</a>
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
