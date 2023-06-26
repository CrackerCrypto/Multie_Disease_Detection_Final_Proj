from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BreastCancerForm(FlaskForm):
    radius_mean = StringField('Enter radius mean: ', validators=[DataRequired()])
    texture_mean = StringField('Enter texture mean: ', validators=[DataRequired()])
    perimeter_mean = StringField('Enter perimeter mean: ', validators=[DataRequired()])
    area_mean = StringField('Enter area mean: ', validators=[DataRequired()])
    symmetry_mean = StringField('Enter symmetry mean: ', validators=[DataRequired()])
    radius_se = StringField('Enter radius se value:', validators=[DataRequired()])
    perimeter_se  =StringField('Enter perimeter se value:', validators=[DataRequired()])
    area_se = StringField('Enter area se value:', validators=[DataRequired()])
    radius_worst = StringField('Enter radius worst: ', validators=[DataRequired()])
    texture_worst = StringField('Enter texture worst: ', validators=[DataRequired()])
    perimeter_worst = StringField('Enter perimeter worst value:', validators=[DataRequired()])
    area_worst = StringField('Enter area worst value:', validators=[DataRequired()])
    smoothness_worst = StringField('Enter smoothness worst: ', validators=[DataRequired()])
    compactness_worst = StringField('Enter compactness worst: ', validators=[DataRequired()])

    submit = SubmitField("Submit")


class ThyroidForm(FlaskForm):
    tsh_value = StringField('Thyroid-stimulating Hormone value: ', validators=[DataRequired()])
    t3_value = StringField('Triiodothyronine value: ', validators=[DataRequired()])
    tt4_value = StringField('Total Thyroxine value: ', validators=[DataRequired()])
    t4u_value = StringField('Thyroxine Utilization Rate: ', validators=[DataRequired()])
    fti_value = StringField('Free Thyroxine Index value: ', validators=[DataRequired()])

    submit = SubmitField("Submit")


class FetalHealthForm(FlaskForm):
    baseline_value = StringField('Fetal Heart Rate: ', validators=[DataRequired()])
    abnormal_short_term_variability = StringField('Value of Short Term Variability(STV): ', validators=[DataRequired()])
    abnormal_long_term_variability = StringField('Value of Long Term Variability(LTV): ', validators=[DataRequired()])
    histogram_width = StringField('Width of FHR histogram: ', validators=[DataRequired()])
    histogram_min = StringField('Minimum of FHR histogram: ', validators=[DataRequired()])
    histogram_max = StringField('Maximum of FHR histogram: ', validators=[DataRequired()])
    histogram_mode = StringField('Mode of FHR histogram: ', validators=[DataRequired()])
    histogram_mean = StringField('Mean of FHR histogram: ', validators=[DataRequired()])
    histogram_median = StringField('Median of FHR histogram: ', validators=[DataRequired()])
    
    submit = SubmitField("Submit")