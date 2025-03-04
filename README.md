# IP Visitor Tracking

## Descripción
Este módulo para **Odoo 16 Community** permite obtener información sobre la geolocalización de los visitantes de la web oficial. Utiliza la API de **ipgeolocation.io** para extraer datos como la dirección IP, el país, la ciudad, la ubicación geográfica y el proveedor de servicios de internet (ISP).

## Características
- Registro automático de la dirección IP de los visitantes.
- Obtención de datos geográficos y del ISP.
- Interfaz de administración con vistas de lista y formularios en Odoo.
- Botón para actualizar la información de geolocalización manualmente.
- Control de acceso basado en roles.

## Requisitos
- **Odoo 16 Community**
- **Clave API de ipgeolocation.io**

## Instalación
1. Clonar el repositorio en la carpeta de módulos de Odoo:
   ```sh
   git clone https://github.com/Sugo04/ip_visitor_tracking.git
   ```
2. Acceder a la carpeta de Odoo y actualizar la lista de aplicaciones:
   ```sh
   odoo -u ip_visitor_tracking --stop-after-init
   ```
3. Ir a **Aplicaciones** en Odoo, buscar "IP Visitor Tracking" e instalar el módulo.

## Configuración
1. En la configuración del módulo, ingresar la **clave API** de ipgeolocation.io.
2. Acceder al menú **Visitor Tracking** para ver los registros de visitantes.

## Uso
- Los registros de visitantes se crean automáticamente con su información geográfica.
- Se puede hacer clic en el botón **"Track Visitor"** para actualizar la información manualmente.

## Estructura del Proyecto
```
ip_visitor_tracking/
  ├── models/
  │   ├── __init__.py
  │   ├── visitor_tracking.py  # Modelo principal de seguimiento de visitantes
  ├── security/
  │   ├── security.xml  # Configuración de grupos de seguridad
  │   ├── ir.model.access.csv  # Reglas de acceso para el modelo
  ├── views/
  │   ├── visitor_tracking_views.xml  # Definición de las vistas de lista y formulario
  ├── __init__.py  # Importa las clases del módulo
  ├── __manifest__.py  # Metadatos del módulo
  ├── README.md  # Documentación
```

## Clases y Archivos Clave

### `models/visitor_tracking.py`
Esta clase define el modelo `ip.visitor.tracking`, el cual almacena la información de los visitantes.

#### Código de ejemplo:
```python
from odoo import models, fields, api
from datetime import datetime
import requests

class VisitorTracking(models.Model):
    _name = 'ip.visitor.tracking'
    _description = 'Seguimiento de Visitantes por IP'
    
    ip_address = fields.Char('Dirección IP', readonly=True)
    country = fields.Char('País', readonly=True)
    city = fields.Char('Ciudad', readonly=True)
    visit_time = fields.Datetime('Hora de Visita', readonly=True)
```

### `views/visitor_tracking_views.xml`
Define las interfaces gráficas del módulo.

#### Código de ejemplo:
```xml
<record id="view_ip_visitor_tracking_tree" model="ir.ui.view">
    <field name="name">ip.visitor.tracking.tree</field>
    <field name="model">ip.visitor.tracking</field>
    <field name="arch" type="xml">
        <tree>
            <field name="ip_address"/>
            <field name="country"/>
            <field name="city"/>
            <field name="visit_time"/>
        </tree>
    </field>
</record>
```

### `security/security.xml`
Define los permisos y accesos del módulo.

#### Código de ejemplo:
```xml
<record id="group_ip_visitor_tracking_admin" model="res.groups">
    <field name="name">IP Visitor Tracking / Administrator</field>
</record>
```

### `security/ir.model.access.csv`
Especifica los permisos de acceso sobre el modelo `ip.visitor.tracking`.

#### Código de ejemplo:
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_ip_visitor_tracking_admin,ip.visitor.tracking.admin,model_ip_visitor_tracking,ip_visitor_tracking.group_ip_visitor_tracking_admin,1,1,1,1
```

### `__manifest__.py`
Archivo de configuración del módulo.

#### Código de ejemplo:
```python
{
    'name': 'IP Visitor Tracking',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Localiza a los usuarios que se conecten geográficamente.',
    'depends': ['base', 'website'],
    'data': ['security/security.xml', 'views/visitor_tracking_views.xml'],
    'installable': True,
}
```

## Autor
- **Héctor Martín Ortega**
- [Repositorio en GitHub](https://github.com/Sugo04/ip_visitor_tracking)

## Licencia
Este proyecto se distribuye bajo la **licencia MIT**.

