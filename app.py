from flask import Flask, render_template, request, session
app = Flask(__name__)

from API_KEY import apiKey

import cohere
from cohere.classify import Example


@app.route("/")
def home():
    return render_template("index.html", label="")


@app.route("/chat", methods=["GET", "POST"])
def chat():
    inp = request.form.get('text-chat')
    print(inp)

    co = cohere.Client(apiKey)
    response = co.classify(
    inputs=[inp],
    examples=[Example("love this movie", "positive"), 
        Example("I would watch this movie again with my friends", "positive"), 
        Example("I would watch this movie again", "positive"), 
        Example("i liked this book", "positive"), 
        Example("this is my favourite thing to do", "positive"), 
        Example("worst movie of all time", "negative"), 
        Example("I would not recommend this place to my friends", "negative"), 
        Example("I did not want to finish the run", "negative"), 
        Example("hate this show", "negative"), 
        Example("we made it only a quarter way through before we stopped", "negative"), 
        Example("this movie was okay", "neutral"), 
        Example("this movie was neither amazing or terrible", "neutral"), 
        Example("I would not watch this movie again but it was not a waste of time", "neutral"), 
        Example("this movie lacked any originality or depth", "neutral"), 
        Example("this movie was nothing special", "neutral"), 
        Example("I hate the student union. Their products are designed to cause headaches", "negative"), 
        Example("Nush, Ryan and Josh are good teammates because they are very supportive and empathetic", "positive"), 
        Example("Theresa has horrible taste", "negative"), 
        Example("today is Saturday", "neutral"),
        Example("Hack the North is a great event because it promotes teamwork, critical thinking and hardwork", "positive")])

    print('The confidence levels of the labels are: {}'.format(response.classifications)) 
    prediction = response.classifications[0].prediction
    print(prediction)

    return render_template("index.html", label=prediction)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
