from django.shortcuts import render, redirect
import joblib

model = joblib.load(r'D:\Projects\SPAM\spam_detector_project\detector\spam_classifier.pkl')

def home(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            prediction = model.predict([message])
            print("Model Prediction:", prediction)  # Debug print
            result = "Spam" if prediction[0] == "spam" else "Not Spam"
            request.session['result'] = result
            request.session['message'] = message
            return redirect('home')
    result = request.session.pop('result', '')
    message = request.session.pop('message', '')
    return render(request, 'detector/home.html', {'result': result, 'message': message})


