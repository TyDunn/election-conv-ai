Author: Ty Dunn
Created: December 2018

# Setup

Clone Repo
- `git clone https://github.com/TyDunn/election-conv-ai.git`

Install
- `pip install -r requirements.txt`
- `python -m spacy download en`
- Install `Flask` and `SQLite`

Makefile
- `make train-nlu`
- `make tain-core`
- `make cmdline`
- `make action-server`

# What is in this repo?
- rest_api
- nlu_data
- stories
- config

# How to use this?
- Say hello! 
- Ask the interface to start the questionnaire
- Answer the ten questions asked by the interface
- Recieve a final report about how your views align
- You can also ask questions about the views of candidates on the issues

# What to do next?
- Take it and run
- Look at my next steps ideas for inspiration
- Use it for your own local election

# Technologies
- [AWS](https://aws.amazon.com/)
- [Rasa Stack (NLU and Core)](https://rasa.com/docs/)
- [SpaCy](https://spacy.io/)
- [TensorFlow](https://www.tensorflow.org/)
- [FuzzyWuzzy](https://github.com/seatgeek/fuzzywuzzy)
- [Flask](http://flask.pocoo.org/)
- [SQLite](https://www.sqlite.org/index.html)
