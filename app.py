from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    moyenne = None
    mention = ""
    color = "secondary"

    if request.method == "POST":
        try:
            maths = float(request.form["maths"])
            pc = float(request.form["pc"])
            svt = float(request.form["svt"])
            histo = float(request.form["histo"])
            francais = float(request.form["francais"])
            anglais = float(request.form["anglais"])
            philo = float(request.form["philo"])
            eps = float(request.form["eps"])

            total = (
                maths * 5 +
                pc * 6 +
                svt * 6 +
                histo * 2 +
                francais * 3 +
                anglais * 2 +
                philo * 2 +
                eps * 1
            )

            moyenne = round(total / 27, 2)

            if moyenne < 10:
                mention = "Insuffisant"
                color = "danger"
            elif moyenne < 12:
                mention = "Passable"
                color = "warning"
            elif moyenne < 14:
                mention = "A. Bien"
                color = "info"
            elif moyenne <= 16:
                mention = "Bien"
                color = "primary"
            else:
                mention = "T. Bien 🏆"
                color = "success"

        except:
            mention = "Erreur de saisie"
            color = "dark"

    return f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Calculateur de Moyenne</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{
                background: linear-gradient(to right, #4e73df, #1cc88a);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }}
            .card {{
                border-radius: 20px;
            }}
            .title {{
                font-weight: bold;
            }}
        </style>
    </head>
    <body>

    <div class="container">
        <div class="card shadow-lg p-4">
            <h2 class="text-center title mb-4">🎓 Calculateur de Moyenne</h2>

            <form method="POST" class="row g-3">
                <div class="col-md-3"><input type="number" step="0.01" class="form-control" name="maths" placeholder="Maths (coef 5)" required></div>
                <div class="col-md-3"><input type="number" step="0.01" class="form-control" name="pc" placeholder="PC (coef 6)" required></div>
                <div class="col-md-3"><input type="number" step="0.01" class="form-control" name="svt" placeholder="SVT (coef 6)" required></div>
                <div class="col-md-3"><input type="number" step="0.01" class="form-control" name="histo" placeholder="Histo-Géo (coef 2)" required></div>
                <div class="col-md-3"><input type="number" step="0.01" class="form-control" name="francais" placeholder="Français (coef 3)" required></div>
                <div class="col-md-3"><input type="number" step="0.01" class="form-control" name="anglais" placeholder="Anglais (coef 2)" required></div>
                <div class="col-md-3"><input type="number" step="0.01" class="form-control" name="philo" placeholder="Philo (coef 2)" required></div>
                <div class="col-md-3"><input type="number" step="0.01" class="form-control" name="eps" placeholder="EPS (coef 1)" required></div>

                <div class="col-12 text-center mt-3">
                    <button type="submit" class="btn btn-dark px-5">Calculer</button>
                </div>
            </form>

            {f'''
            <div class="alert alert-{color} text-center mt-4">
                <h4>Moyenne : {moyenne} / 20</h4>
                <h5>Mention : {mention}</h5>
            </div>
            '
