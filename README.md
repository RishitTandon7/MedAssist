README

PROJECT TITLE : MED ASSIST


Overview

Med Assist identifies potential diseases or injuries based on user-provided symptoms and recommends medications or first aid steps accordingly.
This application is an innovative health assistant platform integrating a WhatsApp chatbot with a user-friendly web interface. The project uses Twilio for chatbot functionality, Python for backend logic, and Ngrok for secure local development. The frontend is designed with HTML and CSS and features essential navigation tabs to enhance user experience.


Prerequisites:

Twilio Account- Needed for WhatsApp access.
Python-Required for backend development.
Ngrok - Used for exposing the local server to the internet.
Basic Knowledge - Familiarity with HTML, CSS, and Python.



Features:

WhatsApp Chatbot Integration: 
Twilio: Facilitates WhatsApp API integration, enabling the chatbot to interact with users and recommend medicines based on symptoms.
Python: Manages backend processes and interacts with the Twilio API.
Ngrok: Provides a secure tunnel for local development, exposing your local Python server to the internet.


Frontend Development:
HTML & CSS: Ensure a modern, responsive design with intuitive navigation.


Website Navigation Tabs:

 Home: Main landing page of the site.
 Prevention: Links to Wikipedia articles related to health prevention.
 Shop: Displays a list of available medicines.
 Cart: Shows the number of items in the shopping cart.
 Track Your Order: Allows users to track the status of their orders.
 About Us: Provides a brief description of the project and team.
 Contact Us: Contains contact details and an inquiry form.




Installation process:

1. Clone the Repository:
   bash
   git clone https://github.com/your-repository/medassist.git
   cd medassist
   

2. Set Up Python Environment:
   bash
   python -m venv venv
   source venv/bin/activate  # For Unix-based systems
   venv\Scripts\activate     # For Windows
   pip install -r requirements.txt
   

3. Configure Twilio:
   - Sign up for a Twilio account and obtain the Account SID, Auth Token, and a WhatsApp-enabled phone number.
   - Set up the environment variables or configuration file with these details.

4. Create a Python Script:
   Create a file named app.py and add the following code to handle WhatsApp messages:

   python
   from flask import Flask, request, jsonify
   from twilio.rest import Client
   from twilio.twiml.messaging_response import MessagingResponse

   app = Flask(__name__)

   # Twilio credentials
   ACCOUNT_SID = 'your_account_sid'
   AUTH_TOKEN = 'your_auth_token'
   TWILIO_PHONE_NUMBER = 'whatsapp:+your_twilio_number'

   client = Client(ACCOUNT_SID, AUTH_TOKEN)

   @app.route('/whatsapp', methods=['POST'])
   def whatsapp():
       incoming_msg = request.values.get('Body', '').lower()
       resp = MessagingResponse()

       if 'symptom' in incoming_msg:
           # Example response, replace with actual logic
           response_message = 'Based on your symptoms, we recommend XYZ medicine.'
       else:
           response_message = 'Please describe your symptoms to receive a recommendation.'

       resp.message(response_message)
       return str(resp)

   if __name__ == '__main__':
       app.run(debug=True)
   

5. Run Ngrok:
   Start Ngrok to expose your local server:
   bash
   ngrok http 5000
   

6. Update Twilio Webhook URL:
   Configure your Twilio WhatsApp number to use the Ngrok URL for incoming messages:
   - Go to the Twilio Console.
   - Navigate to the "Messaging" section.
   - Under "Configure," set the webhook URL to http://<ngrok-url>/whatsapp.

7. Customize Frontend:
   Edit HTML and CSS files as needed to fit the project requirements.

8. Deploy the Frontend:
   Host the frontend files on a web server or a platform like GitHub Pages or Netlify.

Demo Video Link: https://drive.google.com/file/d/1qLj4cJwJ6W3qk7amkL8-lDJqs1-KYFQb/view?usp=drivesdk

To use the WhatsApp chatbot we need to go on this number and type this code:
+14155238886

Join under-tired



