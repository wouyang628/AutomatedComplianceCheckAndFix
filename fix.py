import jinja2
import os
import csv
from jnpr.junos import Device
from jnpr.junos.utils.config import Config


env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."))
template_file = "junos-isis.j2"
template = env.get_template(template_file)


with open('testing') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
      if line_count > 2:
        #print "c0: " + row[0] + "     c1: " + row[2]
        hostname = row[2]
        interfaces = row[0]
        #print(interfaces)
        interfaces = interfaces[1:-1]
        #print(interfaces)
        interfaces = [x.strip() for x in interfaces.split(',')]
        #print(interfaces)
        config = {
            'interfaces': interfaces,
        }
        configlet = template.render(config)
        print("FIXING " + hostname)
        print(configlet)
        dev = Device(host=hostname,user='northstar', password='Embe1mpls').open()
        with Config(dev) as cu:
            cu.load(configlet)
            cu.commit()
        dev.close()
        #print(configlet)
      else:
        line_count += 1

