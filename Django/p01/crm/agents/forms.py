from django import forms
from leads.models import Agent

class AgentModeForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            'user',
        )