from controller import ExampleSwitch13

from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib import hub

import os
import csv
import numpy as np
import pandas as pd
import tensorflow as tf
#import xgboost as xgb
from catboost import CatBoostClassifier

class Traffic_Classifier(ExampleSwitch13):
	def __init__(self, *args, **kwargs):
		super(Traffic_Classifier, self).__init__(*args, **kwargs)
		self.monitor_thread = hub.spawn(self._monitor)
		self.files = {}
		self.all_features = {}
		self.sleep_interval = 10 
		#self.model = tf.keras.models.load_model("tf_model.pkl") 
		self.model = CatBoostClassifier()
		self.model.load_model('cat_boost')
		self.output = open("result.txt", "a")
	
	def _monitor(self):
		while True:
		    #print("Plussssss Ultraaaaa!!!")
		    hub.sleep(self.sleep_interval)
		    features = self.extract_features()
		    if len(features) > 0:
		    	print("Doing Inference!!")
		    	prediction = self.inference(features) 
		    
	def extract_features(self):
		features = []
		for file in os.listdir(os.getcwd()):
		#Format of csv file -> flow_x_y.csv
			t = file.split(".")
			if t[-1] == "csv":
				with open(file) as csvfile:
					csv_dict = [row for row in csv.DictReader(file)]
					if len(csv_dict) == 0:
						continue
				temp = pd.read_csv(file)	
				dr = temp[['src_ip','dst_ip','src_port','dst_port','timestamp']]
				temp.drop(['src_ip','dst_ip','src_port','dst_port','timestamp'],axis=1,inplace=True)
				features.append([dr, temp])
				print("Successfully extracted features!!")
		return features
		
	def inference(self, features):
		for f in features:
			res = self.model.predict(f[1].to_numpy())
			if np.argmax(res) == 0:
				self.output.write("No Attack Detected!")
				print("No Attack Detected!")
			elif np.argmax(res) == 1:
				self.output.write("LDAP Attack Detected")
				print("LDAP Attack Detected")
			elif np.argmax(res) == 2:
				self.output.write("MSSQL Attack Detected")
				print("MSSQL Attack Detected")
			elif np.argmax(res) == 3:
				self.output.write("NetBIOS Attack Detected")
				print("NetBIOS Attack Detected")
			elif np.argmax(res) == 4:
				self.output.write("Portmap Attack Detected")
				print("Portmap Attack Detected")
			elif np.argmax(res) == 5:
				self.output.write("SYN Attack Detected")
				print("SYN Attack Detected")
			elif np.argmax(res) == 6:
				self.output.write("UDP Detected")
				print("UDP Detected")
			elif np.argmax(res) == 7:
				self.output.write("UDPLag Detected")
				print("UDPLag Detected")
			print("Inference Completed")