# python 3
# this class combines all basic features of a generic player
import numpy as np
import pandas as pa
random_lambda = np.random.rand(48)
class Player:

	def __init__(self):
		# some player might not have parameters
		self.parameters = 0
		self.horizon = 48
		self.nb_slow=2
		self.nb_fast=2
		self.pslow=3
		self.pfast=22
		self.capacite_min=10
		self.capacite=40
		self.rho_c=0.95


	def set_scenario(self, scenario_data):
		self.data = scenario_data
		# depart et arr contiennent respectivement la liste des heures de départ et d'arrivée des véhicules à la date d
		d="01/01/2014"
		self.depart=list(scenario_data[(scenario_data["day"] == d)]["time_slot_dep"][:p.nb_slow + p.nb_fast])
		self.arr = list(scenario_data[(scenario_data["day"] == d)]["time_slot_arr"][:p.nb_slow + p.nb_fast])

	def set_prices(self, prices):
		self.prices = prices

	def compute_all_load(self):
		load = np.zeros(self.horizon+self.nb_slow+self.nb_fast)
		# l est une liste temporaire, on reprend ses valeurs et on les réordonne avant de les mettre dans load

		#chargement prend en compte le chargement pour chacun des véhicules
		chargement=np.zeros(self.nb_slow+self.nb_fast)

		m = np.min(self.depart)
		copie_prix=self.prices[:m].copy()
		cpt=0
		while cpt<m:
			arg_min = np.argmin(copie_prix)
			for i in range (self.nb_slow + self.nb_fast):
				arg_min=np.argmin(chargement)
				if (chargement[arg_min]<10):
					if (i<self.nb_fast):
						plus=min(self.pfast,(10-chargement[arg_min])/self.roh_c)
						chargement[arg_min]+=plus*self.roh_c
						load[arg_min]+=plus
					else:
						plus+=min(self.pslow,(10-chargement[arg_min])/self.roh_c)
						chargement[arg_min]+=plus*self.roh_c
						load[arg_min]+=plus
			copie_prix[arg_min] = np.inf
			cpt+=1
		for i in range (self.nb_slow + self.nb_fast):
			load[self.horizon+i]=chargement[i]
		print(load)
		return load

	def take_decision(self, time):
		# TO BE COMPLETED
		return 0

	def compute_load(self, time):
		load = self.take_decision(time)

		return load

	def reset(self):
		# reset all observed data
		pass

def cout(p,l):
	c=0
	for time in range(48):
		c+=l[time]*p[time]
	for i in range(self.nb_slow+self.nb_fast):
		if (l[self.horizon+i]<self.capacite_min):
			c+=5
	return c
#print(cout(p.prices,l))

if __name__=="__main__":
	import os
	print(os.getcwd())
	f=pa.read_csv("C:\\Users\\xache\\Documents\\ENPC\\1A\\S2\\microgrid-player-1\\ev_scenarios.csv")
	p=Player()
	p.__init__()
	p.set_scenario(f)
	p.set_prices(random_lambda)

	l=p.compute_all_load()

#fonction de cout qui ne prend pas encore en compte les amendes si les voitures ne sont pas chargées à temps
