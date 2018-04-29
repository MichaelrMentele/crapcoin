from django import forms


class BlockCreateForm(forms.Form):
    payee = forms.CharField()
    payer = forms.CharField()
    amount = forms.CharField()
    signing_private_key = forms.CharField()

    def is_valid(self):
        return (self.data['payee'] and
                self.data['payer'] and
                self.data['amount'] and
                self.data['signing_private_key'])
