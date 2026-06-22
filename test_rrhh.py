"""
Test RR.HH. - Gestión de Personas y Comportamiento Organizacional
-----------------------------------------------------------------
App de estudio tipo certamen. Permite elegir entre dos cuestionarios,
muestra una pregunta a la vez, comprueba la respuesta y lleva el puntaje.

Cuestionarios:
  1) "Test RR.HH. (60 preguntas)"  -> banco original.
  2) "Guía de Estudio del Certamen" -> preguntas construidas SOLO con la
     información del documento Guia_Estudio_Certamen_Gestion_Personas.md.

Cómo ejecutar (Windows / terminal):
    pip install streamlit
    streamlit run test_rrhh.py

Se abre solo en el navegador (normalmente http://localhost:8501).
"""

import random
import streamlit as st

# ---------------------------------------------------------------------------
# Banco de preguntas 1: Test RR.HH. original
#   tipo: "single" -> una sola respuesta correcta (radio)
#         "multi"  -> varias respuestas correctas (checkbox)
#   correctas: lista con el/los texto(s) exactos de la(s) opción(es) correcta(s)
# ---------------------------------------------------------------------------
PREGUNTAS = [
    {
        "n": 1, "tipo": "single",
        "pregunta": "Sam trabaja como asociado de cuentas en una editorial. ¿Cuál de las siguientes opciones probablemente ayudaría a Sam con la planificación y el desarrollo profesional?",
        "opciones": ["Sistemas de seguimiento de candidatos", "Programas de compensación",
                     "Evaluaciones de desempeño", "Evaluaciones en el trabajo"],
        "correctas": ["Evaluaciones de desempeño"],
    },
    {
        "n": 2, "tipo": "single",
        "pregunta": "¿Cuál de los siguientes es un problema asociado con las evaluaciones de desempeño?",
        "opciones": ["El rendimiento pasado no necesariamente indica un potencial futuro.",
                     "Los gerentes de línea no están familiarizados con los subordinados.",
                     "Las habilidades técnicas no están suficientemente evaluadas.",
                     "El rendimiento no indica necesidades de formación."],
        "correctas": ["El rendimiento pasado no necesariamente indica un potencial futuro."],
    },
    {
        "n": 3, "tipo": "single",
        "pregunta": "¿Qué han destacado tradicionalmente los sindicatos como base para los ascensos y los aumentos salariales?",
        "opciones": ["Trabajo en equipo", "Desempeño", "Antigüedad", "Productividad"],
        "correctas": ["Antigüedad"],
    },
    {
        "n": 4, "tipo": "single",
        "pregunta": "¿Cuál es el primer paso del proceso de evaluación del desempeño?",
        "opciones": ["Establecer las expectativas laborales de los empleados",
                     "Realizar un análisis exhaustivo del trabajo",
                     "Evaluar el desempeño laboral",
                     "Identificar metas de desempeño específicas"],
        "correctas": ["Identificar metas de desempeño específicas"],
    },
    {
        "n": 5, "tipo": "single",
        "pregunta": "¿Cuál es la causa más común de falla de los sistemas de evaluación del desempeño?",
        "opciones": ["Requiere mucho tiempo para los gerentes", "Planes de desarrollo irrelevantes",
                     "Altos costos de implementación", "Metas y expectativas poco claras"],
        "correctas": ["Metas y expectativas poco claras"],
    },
    {
        "n": 6, "tipo": "single",
        "pregunta": "El compromiso de los empleados es un tema importante para RR.HH. porque:",
        "opciones": ["Ralentiza el proceso de contratación", "Aumenta los indicadores de selección",
                     "Altera las percepciones", "Afecta el desempeño organizacional"],
        "correctas": ["Afecta el desempeño organizacional"],
    },
    {
        "n": 7, "tipo": "single",
        "pregunta": "¿Cuál de los siguientes enunciados es menos probable que mejore el compromiso de los empleados?",
        "opciones": ["Entregar a los trabajadores una ampliación del empleo",
                     "Alentar a los trabajadores a ser innovadores",
                     "Tratar a los trabajadores con confianza y respeto",
                     "Asignar trabajadores a trabajos que utilicen sus habilidades"],
        "correctas": ["Entregar a los trabajadores una ampliación del empleo"],
    },
    {
        "n": 8, "tipo": "single",
        "pregunta": "¿Qué término se refiere a un proceso orientado a objetivos, dirigido a asegurar que los procesos organizacionales estén en su lugar para maximizar la productividad de los empleados, los equipos y la organización?",
        "opciones": ["Análisis de desarrollo", "Planificación Estratégica de RRHH",
                     "Gestión del desempeño", "Evaluación del Desempeño"],
        "correctas": ["Gestión del desempeño"],
    },
    {
        "n": 9, "tipo": "single",
        "pregunta": "Con la gestión del desempeño, el esfuerzo de cada trabajador debe dirigirse hacia:",
        "opciones": ["Analizar el entendimiento corporativo", "Mejorar la conciencia de la compensación",
                     "El logro de metas estratégicas", "Mejorar el ajuste organizacional general"],
        "correctas": ["El logro de metas estratégicas"],
    },
    {
        "n": 10, "tipo": "single",
        "pregunta": "Las evaluaciones de desempeño se utilizan para todos los siguientes propósitos EXCEPTO:",
        "opciones": ["Identificar las necesidades de formación", "Defender las decisiones del personal",
                     "Implementación de pruebas de selección", "Proporcionar comentarios a los empleados"],
        "correctas": ["Implementación de pruebas de selección"],
    },
    {
        "n": 11, "tipo": "single",
        "pregunta": "¿Cómo se utilizan las evaluaciones de desempeño para el reclutamiento y la selección?",
        "opciones": ["Desarrollar una estrategia promocional", "Predecir el desempeño laboral del solicitante",
                     "Iniciar negociaciones salariales del solicitante",
                     "Determinación de las necesidades de formación y desarrollo"],
        "correctas": ["Predecir el desempeño laboral del solicitante"],
    },
    {
        "n": 12, "tipo": "single",
        "pregunta": "Las tendencias actuales en el pago de ejecutivos implican vincular la compensación con:",
        "opciones": ["Sistemas de antigüedad", "Opciones sobre acciones diferidas",
                     "Resultados de desempeño", "Paquetes de contratos de varios años"],
        "correctas": ["Resultados de desempeño"],
    },
    {
        "n": 13, "tipo": "single",
        "pregunta": "Como gerente de recursos humanos, ¿qué herramienta probablemente usaría para determinar si existe equidad externa en su empresa?",
        "opciones": ["Análisis de trabajos", "Encuestas de compensación",
                     "Informes de estadísticas laborales", "Evaluaciones laborales"],
        "correctas": ["Encuestas de compensación"],
    },
    {
        "n": 14, "tipo": "single",
        "pregunta": "Como gerente de recursos humanos, ¿qué herramienta probablemente usaría para determinar si existe equidad interna en su empresa?",
        "opciones": ["Evaluación del trabajo", "Encuesta de compensación",
                     "Estudio de métodos conductuales", "Análisis de trabajo"],
        "correctas": ["Evaluación del trabajo"],
    },
    {
        "n": 15, "tipo": "single",
        "pregunta": "Benson Enterprises paga salarios más altos que sus competidores para atraer empleados productivos y de alta calidad. ¿Qué tipo de política de compensación es más probable que exista en Benson Enterprises?",
        "opciones": ["Tarifa individual", "Tasa de mercado", "Líder en salarios", "Seguidor de pago"],
        "correctas": ["Líder en salarios"],
    },
    {
        "n": 16, "tipo": "single",
        "pregunta": "El salario promedio que la mayoría de los empleadores proporcionan por un trabajo similar en un área o industria en particular se conoce como:",
        "opciones": ["Tasa de mercado", "Líder de pago", "Salario", "Seguidor de pago"],
        "correctas": ["Tasa de mercado"],
    },
    {
        "n": 17, "tipo": "single",
        "pregunta": "¿Qué término se refiere al total de todas las recompensas otorgadas a los empleados a cambio de sus servicios?",
        "opciones": ["Beneficios", "Comisiones", "Bonificaciones", "Compensación"],
        "correctas": ["Compensación"],
    },
    {
        "n": 18, "tipo": "single",
        "pregunta": "¿Cuál es el estándar más importante para determinar el salario?",
        "opciones": ["Áreas geográficas", "Pago de los líderes", "Niveles organizacionales", "Tasa de mercado"],
        "correctas": ["Tasa de mercado"],
    },
    {
        "n": 19, "tipo": "single",
        "pregunta": "¿Cuál es la razón MENOS probable por la que una empresa utilizaría la evaluación de puestos?",
        "opciones": ["Eliminar las desigualdades salariales",
                     "Estimación de la tasa salarial industrial promedio",
                     "Identificar la estructura de trabajo de la organización",
                     "Desarrollar una jerarquía del valor del trabajo para crear una estructura salarial"],
        "correctas": ["Estimación de la tasa salarial industrial promedio"],
    },
    {
        "n": 20, "tipo": "single",
        "pregunta": "Como enfermera pediátrica, Cary experimenta una cantidad significativa de satisfacción laboral, esto se considera como:",
        "opciones": ["Ajuste organizacional", "Compensación indirecta", "Equidad personal", "Compensación no financiera"],
        "correctas": ["Compensación no financiera"],
    },
    {
        "n": 21, "tipo": "multi",
        "pregunta": "Las prestaciones legales en Chile incluyen: (selección múltiple)",
        "opciones": ["Cotizaciones para la seguridad en el trabajo", "Servicio de alimentación",
                     "Seguro de cesantía", "Seguro de vida"],
        "correctas": ["Cotizaciones para la seguridad en el trabajo", "Seguro de cesantía"],
    },
    {
        "n": 22, "tipo": "single",
        "pregunta": "Las organizaciones que pagan menos que el promedio del mercado por el trabajo es más probable que tengan:",
        "opciones": ["Menos reclamos", "Niveles de productividad mayores",
                     "Niveles de rotación de personal mayores", "Niveles de costos unitarios del trabajo más bajos"],
        "correctas": ["Niveles de rotación de personal mayores"],
    },
    {
        "n": 23, "tipo": "single",
        "pregunta": "Todo lo que un empleado percibe como valioso como resultado de la relación laboral, se conoce mejor como:",
        "opciones": ["Ventajas globales", "Salario completo", "Recompensas totales"],
        "correctas": ["Recompensas totales"],
    },
    {
        "n": 24, "tipo": "single",
        "pregunta": "Thomas estuvo involucrado en un accidente automovilístico grave y no puede regresar al trabajo durante 8 semanas. ¿Cuál de las siguientes opciones probablemente le proporcionaría ingresos a Thomas mientras está incapacitado?",
        "opciones": ["Seguro de vida", "Seguro por discapacidad", "Seguro de cesantía", "Compensación económica directa"],
        "correctas": ["Seguro por discapacidad"],
    },
    {
        "n": 25, "tipo": "single",
        "pregunta": "El esposo de Margaret, que trabajaba como contador, murió recientemente de un ataque al corazón mientras estaba de vacaciones. ¿Cuál de las siguientes opciones probablemente se le proporcionaría a Margaret?",
        "opciones": ["Seguro de desempleo", "Seguro para sobrevivientes",
                     "Pagos médicos suplementarios", "Beneficios discrecionales"],
        "correctas": ["Seguro para sobrevivientes"],
    },
    {
        "n": 26, "tipo": "single",
        "pregunta": "La edad de jubilación actual es:",
        "opciones": ["65 para hombres y 60 para mujeres", "60 para hombres y 65 para mujeres",
                     "65 para hombres y mujeres", "60 para hombres y mujeres"],
        "correctas": ["65 para hombres y 60 para mujeres"],
    },
    {
        "n": 27, "tipo": "single",
        "pregunta": "Jack, un trabajador de la construcción, resbaló y cayó en un lugar de trabajo. Como resultado, Jack se lesionó la rodilla y necesita fisioterapia y atención médica. Los gastos médicos de Jack probablemente estarían cubiertos por:",
        "opciones": ["Seguro de vida", "Seguro de salud laboral", "Seguro de desempleo", "Seguro de cesantía"],
        "correctas": ["Seguro de salud laboral"],
    },
    {
        "n": 28, "tipo": "single",
        "pregunta": "Todas las recompensas financieras que NO están incluidas en la compensación financiera directa se conocen como:",
        "opciones": ["Comisiones", "Bonificaciones", "Salarios", "Beneficios"],
        "correctas": ["Beneficios"],
    },
    {
        "n": 29, "tipo": "single",
        "pregunta": "En general, ¿por qué los empleados reciben beneficios de su empleador?",
        "opciones": ["Nivel de educación", "Productividad de los empleados",
                     "Desempeño corporativo", "Membresía organizacional"],
        "correctas": ["Membresía organizacional"],
    },
    {
        "n": 30, "tipo": "single",
        "pregunta": "¿Cuál de los siguientes enunciados es una ventaja de la compensación financiera indirecta?",
        "opciones": ["Generalmente no tributable al empleado", "Siempre patrocinado por el gobierno",
                     "Típicamente vinculado a la productividad del trabajador",
                     "Siempre menos costoso para las pequeñas empresas"],
        "correctas": ["Generalmente no tributable al empleado"],
    },
    {
        "n": 31, "tipo": "single",
        "pregunta": "Los beneficios son valiosos por todas las siguientes razones EXCEPTO:",
        "opciones": ["Retener a los empleados actuales", "Mejorar la satisfacción laboral",
                     "Contratación de nuevos empleados", "Mejorar la productividad de los trabajadores"],
        "correctas": ["Mejorar la productividad de los trabajadores"],
    },
    {
        "n": 32, "tipo": "single",
        "pregunta": "En la mayoría de los casos, los costos de los beneficios voluntarios son pagados por:",
        "opciones": ["Gobiernos comunales", "Empleados", "Empleadores", "Agencias gubernamentales"],
        "correctas": ["Empleados"],
    },
    {
        "n": 33, "tipo": "multi",
        "pregunta": "¿Cuál o cuáles de los siguientes son un factor del entorno laboral que forma parte de un paquete de compensación total? (selección múltiple)",
        "opciones": ["Compañeros de trabajo agradables", "Condiciones de trabajo",
                     "Buenas prácticas de gestión de personas", "Administradores capaces"],
        "correctas": ["Compañeros de trabajo agradables", "Condiciones de trabajo",
                      "Buenas prácticas de gestión de personas", "Administradores capaces"],
    },
    {
        "n": 34, "tipo": "single",
        "pregunta": "¿Cuál de las siguientes afirmaciones no forma parte de un derecho del trabajador en su indemnización?",
        "opciones": ["Indemnización por años de servicio", "Indemnización sustitutiva del aviso previo",
                     "Indemnización por seguros", "Indemnización del feriado anual o vacaciones"],
        "correctas": ["Indemnización por seguros"],
    },
    {
        "n": 35, "tipo": "single",
        "pregunta": "¿Qué implica proteger a los empleados de lesiones causadas por accidentes laborales?",
        "opciones": ["Bienestar", "Seguridad", "Moral", "Salud"],
        "correctas": ["Seguridad"],
    },
    {
        "n": 36, "tipo": "single",
        "pregunta": "¿Qué término se refiere a la ausencia de enfermedad física o emocional de los empleados?",
        "opciones": ["Salud", "Seguridad", "Prevención", "Moral"],
        "correctas": ["Salud"],
    },
    {
        "n": 37, "tipo": "multi",
        "pregunta": "¿Qué agencia o agencias hacen cumplir la Ley de Seguridad y Salud Ocupacional en Chile? (selección múltiple)",
        "opciones": ["Asociación Chilena de Seguridad", "Dirección del trabajo",
                     "Servicio de Salud", "Superintendencia de Seguridad Social"],
        "correctas": ["Dirección del trabajo", "Servicio de Salud", "Superintendencia de Seguridad Social"],
    },
    {
        "n": 38, "tipo": "single",
        "pregunta": "La tasa de accidentes del trabajo en los últimos 5 años en Chile se ha:",
        "opciones": ["Aumentado", "Mantenido", "Reducido"],
        "correctas": ["Reducido"],
    },
    {
        "n": 39, "tipo": "single",
        "pregunta": "La tasa de accidentes trayecto en los últimos 5 años en Chile se ha:",
        "opciones": ["Mantenido", "Reducido", "Aumentado"],
        "correctas": ["Mantenido"],
    },
    {
        "n": 40, "tipo": "multi",
        "pregunta": "La Norma Chilena General de Protección a los trabajadores entre sus artículos sostiene: (selección múltiple)",
        "opciones": ["La empresa está obligada a mantener los lugares de trabajo en condiciones sanitarias y ambientales",
                     "El trabajador es responsable de informarse de los riesgos de su trabajo",
                     "Que los trabajadores son responsables de tener los implementos necesarios para prevenir accidentes",
                     "El empleador estará obligado a tomar todas las medidas necesarias para proteger eficazmente la vida y salud de los trabajadores"],
        "correctas": ["La empresa está obligada a mantener los lugares de trabajo en condiciones sanitarias y ambientales",
                      "El empleador estará obligado a tomar todas las medidas necesarias para proteger eficazmente la vida y salud de los trabajadores"],
    },
    {
        "n": 41, "tipo": "multi",
        "pregunta": "La Ley 16.744 del Seguro Social contra Riesgos de Accidentes del Trabajo y Enfermedades Profesionales entre sus artículos sostiene: (selección múltiple)",
        "opciones": ["No es necesario denunciar accidentes mientras el trabajador sea atendido",
                     "El Seguro Social contra Riesgos de Accidentes del Trabajo y Enfermedades Profesionales es obligatorio",
                     "Todas las enfermedades que se tienen mientras se trabajan están cubiertas por este seguro",
                     "Se entregarán prestaciones en caso de accidentes causados en el trayecto hacia o desde el trabajo"],
        "correctas": ["El Seguro Social contra Riesgos de Accidentes del Trabajo y Enfermedades Profesionales es obligatorio",
                      "Se entregarán prestaciones en caso de accidentes causados en el trayecto hacia o desde el trabajo"],
    },
    {
        "n": 42, "tipo": "multi",
        "pregunta": "El Seguro Social contra Riesgos de Accidentes del Trabajo y Enfermedades Profesionales se financia: (selección múltiple)",
        "opciones": ["Con aportes del empleador y el trabajador", "Completamente por el empleador",
                     "A través de una prima que tiene una parte fija y una variable",
                     "Con un porcentaje de las remuneraciones imponibles mensuales"],
        "correctas": ["Completamente por el empleador",
                      "A través de una prima que tiene una parte fija y una variable"],
    },
    {
        "n": 43, "tipo": "single",
        "pregunta": "¿Cuál es el tipo de enfermedad profesional de mayor incidencia en los trabajadores y trabajadoras Chilenas?",
        "opciones": ["Dermatológicas", "Salud Mental", "Musculo Esqueléticas", "Respiratorias"],
        "correctas": ["Salud Mental"],
    },
    {
        "n": 44, "tipo": "multi",
        "pregunta": "¿Las principales causas de accidentes en el trabajo son? (selección múltiple)",
        "opciones": ["Condiciones de trabajo inseguras", "Malas políticas gubernamentales",
                     "Acciones negligentes de las personas", "Ausencia de fiscalización"],
        "correctas": ["Condiciones de trabajo inseguras", "Acciones negligentes de las personas"],
    },
    {
        "n": 45, "tipo": "single",
        "pregunta": "Foley Foods es una planta de procesamiento de alimentos de tamaño medio que ha tenido un aumento significativo en el negocio. La empresa necesita contratar trabajadores adicionales y desarrollar un segundo turno. ¿Cuál de las siguientes opciones sugiere que un programa de seguridad sería beneficioso para Foley Foods?",
        "opciones": ["Foley Foods contratará nuevos trabajadores para el turno de noche.",
                     "Los gerentes de Foley Foods pronto realizarán evaluaciones de desempeño.",
                     "Los empleados de Foley Foods utilizan simuladores durante los programas de formación.",
                     "Foley Foods se convirtió recientemente en un lugar de trabajo libre de humo."],
        "correctas": ["Foley Foods contratará nuevos trabajadores para el turno de noche."],
    },
    {
        "n": 46, "tipo": "multi",
        "pregunta": "Los Comités Paritarios de Higiene y Seguridad: (selección múltiple)",
        "opciones": ["Están compuestos sólo por representantes de los trabajadores",
                     "Sólo se reúnen cuando hay un accidente",
                     "Dentro de sus funciones está investigar las causas de accidentes del trabajo y enfermedades profesionales que ocurran en la empresa",
                     "Deben existir en todas las empresas con más de 25 trabajadores"],
        "correctas": ["Dentro de sus funciones está investigar las causas de accidentes del trabajo y enfermedades profesionales que ocurran en la empresa",
                      "Deben existir en todas las empresas con más de 25 trabajadores"],
    },
    {
        "n": 47, "tipo": "multi",
        "pregunta": "¿Cuáles son los fines principales de las organizaciones sindicales, de acuerdo a la ley Chilena? (selección múltiple)",
        "opciones": ["Velar por el cumplimiento de las leyes del trabajo o de la seguridad social",
                     "Representar a los Afiliados",
                     "Indicar la escala de sueldos de la organización",
                     "Establecer los descriptores de cargo"],
        "correctas": ["Velar por el cumplimiento de las leyes del trabajo o de la seguridad social",
                      "Representar a los Afiliados"],
    },
    {
        "n": 48, "tipo": "single",
        "pregunta": "Si en una organización existen sindicatos la participación de nuevos trabajadores en los sindicatos es:",
        "opciones": ["Obligatoria", "Voluntaria", "Necesita autorización del empleador"],
        "correctas": ["Voluntaria"],
    },
    {
        "n": 49, "tipo": "single",
        "pregunta": "Una persona no puede pertenecer a más de un sindicato.",
        "opciones": ["Verdadero", "Falso"],
        "correctas": ["Falso"],
    },
    {
        "n": 50, "tipo": "single",
        "pregunta": "Las personas que no tienen un contrato indefinido no pueden pertenecer a un sindicato.",
        "opciones": ["Verdadero", "Falso"],
        "correctas": ["Falso"],
    },
    {
        "n": 51, "tipo": "multi",
        "pregunta": "El contrato colectivo: (selección múltiple)",
        "opciones": ["Establece condiciones comunes de trabajo",
                     "Reemplazarán los contratos individuales de los trabajadores que sean parte de aquellos",
                     "Sólo incluye condiciones de remuneración"],
        "correctas": ["Establece condiciones comunes de trabajo",
                      "Reemplazarán los contratos individuales de los trabajadores que sean parte de aquellos"],
    },
    {
        "n": 52, "tipo": "multi",
        "pregunta": "La huelga: (selección múltiple)",
        "opciones": ["Se puede declarar por cualquier individuo afiliado a un sindicato",
                     "Es un derecho colectivo",
                     "Cuando ocurre en una organización ésta no puede funcionar",
                     "Es legal cuando ocurre en el marco de una negociación colectiva"],
        "correctas": ["Es un derecho colectivo",
                      "Es legal cuando ocurre en el marco de una negociación colectiva"],
    },
    {
        "n": 53, "tipo": "single",
        "pregunta": "Parson Enterprises es una organización sindicalizada. Un empleado de Parson probablemente aprenderá cómo se manejan las quejas en la empresa al:",
        "opciones": ["Revisar la declaración de misión de la empresa", "Leer el contrato colectivo",
                     "Asistir a un programa de formación", "Contactar a su jefe directo"],
        "correctas": ["Leer el contrato colectivo"],
    },
    {
        "n": 54, "tipo": "single",
        "pregunta": "Las principales razones por las que los empleados se unen a sindicatos incluyen todas las siguientes EXCEPTO ___.",
        "opciones": ["Necesidad de avenidas de liderazgo", "Deseo de una salida social",
                     "Insatisfacción con la gerencia", "Presión de los gerentes"],
        "correctas": ["Presión de los gerentes"],
    },
    {
        "n": 55, "tipo": "single",
        "pregunta": "¿Cuál de las siguientes NO es una actividad incluida en las relaciones internas con los empleados?",
        "opciones": ["Selección", "Jubilación", "Transferencia", "Promoción"],
        "correctas": ["Selección"],
    },
    {
        "n": 56, "tipo": "single",
        "pregunta": "La acción disciplinaria más eficaz se dirige al ___ del empleado.",
        "opciones": ["Actitud", "Personalidad", "Comportamiento", "Conciencia"],
        "correctas": ["Comportamiento"],
    },
    {
        "n": 57, "tipo": "single",
        "pregunta": "Parker Pharmaceuticals emplea a más de 400 trabajadores. ¿Cuál de las siguientes preguntas es MENOS relevante para seleccionar un nuevo proceso de acción disciplinaria para Parker?",
        "opciones": ["¿Los gerentes están aplicando disciplina de manera consistente y justa?",
                     "¿Los gerentes pueden aplicar la disciplina de manera impersonal a todos los empleados?",
                     "¿Parker quiere usar el castigo o el estímulo para crear disciplina?",
                     "¿Parker tiene problemas de disciplina similares a los de otras empresas farmacéuticas?"],
        "correctas": ["¿Parker tiene problemas de disciplina similares a los de otras empresas farmacéuticas?"],
    },
    {
        "n": 58, "tipo": "single",
        "pregunta": "Miles, un diseñador de software, recibió una revisión de desempeño que considera incorrecta. A Miles le gustaría discutir sus preocupaciones con una persona imparcial en su firma. ¿Cuál es la mejor persona con la que Miles se puede contactar en esta situación?",
        "opciones": ["Persona de Recursos Humanos", "Mediador", "Árbitro", "Delegado Sindical"],
        "correctas": ["Persona de Recursos Humanos"],
    },
    {
        "n": 59, "tipo": "single",
        "pregunta": "¿A través de qué medios pueden manejarse eficazmente los enfrentamientos de personalidad entre dos empleados valiosos?",
        "opciones": ["Transferencias", "Degradaciones", "Despido", "Promociones"],
        "correctas": ["Transferencias"],
    },
    {
        "n": 60, "tipo": "single",
        "pregunta": "¿Cuál de los siguientes es un método para revelar las verdaderas razones por las que los empleados dejan sus trabajos?",
        "opciones": ["Evaluación del desempeño", "Entrevista de salida",
                     "Evaluación cualitativa", "Entrevista de selección"],
        "correctas": ["Entrevista de salida"],
    },
    # --- Preguntas adicionales del Certamen 2 (2021), solo temas de los 4 PPTs ---
    {
        "n": 61, "tipo": "single",
        "pregunta": "¿Cuál es la principal razón por la que se forman sindicatos en las empresas?",
        "opciones": ["Para una adecuada representación de los trabajadores frente al empleador",
                     "Para mejorar el nivel de organización de los empleados",
                     "Para poder negociar colectivamente",
                     "Para facilitar las comunicaciones con los empleados",
                     "Para generar una instancia de reclamos y quejas ante el empleador"],
        "correctas": ["Para una adecuada representación de los trabajadores frente al empleador"],
    },
    {
        "n": 62, "tipo": "single",
        "pregunta": "¿Cuál de los siguientes NO es un ámbito de acción de los sindicatos?",
        "opciones": ["Pedir que se respete el cumplimiento legal del máximo de 2 horas extra diarias",
                     "Velar por las condiciones de seguridad e higiene de los trabajadores",
                     "Denunciar irregularidades en el otorgamiento de las vacaciones al personal",
                     "Solicitar a la empresa cambios de productos o clientes por la dificultad que genera al trabajador",
                     "Solicitar a la empresa cumplir con los beneficios establecidos en el instrumento colectivo"],
        "correctas": ["Solicitar a la empresa cambios de productos o clientes por la dificultad que genera al trabajador"],
    },
    {
        "n": 63, "tipo": "single",
        "pregunta": "Considerando la tasa de sindicalización en Chile y su evolución, y su relación con otros países del mundo, ¿cuál de las siguientes aseveraciones es correcta?",
        "opciones": ["Si bien hubo un crecimiento en los últimos 5 años, la tasa no supera el 25%",
                     "Chile supera a los países de la comunidad europea que promedian un 35%",
                     "Chile está entre los países que más afiliados tiene en el mundo",
                     "La principal razón por la no creación de sindicatos es el miedo a perder el empleo",
                     "El crecimiento de los últimos años se debió a la reforma laboral alcanzando un 35%"],
        "correctas": ["Si bien hubo un crecimiento en los últimos 5 años, la tasa no supera el 25%"],
    },
    {
        "n": 64, "tipo": "single",
        "pregunta": "Ud. es el Gerente de RRHH de una empresa donde recién se formó un sindicato. ¿Cuál sería su principal preocupación estratégica en el corto plazo?",
        "opciones": ["Evaluar qué nuevos beneficios le va a ofrecer al sindicato antes que se los pidan",
                     "Empezar a preparar una posible presentación de proyecto de negociación colectiva",
                     "Que las personas no ingresen al sindicato",
                     "Que los supervisores y jefaturas traten bien a los dirigentes",
                     "Disponer de la lista de las personas sindicalizadas para identificarlas"],
        "correctas": ["Evaluar qué nuevos beneficios le va a ofrecer al sindicato antes que se los pidan"],
    },
    {
        "n": 65, "tipo": "single",
        "pregunta": "¿Cuál de las siguientes recomendaciones NO se debe seguir al momento de enfrentar un proceso de negociación colectiva?",
        "opciones": ["Focalizar su estrategia Ganar-Ganar para lograr el mejor de los acuerdos",
                     "Potenciar a los dirigentes sindicales para que no sean meros representantes",
                     "Disponer de ejemplos claros para contraargumentar siempre lo pedido por el sindicato",
                     "Definir claros y expeditos canales de comunicación para dar libertad al rol del dirigente",
                     "Buscar la aprobación de las mayorías y extender beneficios a los no sindicalizados"],
        "correctas": ["Disponer de ejemplos claros para contraargumentar siempre lo pedido por el sindicato"],
    },
    {
        "n": 66, "tipo": "single",
        "pregunta": "Si Ud. desea mejorar los resultados en su organización, ¿qué tipo de beneficio implementaría?",
        "opciones": ["Bono de productividad", "Bonos de asistencia", "Bonos de turno",
                     "Comisión de servicios", "Bono de vacaciones"],
        "correctas": ["Bono de productividad"],
    },
    {
        "n": 67, "tipo": "single",
        "pregunta": "En el proceso de acción disciplinaria, ¿qué debe ocurrir inmediatamente después de que la gerencia establezca las reglas?",
        "opciones": ["Comunicar las reglas a los empleados", "Evaluar el desempeño",
                     "Comparar el desempeño con las reglas", "Establecer metas organizacionales"],
        "correctas": ["Comunicar las reglas a los empleados"],
    },
    {
        "n": 68, "tipo": "single",
        "pregunta": "Para ser más eficaz, la acción disciplinaria debe ser un proceso de ___.",
        "opciones": ["Aprendizaje", "Castigo", "Sanción inmediata", "Control"],
        "correctas": ["Aprendizaje"],
    },
    {
        "n": 69, "tipo": "single",
        "pregunta": "Todas las personas que prestan servicios a una organización deben ser incorporadas a las políticas de relaciones internas con los empleados.",
        "opciones": ["Verdadero", "Falso"],
        "correctas": ["Falso"],
    },
]


# ---------------------------------------------------------------------------
# Banco de preguntas 2: Guía de Estudio del Certamen
#   Construido EXCLUSIVAMENTE con la información del documento
#   "Guia_Estudio_Certamen_Gestion_Personas.md".
# ---------------------------------------------------------------------------
PREGUNTAS_GUIA = [
    # ----- Presentación 1: Higiene y Seguridad -----
    {
        "n": 1, "tipo": "single",
        "pregunta": "Según la guía, ¿cómo se define la SEGURIDAD en el ámbito laboral?",
        "opciones": ["Proteger a los empleados de lesiones causadas por accidentes",
                     "Estar libre de enfermedades físicas y emocionales",
                     "Cumplir con la normativa de remuneraciones",
                     "Mantener un clima laboral positivo"],
        "correctas": ["Proteger a los empleados de lesiones causadas por accidentes"],
    },
    {
        "n": 2, "tipo": "single",
        "pregunta": "Según la guía, ¿cómo se define la SALUD en el ámbito laboral?",
        "opciones": ["Estar libre de enfermedades físicas y emocionales",
                     "Proteger a los empleados de lesiones por accidentes",
                     "Contar con seguros complementarios",
                     "Tener un ambiente físico ergonómico"],
        "correctas": ["Estar libre de enfermedades físicas y emocionales"],
    },
    {
        "n": 3, "tipo": "multi",
        "pregunta": "¿Cuál es la base normativa de la seguridad y salud laboral en Chile? (selección múltiple)",
        "opciones": ["Código del Trabajo", "Código Sanitario", "Ley N° 16.744", "Ley de Bancos"],
        "correctas": ["Código del Trabajo", "Código Sanitario", "Ley N° 16.744"],
    },
    {
        "n": 4, "tipo": "single",
        "pregunta": "¿Qué institución fiscaliza la seguridad y salud laboral en el sector minero?",
        "opciones": ["SERNAGEOMIN", "Directemar", "SUSESO", "SEREMI de Salud"],
        "correctas": ["SERNAGEOMIN"],
    },
    {
        "n": 5, "tipo": "single",
        "pregunta": "¿Qué institución fiscaliza la seguridad y salud laboral en el sector pesca?",
        "opciones": ["Directemar", "SERNAGEOMIN", "Dirección del Trabajo", "SUSESO"],
        "correctas": ["Directemar"],
    },
    {
        "n": 6, "tipo": "single",
        "pregunta": "El Art. 184 de la Norma General de Protección establece:",
        "opciones": ["La obligación del empleador de proteger eficazmente la vida y salud de los trabajadores",
                     "La afiliación voluntaria a los sindicatos",
                     "El financiamiento del seguro contra accidentes",
                     "El derecho a la negociación colectiva"],
        "correctas": ["La obligación del empleador de proteger eficazmente la vida y salud de los trabajadores"],
    },
    {
        "n": 7, "tipo": "single",
        "pregunta": "Según el Reglamento de Condiciones Sanitarias y Ambientales, los Comités Paritarios deben existir en empresas con:",
        "opciones": ["Más de 25 trabajadores", "Más de 100 trabajadores",
                     "Más de 50 trabajadores", "Más de 10 trabajadores"],
        "correctas": ["Más de 25 trabajadores"],
    },
    {
        "n": 8, "tipo": "single",
        "pregunta": "Los Departamentos de Prevención de Riesgos deben existir en empresas con:",
        "opciones": ["Más de 100 trabajadores", "Más de 25 trabajadores",
                     "Más de 50 trabajadores", "Más de 200 trabajadores"],
        "correctas": ["Más de 100 trabajadores"],
    },
    {
        "n": 9, "tipo": "single",
        "pregunta": "¿En qué año se promulgó la Ley 16.744?",
        "opciones": ["1968", "1980", "1973", "1990"],
        "correctas": ["1968"],
    },
    {
        "n": 10, "tipo": "single",
        "pregunta": "Según el Artículo 1° de la Ley 16.744, el Seguro Social contra accidentes del trabajo y enfermedades profesionales es:",
        "opciones": ["Obligatorio", "Voluntario", "Optativo para grandes empresas", "Exclusivo del sector público"],
        "correctas": ["Obligatorio"],
    },
    {
        "n": 11, "tipo": "multi",
        "pregunta": "¿Cuáles de las siguientes son MUTUALIDADES administradoras del seguro de la Ley 16.744? (selección múltiple)",
        "opciones": ["ACHS", "IST", "MUSEG", "ISL"],
        "correctas": ["ACHS", "IST", "MUSEG"],
    },
    {
        "n": 12, "tipo": "single",
        "pregunta": "¿Cómo se financia el seguro de la Ley 16.744?",
        "opciones": ["Con una prima fija (0,95%) más una cotización variable según siniestralidad e industria",
                     "Completamente con aportes del trabajador",
                     "Con un porcentaje fijo del 5% de las remuneraciones",
                     "Con aportes exclusivos del Estado"],
        "correctas": ["Con una prima fija (0,95%) más una cotización variable según siniestralidad e industria"],
    },
    {
        "n": 13, "tipo": "multi",
        "pregunta": "Según la guía, las causas de accidentes en los programas de seguridad se clasifican en: (selección múltiple)",
        "opciones": ["Acciones negligentes", "Condiciones inseguras",
                     "Malas políticas gubernamentales", "Falta de fiscalización"],
        "correctas": ["Acciones negligentes", "Condiciones inseguras"],
    },
    {
        "n": 14, "tipo": "single",
        "pregunta": "Según la guía, ¿cómo se compone un Comité Paritario?",
        "opciones": ["3 representantes del empleador y 3 de los trabajadores",
                     "Solo representantes de los trabajadores",
                     "5 representantes del empleador y 2 de los trabajadores",
                     "Un representante por cada departamento"],
        "correctas": ["3 representantes del empleador y 3 de los trabajadores"],
    },
    {
        "n": 15, "tipo": "single",
        "pregunta": "La Ley Karin corresponde a la Ley N°:",
        "opciones": ["21.643", "16.744", "21.220", "20.940"],
        "correctas": ["21.643"],
    },
    {
        "n": 16, "tipo": "single",
        "pregunta": "¿Qué regula la Ley Karin (N° 21.643)?",
        "opciones": ["La prevención, investigación y sanción del acoso y la violencia en el trabajo",
                     "El financiamiento del seguro de accidentes",
                     "La reducción de la jornada laboral",
                     "La negociación colectiva"],
        "correctas": ["La prevención, investigación y sanción del acoso y la violencia en el trabajo"],
    },
    {
        "n": 17, "tipo": "single",
        "pregunta": "El acoso laboral está definido en el:",
        "opciones": ["Art. 2 del Código del Trabajo", "Art. 184 del Código del Trabajo",
                     "Art. 220 del Código del Trabajo", "Art. 1° de la Ley 16.744"],
        "correctas": ["Art. 2 del Código del Trabajo"],
    },
    {
        "n": 18, "tipo": "single",
        "pregunta": "El protocolo psicosocial CEAL-SM de SUSESO evalúa:",
        "opciones": ["12 dimensiones", "5 dimensiones", "8 dimensiones", "20 dimensiones"],
        "correctas": ["12 dimensiones"],
    },
    {
        "n": 19, "tipo": "single",
        "pregunta": "Según la guía, ¿cómo se denomina el estrés positivo?",
        "opciones": ["Eustrés", "Distrés", "Burnout", "Tecnoestrés"],
        "correctas": ["Eustrés"],
    },
    {
        "n": 20, "tipo": "single",
        "pregunta": "Según la guía, ¿cómo se denomina el estrés negativo?",
        "opciones": ["Distrés", "Eustrés", "Fatiga", "Ansiedad"],
        "correctas": ["Distrés"],
    },
    {
        "n": 21, "tipo": "single",
        "pregunta": "¿Cómo se llama el programa de SENDA sobre consumo de alcohol y drogas en el trabajo?",
        "opciones": ["Trabajar con Calidad de Vida", "Chile sin Drogas",
                     "Espacios Laborales Saludables", "Cuida tu Salud"],
        "correctas": ["Trabajar con Calidad de Vida"],
    },

    # ----- Presentación 2: Derechos y Relaciones Laborales -----
    {
        "n": 22, "tipo": "single",
        "pregunta": "Según la guía, la jornada laboral es de ____ horas (con posibilidad de 40 h).",
        "opciones": ["44", "45", "40", "48"],
        "correctas": ["44"],
    },
    {
        "n": 23, "tipo": "single",
        "pregunta": "El contrato psicológico, dentro del derecho de protección del trabajo, se refiere a:",
        "opciones": ["Un intercambio justo entre trabajador y empleador",
                     "Un documento firmado ante notario",
                     "El reglamento interno de la empresa",
                     "El contrato colectivo del sindicato"],
        "correctas": ["Un intercambio justo entre trabajador y empleador"],
    },
    {
        "n": 24, "tipo": "single",
        "pregunta": "El Art. 220 del Código del Trabajo establece:",
        "opciones": ["Los fines de las organizaciones sindicales",
                     "El derecho a huelga",
                     "La obligación de proteger la vida y salud del trabajador",
                     "La definición del contrato colectivo"],
        "correctas": ["Los fines de las organizaciones sindicales"],
    },
    {
        "n": 25, "tipo": "single",
        "pregunta": "Según el Art. 214, la afiliación a un sindicato es:",
        "opciones": ["Voluntaria", "Obligatoria",
                     "Automática al firmar el contrato", "Decidida por el empleador"],
        "correctas": ["Voluntaria"],
    },
    {
        "n": 26, "tipo": "multi",
        "pregunta": "Según el Art. 216, ¿cuáles son tipos de sindicato? (selección múltiple)",
        "opciones": ["De empresa", "Interempresa", "De trabajadores independientes",
                     "De eventuales o transitorios"],
        "correctas": ["De empresa", "Interempresa", "De trabajadores independientes",
                      "De eventuales o transitorios"],
    },
    {
        "n": 27, "tipo": "single",
        "pregunta": "El Art. 345 del Código del Trabajo establece, respecto de la huelga:",
        "opciones": ["El derecho a huelga y la prohibición de reemplazo",
                     "La última oferta del empleador",
                     "La convocatoria a votación",
                     "La definición del instrumento colectivo"],
        "correctas": ["El derecho a huelga y la prohibición de reemplazo"],
    },
    {
        "n": 28, "tipo": "single",
        "pregunta": "El Art. 320 del Código del Trabajo corresponde a:",
        "opciones": ["La definición del instrumento/contrato colectivo",
                     "El derecho a huelga",
                     "Los fines de las organizaciones sindicales",
                     "La afiliación voluntaria"],
        "correctas": ["La definición del instrumento/contrato colectivo"],
    },

    # ----- Presentación 3: Beneficios y HPWS -----
    {
        "n": 29, "tipo": "multi",
        "pregunta": "Según la guía, ¿cuáles son los tipos de beneficios? (selección múltiple)",
        "opciones": ["Legales", "Voluntarios", "Flexibles", "Intangibles"],
        "correctas": ["Legales", "Voluntarios", "Flexibles", "Intangibles"],
    },
    {
        "n": 30, "tipo": "single",
        "pregunta": "¿Cuál es la PRIMERA etapa de la implementación de un plan de beneficios?",
        "opciones": ["Diagnóstico", "Diseño", "Comunicación", "Evaluación"],
        "correctas": ["Diagnóstico"],
    },
    {
        "n": 31, "tipo": "single",
        "pregunta": "¿Cuál es la ÚLTIMA etapa de la implementación de un plan de beneficios?",
        "opciones": ["Evaluación", "Implementación", "Comunicación", "Segmentación"],
        "correctas": ["Evaluación"],
    },
    {
        "n": 32, "tipo": "single",
        "pregunta": "Según la guía, la reducción de jornada en Chile contempla pasar a ____ horas en 2028.",
        "opciones": ["40", "42", "44", "38"],
        "correctas": ["40"],
    },
    {
        "n": 33, "tipo": "multi",
        "pregunta": "¿Cuáles de los siguientes son beneficios LEGALES en Chile? (selección múltiple)",
        "opciones": ["Vacaciones", "Indemnización por años de servicio",
                     "Bono de desempeño", "Seguro complementario de salud"],
        "correctas": ["Vacaciones", "Indemnización por años de servicio"],
    },
    {
        "n": 34, "tipo": "multi",
        "pregunta": "Según la guía, las preferencias de beneficios se analizan por generación. ¿Cuáles se mencionan? (selección múltiple)",
        "opciones": ["Baby Boomers", "Generación X", "Generación Z", "Generación Beta"],
        "correctas": ["Baby Boomers", "Generación X", "Generación Z"],
    },
    {
        "n": 35, "tipo": "multi",
        "pregunta": "Los principios fundamentales de un Sistema de Trabajo de Alto Desempeño (HPWS) incluyen: (selección múltiple)",
        "opciones": ["Igualitarismo y compromiso", "Información compartida y confianza",
                     "Desarrollo del conocimiento", "Vínculos desempeño–recompensa"],
        "correctas": ["Igualitarismo y compromiso", "Información compartida y confianza",
                      "Desarrollo del conocimiento", "Vínculos desempeño–recompensa"],
    },
    {
        "n": 36, "tipo": "single",
        "pregunta": "¿Qué significa la sigla HPWS?",
        "opciones": ["Sistema de Trabajo de Alto Desempeño (High Performance Work System)",
                     "Plan de Beneficios de Alto Valor",
                     "Sistema de Higiene y Prevención Laboral",
                     "Política de Recursos Humanos Sostenibles"],
        "correctas": ["Sistema de Trabajo de Alto Desempeño (High Performance Work System)"],
    },
    {
        "n": 37, "tipo": "multi",
        "pregunta": "Según la guía, los beneficios MÁS VALORADOS en Chile incluyen: (selección múltiple)",
        "opciones": ["Teletrabajo", "Horarios flexibles", "Salud mental",
                     "Aumento de la jornada laboral"],
        "correctas": ["Teletrabajo", "Horarios flexibles", "Salud mental"],
    },

    # ----- Presentación 4: RRHH Internacional -----
    {
        "n": 38, "tipo": "multi",
        "pregunta": "El análisis PEST estudia los factores: (selección múltiple)",
        "opciones": ["Políticos", "Económicos", "Socioculturales", "Tecnológicos"],
        "correctas": ["Políticos", "Económicos", "Socioculturales", "Tecnológicos"],
    },
    {
        "n": 39, "tipo": "single",
        "pregunta": "Una organización que adapta sus productos sin cambiar significativamente sus operaciones es:",
        "opciones": ["Internacional", "Multinacional", "Transnacional", "Global"],
        "correctas": ["Internacional"],
    },
    {
        "n": 40, "tipo": "single",
        "pregunta": "Una organización con filiales independientes y poca integración es:",
        "opciones": ["Multinacional", "Internacional", "Transnacional", "Global"],
        "correctas": ["Multinacional"],
    },
    {
        "n": 41, "tipo": "single",
        "pregunta": "Una organización con estructura flexible que combina autonomía e integración es:",
        "opciones": ["Transnacional", "Multinacional", "Internacional", "Global"],
        "correctas": ["Transnacional"],
    },
    {
        "n": 42, "tipo": "single",
        "pregunta": "Una organización que opera de forma similar a una nacional, pero con el mundo como mercado, es:",
        "opciones": ["Global", "Internacional", "Multinacional", "Transnacional"],
        "correctas": ["Global"],
    },
    {
        "n": 43, "tipo": "multi",
        "pregunta": "Según la nacionalidad de los colaboradores en RRHH internacional, se distingue entre: (selección múltiple)",
        "opciones": ["Expatriados", "Ciudadanos del país anfitrión",
                     "Ciudadanos de un tercer país", "Ciudadanos sin nacionalidad"],
        "correctas": ["Expatriados", "Ciudadanos del país anfitrión", "Ciudadanos de un tercer país"],
    },
    {
        "n": 44, "tipo": "single",
        "pregunta": "¿Qué significan las siglas OIT?",
        "opciones": ["Organización Internacional del Trabajo",
                     "Confederación Internacional de Sindicatos",
                     "Organización Industrial del Trabajo",
                     "Oficina Internacional de Trabajadores"],
        "correctas": ["Organización Internacional del Trabajo"],
    },
    {
        "n": 45, "tipo": "single",
        "pregunta": "¿Qué significan las siglas ITUC?",
        "opciones": ["Confederación Internacional de Sindicatos",
                     "Organización Internacional del Trabajo",
                     "Instituto Técnico de Unión y Cooperación",
                     "Tribunal Internacional de Unión Comercial"],
        "correctas": ["Confederación Internacional de Sindicatos"],
    },
    {
        "n": 46, "tipo": "single",
        "pregunta": "La codeterminación, como forma de participación de los trabajadores en la administración, es característica de:",
        "opciones": ["Alemania", "Japón", "Estados Unidos", "Chile"],
        "correctas": ["Alemania"],
    },
]


# ---------------------------------------------------------------------------
# Banco de preguntas 3: Guía de Estudio — Nivel Avanzado
#   Mismo contenido del documento "Guia_Estudio_Certamen_Gestion_Personas.md",
#   pero redactado al estilo aplicado/situacional de las 60 originales
#   (casos con personajes, "EXCEPTO", clasificación de ejemplos, umbrales).
#   Dificultad más alta.
# ---------------------------------------------------------------------------
PREGUNTAS_GUIA_AVANZADO = [
    # ----- Presentación 1: Higiene y Seguridad -----
    {
        "n": 1, "tipo": "multi",
        "pregunta": "Manufacturas del Sur cuenta con 130 trabajadores. De acuerdo con el reglamento de condiciones sanitarias y ambientales, ¿qué entidad(es) está obligada a constituir? (selección múltiple)",
        "opciones": ["Comité Paritario de Higiene y Seguridad",
                     "Departamento de Prevención de Riesgos",
                     "Un sindicato de empresa",
                     "Su propia mutualidad"],
        "correctas": ["Comité Paritario de Higiene y Seguridad",
                      "Departamento de Prevención de Riesgos"],
    },
    {
        "n": 2, "tipo": "single",
        "pregunta": "Una pyme de 18 trabajadores evalúa qué organismos de seguridad debe constituir obligatoriamente. ¿Cuál corresponde?",
        "opciones": ["Ninguno de los dos, pues no alcanza el mínimo de 25 trabajadores para el Comité Paritario",
                     "Solo el Comité Paritario",
                     "Solo el Departamento de Prevención de Riesgos",
                     "Ambos: Comité Paritario y Departamento de Prevención"],
        "correctas": ["Ninguno de los dos, pues no alcanza el mínimo de 25 trabajadores para el Comité Paritario"],
    },
    {
        "n": 3, "tipo": "single",
        "pregunta": "Laura, ciudadana chilena, es enviada por su empresa a dirigir la filial en Perú. Según la clasificación de RRHH internacional, Laura es:",
        "opciones": ["Expatriada", "Ciudadana del país anfitrión",
                     "Ciudadana de un tercer país", "Trabajadora transnacional"],
        "correctas": ["Expatriada"],
    },
    {
        "n": 4, "tipo": "single",
        "pregunta": "En esa misma filial peruana trabaja Marco, nacido y residente en Perú y contratado localmente. Según la clasificación por nacionalidad, Marco es:",
        "opciones": ["Ciudadano del país anfitrión", "Expatriado",
                     "Ciudadano de un tercer país", "Ciudadano global"],
        "correctas": ["Ciudadano del país anfitrión"],
    },
    {
        "n": 5, "tipo": "single",
        "pregunta": "Un trabajador no se coloca los guantes de seguridad, pese a estar disponibles, y sufre un corte. Según la clasificación de causas de accidentes, esto corresponde a:",
        "opciones": ["Una acción negligente", "Una condición insegura",
                     "Una enfermedad profesional", "Un accidente de trayecto"],
        "correctas": ["Una acción negligente"],
    },
    {
        "n": 6, "tipo": "single",
        "pregunta": "Una máquina sin protección y con cables expuestos provoca un accidente. Esta causa se clasifica como:",
        "opciones": ["Una condición insegura", "Una acción negligente",
                     "Una falta de fiscalización", "Una falla psicosocial"],
        "correctas": ["Una condición insegura"],
    },
    {
        "n": 7, "tipo": "single",
        "pregunta": "Todas las siguientes son instituciones fiscalizadoras del sistema de seguridad y salud laboral en Chile, EXCEPTO:",
        "opciones": ["ACHS", "Dirección del Trabajo", "SEREMI de Salud", "SERNAGEOMIN"],
        "correctas": ["ACHS"],
    },
    {
        "n": 8, "tipo": "single",
        "pregunta": "Pedro sufre un accidente mientras se dirige desde su casa al trabajo. Según la Ley 16.744, este accidente:",
        "opciones": ["Está cubierto, pues el seguro contempla los accidentes de trayecto",
                     "No está cubierto, porque ocurrió fuera del lugar de trabajo",
                     "Solo se cubre si el trabajador tiene contrato indefinido",
                     "Debe ser cubierto por el seguro de cesantía"],
        "correctas": ["Está cubierto, pues el seguro contempla los accidentes de trayecto"],
    },
    {
        "n": 9, "tipo": "single",
        "pregunta": "La cotización del seguro de la Ley 16.744 se compone de una prima fija de 0,95% más una parte variable que depende de:",
        "opciones": ["La siniestralidad y la actividad (industria) de la empresa",
                     "El número de sindicatos de la empresa",
                     "El sueldo del gerente general",
                     "La antigüedad promedio de los trabajadores"],
        "correctas": ["La siniestralidad y la actividad (industria) de la empresa"],
    },
    {
        "n": 10, "tipo": "single",
        "pregunta": "Una empresa principal que subcontrata servicios y agrupa a más de 50 trabajadores debe, según la Ley 16.744:",
        "opciones": ["Implementar un sistema de gestión de seguridad y salud en el trabajo",
                     "Eximirse de toda responsabilidad sobre los subcontratados",
                     "Constituir una mutualidad propia",
                     "Reducir la jornada de los subcontratados"],
        "correctas": ["Implementar un sistema de gestión de seguridad y salud en el trabajo"],
    },
    {
        "n": 11, "tipo": "multi",
        "pregunta": "Respecto del Comité Paritario de Higiene y Seguridad, son correctas: (selección múltiple)",
        "opciones": ["Está compuesto por 3 representantes del empleador y 3 de los trabajadores",
                     "Es obligatorio en empresas con más de 25 trabajadores",
                     "Investiga las causas de los accidentes del trabajo y enfermedades profesionales",
                     "Está formado únicamente por representantes de los trabajadores"],
        "correctas": ["Está compuesto por 3 representantes del empleador y 3 de los trabajadores",
                      "Es obligatorio en empresas con más de 25 trabajadores",
                      "Investiga las causas de los accidentes del trabajo y enfermedades profesionales"],
    },
    {
        "n": 12, "tipo": "single",
        "pregunta": "Ante denuncias reiteradas de hostigamiento entre compañeros, una empresa debe activar el procedimiento de prevención, investigación y sanción establecido por:",
        "opciones": ["La Ley Karin (N° 21.643)", "La Ley 16.744",
                     "El Art. 220 del Código del Trabajo", "El protocolo CEAL-SM"],
        "correctas": ["La Ley Karin (N° 21.643)"],
    },
    {
        "n": 13, "tipo": "single",
        "pregunta": "Una empresa aplica el protocolo psicosocial CEAL-SM de SUSESO. Este instrumento evalúa un total de:",
        "opciones": ["12 dimensiones", "5 dimensiones", "8 dimensiones", "3 dimensiones"],
        "correctas": ["12 dimensiones"],
    },
    {
        "n": 14, "tipo": "single",
        "pregunta": "María enfrenta un proyecto desafiante que le genera una presión que la motiva y mejora su rendimiento. Este tipo de estrés positivo se denomina:",
        "opciones": ["Eustrés", "Distrés", "Burnout", "Fatiga crónica"],
        "correctas": ["Eustrés"],
    },
    {
        "n": 15, "tipo": "single",
        "pregunta": "El agotamiento crónico que resulta de un distrés sostenido en el tiempo se conoce como:",
        "opciones": ["Burnout", "Eustrés", "Ergonomía", "Acoso laboral"],
        "correctas": ["Burnout"],
    },

    # ----- Presentación 2: Derechos y Relaciones Laborales -----
    {
        "n": 16, "tipo": "single",
        "pregunta": "Diego ingresa a una empresa que cuenta con un sindicato. Según el Art. 214, su afiliación al sindicato es:",
        "opciones": ["Voluntaria", "Obligatoria",
                     "Automática tras el período de prueba", "Decidida por el empleador"],
        "correctas": ["Voluntaria"],
    },
    {
        "n": 17, "tipo": "multi",
        "pregunta": "Según el Art. 216, son tipos de sindicato reconocidos: (selección múltiple)",
        "opciones": ["De empresa", "Interempresa", "De trabajadores independientes",
                     "De eventuales o transitorios"],
        "correctas": ["De empresa", "Interempresa", "De trabajadores independientes",
                      "De eventuales o transitorios"],
    },
    {
        "n": 18, "tipo": "single",
        "pregunta": "Durante una huelga legal enmarcada en una negociación colectiva, el empleador, conforme al Art. 345:",
        "opciones": ["No puede reemplazar a los trabajadores en huelga",
                     "Puede reemplazarlos libremente con personal externo",
                     "Puede despedir a los huelguistas",
                     "Debe cerrar definitivamente la empresa"],
        "correctas": ["No puede reemplazar a los trabajadores en huelga"],
    },
    {
        "n": 19, "tipo": "single",
        "pregunta": "Los trabajadores cubiertos por un contrato colectivo mantienen intactas todas las cláusulas de sus contratos individuales, sin que el colectivo las afecte.",
        "opciones": ["Falso", "Verdadero"],
        "correctas": ["Falso"],
    },
    {
        "n": 20, "tipo": "single",
        "pregunta": "Todos los siguientes son fines de las organizaciones sindicales según el Art. 220, EXCEPTO:",
        "opciones": ["Fijar unilateralmente la escala de sueldos de la empresa",
                     "Representar a los afiliados",
                     "Velar por la seguridad y salud de los trabajadores",
                     "Promover la capacitación y el desarrollo"],
        "correctas": ["Fijar unilateralmente la escala de sueldos de la empresa"],
    },

    # ----- Presentación 3: Beneficios y HPWS -----
    {
        "n": 21, "tipo": "single",
        "pregunta": "El pago de las cotizaciones previsionales de un trabajador corresponde a un beneficio de tipo:",
        "opciones": ["Legal", "Voluntario", "Flexible", "Intangible"],
        "correctas": ["Legal"],
    },
    {
        "n": 22, "tipo": "single",
        "pregunta": "Una empresa ofrece, por decisión propia, un seguro complementario de salud a sus colaboradores. Este corresponde a un beneficio:",
        "opciones": ["Voluntario", "Legal", "Obligatorio", "Previsional"],
        "correctas": ["Voluntario"],
    },
    {
        "n": 23, "tipo": "single",
        "pregunta": "En la implementación de un plan de beneficios, la etapa que sigue inmediatamente a la 'Definición de objetivos' es:",
        "opciones": ["Segmentación", "Diseño", "Comunicación", "Diagnóstico"],
        "correctas": ["Segmentación"],
    },
    {
        "n": 24, "tipo": "single",
        "pregunta": "Dentro de las 7 etapas de un plan de beneficios, la 'Comunicación' se ubica:",
        "opciones": ["Después del Diseño y antes de la Implementación",
                     "Antes del Diagnóstico",
                     "Inmediatamente después de la Segmentación",
                     "Como última etapa del proceso"],
        "correctas": ["Después del Diseño y antes de la Implementación"],
    },
    {
        "n": 25, "tipo": "single",
        "pregunta": "Todos los siguientes son beneficios legales en Chile, EXCEPTO:",
        "opciones": ["Bono de productividad", "Vacaciones",
                     "Indemnización por años de servicio", "Cotizaciones previsionales"],
        "correctas": ["Bono de productividad"],
    },
    {
        "n": 26, "tipo": "multi",
        "pregunta": "Son principios fundamentales de un Sistema de Trabajo de Alto Desempeño (HPWS): (selección múltiple)",
        "opciones": ["Igualitarismo y compromiso", "Información compartida y confianza",
                     "Desarrollo del conocimiento", "Vínculos desempeño–recompensa"],
        "correctas": ["Igualitarismo y compromiso", "Información compartida y confianza",
                      "Desarrollo del conocimiento", "Vínculos desempeño–recompensa"],
    },
    {
        "n": 27, "tipo": "single",
        "pregunta": "La reducción de la jornada laboral en Chile contempla llegar a 40 horas en el año:",
        "opciones": ["2028", "2025", "2030", "2026"],
        "correctas": ["2028"],
    },

    # ----- Presentación 4: RRHH Internacional -----
    {
        "n": 28, "tipo": "single",
        "pregunta": "Una empresa posee una estructura flexible que combina, a la vez, autonomía de sus unidades e integración global. Según los tipos de organización, es del tipo:",
        "opciones": ["Transnacional", "Multinacional", "Internacional", "Global"],
        "correctas": ["Transnacional"],
    },
    {
        "n": 29, "tipo": "single",
        "pregunta": "Una compañía opera de manera muy similar a una empresa nacional, pero considerando al mundo entero como su mercado. Este tipo de organización es:",
        "opciones": ["Global", "Internacional", "Multinacional", "Transnacional"],
        "correctas": ["Global"],
    },
    {
        "n": 30, "tipo": "single",
        "pregunta": "Una empresa con filiales independientes entre sí y con poca integración entre ellas corresponde al tipo:",
        "opciones": ["Multinacional", "Transnacional", "Global", "Internacional"],
        "correctas": ["Multinacional"],
    },
    {
        "n": 31, "tipo": "single",
        "pregunta": "Al analizar la inflación y el tipo de cambio de un país mediante el modelo PEST, estos elementos corresponden a factores:",
        "opciones": ["Económicos", "Políticos", "Socioculturales", "Tecnológicos"],
        "correctas": ["Económicos"],
    },
    {
        "n": 32, "tipo": "single",
        "pregunta": "Los cambios en hábitos, valores y estilos de vida de la población, dentro del modelo PEST, son factores:",
        "opciones": ["Socioculturales", "Políticos", "Económicos", "Tecnológicos"],
        "correctas": ["Socioculturales"],
    },
    {
        "n": 33, "tipo": "single",
        "pregunta": "En las relaciones laborales internacionales, el organismo encargado de promover estándares laborales a nivel mundial es la OIT, cuyo nombre completo es:",
        "opciones": ["Organización Internacional del Trabajo",
                     "Confederación Internacional de Sindicatos",
                     "Organización Industrial del Trabajo",
                     "Oficina Internacional de Trabajadores"],
        "correctas": ["Organización Internacional del Trabajo"],
    },
    {
        "n": 34, "tipo": "single",
        "pregunta": "La codeterminación, mecanismo de participación de los trabajadores en la administración de la empresa, es característica especialmente de:",
        "opciones": ["Alemania", "Japón", "Estados Unidos", "Chile"],
        "correctas": ["Alemania"],
    },
    {
        "n": 35, "tipo": "single",
        "pregunta": "Todas las siguientes son formas de participación de los trabajadores en la administración mencionadas en la guía, EXCEPTO:",
        "opciones": ["La negociación de acciones bursátiles de la empresa",
                     "Los consejos de empleados",
                     "La representación legal en Europa",
                     "La codeterminación en Alemania"],
        "correctas": ["La negociación de acciones bursátiles de la empresa"],
    },
]


# ---------------------------------------------------------------------------
# Banco de preguntas 4: Certamen — Nivel Difícil
#   Construido EXCLUSIVAMENTE con el contenido de los 4 archivos del certamen:
#     - Cap 12 Higiene y Seguridad
#     - Cap 14 y 15 Derechos de los trabajadores y Relaciones laborales (PDF)
#     - Clase 10 Adm. de Beneficios y equipos de alto desempeño (PPTX)
#     - Clase 14 Adm. internacional de RRHH (PPTX)
#   Estilo aplicado/situacional de las 60 originales, con cifras, artículos y
#   plazos exactos. Mayor nivel de dificultad.
# ---------------------------------------------------------------------------
PREGUNTAS_CERTAMEN_DIFICIL = [
    # ----- Beneficios legales (Clase 10) -----
    {
        "n": 1, "tipo": "single",
        "pregunta": "Según los beneficios legales en Chile, las vacaciones corresponden a 15 días hábiles al año, con posibilidad de acumular hasta:",
        "opciones": ["2 períodos", "3 períodos", "1 período (no se acumulan)", "4 períodos"],
        "correctas": ["2 períodos"],
        "explicacion": "Clase 10: las vacaciones son 15 días hábiles al año, acumulables hasta 2 períodos.",
    },
    {
        "n": 2, "tipo": "single",
        "pregunta": "La indemnización por años de servicio (despido sin causa justificada) equivale a un mes por año, con un tope de:",
        "opciones": ["11 años y un tope de monto de 90 UF", "5 años y tope de 60 UF",
                     "11 años, sin tope de monto", "Sin tope de años, con tope de 90 UF"],
        "correctas": ["11 años y un tope de monto de 90 UF"],
        "explicacion": "Clase 10: un mes por año, con tope de 11 años y tope de monto de 90 UF, aplicable a despidos sin causa justificada.",
    },
    {
        "n": 3, "tipo": "single",
        "pregunta": "Las cotizaciones previsionales obligatorias en Chile contemplan, además del seguro de cesantía:",
        "opciones": ["10% para AFP y 7% para salud", "7% para AFP y 10% para salud",
                     "12% para AFP y 5% para salud", "10% para AFP y 10% para salud"],
        "correctas": ["10% para AFP y 7% para salud"],
        "explicacion": "Clase 10: cotizaciones de 10% AFP, 7% salud (Fonasa/Isapre) y seguro de cesantía.",
    },
    {
        "n": 4, "tipo": "single",
        "pregunta": "El postnatal parental corresponde a 84 días; si la trabajadora opta por tomarlo en media jornada, se extiende a:",
        "opciones": ["126 días", "168 días", "112 días", "90 días"],
        "correctas": ["126 días"],
        "explicacion": "Clase 10: postnatal parental de 84 días, o 126 días si se toma en media jornada.",
    },
    {
        "n": 5, "tipo": "single",
        "pregunta": "Ante el fallecimiento del cónyuge o de un hijo, el trabajador tiene derecho a un permiso de 7 días corridos acompañado de:",
        "opciones": ["Fuero laboral por un mes", "Fuero laboral por seis meses",
                     "Indemnización adicional de 90 UF", "Reducción de jornada por un año"],
        "correctas": ["Fuero laboral por un mes"],
        "explicacion": "Clase 10: por muerte de cónyuge o hijo, 7 días corridos con fuero laboral por un mes (padre/madre 3 días, hermano 1 día).",
    },
    {
        "n": 6, "tipo": "single",
        "pregunta": "El permiso por matrimonio o unión civil es de 5 días hábiles consecutivos, que pueden usarse dentro de:",
        "opciones": ["Los 30 días siguientes al matrimonio", "Los 15 días siguientes",
                     "El mismo mes calendario", "Los 60 días siguientes"],
        "correctas": ["Los 30 días siguientes al matrimonio"],
        "explicacion": "Clase 10: 5 días hábiles consecutivos, dentro de los 30 días siguientes al matrimonio o unión civil.",
    },
    {
        "n": 7, "tipo": "single",
        "pregunta": "Todos los siguientes son beneficios LEGALES en Chile, EXCEPTO:",
        "opciones": ["Bonos de desempeño", "Vacaciones", "Licencias médicas", "Cotizaciones previsionales"],
        "correctas": ["Bonos de desempeño"],
        "explicacion": "Clase 10: los bonos de desempeño son un beneficio VOLUNTARIO; vacaciones, licencias médicas y cotizaciones son legales.",
    },
    {
        "n": 8, "tipo": "single",
        "pregunta": "El teletrabajo, los horarios adaptables y los días libres adicionales se clasifican como beneficios:",
        "opciones": ["Flexibles", "Legales", "Voluntarios", "Intangibles"],
        "correctas": ["Flexibles"],
        "explicacion": "Clase 10: los beneficios flexibles incluyen días libres adicionales, teletrabajo y horarios adaptables.",
    },
    {
        "n": 9, "tipo": "single",
        "pregunta": "El reconocimiento, el desarrollo profesional y el mentoring corresponden a beneficios:",
        "opciones": ["Intangibles", "Flexibles", "Monetarios", "Legales"],
        "correctas": ["Intangibles"],
        "explicacion": "Clase 10: los beneficios intangibles son el reconocimiento, el desarrollo profesional y el mentoring.",
    },
    {
        "n": 10, "tipo": "single",
        "pregunta": "La generación que prioriza seguridad laboral, pensiones y salud (nacidos entre 1945 y 1965) es:",
        "opciones": ["Baby Boomers", "Generación X", "Millennials / Generación Y", "Generación Z"],
        "correctas": ["Baby Boomers"],
        "explicacion": "Clase 10: los Baby Boomers (1945-1965) priorizan seguridad laboral, pensiones y salud.",
    },
    {
        "n": 11, "tipo": "single",
        "pregunta": "La diversidad, la inclusión, los beneficios digitales y el bienestar mental son preferencias asociadas principalmente a la:",
        "opciones": ["Generación Z", "Generación X", "Baby Boomers", "Generación Alfa"],
        "correctas": ["Generación Z"],
        "explicacion": "Clase 10: la Generación Z (2000-2015) valora diversidad, inclusión, beneficios digitales y bienestar mental.",
    },
    {
        "n": 12, "tipo": "single",
        "pregunta": "En la implementación de un plan de beneficios, el objetivo principal de la etapa de 'Segmentación' es:",
        "opciones": ["Identificar perfiles y adaptar los beneficios a las generaciones",
                     "Medir los KPIs de impacto",
                     "Alinear el plan con la estrategia de la empresa",
                     "Conocer la situación actual y las brechas"],
        "correctas": ["Identificar perfiles y adaptar los beneficios a las generaciones"],
        "explicacion": "Clase 10: la etapa 3 (Segmentación) busca identificar perfiles y adaptar los beneficios a las generaciones. (Las 7 etapas: Diagnóstico, Definición de objetivos, Segmentación, Diseño, Comunicación, Implementación, Evaluación.)",
    },
    {
        "n": 13, "tipo": "single",
        "pregunta": "En Chile, las grandes empresas destinan a beneficios un porcentaje del presupuesto de compensaciones de entre:",
        "opciones": ["15% y 25%", "5% y 10%", "20% y 30%", "30% y 40%"],
        "correctas": ["15% y 25%"],
        "explicacion": "Clase 10: en Chile las grandes empresas destinan 15%-25% del presupuesto de compensaciones (el 20%-30% corresponde al nivel internacional).",
    },
    {
        "n": 14, "tipo": "single",
        "pregunta": "Un High Performance Work System (HPWS) se define como:",
        "opciones": ["La combinación específica de prácticas de RRHH, estructuras y procesos que maximiza el conocimiento, habilidades, compromiso, flexibilidad y resiliencia del empleado",
                     "Un sistema de remuneración basado únicamente en la antigüedad",
                     "Un plan de beneficios legales obligatorios",
                     "Un software de control de asistencia del personal"],
        "correctas": ["La combinación específica de prácticas de RRHH, estructuras y procesos que maximiza el conocimiento, habilidades, compromiso, flexibilidad y resiliencia del empleado"],
        "explicacion": "Clase 10: un HPWS combina prácticas de RRHH, estructuras y procesos que maximizan conocimiento, habilidades, compromiso, flexibilidad y resiliencia para mejorar la competitividad.",
    },
    {
        "n": 15, "tipo": "single",
        "pregunta": "Todos los siguientes son principios fundamentales de un HPWS, EXCEPTO:",
        "opciones": ["Centralización y reserva de la información",
                     "Igualitarismo y compromiso",
                     "Desarrollo del conocimiento",
                     "Vínculos desempeño-recompensa"],
        "correctas": ["Centralización y reserva de la información"],
        "explicacion": "Clase 10: los 4 principios son igualitarismo y compromiso, INFORMACIÓN COMPARTIDA y confianza, desarrollo del conocimiento y vínculos desempeño-recompensa; 'centralizar la información' es lo contrario.",
    },

    # ----- Derechos de los trabajadores y relaciones internas (Cap 14-15) -----
    {
        "n": 16, "tipo": "multi",
        "pregunta": "¿Cuáles son los límites a la privacidad de los trabajadores señalados en la presentación? (selección múltiple)",
        "opciones": ["Las leyes", "Las políticas y reglamentos internos", "La ética",
                     "La decisión del sindicato"],
        "correctas": ["Las leyes", "Las políticas y reglamentos internos", "La ética"],
        "explicacion": "Cap 14-15: los límites a la privacidad del trabajador son las leyes, las políticas y reglamentos internos, y la ética.",
    },
    {
        "n": 17, "tipo": "single",
        "pregunta": "El 'intercambio justo' entre lo que el trabajador aporta y lo que recibe, dentro del derecho de protección del trabajo, se denomina:",
        "opciones": ["Contrato psicológico", "Contrato negligente", "Empleo a voluntad", "Contrato colectivo"],
        "correctas": ["Contrato psicológico"],
        "explicacion": "Cap 14-15: el contrato psicológico es el 'intercambio justo' dentro del derecho de protección del trabajo.",
    },
    {
        "n": 18, "tipo": "single",
        "pregunta": "El concepto de 'Empleo a Voluntad' comprende:",
        "opciones": ["El derecho a despedir y el derecho a renunciar",
                     "La obligación de afiliarse a un sindicato",
                     "El derecho a huelga indefinida",
                     "La negociación colectiva obligatoria"],
        "correctas": ["El derecho a despedir y el derecho a renunciar"],
        "explicacion": "Cap 14-15: el 'Empleo a Voluntad' comprende el derecho a despedir y el derecho a renunciar.",
    },
    {
        "n": 19, "tipo": "single",
        "pregunta": "Para evitar demandas por despidos injustificados se recomienda todo lo siguiente, EXCEPTO:",
        "opciones": ["Despedir sin necesidad de justificar la causa",
                     "Despedir solo si existe una razón clara",
                     "Documentar todos los problemas de desempeño",
                     "Ser consistente con los empleados en situaciones similares"],
        "correctas": ["Despedir sin necesidad de justificar la causa"],
        "explicacion": "Cap 14-15: se recomienda despedir solo con razón clara, seguir normas, documentar y ser consistente; despedir sin justificar es justamente lo que genera demandas.",
    },
    {
        "n": 20, "tipo": "multi",
        "pregunta": "¿Cuáles de las siguientes forman parte de las relaciones internas con los empleados? (selección múltiple)",
        "opciones": ["Promociones", "Transferencias", "Jubilación", "Selección"],
        "correctas": ["Promociones", "Transferencias", "Jubilación"],
        "explicacion": "Cap 14-15: las relaciones internas abarcan promociones, transferencias, renuncias, despidos, jubilación y acciones disciplinarias. La selección es parte del reclutamiento, no de las relaciones internas.",
    },
    {
        "n": 21, "tipo": "single",
        "pregunta": "Según el proceso de acción disciplinaria, ésta debe estar apuntada al ___ del empleado, ser justa y aplicarse en el momento indicado.",
        "opciones": ["Comportamiento", "Carácter", "Actitud", "Rendimiento histórico"],
        "correctas": ["Comportamiento"],
        "explicacion": "Cap 14-15: la acción disciplinaria debe apuntar al comportamiento, ser justa y darse en el momento indicado.",
    },
    {
        "n": 22, "tipo": "single",
        "pregunta": "Un aspecto clave ('ojo') de la acción disciplinaria es que:",
        "opciones": ["No afecta solo a una persona, sino a todo el grupo",
                     "Debe aplicarse en secreto y nunca documentarse",
                     "Solo la puede aplicar el sindicato",
                     "Debe basarse en la personalidad del trabajador"],
        "correctas": ["No afecta solo a una persona, sino a todo el grupo"],
        "explicacion": "Cap 14-15: 'ojo': la acción disciplinaria no afecta solo a una persona, sino a todo el grupo.",
    },

    # ----- Sindicatos (Cap 14-15) -----
    {
        "n": 23, "tipo": "single",
        "pregunta": "El Art. 212 reconoce el derecho a constituir organizaciones sindicales, sin autorización previa, a:",
        "opciones": ["Los trabajadores del sector privado y de las empresas del Estado",
                     "Solo a los trabajadores del sector privado",
                     "Solo a trabajadores con contrato indefinido",
                     "Únicamente a los trabajadores mayores de edad"],
        "correctas": ["Los trabajadores del sector privado y de las empresas del Estado"],
        "explicacion": "Art. 212: reconoce a los trabajadores del sector privado y de las empresas del Estado el derecho a constituir sindicatos sin autorización previa.",
    },
    {
        "n": 24, "tipo": "single",
        "pregunta": "Según el Art. 214, un trabajador no puede pertenecer a más de un sindicato simultáneamente:",
        "opciones": ["En función de un mismo empleo", "Bajo ninguna circunstancia",
                     "Salvo que el empleador lo autorice", "Salvo que tenga contrato indefinido"],
        "correctas": ["En función de un mismo empleo"],
        "explicacion": "Art. 214: la prohibición es pertenecer a más de un sindicato 'en función de un mismo empleo' (con otro empleo distinto sí podría).",
    },
    {
        "n": 25, "tipo": "single",
        "pregunta": "De acuerdo con el Art. 214, la afiliación a un sindicato es:",
        "opciones": ["Voluntaria, personal e indelegable", "Obligatoria y permanente",
                     "Voluntaria pero delegable", "Automática al ingresar a la empresa"],
        "correctas": ["Voluntaria, personal e indelegable"],
        "explicacion": "Art. 214: la afiliación a un sindicato es voluntaria, personal e indelegable; nadie puede ser obligado a afiliarse.",
    },
    {
        "n": 26, "tipo": "single",
        "pregunta": "Según el Art. 216, el sindicato que agrupa a trabajadores de dos o más empleadores distintos es el sindicato:",
        "opciones": ["Interempresa", "De empresa", "De trabajadores independientes",
                     "De eventuales o transitorios"],
        "correctas": ["Interempresa"],
        "explicacion": "Art. 216: el sindicato interempresa agrupa a trabajadores de dos o más empleadores distintos.",
    },
    {
        "n": 27, "tipo": "single",
        "pregunta": "El sindicato que agrupa a trabajadores que no dependen de empleador alguno es, según el Art. 216, el sindicato:",
        "opciones": ["De trabajadores independientes", "Interempresa", "De empresa",
                     "De eventuales o transitorios"],
        "correctas": ["De trabajadores independientes"],
        "explicacion": "Art. 216: el sindicato de trabajadores independientes agrupa a quienes no dependen de empleador alguno.",
    },
    {
        "n": 28, "tipo": "single",
        "pregunta": "En su rol de representación (Art. 220), las organizaciones sindicales:",
        "opciones": ["En ningún caso podrán percibir las remuneraciones de sus afiliados",
                     "Pueden retener parte de la remuneración de sus afiliados",
                     "Fijan las remuneraciones de la empresa",
                     "Administran directamente las cotizaciones de los afiliados"],
        "correctas": ["En ningún caso podrán percibir las remuneraciones de sus afiliados"],
        "explicacion": "Art. 220 (rol de representación): en ningún caso las organizaciones sindicales podrán percibir las remuneraciones de sus afiliados.",
    },
    {
        "n": 29, "tipo": "multi",
        "pregunta": "Según la presentación, ¿por qué se sindicalizan los empleados? (selección múltiple)",
        "opciones": ["Insatisfacción con la administración",
                     "Intereses sociales / oportunidades de liderazgo",
                     "Presiones para la sindicalización",
                     "Un aumento de sueldo garantizado por ley"],
        "correctas": ["Insatisfacción con la administración",
                      "Intereses sociales / oportunidades de liderazgo",
                      "Presiones para la sindicalización"],
        "explicacion": "Cap 14-15: se sindicalizan por insatisfacción con la administración, intereses sociales/liderazgo y presiones (de compañeros u organización). No hay un aumento garantizado por ley.",
    },

    # ----- Negociación colectiva y huelga (Cap 14-15) -----
    {
        "n": 30, "tipo": "single",
        "pregunta": "El Art. 320 define el instrumento colectivo como la convención entre empleadores y trabajadores cuyo objeto es establecer:",
        "opciones": ["Condiciones comunes de trabajo y remuneraciones u otros beneficios, por un tiempo determinado",
                     "Únicamente el monto del salario mínimo",
                     "La estructura organizacional de la empresa",
                     "El reglamento interno de higiene y seguridad"],
        "correctas": ["Condiciones comunes de trabajo y remuneraciones u otros beneficios, por un tiempo determinado"],
        "explicacion": "Art. 320: el instrumento colectivo establece condiciones comunes de trabajo y remuneraciones u otros beneficios, por un tiempo determinado.",
    },
    {
        "n": 31, "tipo": "multi",
        "pregunta": "Según el Art. 305, NO pueden negociar colectivamente: (selección múltiple)",
        "opciones": ["Los gerentes y apoderados con facultades generales de administración",
                     "Las personas autorizadas para contratar o despedir trabajadores",
                     "Los trabajadores con contrato de aprendizaje",
                     "Todos los trabajadores con contrato indefinido"],
        "correctas": ["Los gerentes y apoderados con facultades generales de administración",
                      "Las personas autorizadas para contratar o despedir trabajadores",
                      "Los trabajadores con contrato de aprendizaje"],
        "explicacion": "Art. 305: no negocian colectivamente los aprendices y de obra/faena transitoria, los gerentes/apoderados con facultades generales de administración, y quienes pueden contratar o despedir. Tener contrato indefinido no impide negociar.",
    },
    {
        "n": 32, "tipo": "single",
        "pregunta": "Según el Art. 306, NO serán objeto de negociación colectiva:",
        "opciones": ["Las materias que restrinjan la facultad del empleador de organizar, dirigir y administrar la empresa",
                     "Las remuneraciones",
                     "Los beneficios en especie o en dinero",
                     "Las condiciones comunes de trabajo"],
        "correctas": ["Las materias que restrinjan la facultad del empleador de organizar, dirigir y administrar la empresa"],
        "explicacion": "Art. 306: se negocian remuneraciones, beneficios y condiciones comunes de trabajo, pero NO las materias que limiten la facultad del empleador de organizar, dirigir y administrar la empresa.",
    },
    {
        "n": 33, "tipo": "single",
        "pregunta": "Según el Art. 311, las estipulaciones de un instrumento colectivo:",
        "opciones": ["Reemplazarán, en lo pertinente, a las de los contratos individuales de los trabajadores que sean parte de aquel",
                     "No producen ningún efecto sobre los contratos individuales",
                     "Pueden disminuir las remuneraciones del contrato individual",
                     "Solo aplican a los trabajadores no sindicalizados"],
        "correctas": ["Reemplazarán, en lo pertinente, a las de los contratos individuales de los trabajadores que sean parte de aquel"],
        "explicacion": "Art. 311: las estipulaciones del instrumento colectivo reemplazan en lo pertinente a las de los contratos individuales, sin poder disminuir las remuneraciones o beneficios del trabajador.",
    },
    {
        "n": 34, "tipo": "single",
        "pregunta": "De acuerdo con el Art. 345, durante una huelga legal:",
        "opciones": ["Se prohíbe el reemplazo de los trabajadores en huelga, pero no se afecta la libertad de trabajo de los no involucrados",
                     "El empleador puede reemplazar libremente a los huelguistas",
                     "Ningún trabajador de la empresa puede seguir trabajando",
                     "La empresa debe cerrar por completo"],
        "correctas": ["Se prohíbe el reemplazo de los trabajadores en huelga, pero no se afecta la libertad de trabajo de los no involucrados"],
        "explicacion": "Art. 345: la huelga es un derecho colectivo; se prohíbe el reemplazo de los huelguistas, pero no se afecta la libertad de trabajo de quienes no participan.",
    },
    {
        "n": 35, "tipo": "single",
        "pregunta": "La 'última oferta' del empleador (Art. 346) debe presentarse con a lo menos ___ de anticipación al inicio del período de votación de la huelga.",
        "opciones": ["2 días", "5 días", "10 días", "45 días"],
        "correctas": ["2 días"],
        "explicacion": "Art. 346: la 'última oferta' del empleador se presenta con a lo menos 2 días de anticipación al inicio del período de votación.",
    },
    {
        "n": 36, "tipo": "single",
        "pregunta": "Según el Art. 347, la comisión negociadora sindical debe convocar a la votación de la huelga con a lo menos ___ de anticipación.",
        "opciones": ["5 días", "2 días", "10 días", "30 días"],
        "correctas": ["5 días"],
        "explicacion": "Art. 347: la comisión negociadora sindical convoca a la votación de la huelga con a lo menos 5 días de anticipación.",
    },
    {
        "n": 37, "tipo": "single",
        "pregunta": "Según el Art. 348, si NO existe instrumento colectivo vigente, la huelga debe votarse dentro de los últimos 5 días de un total de ___ contados desde la presentación del proyecto de contrato colectivo.",
        "opciones": ["45 días", "30 días", "60 días", "90 días"],
        "correctas": ["45 días"],
        "explicacion": "Art. 348: sin instrumento vigente, la huelga se vota en los últimos 5 días de un total de 45 contados desde la presentación del proyecto de contrato colectivo.",
    },

    # ----- Administración internacional de RRHH (Clase 14) -----
    {
        "n": 38, "tipo": "single",
        "pregunta": "Una empresa que opera con estructura flexible, concede gran autonomía a sus operaciones independientes del país, pero unifica esas actividades en un todo integrado, es del tipo:",
        "opciones": ["Transnacional", "Multinacional", "Internacional", "Global"],
        "correctas": ["Transnacional"],
        "explicacion": "Clase 14: la organización transnacional combina gran autonomía de las operaciones con la integración de todas ellas en un todo.",
    },
    {
        "n": 39, "tipo": "single",
        "pregunta": "Una empresa cuyas filiales se manejan como organizaciones independientes, sin mucha integración entre ellas, es del tipo:",
        "opciones": ["Multinacional", "Transnacional", "Global", "Internacional"],
        "correctas": ["Multinacional"],
        "explicacion": "Clase 14: en la organización multinacional las filiales se manejan como organizaciones independientes, con poca integración.",
    },
    {
        "n": 40, "tipo": "single",
        "pregunta": "Un empleado cuya nacionalidad es diferente tanto a la del país anfitrión como a la del país de origen de la empresa se denomina:",
        "opciones": ["Ciudadano de un tercer país", "Expatriado",
                     "Ciudadano del país anfitrión", "Trabajador global"],
        "correctas": ["Ciudadano de un tercer país"],
        "explicacion": "Clase 14: el ciudadano de un tercer país tiene una nacionalidad distinta a la del país anfitrión y a la del país de origen de la empresa.",
    },
    {
        "n": 41, "tipo": "single",
        "pregunta": "La ITUC, organización laboral internacional, corresponde a:",
        "opciones": ["La Confederación Internacional de Sindicatos",
                     "La Organización Internacional del Trabajo",
                     "Un consejo de empleados europeo",
                     "Una mutualidad internacional"],
        "correctas": ["La Confederación Internacional de Sindicatos"],
        "explicacion": "Clase 14: la ITUC es la Confederación Internacional de Sindicatos, que promueve los derechos de los trabajadores a nivel global.",
    },
    {
        "n": 42, "tipo": "single",
        "pregunta": "La codeterminación, que por ley exige la representación de los empleados en el consejo de administración, es característica de:",
        "opciones": ["Alemania", "Japón", "Estados Unidos", "Chile"],
        "correctas": ["Alemania"],
        "explicacion": "Clase 14: la codeterminación, que exige por ley la representación de los empleados en el consejo de administración, es propia de Alemania.",
    },
]


# ---------------------------------------------------------------------------
# Cuestionarios disponibles
# ---------------------------------------------------------------------------
BANCOS = {
    "📘 Test RR.HH. (69 preguntas)": PREGUNTAS,
    "📗 Guía de Estudio del Certamen": PREGUNTAS_GUIA,
    "📕 Guía — Nivel Avanzado": PREGUNTAS_GUIA_AVANZADO,
    "📙 Certamen — Nivel Difícil": PREGUNTAS_CERTAMEN_DIFICIL,
}


# ---------------------------------------------------------------------------
# Configuración de la página + estilos
# ---------------------------------------------------------------------------
st.set_page_config(page_title="Test RR.HH.", page_icon="📝", layout="centered")

st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
      html, body, [class*="css"], .stMarkdown, button, input, select { font-family: 'Poppins', sans-serif; }

      /* Fondo general claro tipo dashboard */
      .stApp { background: #f4f6fb; }
      .block-container { padding-top: 2.2rem; }

      /* Cabecera / saludo */
      .greeting { font-size: 1.6rem; font-weight: 700; color: #1f2a44; margin: 0; }
      .greeting span { color: #4f7cff; }
      .subtitle { color: #98a1b5; font-size: 0.9rem; margin: 2px 0 0 0; }

      /* Título de sección */
      .section-title { font-size: 1.05rem; font-weight: 700; color: #1f2a44; margin: 6px 0 2px 0; }

      /* Tarjetas de estadísticas (Quick Stats) */
      .stat-card {
          background: #ffffff; border-radius: 16px; padding: 14px 16px;
          box-shadow: 0 6px 18px rgba(20,30,60,0.06);
          border-left: 4px solid var(--c, #4f7cff);
          display: flex; align-items: center; gap: 12px; min-height: 64px;
      }
      .stat-ico {
          width: 42px; height: 42px; border-radius: 12px; flex: 0 0 42px;
          display: flex; align-items: center; justify-content: center; font-size: 20px;
          background: var(--cb, #eaf0ff);
      }
      .stat-label { font-size: 0.72rem; color: #9aa3b5; font-weight: 600; line-height: 1.15; }
      .stat-value { font-size: 1.22rem; font-weight: 700; color: #1f2a44; line-height: 1.2; }

      /* Tarjeta de pregunta con cabecera en degradado (como la imagen) */
      .qcard {
          background: #ffffff; border-radius: 20px; overflow: hidden;
          box-shadow: 0 10px 28px rgba(20,30,60,0.09); margin-bottom: 8px;
      }
      .qhead { padding: 18px 24px; }
      .qbadge {
          display: inline-block; background: rgba(255,255,255,0.28); color: #ffffff;
          font-weight: 600; font-size: 0.75rem; padding: 4px 13px; border-radius: 999px;
      }
      .qbody { padding: 20px 24px 6px 24px; }
      .qtext { font-size: 1.13rem; font-weight: 600; color: #27304a; line-height: 1.45; }

      /* Botones tipo "pill" */
      .stButton > button {
          border-radius: 12px; font-weight: 600; border: none; padding: 0.5rem 1rem;
          transition: transform .06s ease, box-shadow .2s ease;
      }
      .stButton > button[kind="primary"] {
          background: linear-gradient(120deg, #4f7cff, #6a8dff); color: #fff;
          box-shadow: 0 6px 16px rgba(79,124,255,0.30);
      }
      .stButton > button[kind="primary"]:hover {
          transform: translateY(-1px); box-shadow: 0 10px 22px rgba(79,124,255,0.42); color:#fff;
      }
      .stButton > button[kind="secondary"] {
          background: #ffffff; color: #4f7cff; border: 1.5px solid #e3e8f2;
      }
      .stButton > button[kind="secondary"]:hover {
          border-color: #4f7cff; color: #4f7cff; transform: translateY(-1px);
      }

      /* Barra de progreso */
      .stProgress > div > div > div > div { background: linear-gradient(90deg,#4f7cff,#9b6bff); }

      /* Radios y checkboxes: aire + texto oscuro */
      div[role="radiogroup"] label, .stCheckbox { padding: 3px 0; }
      div[role="radiogroup"] label p, .stCheckbox label p,
      div[role="radiogroup"] label, .stCheckbox label { color: #27304a !important; }

      /* Barra lateral más limpia */
      section[data-testid="stSidebar"] { background: #ffffff; border-right: 1px solid #eceff5; }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------------------
# Estado de la sesión
# ---------------------------------------------------------------------------
def iniciar_estado(mezclar=False, orden=None, modo_repaso=False):
    """Reinicia el cuestionario activo. Si se pasa `orden`, usa ese subconjunto
    de preguntas (por ejemplo, para repasar solo las falladas)."""
    banco = BANCOS[st.session_state.banco_nombre]
    if orden is None:
        orden = list(range(len(banco)))
        if mezclar:
            random.shuffle(orden)
    st.session_state.orden = orden
    st.session_state.idx = 0
    st.session_state.aciertos = 0
    st.session_state.respondidas = 0
    st.session_state.comprobada = False
    st.session_state.ultimo_ok = None
    st.session_state.falladas = []          # índices reales de preguntas erradas
    st.session_state.modo_repaso = modo_repaso


# Cuestionario por defecto + primera inicialización
if "banco_nombre" not in st.session_state:
    st.session_state.banco_nombre = list(BANCOS.keys())[0]
if "orden" not in st.session_state:
    iniciar_estado(mezclar=False)


# ---------------------------------------------------------------------------
# Cabecera
# ---------------------------------------------------------------------------
st.markdown(
    """
    <div>
      <p class="greeting">📝 Test <span>RR.HH.</span></p>
      <p class="subtitle">Gestión de Personas y Comportamiento Organizacional</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Barra lateral: selección de cuestionario y controles ---
with st.sidebar:
    st.header("⚙️ Controles")

    nombres = list(BANCOS.keys())
    seleccion_banco = st.selectbox(
        "Elige el cuestionario:",
        nombres,
        index=nombres.index(st.session_state.banco_nombre),
    )
    if seleccion_banco != st.session_state.banco_nombre:
        st.session_state.banco_nombre = seleccion_banco
        iniciar_estado(mezclar=False)
        st.rerun()

    st.divider()

    if st.button("🔀 Mezclar y reiniciar", use_container_width=True):
        iniciar_estado(mezclar=True)
        st.rerun()
    if st.button("🔁 Reiniciar (en orden)", use_container_width=True):
        iniciar_estado(mezclar=False)
        st.rerun()

    st.divider()
    banco = BANCOS[st.session_state.banco_nombre]
    n_total = len(st.session_state.orden)
    st.progress(st.session_state.respondidas / n_total,
                text=f"Avance: {st.session_state.respondidas}/{n_total}")

# Banco activo (también disponible fuera del sidebar)
banco = BANCOS[st.session_state.banco_nombre]
n_total = len(st.session_state.orden)

# --- Quick Stats (datos reales del intento actual) ---
_aciertos = st.session_state.aciertos
_resp = st.session_state.respondidas
_pct = (_aciertos / _resp * 100) if _resp else 0
_restantes = n_total - _resp

st.markdown('<p class="section-title">Quick Stats</p>', unsafe_allow_html=True)


def _stat(ico, label, value, color, cbg):
    return (f'<div class="stat-card" style="--c:{color};--cb:{cbg}">'
            f'<div class="stat-ico" style="color:{color}">{ico}</div>'
            f'<div><div class="stat-label">{label}</div>'
            f'<div class="stat-value">{value}</div></div></div>')


_c1, _c2, _c3, _c4 = st.columns(4)
_c1.markdown(_stat("✅", "Aciertos", f"{_aciertos}/{_resp}", "#22c55e", "#e7f8ee"), unsafe_allow_html=True)
_c2.markdown(_stat("🎯", "Precisión", f"{_pct:.0f}%", "#8b5cf6", "#f0ebff"), unsafe_allow_html=True)
_c3.markdown(_stat("📊", "Avance", f"{_resp}/{n_total}", "#4f7cff", "#eaf0ff"), unsafe_allow_html=True)
_c4.markdown(_stat("📚", "Restantes", f"{_restantes}", "#fb923c", "#fff1e6"), unsafe_allow_html=True)

_modo = " · 🔁 Repaso de falladas" if st.session_state.get("modo_repaso") else ""
st.markdown(
    f'<p class="subtitle" style="margin-top:12px">Cuestionario activo: '
    f'<b style="color:#27304a">{st.session_state.banco_nombre}</b> · {n_total} preguntas{_modo}</p>',
    unsafe_allow_html=True,
)

# --- ¿Terminó el test? ---
if st.session_state.idx >= n_total:
    pct = (st.session_state.aciertos / n_total) * 100
    if pct >= 80:
        emoji, msg = "🏆", "¡Excelente dominio!"
    elif pct >= 50:
        emoji, msg = "💪", "¡Buen trabajo, sigue repasando!"
    else:
        emoji, msg = "📚", "A repasar un poco más."
    st.success(f"### ¡Test terminado! {emoji}\n\n"
               f"{msg}\n\n"
               f"Puntaje final: **{st.session_state.aciertos} / {n_total}**  "
               f"({pct:.1f}%)")

    falladas = st.session_state.get("falladas", [])
    if falladas:
        st.warning(f"Tuviste **{len(falladas)}** pregunta(s) incorrecta(s).")
        if st.button(f"🔁 Repasar mis {len(falladas)} preguntas falladas",
                     type="primary", use_container_width=True):
            iniciar_estado(orden=list(falladas), modo_repaso=True)
            st.rerun()

    if st.button("↩️ Volver a empezar (todo el cuestionario)", use_container_width=True):
        iniciar_estado(mezclar=False)
        st.rerun()
    st.stop()

# --- Pregunta actual ---
real_idx = st.session_state.orden[st.session_state.idx]
p = banco[real_idx]

# Tarjeta de pregunta con cabecera en degradado (color rotativo por pregunta)
tipo_badge = "Selección múltiple" if p["tipo"] == "multi" else "Una respuesta"
_paleta = [("#6a8dff", "#9b6bff"), ("#34d399", "#10b981"), ("#f472b6", "#a855f7"),
           ("#38bdf8", "#3b82f6"), ("#fbbf24", "#fb923c"), ("#fb7185", "#ef4444")]
_g0, _g1 = _paleta[st.session_state.idx % len(_paleta)]
st.markdown(
    f"""
    <div class="qcard">
      <div class="qhead" style="background:linear-gradient(120deg,{_g0},{_g1})">
        <span class="qbadge">Pregunta {st.session_state.idx + 1} de {n_total} · {tipo_badge}</span>
      </div>
      <div class="qbody">
        <div class="qtext">{p['pregunta']}</div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Clave única por pregunta para que el widget se "limpie" al avanzar
key = f"resp_{st.session_state.banco_nombre}_{st.session_state.idx}"

if p["tipo"] == "single":
    seleccion = st.radio("Selecciona una opción:", p["opciones"],
                         index=None, key=key, disabled=st.session_state.comprobada)
    seleccionadas = {seleccion} if seleccion is not None else set()
else:
    st.write("Selecciona **todas** las que correspondan:")
    seleccionadas = set()
    for i, op in enumerate(p["opciones"]):
        if st.checkbox(op, key=f"{key}_{i}", disabled=st.session_state.comprobada):
            seleccionadas.add(op)

# --- Botones comprobar / siguiente ---
col1, col2 = st.columns(2)

with col1:
    if not st.session_state.comprobada:
        if st.button("✅ Comprobar respuesta", type="primary", use_container_width=True):
            if not seleccionadas:
                st.warning("Selecciona al menos una opción antes de comprobar.")
            else:
                correctas = set(p["correctas"])
                ok = seleccionadas == correctas
                st.session_state.comprobada = True
                st.session_state.ultimo_ok = ok
                st.session_state.respondidas += 1
                if ok:
                    st.session_state.aciertos += 1
                else:
                    st.session_state.falladas.append(real_idx)
                st.rerun()

with col2:
    if st.session_state.comprobada:
        es_ultima = st.session_state.idx == n_total - 1
        etiqueta = "🏁 Ver resultado" if es_ultima else "➡️ Siguiente pregunta"
        if st.button(etiqueta, type="primary", use_container_width=True):
            st.session_state.idx += 1
            st.session_state.comprobada = False
            st.session_state.ultimo_ok = None
            st.rerun()

# --- Feedback tras comprobar ---
if st.session_state.comprobada:
    if st.session_state.ultimo_ok:
        st.success("¡Correcto! 🎯")
    else:
        st.error("Incorrecto.")
    correctas_txt = "\n".join(f"- {c}" for c in p["correctas"])
    st.info(f"**Respuesta(s) correcta(s):**\n{correctas_txt}")
    if p.get("explicacion"):
        st.markdown(f"> 💡 **Explicación:** {p['explicacion']}")
