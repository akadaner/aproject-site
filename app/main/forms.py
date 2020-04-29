from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, SubmitField, SelectField, FloatField, FileField
from wtforms.validators import Required, InputRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    curname = StringField('What is your curname?', validators=[Required()])
    submit = SubmitField('Submit')


class ImageForm(FlaskForm):
    url = StringField('What is your avatar?', validators=[Required()])
    submit = SubmitField('Submit')


class UploadForm(FlaskForm):
    validators = [
        FileRequired(message='There was no file!'),
        FileAllowed(['mat'], message='Must be a mat file!')
    ]

    input_file = FileField('', validators=validators)
    model_name = StringField("Enter model name:", validators=[Required()])
    dxvalue = FloatField("Enter value dx, m: ", validators=[Required()])
    submit = SubmitField(label="Submit")


class ScattererForm(FlaskForm):
    model_names_list = SelectField('Field name', coerce=int, validators=[InputRequired()])
    radius = FloatField("Enter value radius, mm", default=0.0001)
    longitudinal = FloatField("Enter longitudinal speed of sound, m/s", default=2620.0)
    transverse = FloatField("Enter transverse speed of sound, m/s", default=1080.0)
    density_of_scatter = FloatField("Enter density of scatterer, kg/m^3", default=1125.0)
    frequency = FloatField("Enter value of frequency", default=1000000)
    speed_of_sound = FloatField("Enter value speed of sound", default=1500.0)
    density_of_medium = FloatField("Enter density of medium", default=1000.0)
    type_value = StringField("Enter type of coordinates (X, Y or Z)", default='Z')
    from_value = FloatField("Enter begin coordinate value", default=-0.02)
    to_value = FloatField("Enter end coordinate value", default=0.02)
    step = FloatField("Enter step value", default=0.001)
    submit = SubmitField(label="Submit")


class ModelResultsForm(FlaskForm):
    model_names_list = SelectField('Field name', coerce=int, validators=[InputRequired()], default=None)
    submit = SubmitField(label="Search")