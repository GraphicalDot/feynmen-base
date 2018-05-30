#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import uuid
from kivy.properties import StringProperty, NumericProperty
from functools import partial


class TableHeader(Label):
    pass


class PlayerRecord(Label):
    pass


class MyGrid(GridLayout):

    def __init__(self, data, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.data = data
        self.display_scores()

    def fetch_data_from_database(self):
        self.data = [
            {'name': 'name', 'score': 'score', 'car': 'car'},
            {'name': 'przyczajony', 'score': '1337', 'car': 'Fiat 126p'},
            {'name': 'Krusader Jake', 'score': '777', 'car': 'Ford'},
            {'name': 'dummy', 'score': '10', 'car': 'none'},
            {'name': 'dummy', 'score': '102', 'car': 'none'},
            {'name': 'dummy', 'score': '60', 'car': 'none'},
            {'name': 'dummy', 'score': '990', 'car': 'none'},
            {'name': 'dummy', 'score': '550', 'car': 'none'},
            {'name': 'dummy', 'score': '310', 'car': 'none'},
            {'name': 'dummy', 'score': '320', 'car': 'none'},
            {'name': 'dummy', 'score': '880', 'car': 'none'}
        ]

    def display_scores(self):
        self.clear_widgets()
        for i in range(len(self.data)):
            if i < 1:
                row = self.create_header(i)
            else:
                row = self.create_player_info(i)
            for item in row:
                self.add_widget(item)

    def create_header(self, i):
        first_column = TableHeader(text=self.data[i]['name'])
        second_column = TableHeader(text=self.data[i]['score'])
        third_column = TableHeader(text=self.data[i]['car'])
        fourth_column = TableHeader(text="action")
        return [first_column, second_column, third_column, fourth_column]

    def create_player_info(self, i):
        first_column = PlayerRecord(text=self.data[i]['name'])
        second_column = PlayerRecord(text=self.data[i]['score'])
        third_column = PlayerRecord(text=self.data[i]['car'])
        fourth_column = Button(text="edit")
        fourth_column.bind(on_press=partial(self.on_enter, self.data[i]))
        return [first_column, second_column, third_column, fourth_column]

    def on_enter(self, *args):
        print (args[0])

class Table(App):
    pass


#Test().run()