from odoo import models, fields, api, _
import requests
import logging
from datetime import datetime
import json

_logger = logging.getLogger(__name__)

class VisitorTracking(models.Model):
    _name = 'ip.visitor.tracking'
    _description = 'Seguimiento de Visitantes por IP'
    _rec_name = 'ip_address'
    _order = 'visit_time desc'

    api_key = fields.Char('Clave API', required=True)
    ip_address = fields.Char('Dirección IP', readonly=True)
    country = fields.Char('País', readonly=True)
    city = fields.Char('Ciudad', readonly=True)
    longitude = fields.Float('Longitud', readonly=True)
    latitude = fields.Float('Latitud', readonly=True)
    isp = fields.Char('Proveedor de Internet', readonly=True, help="Proveedor de Servicios de Internet")
    organization = fields.Char('Organización', readonly=True)
    visit_time = fields.Datetime('Hora de Visita', readonly=True)
    
    def get_geolocation(self):
        """Obtener datos de geolocalización desde la API ipgeolocation.io"""
        for record in self:
            if not record.api_key:
                raise models.ValidationError(_('Se requiere una Clave API'))
                
            try:
                ip_response = requests.get('https://api.ipify.org?format=json')
                ip_data = ip_response.json()
                public_ip = ip_data.get('ip')
                
                url = f"https://api.ipgeolocation.io/ipgeo?apiKey={record.api_key}&ip={public_ip}"
                response = requests.get(url)
                
                if response.status_code != 200:
                    raise models.ValidationError(_('Error al obtener los datos de geolocalización. Verifica tu Clave API.'))
                
                data = response.json()
                record.write({
                    'ip_address': data.get('ip'),
                    'country': data.get('country_name'),
                    'city': data.get('city'),
                    'longitude': float(data.get('longitude') or 0.0),
                    'latitude': float(data.get('latitude') or 0.0),
                    'isp': data.get('isp'),
                    'organization': data.get('organization'),
                    'visit_time': datetime.now(),
                })
                
            except Exception as e:
                _logger.error(f"Error al obtener datos de geolocalización: {str(e)}")
                raise models.ValidationError(_('Error al obtener datos de geolocalización: %s') % str(e))