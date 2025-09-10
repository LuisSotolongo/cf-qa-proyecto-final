import json
import pytest

def save_html_report(filename, title, payload, response):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"<h1>{title}</h1>")
        f.write(f"<h2>Payload</h2><pre>{json.dumps(payload, indent=2, ensure_ascii=False)}</pre>")
        f.write(f"<h2>Respuesta</h2><pre>{json.dumps(response, indent=2, ensure_ascii=False)}</pre>")

def save_json_screenshot(filename, payload, response):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump({"payload": payload, "response": response}, f, indent=2, ensure_ascii=False)