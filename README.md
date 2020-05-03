# Pokémon

Esta aplicación de Django consiste principalmente en un comando que puede ser invocado por consola para obtener la
información de una cadena de evolución según su ID y en un servicio web que retorna la información de un pokémon según
su nombre.

Para correr la aplicación después de clonar el repositorio debes instalar sus dependencias con 
`pip install -r requirements.txt`

Para usar el comando de la consola usa el siguiente código:
`python manage.py evolution_chain <ID>`

Para obtener información de un pokemon usa la siguiente dirección: `/name/<nombre>`