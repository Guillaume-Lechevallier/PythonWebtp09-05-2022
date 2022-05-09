import web
import xml.etree.ElementTree as ET
import os




# Generating routes
urls = (
    '/c=(.*)', 'Celsus',
    '/f=(.*)', 'Fahrenheit',
    '/k=(.*)', 'Kelvin',
    '(.*)', 'Error',
)
app = web.application(urls, globals())


class Celsus:
    def GET(self, value):
        os.remove("temp_data.xml")
        open("temp_data.xml", "a").write("<temperature></temperature>")

        tree = ET.parse('temp_data.xml')
        root = tree.getroot()
        valuecelsus = int(value)
        valuefahrenheit = int(value)*1.8+32
        valuekelvin = int(value)-273.5
        ET.SubElement(root, "Celsus").text = str(valuecelsus)
        ET.SubElement(root, "Fahrenheit").text = str(valuefahrenheit)
        ET.SubElement(root, "Kelvin").text = str(valuekelvin)

        tree = ET.ElementTree(root)

        tree.write("temp_data.xml")
        return ET.tostring(tree.getroot())


class Fahrenheit:
    def GET(self, value):

        os.remove("temp_data.xml")
        open("temp_data.xml", "a").write("<temperature></temperature>")

        tree = ET.parse('temp_data.xml')
        root = tree.getroot()
        valuecelsus = (int(value) - 32) / 1.8
        valuefahrenheit = int(value)
        valuekelvin = (int(value)+ 459.67) * 5/9
        ET.SubElement(root, "Celsus").text = str(valuecelsus)
        ET.SubElement(root, "Fahrenheit").text = str(valuefahrenheit)
        ET.SubElement(root, "Kelvin").text = str(valuekelvin)

        tree = ET.ElementTree(root)

        tree.write("temp_data.xml")
        return ET.tostring(tree.getroot())



class Kelvin:
    def GET(self, value):

        os.remove("temp_data.xml")
        open("temp_data.xml", "a").write("<temperature></temperature>")

        tree = ET.parse('temp_data.xml')
        root = tree.getroot()
        valuecelsus = int(value)+273.5
        valuefahrenheit = int(value)*9/5 - 459.67
        valuekelvin = int(value)
        ET.SubElement(root, "Celsus").text = str(valuecelsus)
        ET.SubElement(root, "Fahrenheit").text = str(valuefahrenheit)
        ET.SubElement(root, "Kelvin").text = str(valuekelvin)

        tree = ET.ElementTree(root)

        tree.write("temp_data.xml")
        return ET.tostring(tree.getroot())



class Error:
    def GET(self, value):

        os.remove("temp_data.xml")
        open("temp_data.xml", "a").write("<temperature></temperature>")

        tree = ET.parse('temp_data.xml')
        root = tree.getroot()

        ET.SubElement(root, "Error").text = str("Error")

        tree = ET.ElementTree(root)

        tree.write("temp_data.xml")
        return ET.tostring(tree.getroot())



if __name__ == "__main__":
    app.run()
