from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Einfache Statik",
    description="Vereinfachte statische Nachweise (Schnee, Wind, Holzbau)",
    version="0.1.0",
)


@app.get("/", response_class=HTMLResponse)
def startseite():
    return """
    <html>
        <head>
            <title>Einfache Statik</title>
        </head>
        <body>
            <h1>Einfache Statik</h1>

            <p>
                Dieses Tool stellt vereinfachte statische Nachweise zur Verfügung.
                Es ersetzt keine prüffähige Statik.
            </p>

            <h2>Module</h2>
            <ul>
                <li><a href="/schnee">Schneelast</a></li>
                <li>Windlast (in Vorbereitung)</li>
                <li>Holzträger (in Vorbereitung)</li>
            </ul>

            <hr>
            <p style="font-size: 0.9em;">
                Haftungsausschluss: Keine Gewähr für Richtigkeit oder Vollständigkeit.
            </p>
        </body>
    </html>
    """