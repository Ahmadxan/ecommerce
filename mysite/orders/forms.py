from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['size', 'quantity', 'pay_type', 'address']

        # def form_valid(self):
        #     self.model.product_id = self.request.product

        # widgets = {
        #     'size': forms.TextInput(
        #         attrs={
        #             'class': 'form control'
        #         }
        #     ),
        #     'quantity': forms.TextInput(
        #         attrs={
        #             'class': 'form control'
        #         }
        #     ),
        #     'pay_type': forms.TextInput(
        #         attrs={
        #             'class': 'form control'
        #         }
        #     ),
        #     'address': forms.TextInput(
        #         attrs={
        #             'class': 'form control'
        #         }
        #     )
        # }
