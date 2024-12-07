
import markdown
import webbrowser
import os

def main():
    # Especifica la ruta del archivo Markdown aquí
    input_filename = r"C:\Users\jairc\Downloads\rag\curso\unidad 4\3 Propiedades de transporte.md"

    # Verifica si el archivo existe
    if not os.path.isfile(input_filename):
        print(f"El archivo {input_filename} no existe.")
        return

    # Leer el archivo Markdown
    with open(input_filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # Convertir Markdown a HTML
    html = markdown.markdown(text, extensions=['extra', 'codehilite'])

    # Plantilla HTML que incluye MathJax con configuración personalizada
    html_template = '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{title}</title>
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script>
  window.MathJax = {{
    tex: {{
      inlineMath: [['$','$'], ['\\(','\\)']],
      displayMath: [['$$','$$'], ['\\[','\\]']]
    }},
    svg: {{
      fontCache: 'global'
    }}
  }};
</script>
<script id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js">
</script>
</head>
<body>
{content}
</body>
</html>
'''

    html_output = html_template.format(title=os.path.basename(input_filename), content=html)

    # Escribir el HTML en un archivo
    output_filename = os.path.splitext(input_filename)[0] + '.html'
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(html_output)

    # Abrir el archivo HTML en el navegador web predeterminado
    webbrowser.open('file://' + os.path.realpath(output_filename))

if __name__ == '__main__':
    main()
