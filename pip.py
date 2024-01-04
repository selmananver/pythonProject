


import pdfkit
config =pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
pdfkit.from_url("http://google.com","google.pdf",configuration=config)