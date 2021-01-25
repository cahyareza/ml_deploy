from django.test import TestCase
from .forms import EstimateForm
from estimate import build_model

# Create your tests here.
class EstimateTestsForm(TestCase):

    def setUp(self):
        self.form_data = {
            'Gender': 1,
            'Married': 0,
            'Dependents': 3,
            'Education': 0,
            'Self_Employed': 1,
            'ApplicantIncome': 100000,
            'CoapplicantIncome': 3000,
            'LoanAmount': 40000,
            'Loan_Amount_Term': 270,
            'Credit_History': 1,
            'Property_Area': 2,
        }


    def test_estimate_form_gender_field_label(self):
        form = EstimateForm()
        self.assertTrue(form.fields['Gender'].label == None or form.fields['Gender'].label == 'Gender')

    def test_forms(self):
        form = EstimateForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    # view test
    def test_home_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    # if form add with data go to "result/" if not return to home
    def test_result_url_exists_at_desired_location(self):
        form = EstimateForm(data=self.form_data)
        if self.assertTrue(form.is_valid()):
            response = self.client.get('result/')
            self.assertEqual(response.status_code, 200)
        else:
            form = EstimateForm()
            response = self.client.get('')
            self.assertEqual(response.status_code, 200)

    def test_home_uses_correct_template(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')


    def test_result_uses_correct_template(self):
        form = EstimateForm(data=self.form_data)
        if self.assertTrue(form.is_valid()):
            response = self.client.get('result/')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'result.html')
        else:
            form = EstimateForm()
            response = self.client.get('')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'form.html')

    def result_get(self):
        form = EstimateForm(data=self.form_data)
        if self.form.is_valid():
            data = self.form.cleaned_data
            int_features = [x for x in data.values()]
            final = np.array(int_features)
            df = pd.DataFrame([final], columns=cols)
            df['Gender'] = df['Gender'].astype('int8')
            df['Married'] = df['Married'].astype('int8')
            df['Dependents'] = df['Dependents'].astype('int8')
            df['Education'] = df['Education'].astype('int8')
            df['Self_Employed'] = df['Self_Employed'].astype('int8')
            df['Credit_History'] = df['Credit_History'].astype('int8')
            df['Property_Area'] = df['Property_Area'].astype('int8')
            df['ApplicantIncome'] = df['ApplicantIncome'].astype('int64')
            df['CoapplicantIncome'] = df['CoapplicantIncome'].astype('float64')
            df['LoanAmount'] = df['LoanAmount'].astype('float64')
            df['Loan_Amount_Term'] = df['Loan_Amount_Term'].astype('float64')
            df = build_model.ins_null(df)

            with open('/Users/apple/Documents/course_DPHi_DataScience_Bootcamp_Advance/assignment_3/clf_model.pkl','rb') as file:
                model = pickle.load(file)

            result = model.predict(df)[0]
            self.assertEqual(response.status_code, [1])