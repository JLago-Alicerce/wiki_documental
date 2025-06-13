---
source: PropuestaTecnica_Navantia_ActivosHistoricos_JR_v2.md
doc_source: PropuestaTecnica_Navantia_ActivosHistoricos_JR_v2.docx
created: 2025-06-13T05:51:58.231831
---
# Condiciones de ejecución del proyecto

## Lugar y medios de trabajo

Las distintas labores objeto de este proyecto (entrevistas,
consultorías, reuniones de seguimiento, asistencia a usuarios…), se
ejecutarán en su totalidad en las dependencias de ALTIA, que aportará
sus propios recursos físicos y lógicos (ordenadores, software de
desarrollo, etc.).

Los servicios del equipo técnico central se prestarán en remoto desde
las instalaciones de ALTIA. Los gastos de desplazamiento a Navantia de
cualquier miembro del equipo relacionado con el seguimiento y control
del proyecto, correrán a cargo de ALTIA. Sin embargo, para otras
intervenciones, Navantia puede requerir el desplazamiento de cualquier
miembro del equipo a cualquiera de las instalaciones de las que dispone
(Dársena de Cartagena, Ría de Ferrol, Bahía de Cádiz y Madrid). Los
gastos de desplazamiento puntuales se facturarán aparte como gastos a
justificar. ALTIA dispone de presencia física actualmente próxima a tres
de sus centros: Ferrol (Coruña), Cartagena (Alicante) y Madrid (Madrid).

## Medidas de seguridad

En este apartado describimos las medidas de seguridad a adoptar en los
equipos destinados al proyecto con la red corporativa de la empresa.

Todos los equipos del personal de ALTIA que forman parte del equipo
definido en la propuesta están integrados en un dominio aislado de
Active Directory.

En este dominio se establecen unas estrictas políticas de seguridad:

- Los usuarios de los equipos tienen carácter nominal.

- La vigencia máxima de las contraseñas de los usuarios es de 30 días.

- Las contraseñas de los equipos de trabajo tienen una longitud mínima
  de 8 caracteres.

- Tras tres intentos consecutivos de acceso al equipo con una contraseña
  no válida se procede al bloqueo automático de la cuenta. Sólo podrá
  ser desbloqueado por el Administrador de Sistemas de la Oficina de
  ALTIA con el visto bueno del responsable máximo del proyecto en
  cuestión.

- Están auditadas todas las validaciones de los usuarios en el Active
  Directory, de forma que el Administrador del Sistemas de la oficina
  revisa periódicamente los ficheros de log generados.

- El Administrador de Sistemas de la Oficina de ALTIA revisa
  periódicamente los usuarios del mismo, contrastando los usuarios
  existentes en el mismo, con los usuarios reales. Cualquier
  discrepancia de usuarios es informada al responsable máximo del
  proyecto en cuestión para proceder a la corrección de la misma.

En caso de baja temporal o definitiva, tanto del proyecto como de la
empresa, se establece la siguiente política:

- Si la baja es temporal, se bloquea el usuario en el Active Directory
  hasta nuevo aviso por parte del responsable máximo del proyecto en
  cuestión.

- Si la baja es definitiva, se procede a la eliminación de la cuenta del
  Active Directory y al formateo del disco duro del equipo tras el visto
  bueno del responsable máximo del proyecto en cuestión.

En cuanto a otras medidas de seguridad que se establecen de forma
concreta sobre los equipos del personal de ALTIA que formarán parte del
equipo de trabajo son:

- La instalación de cualquier tipo de software en el equipo es realizada
  por el Administrador de Sistemas de la Oficina de ALTIA.

> En ningún caso, el personal de ALTIA tiene acceso a la cuenta de
> Administrador del equipo para la instalación de software, así como la
> modificación de parámetros del equipo.
>
> La instalación de software adicional tiene que ser aprobada por el
> responsable máximo del proyecto en cuestión.

- El arranque del equipo se realiza desde el disco duro local, quedando
  deshabilitadas por el Administrador de Sistemas de la Oficina de ALTIA
  las demás opciones de arranque.

- El acceso a la BIOS del equipo de trabajo está protegido por una
  contraseña establecida por Administrador de Sistemas de la Oficina de
  ALTIA.

- Tras un minuto de inactividad del equipo, éste se bloquea
  automáticamente procediéndose al desbloqueo del mismo con la
  contraseña de usuario de dicho equipo.

- Todos los equipos cuentan con un antivirus y anti-spyware que se
  actualiza automáticamente todos los días para evitar la entrada en el
  sistema de virus o robots spyware que puedan infectar al resto de los
  equipos que forman parte del equipo de trabajo.

- Cada equipo dispone de un volumen encriptado en donde se almacena toda
  la información crítica confidencial necesaria para la ejecución del
  proyecto (parámetros de acceso a bases de datos, parámetros de acceso
  a consolas de administración, …). Estos volúmenes encriptados son
  generados por el software libre TrueCrypt.

Las contraseñas de las cuentas de Administrador de los equipos, así como
la que protege la BIOS de los equipos, y otras contraseñas de
conocimiento restringido, sólo tienen conocimiento de las mismas el
Administrador de Sistemas de la Oficina de y el responsable máximo del
proyecto en cuestión.

Asimismo, se establecen políticas de seguridad en lo referente tanto a
los servidores que prestan servicio al equipo de trabajo como al acceso
desde los equipos de trabajo a la red corporativa y a internet. Se
pueden enumerar las siguientes:

- El acceso al espacio físico donde se encuentran localizados los
  servidores y equipos de comunicaciones necesarios para el desarrollo
  del proyecto está restringido al Administrador de Sistemas de la
  Oficina de ALTIA.

- El acceso a los servidores es restringido. Sólo tienen acceso a los
  mismos el Administrador de Sistemas de la Oficina. En caso de que
  personal del equipo de proyecto necesite acceso al servidor, el
  responsable máximo del proyecto gestionará a través del gestor de
  incidencias del GLPI, una petición de acceso al servidor. El
  Administrador de Sistemas proporcionará un usuario temporal con los
  permisos suficientes para que se puedan acometer las operaciones que
  necesite realizar el personal del equipo de proyecto. Una vez
  finalizadas las operaciones, se notificará en el gestor de incidencias
  que las tareas han finalizado, procediendo el Administrador de
  Sistemas a deshabilitar el usuario temporal.

- Tanto el acceso a la red corporativa como a internet será auditada y
  controlada por el software que nos provee el fabricante de los equipos
  de comunicaciones. Esta tarea es realizada periódicamente
  (semanalmente) por el Administrador de Sistemas de la oficina,
  siguiendo los procedimientos existentes en la oficina documentados al
  efecto.

Como software de gestión de las copias de seguridad se utiliza el
software libre Bácula en toda la Oficina de ALTIA. Todos los equipos de
la oficina tienen instalado un agente de software libre de copias de
seguridad Bácula. Con este software se realizan las copias de los datos
de vital importancia del equipo de trabajo, de forma que la recuperación
de los ritmos de trabajo ante un posible desastre en nuestras oficinas
sea lo más rápido posible. Asimismo, se realizan las copias de seguridad
de los servidores que se consideren necesarias.

La política existente para las copias de seguridad es la siguiente:

- El primer lunes de cada mes se realiza una copia nivel 0 (total) del
  equipo/servidor.

- Los restantes lunes de cada mes se realizan copias de nivel 1
  (diferencial total) del equipo/servidor.

- Los restantes días del mes se realizan copias de nivel 2
  (incrementales diarias) del equipo/servidor.

- Todas las copias son realizadas a disco, realizándose posteriormente a
  cinta DDS-4 las copias de nivel 0 realizadas.

- La vigencia de las copias de seguridad (período en el cual se
  mantendrán estas copias de seguridad disponibles) es de 12 meses en el
  caso de las copias a disco y 24 meses en el caso de las copias
  realizadas a cinta DDS-4.

Las cintas DDS-4 en las cuales se realizan las copias de seguridad son
depositadas en una caja ignifuga situada en las dependencias de la
Oficina de ALTIA, con acceso restringido al contenido de la misma por
parte del Administrador de Sistemas y el Director de la Oficina de
ALTIA.

Por último, todo el material en papel o soporte digital (CD) que cuente
con información confidencial tendrá que ser destruido tras su uso por
las trituradoras de papel/CD que están disponibles para el equipo de
proyecto.

## Confidencialidad de la información

ALTIA acepta de manera explícita mantener la confidencialidad y reserva
sobre cualquier dato que pudiera conocer con ocasión del cumplimiento
del contrato, especialmente los de carácter personal, que no podrá
copiar o utilizar con fin distinto al que figura en este pliego, ni
tampoco ceder a otros ni siquiera a efectos de conservación.

ALTIA acepta lo dispuesto en la Ley orgánica 15/1999 de 13 de diciembre,
sobre protección datos de carácter personal y especialmente en lo
indicado en su artículo número 12, sobre la cesión y el acceso a los
datos por cuenta de terceros, así como lo dispuesto en el Real Decreto
994/1999 de 11 de junio, sobre medidas de seguridad de los ficheros
automatizados que contengan datos de carácter personal y especialmente
las medidas indicadas en su artículo 4.

ALTIA incorporará en su contrato un acuerdo de confidencialidad con el
que se compromete a no usar, revelar o difundir la INFORMACIÓN obtenida
mediante el transcurso de este proyecto para otro fin que no sea el
objetivo del mismo proyecto. Los términos de este acuerdo se fijarán a
la firma del contrato.

Así mismo una de las principales normas de comportamiento en las que se
basa el comportamiento del personal de las empresas que integran ALTIA,
ha sido y será su discreción y confidencialidad en todos los proyectos.

## Propiedad intelectual de los entregables

ALTIA acepta expresamente que la propiedad de todos los entregables,
cualquiera que sea su naturaleza, elaborados al amparo del presente
contrato, corresponde a Navantia, con exclusividad y a todos los
efectos.

Todos los estudios y documentos, así como los productos y subproductos
elaborados por el adjudicatario como consecuencia de la ejecución del
presente contrato serán propiedad de Navantia, quien podrá
reproducirlos, publicarlos y divulgarlos, total o parcialmente, sin que
pueda oponerse a ello el adjudicatario autor material de los trabajos.

ALTIA renuncia expresamente a cualquier derecho que sobre los trabajos
realizados como consecuencia de la ejecución del presente contrato
pudieran corresponderle, y no podrá hacer ningún uso o divulgación de
los estudios y documentos utilizados o elaborados en base a este pliego
de condiciones, bien sea en forma total o parcial, directa o extractada,
original o reproducida, sin autorización expresa de Navantia.
Específicamente todos los derechos de explotación y titularidad de las
aplicaciones informáticas y programas de ordenador desarrollados al
amparo del contrato resultante de la adjudicación del presente concurso,
corresponden únicamente a Navantia.

ALTIA no podrá utilizar la información obtenida en la actividad
desarrollada como consecuencia de este contrato, no pudiendo transmitir
dicho conocimiento, sin el consentimiento escrito de Navantia.

## Duración del proyecto

La duración estimada de ejecución del proyecto es de 12 meses acorde a
la planificación indicada en el punto 6 del PCAP siendo la fecha
estimada de inicio de los trabajos en Abril del 2023 y la fecha estimada
de finalización de los mismos y cierre del proyecto en Marzo del 2024,
pudiendo ser prorrogado por un plazo de un año adicional.

