from . import app, db
from .models import Medico, Paciente, Consultorio, Cita
from flask import render_template, request

@app.route('/medicos')
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template('medicos.html', medicos = medicos)

@app.route('/pacientes')
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template('pacientes.html', pacientes = pacientes)

@app.route('/consultorios')
def get_all_consultorios():
    consultorios = Consultorio.query.all()
    return render_template('consultorios.html', consultorios = consultorios)

@app.route('/citas')
def get_all_citas():
    citas = Cita.query.all()
    return render_template('citas.html', citas = citas)

@app.route('/medicos/<int:id>')
def get_medico_by_id(id):
    medico = Medico.query.get(id)
    return render_template('medico.html', medico = medico)

@app.route('/pacientes/<int:id>')
def get_paciente_by_id(id):
    paciente = Paciente.query.get(id)
    return render_template('paciente.html', paciente = paciente)

@app.route('/consultorios/<int:id>')
def get_consultorio_by_id(id):
    consultorio = Consultorio.query.get(id)
    return render_template('consultorio.html', consultorio = consultorio)

@app.route('/medicos/create', methods = ['GET', 'POST'])
def create_medico():
    if request.method == 'GET':
        especialidades = ["Cardiología", "Dermatología", "Gastroenterología", "Neurología", "Psiquiatría", "Pediatría", "Medicina Interna", "Oncología", "Ortopedia", "Oftalmología"]
        ti = ["CC", "CE", "Visa", "PEP"]
        return render_template('medico_form.html', especialidades = especialidades, ti = ti)
    elif request.method == 'POST':
        new_medico = Medico(nombre = request.form['nombre'], apellidos = request.form['apellido'], tipo_identificacion = request.form['ti'], numero_identificacion = request.form['ni'], registro_medico = request.form['rm'], especialidad = request.form['es'])
        db.session.add(new_medico)
        db.session.commit()
        return 'medico registrado'