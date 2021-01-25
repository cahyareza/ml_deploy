from django import forms

GENDER_CHOICES = [
    (1, 'M'),
    (0, 'F')
]

MARRIED_CHOICES = [
    (1, 'Yes'),
    (0, 'No')
]

DEPENDENTS_CHOICES = [
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3+')
]

EDUCATION_CHOICES = [
    (0, 'Graduate'),
    (1, 'Not Graduate')
]

SELF_EMPLOYED_CHOICES = [
    (1, 'Yes'),
    (0, 'No')
]

CREDIT_HISTORY_CHOICES = [
    (1, 'debt paid'),
    (0, 'debt not paid')
]

PROPERTY_AREA_CHOICES = [
    (2, 'Rural'),
    (1, 'Semiurban'),
    (3, 'Urban')
]

LOAN_AMOUNT_TERM_CHOICES = [
    (360, '12 MONTHS'),
    (270, '9 MONTHS'),
    (180, '6 MONTHS'),
    (90, '3 MONTHS'),
]


class EstimateForm(forms.Form):
    Gender = forms.ChoiceField(choices=GENDER_CHOICES)
    Married = forms.ChoiceField(choices=MARRIED_CHOICES)
    Dependents = forms.ChoiceField(choices=DEPENDENTS_CHOICES)
    Education = forms.ChoiceField(choices=EDUCATION_CHOICES)
    Self_Employed = forms.ChoiceField(choices=SELF_EMPLOYED_CHOICES)
    ApplicantIncome = forms.DecimalField(max_digits=10, decimal_places=2)
    CoapplicantIncome = forms.DecimalField(max_digits=10, decimal_places=2)
    LoanAmount = forms.DecimalField(max_digits=10, decimal_places=2)
    Loan_Amount_Term = forms.ChoiceField(choices=LOAN_AMOUNT_TERM_CHOICES)
    Credit_History = forms.ChoiceField(choices=CREDIT_HISTORY_CHOICES)
    Property_Area = forms.ChoiceField(choices=PROPERTY_AREA_CHOICES)