from flask import Flask, render_template, request, jsonify

app = Flask(__name__)   

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hesapla", methods=["POST"])
def hesapla():
    sayi1 = float(request.form["sayi1"])
    sayi2 = float(request.form["sayi2"])
    islem = request.form["islem"]

    if islem == "+":
        sonuc = sayi1 + sayi2
    elif islem == "-":
        sonuc = sayi1 - sayi2
    elif islem == "*":
        sonuc = sayi1 * sayi2
    elif islem == "/":
        if sayi2 == 0:
            sonuc = "Sıfıra bölünemez!"
        else:
            sonuc = sayi1 / sayi2
    else:
        sonuc = "Hatalı işlem"

    return jsonify({"sonuc": sonuc})

if __name__ == "__main__":
    app.run(debug=True)
