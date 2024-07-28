# API KEY = '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'

url1="https://www.tylenol.com/products/tylenol-extra-strength-caplets"
medications_data = {
    'Common Cold': ('Acetaminophen (Tylenol)', f'you can buy this from: {url1}'),
    'Influenza (Flu)': ('Oseltamivir (Tamiflu)',),
    'Pneumonia': ('Antibiotics', 'Consult a doctor for dosage information'),
    'Asthma': ('Inhaler (Albuterol)', 'Consult a doctor for dosage information'),
    'Bronchitis': ('Antibiotics', 'Consult a doctor for dosage information'),
    'Allergic Rhinitis (Hay Fever)': ('Antihistamines (Loratadine)', 'Consult a doctor for dosage information'),
    'Gastroenteritis (Stomach Flu)': ('Hydration, antiemetics', 'Consult a doctor for dosage information'),
    'Urinary Tract Infection (UTI)': ('Antibiotics (Trimethoprim/sulfamethoxazole)', 'Consult a doctor for dosage information'),
    'Sinusitis': ('Decongestants, saline nasal spray', 'Consult a doctor for dosage information'),
    'Migraine': ('Pain relievers (Ibuprofen)', 'Consult a doctor for dosage information')
}


def identify_disease(symptoms):  # This function identifies the possible disease based on symptoms
    diseases_data = [
        ('Common Cold', 'Runny or stuffy nose, sore throat, cough, sneezing, mild body aches'),
        ('Influenza (Flu)', 'High fever, muscle aches, fatigue, headache, dry cough, sore throat'),
        ('Pneumonia', 'High fever, chills, cough with phlegm, shortness of breath, chest pain'),
        ('Asthma', 'Wheezing, shortness of breath, coughing, chest tightness, difficulty breathing'),
        ('Bronchitis', 'Persistent cough, chest discomfort, fatigue, shortness of breath, mucus production'),
        ('Allergic Rhinitis (Hay Fever)', 'Sneezing, runny or stuffy nose, itchy eyes, nose, or throat, watery eyes'),
        ('Gastroenteritis (Stomach Flu)', 'Diarrhea, nausea, vomiting, abdominal cramps, fever, dehydration'),
        ('Urinary Tract Infection (UTI)', 'Pain or burning sensation during urination, frequent urination, cloudy or bloody urine, pelvic pain'),
        ('Sinusitis', 'Facial pain or pressure, nasal congestion, headache, postnasal drip, loss of smell'),
        ('Migraine', 'Intense headache, often on one side of the head, nausea, vomiting, sensitivity to light and sound')
    ]

    for disease, symptom_list in diseases_data:
        symptoms_matched = set(symptoms.lower().split(',')) & set(symptom_list.lower().split(','))
        if len(symptoms_matched) > 0:
            return disease

    return "We couldn't identify any specific disease based on your symptoms. Please consult a healthcare professional for further evaluation."


def get_age_weight():
    age_years = int(input("Please enter your age in years (for example, 2 for a 2-year-old): "))
    weight_kg = float(input("Please enter your weight in kilograms (for example, 12 for 12 kg): "))
    age_months = age_years * 12
    return age_months, weight_kg

# Main starts
user_input = input("Please enter your symptoms separated by commas (for example, 'fever, cough'): ").strip()
result_disease = identify_disease(user_input)
print("Based on your symptoms, you may have ",result_disease)
med = result_disease
med_to_take=value = medications_data[med][0]

if med in medications_data:
    print("In this dieses you can take this medicine: ",med_to_take)
else:
    print("You should consult a doctor")