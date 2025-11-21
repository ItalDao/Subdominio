# app.py
from flask import Flask, request, redirect, url_for, render_template_string, flash
from markupsafe import escape

app = Flask(__name__)
app.secret_key = "cambia_esta_clave_por_una_segura"

PAGE = """
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Alcivar | NeoGlass UI</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap" rel="stylesheet">

<style>
:root{
  --bg: #05060a;
  --glass: rgba(255,255,255,0.09);
  --glass-border: rgba(255,255,255,0.16);
  --neon: #00c6ff;
  --neon2: #0072ff;
  --text: #e3e8f1;
  --muted: #8b9bb5;
}

*{margin:0;padding:0;box-sizing:border-box;font-family:"Poppins",sans-serif;}

body{
  background: radial-gradient(circle at 20% 20%, rgba(0,153,255,0.18), transparent 40%),
              radial-gradient(circle at 80% 80%, rgba(0,255,153,0.18), transparent 40%),
              var(--bg);
  color: var(--text);
  min-height:100vh;
  display:flex;
  justify-content:center;
  align-items:center;
  padding:40px;
}

/* Layout */
.container{
  max-width:1200px;
  display:grid;
  grid-template-columns: 1fr 420px;
  gap:40px;
}

.glass-box{
  background: var(--glass);
  backdrop-filter: blur(18px);
  border: 1px solid var(--glass-border);
  padding:30px;
  border-radius:18px;
  box-shadow:
    0 0 20px rgba(0,255,255,0.05),
    0 8px 25px rgba(0,0,0,0.45);
  position: relative;
}

/* Title */
.logo{
  display:flex;
  align-items:center;
  gap:10px;
  font-size:24px;
  font-weight:700;
  text-decoration:none;
  color:white;
  margin-bottom:18px;
}
.logo .glow{
  width:40px;height:40px;border-radius:12px;
  background:linear-gradient(135deg, var(--neon), var(--neon2));
  display:flex;align-items:center;justify-content:center;
  font-weight:800;font-size:20px;color:white;
  box-shadow:0 0 22px var(--neon);
}

h1{font-size:34px;margin-bottom:10px;}
.lead{color:var(--muted);margin-bottom:18px;}

.feats{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px;}
.feat{
  padding:8px 12px;
  font-size:14px;
  border-radius:10px;
  background:rgba(255,255,255,0.05);
  border:1px solid rgba(255,255,255,0.06);
  color:var(--muted);
}

.btn-main{
  display:inline-block;
  padding:12px 20px;
  margin-top:20px;
  border-radius:12px;
  background:linear-gradient(90deg, var(--neon), var(--neon2));
  color:black;
  font-weight:600;
  text-decoration:none;
  box-shadow:0 0 14px var(--neon2);
}

footer{margin-top:20px;font-size:13px;color:var(--muted);}

/* Contact */
label{font-size:14px;color:var(--muted);margin-bottom:5px;display:block;}
input,textarea{
  width:100%;
  padding:12px;
  margin-bottom:14px;
  border-radius:10px;
  background:rgba(255,255,255,0.08);
  border:1px solid rgba(255,255,255,0.12);
  color:white;
  outline:none;
}
textarea{resize:vertical;min-height:120px;}

.btn-send{
  width:100%;
  padding:12px 20px;
  border-radius:12px;
  border:none;
  cursor:pointer;
  background:linear-gradient(90deg, var(--neon), var(--neon2));
  font-weight:700;
  color:black;
  box-shadow:0 0 16px var(--neon);
}

/* Flash message */
.flash{
  background:rgba(0,255,100,0.12);
  border:1px solid rgba(0,255,100,0.3);
  color:#b4fcca;
  padding:10px 12px;
  border-radius:10px;
  font-size:14px;
  margin-bottom:12px;
}

/* Responsive */
@media(max-width:900px){
  .container{
    grid-template-columns:1fr;
  }
}
</style>
</head>

<body>
<div class="container">

  <!-- LEFT CARD -->
  <section class="glass-box">
    <a class="logo" href="/">
      <div class="glow">A</div> Alcivar NeoGlass
    </a>

    <h1>Bienvenido ✨</h1>
    <p class="lead">Nuevo diseño moderno estilo *glassmorphism neón*, minimalista y elegante.</p>

    <div class="feats">
      <div class="feat">⚡ Ultra limpio</div>
      <div class="feat">💎 NeoGlass</div>
      <div class="feat">🌙 Dark Mode</div>
      <div class="feat">📱 100% responsive</div>
    </div>

    <a href="#contact" class="btn-main">Ir al formulario</a>

    <footer>Diseño Alcivar — Flask • NeoGlass UI</footer>
  </section>

  <!-- CONTACT FORM -->
  <aside class="glass-box" id="contact">
    <h2 style="margin-bottom:14px;">Contacto</h2>

    {% with messages = get_flashed_messages() %}
    {% if messages %}
      <div class="flash">{{ messages[0] }}</div>
    {% endif %}
    {% endwith %}

    <form method="post" action="{{ url_for('contact') }}">
      <label>Nombre</label>
      <input type="text" name="name" placeholder="Tu nombre" required>

      <label>Correo</label>
      <input type="email" name="email" placeholder="tu@correo.com" required>

      <label>Mensaje</label>
      <textarea name="message" placeholder="Escribe tu mensaje..."></textarea>

      <button class="btn-send" type="submit">Enviar mensaje</button>
    </form>
  </aside>

</div>
</body>
</html>
"""


@app.route("/", methods=["GET"])
def index():
    return render_template_string(PAGE)

@app.route("/contact", methods=["POST"])
def contact():
    name = escape(request.form.get("name", "").strip())
    email = escape(request.form.get("email", "").strip())
    message = escape(request.form.get("message", "").strip())
    flash(f"Gracias {name or 'amigo'}, recibimos tu mensaje — correo: {email or 'no proporcionado'}")
    return redirect(url_for("index") + "#contact")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1737, debug=False)
