from flask import Flask, request, render_template
import boto3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def book():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        service = request.form['service']
        date = request.form['date']
        time = request.form['time']

        # Send Email
        try:
            client = boto3.client('ses', region_name='us-east-1')
            client.send_email(
                Source='mujnabeen200@gmail.com',
                Destination={'ToAddresses': [email]},
                Message={
                    'Subject': {'Data': 'Appointment Confirmation'},
                    'Body': {
                        'Text': {
                            'Data': f"Hi {name},\n\nYour appointment for {service} on {date} at {time} is confirmed.\n\nThank you!"
                        }
                    }
                }
            )
            return "Booking confirmed! Check your email."
        except Exception as e:
            return f"Error sending email: {str(e)}"

    return render_template("form.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
