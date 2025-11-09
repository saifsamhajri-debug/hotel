# ...existing code...
from hotel import create_app
from flask import request, jsonify

app = create_app()

# أسعار تحويل توضيحية إلى الريال اليمني (حدّثها حسب السعر الحقيقي أو اربط API خارجي)
RATES_TO_YER = {
    "YER": 1.0,
    "SAR": 66.0,
    "JOD": 350.0,
    "KWD": 4500.0,
    "BHD": 4000.0,
    "IQD": 0.18,
    "USD": 250.0
}

@app.route("/convert", methods=["GET"])
def convert_currency():
    try:
        amount = float(request.args.get("amount", 1))
    except (TypeError, ValueError):
        return jsonify({"error": "amount must be a number"}), 400

    frm = request.args.get("from", "JOD").upper()
    to = request.args.get("to", "YER").upper()

    if frm not in RATES_TO_YER or to not in RATES_TO_YER:
        return jsonify({"error": "unsupported currency", "supported": list(RATES_TO_YER.keys())}), 400

    converted = amount * RATES_TO_YER[frm] / RATES_TO_YER[to]
    return jsonify({
        "amount": amount,
        "from": frm,
        "to": to,
        "converted": round(converted, 6)
    })

if __name__ == '__main__':
    app.run(debug=True)
# ...existing code...