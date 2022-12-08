from flask import Blueprint, render_template, request, flash, redirect, url_for
import requests
from app.forms import RickyForm
from app.models.ricky import Ricky
from app.db import db
bp_ricky = Blueprint('bp_ricky', __name__)
@bp_ricky.route('/')
def perfil():
    return render_template('perfil.html')
@bp_ricky.route('/lista')
def index():
    rickys = db.rickys.find()
    return render_template('index.html', rickys=rickys)
@bp_ricky.route('/capitulos')
@bp_ricky.route('/capitulos/<int:id>')
def show_ricky(id):
    query={'id':id}
    datos=db.rickys.find(query)
    return render_template('show-ricky.html',datos=datos)
@bp_ricky.route('/store', methods=['GET', 'POST'])
def store_ricky():
    ricky_form = RickyForm()
    
    rango=list(range(1,3,1))# probar de uno a tres
    # rango=list(range(2,0,-1))# 
    rango=list(range(420,0,-1))# para extraer información de page=1 a page=21, total ID=420
    lectura=f'https://rickandmortyapi.com/api/character/{rango}'
    resp = requests.get(lectura)
    dator=resp.json()
    for dato in dator:
        ricky_form.id.data=dato['id']
        ricky_form.name.data=dato['name']
        ricky_form.status.data=dato['status']
        ricky_form.species.data=dato['species']
        ricky_form.typee.data=dato['type']
        ricky_form.origin_name.data=dato['origin']['name']
        ricky_form.location_name.data=dato['location']['name']
        ricky_form.image.data=dato['image']
        location_url_r=dato['location']['url']
        if location_url_r:
            resp_location_url = requests.get(location_url_r)
            location_resp = resp_location_url.json()
            ricky_form.dimension.data = location_resp['dimension']
        else:
            ricky_form.dimension.data=''
        ricky_form.gender.data=dato['gender']
        ricky_form.created.data=dato['created']
        for episode_url_r in dato['episode']:
            resp_episode_url = requests.get(episode_url_r)
            episoder = resp_episode_url.json()
            ricky_form.episode_id.data=episoder['id']
            ricky_form.episode_name.data=episoder['name']
            ricky_form.episode_air_date.data=episoder['air_date']
        ricky_form.episode.data=episoder['episode']
        new_ricky = Ricky(
            ricky_form.id.data,
            ricky_form.name.data,
            ricky_form.status.data,
            ricky_form.species.data,
            ricky_form.typee.data,
            ricky_form.gender.data,
            ricky_form.origin_name.data,
            ricky_form.location_name.data,
            ricky_form.image.data,
            ricky_form.created.data,
            ricky_form.dimension.data,
            ricky_form.episode_id.data,
            ricky_form.episode_name.data,
            ricky_form.episode_air_date.data,
            ricky_form.episode.data,
        )
        db.rickys.insert_one(new_ricky.to_json())
    flash('Rickys created successfully', 'success')
    return redirect(url_for('bp_ricky.index'))