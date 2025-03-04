from odoo import models, fields, api, _
import requests
import logging
from datetime import datetime
import json

_logger = logging.getLogger(__name__)

class VisitorTracking(models.Model):
    _name = 'ip.visitor.tracking'
    _description = 'IP Visitor Tracking'
    _rec_name = 'ip_address'
    _order = 'visit_time desc'

    api_key = fields.Char('API Key', required=True)
    ip_address = fields.Char('IP Address', readonly=True)
    country = fields.Char('Country', readonly=True)
    city = fields.Char('City', readonly=True)
    longitude = fields.Float('Longitude', readonly=True)
    latitude = fields.Float('Latitude', readonly=True)
    isp = fields.Char('ISP', readonly=True, help="Internet Service Provider")
    organization = fields.Char('Organization', readonly=True)
    visit_time = fields.Datetime('Visit Time', readonly=True)
    
    def get_geolocation(self):
        """Fetch geolocation data from ipgeolocation.io API"""
        for record in self:
            if not record.api_key:
                raise models.ValidationError(_('API Key is required'))
                
            try:
                ip_response = requests.get('https://api.ipify.org?format=json')
                ip_data = ip_response.json()
                public_ip = ip_data.get('ip')
                
                url = f"https://api.ipgeolocation.io/ipgeo?apiKey={record.api_key}&ip={public_ip}"
                response = requests.get(url)
                
                if response.status_code != 200:
                    raise models.ValidationError(_('Failed to get geolocation data. Please check your API key.'))
                
                data = response.json()
                
                # Update the record with API response data
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
                _logger.error(f"Error fetching geolocation data: {str(e)}")
                raise models.ValidationError(_('Error fetching geolocation data: %s') % str(e))