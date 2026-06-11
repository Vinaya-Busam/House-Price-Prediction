import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('Model/house_price_prediction.pkl', 'rb'))

