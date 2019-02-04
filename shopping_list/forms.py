from django import forms

class ShoppingForm(forms.Form):
	text = forms.CharField(max_length = 40,
		widget = forms.TextInput(attrs={"id" : "myInput", "placeholder" : "Add an item to your shopping list...", "align": "center"}))