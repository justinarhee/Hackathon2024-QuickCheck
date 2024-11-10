import pandas as pd
from flask import Flask, request, redirect, url_for, send_file
import csv
import qrcode
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    with open("form.html") as f:
        html = f.read()
    return html

@app.route('/submit', methods=['POST'])
def get_input():
    patient_dict = {}
    
    patient_dict["First Name"] = request.form.get("fname")
    patient_dict["Middle Name"] = request.form.get("mname")
    patient_dict["Last Name"] = request.form.get("lname")
    patient_dict["Suffix"] = request.form.get("suffix")
    patient_dict["Date of Birth"] = request.form.get("dob")
    patient_dict["Sex"] = request.form.get("sex")
    patient_dict["Address"] = request.form.get("address")
    patient_dict["City"] = request.form.get("city")
    patient_dict["Zip"] = request.form.get("zip")
    patient_dict["State"] = request.form.get("state")
    patient_dict["Country"] = request.form.get("country")
    patient_dict["Language"] = request.form.get("language")
    patient_dict["SSN"] = request.form.get("ssn")
    patient_dict["Contact"] = request.form.get("contact")
    patient_dict["Email"] = request.form.get("email")
    patient_dict["Emergency Contact #1 First Name"] = request.form.get("emergency1-fname")
    patient_dict["Emergency Contact #1 Last Name"] = request.form.get("emergency1-lname")
    patient_dict["Emergency Contact #1 Relation"] = request.form.get("emergency1-relation")
    patient_dict["Emergency Contact #1 Phone"] = request.form.get("emergency1-phone")
    patient_dict["Emergency Contact #1 Email"] = request.form.get("emergency1-email")
    patient_dict["Emergency Contact #2 First Name"] = request.form.get("emergency2-fname")
    patient_dict["Emergency Contact #2 Last Name"] = request.form.get("emergency2-lname")
    patient_dict["Emergency Contact #2 Relation"] = request.form.get("emergency2-relation")
    patient_dict["Emergency Contact #2 Phone"] = request.form.get("emergency2-phone")
    patient_dict["Emergency Contact #2 Email"] = request.form.get("emergency2-email")
    patient_dict["Provider"] = request.form.get("provider")
    patient_dict["Policy Number"] = request.form.get("policy-number")
    patient_dict["Policy Holder Name"] = request.form.get("policy-holder")
    patient_dict["Policy Holder Date of Birth"] = request.form.get("policy-dob")
    patient_dict["Billing Address"] = request.form.get("billing-address")
    patient_dict["Billing City"] = request.form.get("billing-city")
    patient_dict["Billing ZIP Number"] = request.form.get("billing-zip")
    patient_dict["Billing State"] = request.form.get("billing-state")
    patient_dict["Billing Country"] = request.form.get("billing-country")
    patient_dict["Medications"] = request.form.get("medications")
    patient_dict["Allergies"] = request.form.get("allergies")
    patient_dict["Past Illnesses"] = request.form.get("past-illnesses")
    patient_dict["Family History"] = request.form.get("family_history")
    
    patient_keys = patient_dict.keys()

    csv_file_path = "patient.csv"
    with open(csv_file_path, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=patient_keys)
        writer.writeheader()
        writer.writerow(patient_dict)

    qr_code_image_path = "qrcode.png"
    qrcode_ticket = qrcode.make(request.host_url + csv_file_path)
    qrcode_ticket.save(qr_code_image_path)

    return redirect(url_for('ticket_html'))

@app.route('/ticket.html')
def ticket_html():
    with open("ticket.html") as f:
        html = f.read()
    return html

@app.route('/qrcode.png')
def serve_qr_code():
    return send_file("qrcode.png", mimetype='image/png')

@app.route('/patient.csv')
def download_csv():
    return send_file("patient.csv", as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, threaded=False) # don't change this line!
