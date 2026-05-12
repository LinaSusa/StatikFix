from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from design.snow import snow_load

app = FastAPI(
    title="Simple Structural Design",
    description="Simplified load and structural design tools",
    version="0.1.0",
)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def homepage():
    return """
    <html>
        <body>
            <h1>Simple Structural Design</h1>
            <ul>
                <li>/snow  – Snow load</li>
                <li>Wind load (coming soon)</li>
                <li>Timber beam (coming soon)</li>
            </ul>
        </body>
    </html>
    """


@app.get("/snow", response_class=HTMLResponse)
def snow_form(request: Request):
    return templates.TemplateResponse(
        "snow.html", {"request": request}
    )


@app.post("/snow", response_class=HTMLResponse)
def snow_calculation(
    request: Request,
    ground_snow_load: float = Form(...),
    roof_pitch: float = Form(...),
):
    result = snow_load(
        ground_snow_load=ground_snow_load,
        roof_pitch=roof_pitch,
    )

    return templates.TemplateResponse(
        "snow.html",
        {"request": request, "result": result},
    )