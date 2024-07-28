README
Overview
This project is a Flask-based web application integrated with Twilio for handling SMS messages. The application identifies potential diseases or injuries based on user-provided symptoms and recommends medications or first aid steps accordingly.

Prerequisites
Python 3.x
Flask
Twilio Python Helper Library
Ngrok (for exposing the local server to the internet)
Installation

Clone the Repository

git clone <repository-url>
cd <repository-directory>

Create a Virtual Environment

python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

Install Dependencies

pip install Flask twilio

Set Up Twilio Account

Sign up for a Twilio account here.
Get your Twilio Account SID and Auth Token.
Purchase a Twilio phone number capable of sending and receiving SMS.
Set Environment Variables
Create a .env file in the root directory and add your Twilio credentials:

TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
Usage

Run the Flask Application

python app.py
Expose the Flask App to the Internet

Use Ngrok to make the Flask app accessible over the internet.
ngrok http 5000
Copy the forwarding URL provided by Ngrok (e.g., http://<ngrok-url>.ngrok.io).

Configure Twilio Webhook

Go to the Twilio Console.
Navigate to your phone number settings.
Set the "Messaging" webhook to your Ngrok forwarding URL followed by / (e.g., http://<ngrok-url>.ngrok.io/).
Interacting with the Bot

Send an SMS with your symptoms to your Twilio phone number.
The bot will respond with a diagnosis and medication recommendations or first aid steps.
Project Structure
app.py: The main Flask application file containing routes and logic for handling incoming messages and providing recommendations.
medications_data: A dictionary containing medications, dosages, and usage instructions for various diseases.
identify_disease(): A function that identifies a possible disease based on provided symptoms.
identify_injury(): A function that identifies a possible injury based on provided symptoms.




