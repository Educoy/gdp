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
# Cuestionarios disponibles
# ---------------------------------------------------------------------------
BANCOS = {
    "📘 Test RR.HH. (60 preguntas)": PREGUNTAS,
    "📗 Guía de Estudio del Certamen": PREGUNTAS_GUIA,
    "📕 Guía — Nivel Avanzado": PREGUNTAS_GUIA_AVANZADO,
}


# ---------------------------------------------------------------------------
# Configuración de la página + estilos
# ---------------------------------------------------------------------------
st.set_page_config(page_title="Test RR.HH.", page_icon="📝", layout="centered")

st.markdown(
    """
    <style>
      /* Fondo general */
      .stApp {
          background: linear-gradient(160deg, #eef2ff 0%, #f8fafc 45%, #ffffff 100%);
      }
      /* Banner de título */
      .hero {
          background: linear-gradient(120deg, #4f46e5 0%, #7c3aed 50%, #2563eb 100%);
          padding: 26px 30px;
          border-radius: 18px;
          color: #ffffff;
          box-shadow: 0 10px 30px rgba(79,70,229,0.25);
          margin-bottom: 18px;
      }
      .hero h1 { color:#fff; margin:0; font-size: 2rem; }
      .hero p  { color:#e0e7ff; margin:6px 0 0 0; font-size: 0.98rem; }

      /* Tarjeta de pregunta */
      .qcard {
          background:#ffffff;
          border:1px solid #e5e7eb;
          border-left:6px solid #6366f1;
          border-radius:14px;
          padding:18px 22px;
          box-shadow:0 4px 14px rgba(0,0,0,0.05);
          margin-bottom:10px;
      }
      .qcard .qnum {
          display:inline-block;
          background:#eef2ff;
          color:#4338ca;
          font-weight:600;
          font-size:0.8rem;
          padding:3px 12px;
          border-radius:999px;
          margin-bottom:10px;
      }
      .qcard .qtext { font-size:1.12rem; font-weight:600; color:#1e293b; line-height:1.4; }

      /* Botones */
      .stButton > button {
          border-radius:10px;
          font-weight:600;
          border:none;
          transition:transform .05s ease, box-shadow .2s ease;
      }
      .stButton > button:hover { transform:translateY(-1px); }

      /* Barra de progreso más marcada */
      .stProgress > div > div > div > div { background:linear-gradient(90deg,#6366f1,#8b5cf6); }

      /* Radios y checkboxes con un poco más de aire y texto siempre oscuro */
      div[role="radiogroup"] label, .stCheckbox { padding:2px 0; }
      div[role="radiogroup"] label p,
      .stCheckbox label p,
      div[role="radiogroup"] label,
      .stCheckbox label { color:#1e293b !important; }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------------------
# Estado de la sesión
# ---------------------------------------------------------------------------
def iniciar_estado(mezclar=False):
    """Reinicia el cuestionario activo desde cero."""
    banco = BANCOS[st.session_state.banco_nombre]
    orden = list(range(len(banco)))
    if mezclar:
        random.shuffle(orden)
    st.session_state.orden = orden
    st.session_state.idx = 0
    st.session_state.aciertos = 0
    st.session_state.respondidas = 0
    st.session_state.comprobada = False
    st.session_state.ultimo_ok = None


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
    <div class="hero">
      <h1>📝 Test RR.HH.</h1>
      <p>Gestión de Personas y Comportamiento Organizacional</p>
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
    total = len(banco)
    st.metric("Aciertos", f"{st.session_state.aciertos} / {st.session_state.respondidas}")
    st.progress(st.session_state.respondidas / total,
                text=f"Avance: {st.session_state.respondidas}/{total}")

# Banco activo (también disponible fuera del sidebar)
banco = BANCOS[st.session_state.banco_nombre]

st.caption(f"Cuestionario activo: **{st.session_state.banco_nombre}** · {len(banco)} preguntas")

# --- ¿Terminó el test? ---
if st.session_state.idx >= len(banco):
    pct = (st.session_state.aciertos / len(banco)) * 100
    if pct >= 80:
        emoji, msg = "🏆", "¡Excelente dominio!"
    elif pct >= 50:
        emoji, msg = "💪", "¡Buen trabajo, sigue repasando!"
    else:
        emoji, msg = "📚", "A repasar un poco más."
    st.success(f"### ¡Test terminado! {emoji}\n\n"
               f"{msg}\n\n"
               f"Puntaje final: **{st.session_state.aciertos} / {len(banco)}**  "
               f"({pct:.1f}%)")
    if st.button("↩️ Volver a empezar", type="primary"):
        iniciar_estado(mezclar=False)
        st.rerun()
    st.stop()

# --- Pregunta actual ---
real_idx = st.session_state.orden[st.session_state.idx]
p = banco[real_idx]

# Tarjeta de pregunta
tipo_badge = "Selección múltiple" if p["tipo"] == "multi" else "Una respuesta"
st.markdown(
    f"""
    <div class="qcard">
      <span class="qnum">Pregunta {st.session_state.idx + 1} de {len(banco)} · {tipo_badge}</span>
      <div class="qtext">{p['pregunta']}</div>
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
                st.rerun()

with col2:
    if st.session_state.comprobada:
        es_ultima = st.session_state.idx == len(banco) - 1
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
