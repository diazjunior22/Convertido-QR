import qrcode
import io
import base64
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    qr_code = None
    link = None
    if request.method == "POST":
        link = request.POST.get("link")
        if link:
            if not link.startswith(("http://", "https://")):
                link = "https://" + link
            
            # Generar QR en memoria (para mostrar en la página)
            img = qrcode.make(link)
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            qr_code = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return render(request, "index.html", {"qr_code": qr_code, "link": link})

def descargar_qr(request):
    link = request.GET.get("link")
    if not link:
        return HttpResponse("No se proporcionó ningún link.")

    if not link.startswith(("http://", "https://")):
        link = "https://" + link

    img = qrcode.make(link)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    response = HttpResponse(buffer, content_type="image/png")
    response["Content-Disposition"] = 'attachment; filename="codigo_qr.png"'
    return response
