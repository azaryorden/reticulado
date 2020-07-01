def generate_jimmy_page(content):
    with open ("templates/index.html", "w") as o:
        o.write(content)

content = "<!doctype html> <html lang=es> <meta charset=utf-8>"

content += "<title> Reticulado </title>"

persona = {"nombre" : "Mer",
           "edad" : "33",
           "color_fav" : "verde"}

def dicc_to_html(dix):
    html = "<table> <caption> El diccionario de Mercedes"
    for k, v in dix.items():
        html += "<tr>"
        html += "<td>" + k + "<td>" + str(v)
    return html

content += dicc_to_html(persona)

generate_jimmy_page(content)
