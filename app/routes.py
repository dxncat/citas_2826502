from . import app, db
from .models import Medico, Paciente, Consultorio, Cita
from flask import render_template, request, flash, redirect
from os import path

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
        flash('Medico Registrado Correctamente')
        return redirect('/medicos')
    
@app.route('/pacientes/create', methods = ['GET', 'POST'])
def create_paciente():
    if request.method == 'GET':
        rhs = ["A+", "A-", "B+", "B-", "O+", "O-"]
        ti = ["CC", "CE", "Visa", "PEP"]
        return render_template('paciente_form.html', rhs = rhs, ti = ti)
    elif request.method == 'POST':
        new_paciente = Paciente(nombre = request.form['nombre'], apellidos = request.form['apellido'], tipo_identificacion = request.form['ti'], numero_identificacion = request.form['ni'], altura = request.form['altura'], tipo_sangre = request.form['RH'])
        db.session.add(new_paciente)
        db.session.commit()
        return 'paciente registrado'
    
@app.route('/consultorios/create', methods = ['GET', 'POST'])
def create_consultorio():
    if request.method == 'GET':
        return render_template('consultorio_form.html')
    elif request.method == 'POST':
        new_consultorio = Consultorio(numero = request.form['numero'])
        db.session.add(new_consultorio)
        db.session.commit()
        return 'consultorio registrado'

@app.route('/medicos/update/<int:id>', methods = ['GET', 'POST'])
def update_medico(id):
    medico_update = Medico.query.get(id)
    especialidades = ["Cardiología", "Dermatología", "Gastroenterología", "Neurología", "Psiquiatría", "Pediatría", "Medicina Interna", "Oncología", "Ortopedia", "Oftalmología"]
    ti = ["CC", "CE", "Visa", "PEP"]
    if request.method == 'GET':
        return render_template('medico_upgrade.html', medico_update = medico_update, especialidades = especialidades, ti = ti)
    elif request.method == 'POST':
        medico_update.nombre = request.form['nombre']
        medico_update.apellidos = request.form['apellido']
        medico_update.tipo_identificacion = request.form['ti']
        medico_update.numero_identificacion = request.form['ni']
        medico_update.registro_medico = request.form['rm']
        medico_update.especialidad = request.form['es']
        db.session.commit()
        return 'medico actualizado'
    
@app.route('/medicos/delete/<int:id>')
def delete_medico(id):
    medico_delete = Medico.query.get(id)
    db.session.delete(medico_delete)
    db.session.commit()
    return redirect('/medicos')