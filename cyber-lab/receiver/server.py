from flask import Flask, request, jsonify, render_template_string
from datetime import datetime

app = Flask(__name__)
latest = []

PAGE = '''<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Cybersecurity Consent Lab</title><style>body{font-family:Arial;background:#f5e8ee;color:#43202d;margin:0;padding:24px}.card{max-width:900px;margin:auto;background:white;padding:28px;border-radius:20px;box-shadow:0 15px 50px #7b294833}h1{margin-top:0}.ok{color:#19713a}.warn{background:#fff3cd;padding:12px;border-radius:10px}table{width:100%;border-collapse:collapse;margin-top:20px}th,td{padding:10px;border-bottom:1px solid #eee;text-align:left}</style></head><body><div class="card"><h1>Cybersecurity Consent Lab</h1><p class="ok">Receiver running.</p><p class="warn">This lab accepts synthetic test records only. Use it to study client/server communication without transmitting real private call history.</p>{% if latest %}<p><b>Test device:</b> {{ latest.device }} · <b>Received:</b> {{ latest.time }}</p><table><tr><th>Number</th><th>Type</th><th>Date</th><th>Duration</th></tr>{% for r in latest.records %}<tr><td>{{r.number}}</td><td>{{r.type}}</td><td>{{r.date}}</td><td>{{r.durationSeconds}}s</td></tr>{% endfor %}</table>{% else %}<p>No test data received yet.</p>{% endif %}</div></body></html>'''

@app.get('/')
def home():
    return render_template_string(PAGE, latest=latest[-1] if latest else None)

@app.post('/upload')
def upload():
    data = request.get_json(force=True)
    records = data.get('records', [])
    # Accept only records explicitly marked as synthetic test data.
    if data.get('mode') != 'synthetic' or not all(r.get('synthetic') is True for r in records):
        return jsonify({'ok': False, 'error': 'Only synthetic lab records are accepted.'}), 400
    latest.append({'device': data.get('device','Test Device'), 'records': records, 'time': datetime.now().isoformat(timespec='seconds')})
    return jsonify({'ok': True, 'received': len(records)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
