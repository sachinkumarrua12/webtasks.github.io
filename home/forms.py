from cProfile import label
from dataclasses import fields
import email
from pyexpat import model
from tkinter import Label
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import forms
from django.shortcuts import render

class SignUpForm(UserCreationForm):
    password2 =forms.CharField(label = 'confirm password(again)')
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}

