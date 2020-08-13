# Ejercicio - Investigación / Script
---
# Requisitos
*Se requiere tener instalado **Python** en el sistema*.
| S.O. | Instructivos |
| ------ | ------ |
| Linux | [Como instalar en Linux](https://www.comoinstalarlinux.com/como-instalar-python-3-en-tu-distro-linux/) |
| Windows | [docs.python.org/Windows](https://docs.python.org/3/using/windows.html#the-full-installer) |

Ademas se requieren los siguientes modulos:
| Modulo | Descarga | Documentación |
| ------ | ------ | ------ |
| Requests | [pypi.org/requests 2.24.0](https://pypi.org/project/requests/#files) | [requests.readthedocs.io](https://requests.readthedocs.io/en/master/) |
| PrettyTable | [pypi.org/PrettyTable 0.7.2](https://pypi.org/project/PrettyTable/#files) | [ptable.readthedocs.io](https://ptable.readthedocs.io/en/latest/tutorial.html) |

Para instalar cada modulo ejecute el siguiente comando:
 
```sh
 $ pip install module
```

Para mas información: [packaging.python.org/tutorials/installing-packages](https://packaging.python.org/tutorials/installing-packages/#)
# Instrucciones
---

# Para Linux

Desde la terminal, navegar hacia la ubicación del script y ejecutarlo
 ```sh
 root@ubuntu:~$ python ItemsSeller.py
```


# Para Windows
 Desde Cmd en la ubicación donde se encuentra el script, ejecutar
```sh
 C:\Users\lautaro\scripts>ItemsSeller.py
```
 Otra forma es ir a la ubicacion donde esta instalado Python y ejecutar el script pasando la ubicacion del archivo
 ```sh
 C:\Users\lautaro\Python> python  C:\Users\lautaro\scripts\ItemsSeller.py
```

# Uso del Script

Al ejecutar el script se debe ingresar los Id de los usuarios que desea consultar,  separados por un espacio
 ```sh
 root@ubuntu:~$ python ItemsSeller.py
 root@ubuntu:~$ Ingrese Id de vendedores: 179571326 158482976
```
El script generará un archivo por cada usuario con el nombre: **userId_log.txt**  dentro de la ubicacion en donde se ejecutó, el proceso se muestra en output.

 ```sh
 root@ubuntu:~$ Generando... 179571326_log.txt
 root@ubuntu:~$ COMPLETADO
 root@ubuntu:~$ Generando... 158482976_log.txt
 root@ubuntu:~$ COMPLETADO
 ```
 En este caso se generaron dos archivos: 
 - 179571326_log.txt 
 - 158482976_log.txt
 
 Dentro de cada uno se encuentra una tabla con la informacion solicitada.
