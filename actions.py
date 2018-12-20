from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, AllSlotsReset
import requests
import json
from random import randint
from fuzzywuzzy import process
import datetime
import os

CANDIDATES = ["Florence Johnson", "Edward Vargas", "Jessica Lee", "Angela Newton",
	      "Muhammad Clark", "Leon Crawford", "Marcus Anderson", "Isabella Hughes"]

CANDIDATE_IDS = {"Florence Johnson": 1, "Edward Vargas": 2, "Jessica Lee": 3, "Angela Newton": 4,
		 "Muhammad Clark": 5, "Leon Crawford": 6, "Marcus Anderson": 7, "Isabella Hughes": 8}


class ActionAffirm(Action):
	def name(self):
		return 'action_affirm'
		
	def run(self, dispatcher, tracker, domain):
		
		user_id = tracker.get_slot('user_id')

		r = requests.post('http://{}/users'.format(os.environ['API_URL']), json={"user_id": user_id, "answer": 2})
		response = json.loads(r.text)
		
		user_id = response['user_id']
		question = response['response']

		response = "{}".format(question)
						
		dispatcher.utter_message(response)
		return [SlotSet('user_id', user_id)]


class ActionDeny(Action):
	def name(self):
		return 'action_deny'
		
	def run(self, dispatcher, tracker, domain):
		
		user_id = tracker.get_slot('user_id')
		
		r = requests.post('http://{}/users'.format(os.environ['API_URL']), json={"user_id": user_id, "answer": 1})
		response = json.loads(r.text)
		
		user_id = response['user_id']
		question = response['response']

		response = "{}".format(question)
						
		dispatcher.utter_message(response)
		return [SlotSet('user_id', user_id)]


class ActionQuesitonaire(Action):
	def name(self):
		return 'action_questionaire'
		
	def run(self, dispatcher, tracker, domain):
	
		user_id = tracker.get_slot('user_id')

		if not user_id:
			r = requests.post('http://{}/users'.format(os.environ['API_URL']), json={"user_id": 0, "answer": 0})
			response = json.loads(r.text)
		
			user_id = response['user_id']
			question = response['response']

			response = "I can help you figure out how you align with the candidates. All you need to do is answer the following questions. {}".format(question)
						
		else:
			response = "You have already completed the questionaire!"

		dispatcher.utter_message(response)
		return [SlotSet('user_id', user_id)]


class ActionAskEnergy(Action):
	def name(self):
		return 'action_ask_energy'

	def run(self, dispatcher, tracker, domain):
		
		name = tracker.get_slot('name')
		name = process.extractOne(name, CANDIDATES)[0]
		candidate_id = CANDIDATE_IDS[name]
		
		r = requests.get('http://{}/candidates/{}/1'.format(os.environ['API_URL'], candidate_id))
		response = json.loads(r.text)

		if response['answer'] == 2:
			answer = "supports"
		else:
			answer = "does not support"

		response = "{} {} the government subsidizing alternative energy.".format(name, answer)

		dispatcher.utter_message(response)


class ActionAskMarijuana(Action):
	def name(self):
		return 'action_ask_marijuana'

	def run(self, dispatcher, tracker, domain):
		
		name = tracker.get_slot('name')
		name = process.extractOne(name, CANDIDATES)[0]
		candidate_id = CANDIDATE_IDS[name]

		r = requests.get('http://{}/candidates/{}/2'.format(os.environ['API_URL'], candidate_id))
		response = json.loads(r.text)

		if response['answer'] == 2:
			answer = "supports"
		else:
			answer = "does not support"

		response = "{} {} the legalizaiton of marijuana.".format(name, answer)

		dispatcher.utter_message(response)


class ActionAskSpace(Action):
	def name(self):
		return 'action_ask_space'

	def run(self, dispatcher, tracker, domain):
		
		name = tracker.get_slot('name')
		name = process.extractOne(name, CANDIDATES)[0]
		candidate_id = CANDIDATE_IDS[name]

		r = requests.get('http://{}/candidates/{}/3'.format(os.environ['API_URL'], candidate_id))
		response = json.loads(r.text)

		if response['answer'] == 2:
			answer = "supports"
		else:
			answer = "does not support"

		response = "{} {} the government funding space exploration.".format(name, answer)

		dispatcher.utter_message(response)


class ActionAskTransit(Action):
	def name(self):
		return 'action_ask_transit'

	def run(self, dispatcher, tracker, domain):
		
		name = tracker.get_slot('name')
		name = process.extractOne(name, CANDIDATES)[0]
		candidate_id = CANDIDATE_IDS[name]

		r = requests.get('http://{}/candidates/{}/4'.format(os.environ['API_URL'], candidate_id))
		response = json.loads(r.text)

		if response['answer'] == 2:
			answer = "supports"
		else:
			answer = "does not support"

		response = "{} {} increasing spending on public transportation.".format(name, answer)

		dispatcher.utter_message(response)


class ActionAskHealthcare(Action):
	def name(self):
		return 'action_ask_healthcare'

	def run(self, dispatcher, tracker, domain):
		
		name = tracker.get_slot('name')
		name = process.extractOne(name, CANDIDATES)[0]
		candidate_id = CANDIDATE_IDS[name]

		r = requests.get('http://{}/candidates/{}/5'.format(os.environ['API_URL'], candidate_id))
		response = json.loads(r.text)

		if response['answer'] == 2:
			answer = "supports"
		else:
			answer = "does not support"

		response = "{} {} universal healthcare for all citizens.".format(name, answer)

		dispatcher.utter_message(response)


class ActionAskBorders(Action):
	def name(self):
		return 'action_ask_borders'

	def run(self, dispatcher, tracker, domain):
		
		name = tracker.get_slot('name')
		name = process.extractOne(name, CANDIDATES)[0]
		candidate_id = CANDIDATE_IDS[name]

		r = requests.get('http://{}/candidates/{}/6'.format(os.environ['API_URL'], candidate_id))
		response = json.loads(r.text)

		if response['answer'] == 2:
			answer = "supports"
		else:
			answer = "does not support"

		response = "{} {} doing more to secure our borders.".format(name, answer)

		dispatcher.utter_message(response)


class ActionAskDefense(Action):
	def name(self):
		return 'action_ask_defense'

	def run(self, dispatcher, tracker, domain):
		
		name = tracker.get_slot('name')
		name = process.extractOne(name, CANDIDATES)[0]
		candidate_id = CANDIDATE_IDS[name]

		r = requests.get('http://{}/candidates/{}/7'.format(os.environ['API_URL'], candidate_id))
		response = json.loads(r.text)

		if response['answer'] == 2:
			answer = "supports"
		else:
			answer = "does not support"

		response = "{} {} decreasing government spending on defense.".format(name, answer)

		dispatcher.utter_message(response)


class ActionAskInternet(Action):
	def name(self):
		return 'action_ask_internet'

	def run(self, dispatcher, tracker, domain):
		
		name = tracker.get_slot('name')
		name = process.extractOne(name, CANDIDATES)[0]
		candidate_id = CANDIDATE_IDS[name]

		r = requests.get('http://{}/candidates/{}/8'.format(os.environ['API_URL'], candidate_id))
		response = json.loads(r.text)

		if response['answer'] == 2:
			answer = "supports"
		else:
			answer = "does not support"

		response = "{} {} requiring ISPs to treat all data on the Internet equally.".format(name, answer)

		dispatcher.utter_message(response)


class ActionAskGunControl(Action):
	def name(self):
		return 'action_ask_guncontrol'

	def run(self, dispatcher, tracker, domain):
		
		name = tracker.get_slot('name')
		name = process.extractOne(name, CANDIDATES)[0]
		candidate_id = CANDIDATE_IDS[name]

		r = requests.get('http://{}/candidates/{}/9'.format(os.environ['API_URL'], candidate_id))
		response = json.loads(r.text)

		if response['answer'] == 2:
			answer = "supports"
		else:
			answer = "does not support"

		response = "{} {} adding more restrictions on the purchase of guns.".format(name, answer)

		dispatcher.utter_message(response)


class ActionAskCorporations(Action):
	def name(self):
		return 'action_ask_corporations'

	def run(self, dispatcher, tracker, domain):
		
		name = tracker.get_slot('name')
		name = process.extractOne(name, CANDIDATES)[0]
		candidate_id = CANDIDATE_IDS[name]

		r = requests.get('http://{}/candidates/{}/10'.format(os.environ['API_URL'], candidate_id))
		response = json.loads(r.text)

		if response['answer'] == 2:
			answer = "supports"
		else:
			answer = "does not support"

		response = "{} {} decreasing the influence of corporations in politics".format(name, answer)

		dispatcher.utter_message(response)
