from pickletools import string1
from dojot.api import DojotAPI as Api
from mqtt.mqttClient import MQTTClient
import json
import random
import datetime
import time
import requests
from config import CONFIG

from dojotTester import ROOT_DIR

from common.testutils import *
from common.certUtils import *
from common.base_test import BaseTest
from iotAgentHttp.httpClient import HTTPSClient


class SanityTest(BaseTest):
    """
    Cria templates:
        - medidor de temperatura
        - medidor de pressao
        - medidor de umidade relativa
        - medidor de velocidade
        - protocolo
        - onibus
        - controladores
        - TesteTemplate
        - CameraTemplate
        - MedidorChuva
        - MedidorNivel
        - logger
        - CameraTemplateQualcomm
        - ObterAcesso
        - Token
    """
    def createTemplates(self, jwt: str, templates: list):
        template_ids = []
        for template in templates:
            rc, template_id = Api.create_template(jwt, json.dumps(template))

            template_ids.append(template_id["template"]["id"]) if rc == 200 else template_ids.append(None)

            

        return template_ids

    def createDevices(self, jwt: str, devices: list):
        device_ids = []

        for templates, label in devices:
            self.logger.info('adding device ' + label + ' using templates ' + str(templates))
            rc, device_id = Api.create_device(jwt, templates, label)
            self.assertTrue(device_id is not None, "Error on create device")
            device_ids.append(device_id) if rc == 200 else device_ids.append(None)
        return device_ids



    def runTest(self):
        self.logger.info('Sanity test')
        time.sleep(30)
            
        self.logger.debug('Obtenção do token...')
        jwt = Api.get_jwt()

        templates = []
        self.logger.info('Criação dos templates...')
        templates.append({
            "label": "medidor de temperatura",
            "attrs": [
                {
                    "label": "temperatura",
                    "type": "dynamic",
                    "value_type": "float",
                    "metadata": [{"label": "unidade", "type": "meta", "value_type": "string", "static_value": "°C"}]
                }
            ]
        })
        templates.append({
            "label": "medidor de pressao",
            "attrs": [
                {
                    "label": "SerialNumber",
                    "type": "static",
                    "value_type": "string",
                    "static_value": "undefined"
                },
                {
                    "label": "pressao",
                    "type": "dynamic",
                    "value_type": "float",
                    "metadata": [{"label": "unidade", "type": "meta", "value_type": "string", "static_value": "mmHg"}]
                }
            ]
        })
        templates.append({
            "label": "medidor de umidade relativa",
            "attrs": [
                {
                    "label": "umidade",
                    "type": "dynamic",
                    "value_type": "float",
                    "metadata": [{"label": "unidade", "type": "meta", "value_type": "string", "static_value": "%"}]
                }
            ]
        })
        templates.append({
            "label": "medidor de velocidade",
            "attrs": [
                {
                    "label": "velocidade",
                    "type": "dynamic",
                    "value_type": "float",
                    "metadata": [{"label": "unidade", "type": "meta", "value_type": "string", "static_value": "km/h"}]
                }
            ]
        })
        templates.append({
            "label": "protocolo",
            "attrs": [
                {
                    "label": "protocol",
                    "static_value": "mqtt",
                    "type": "static",
                    "value_type": "string"
                }
            ]
        })
        templates.append({
            "label": "onibus",
            "attrs": [
                {
                    "label": "velocidade",
                    "metadata": [
                        {"label": "unidade", "type": "meta", "value_type": "string", "static_value": "km/h"}],
                    "type": "dynamic",
                    "value_type": "float"
                },
                {
                    "label": "passageiros",
                    "type": "dynamic",
                    "value_type": "integer"
                },
                {
                    "label": "carro",
                    "type": "static",
                    "value_type": "string",
                    "static_value": "indefinido"
                },
                {
                    "label": "gps",
                    "type": "dynamic",
                    "value_type": "geo:point"
                },
                {
                    "label": "operacional",
                    "type": "dynamic",
                    "value_type": "boolean"
                },
                {
                    "label": "mensagem",
                    "type": "dynamic",
                    "value_type": "string"
                },
                {
                    "label": "protocol",
                    "static_value": "mqtt",
                    "type": "static",
                    "value_type": "string"
                },
                {
                    "label": "device_timeout",
                    "static_value": "10000",
                    "type": "static",
                    "value_type": "string"
                },
                {
                    "label": "letreiro",
                    "static_value": "",
                    "type": "actuator",
                    "value_type": "string"
                }
            ]
        })
        templates.append({
            "label": "controladores",
            "attrs": [
                {
                    "label": "mensagem",
                    "type": "dynamic",
                    "value_type": "string"
                },
                {
                    "label": "medida",
                    "type": "dynamic",
                    "value_type": "float"
                },
                {
                    "label": "display",
                    "static_value": "",
                    "type": "actuator",
                    "value_type": "string"
                },
                {
                    "label": "objeto",
                    "static_value": "",
                    "type": "actuator",
                    "value_type": "object"
                }
            ]
        })
        templates.append({
            "label": "TesteTemplate",
            "attrs": [
                {
                    "label": "float",
                    "type": "dynamic",
                    "value_type": "float"
                },
                {
                    "label": "int",
                    "type": "dynamic",
                    "value_type": "integer"
                },
                {
                    "label": "str",
                    "type": "dynamic",
                    "value_type": "string"
                },
                {
                    "label": "gps",
                    "type": "dynamic",
                    "value_type": "geo:point",
                    "metadata": [
                        {"label": "unidade", "type": "meta", "value_type": "string", "static_value": "decimal"},
                        {"label": "descricao", "type": "meta", "value_type": "string", "static_value": "localização do dispositivo"}
                    ]
                },
                {
                    "label": "bool",
                    "type": "dynamic",
                    "value_type": "boolean"
                },
                {
                    "label": "serial",
                    "type": "static",
                    "value_type": "string",
                    "static_value": "indefinido"
                },
                {
                    "label": "mensagem",
                    "static_value": "",
                    "type": "actuator",
                    "value_type": "string"
                },
                {
                    "label": "protocol",
                    "static_value": "mqtt",
                    "type": "static",
                    "value_type": "string"
                }
            ]
        })
        templates.append({
            "label": "CameraTemplate",
            "attrs": [
                {"label": "license_plate", "type": "dynamic", "value_type": "string"},
                {"label": "band", "type": "dynamic", "value_type": "integer"},
                {"label": "coordinates", "type": "dynamic", "value_type": "string"},
                {"label": "vehicle_type", "type": "dynamic", "value_type": "string"},
                {"label": "timestamp", "type": "dynamic", "value_type": "integer"}
            ]
        })
        templates.append({
            "label": "MedidorChuva",
            "attrs": [
                {
                    "label": "chuva",
                    "type": "dynamic",
                    "value_type": "float"
                }
            ]
        })
        templates.append({
            "label": "MedidorNivel",
            "attrs": [
                {
                    "label": "nivel",
                    "type": "dynamic",
                    "value_type": "float"
                }
            ]
        })
        templates.append({
            "label": "logger",
            "attrs": [
                {
                    "label": "data",
                    "type": "dynamic",
                    "value_type": "object"
                },
                {
                    "label": "metadata",
                    "type": "dynamic",
                    "value_type": "object"
                }
            ]
        })
        templates.append({
            "label": "ObterAcesso",
            "attrs": [
                {
                    "label": "username",
                    "type": "dynamic",
                    "value_type": "string"
                },
                {
                    "label": "passwd",
                    "type": "dynamic",
                    "value_type": "string"
                }
            ]
        })
        templates.append({
            "label": "Token",
            "attrs": [
                {
                    "label": "json",
                    "type": "dynamic",
                    "value_type": "object"
                },
                {
                    "label": "jwt",
                    "type": "dynamic",
                    "value_type": "string"
                }
            ]
        })
        templates.append({
            "label": "CameraTemplateQualcomm",
            "attrs": [
                {"label": "license_plate", "type": "dynamic", "value_type": "string"},
                {"label": "band", "type": "dynamic", "value_type": "integer"},
                {"label": "coordinates", "type": "dynamic", "value_type": "geo:point"},
                {"label": "vehicle_type", "type": "dynamic", "value_type": "string"},
                {"label": "timestamp", "type": "dynamic", "value_type": "integer"}
            ]
        })

        template_ids = self.createTemplates(jwt, templates)
        self.logger.info("Templates criados. IDs: " + str(template_ids))

        devices = []
        self.logger.info('Criação dos devices...')
        devices.append(([template_ids[0], template_ids[4]], "termometro Celsius"))
        devices.append(([template_ids[0], template_ids[4]], "termometro Kelvin"))
        devices.append(([template_ids[1], template_ids[4]], "barometro"))
        devices.append(([template_ids[2], template_ids[4]], "higrometro"))
        devices.append(([template_ids[3], template_ids[4]], "anemometro"))
        devices.append(([template_ids[0], template_ids[1], template_ids[2], template_ids[3]], "instrumento de medicao"))
        devices.append(([template_ids[5]], "linha_1"))
        devices.append(([template_ids[5]], "linha_2"))
        devices.append(([template_ids[5]], "linha_3"))
        devices.append(([template_ids[6]], "controle"))
        devices.append(([template_ids[7]], "device"))
        devices.append(([template_ids[7]], "dispositivo"))
        devices.append(([template_ids[8]], "Camera1"))
        devices.append(([template_ids[9]], "Pluviometro"))
        devices.append(([template_ids[10]], "SensorNivel"))
        devices.append(([template_ids[11]], "logger"))
        devices.append(([template_ids[12]], "acesso"))
        devices.append(([template_ids[13]], "token"))
        devices.append(([template_ids[14]], "CameraQualcomm"))

        devices_ids = self.createDevices(jwt, devices)
        self.logger.info("Devices created. IDs: " + str(devices_ids))
        
        

        # publicações
        
        dev_id = Api.get_deviceid_by_label(jwt, "linha_1")
        dev_topic = CONFIG['app']['tenant'] + ":" + dev_id + "/attrs"
        dev = MQTTClient(dev_id)
        self.logger.info("publicando com dispositivo: " + dev_id + ", linha_1")
        rc = dev.publish(dev_topic,
                     {"gps":"-22.890970, -47.063006","velocidade":50,"passageiros":30,"operacional":False})
        self.logger.debug("rc: " + str(rc))
        self.assertTrue(rc == 0, "** FAILED ASSERTION: received an unexpected result code: " + str(rc) + " **")

        time.sleep(3)

        dev.publish(dev_topic,
                     {"gps":"-22.893619, -47.052921","velocidade":40,"passageiros":45,"operacional":True})

        time.sleep(3)


        dev_id = Api.get_deviceid_by_label(jwt, "dispositivo")
        dev_topic = CONFIG['app']['tenant'] + ":" + dev_id + "/attrs"
        dev = MQTTClient(dev_id)
        self.logger.info("publicando com dispositivo: " + dev_id + ", dispositivo")
        dev.publish(dev_topic, {"int": 2, "bool": True})

        time.sleep(3)

        dev_id = Api.get_deviceid_by_label(jwt, "device")
        dev_topic = CONFIG['app']['tenant'] + ":" + dev_id + "/attrs"
        dev = MQTTClient(dev_id)
        self.logger.info("publicando com dispositivo: " + dev_id + ", device")
        dev.publish(dev_topic, {"int": 1, "bool": True})

        time.sleep(3)

        dev_id = Api.get_deviceid_by_label(jwt, "anemometro")
        dev_topic = CONFIG['app']['tenant'] + ":" + dev_id + "/attrs"
        dev = MQTTClient(dev_id)
        self.logger.info("publicando com dispositivo: " + dev_id + ", anemometro")
        dev.publish(dev_topic, {"velocidade": 50})

        time.sleep(3)

        dev_id = Api.get_deviceid_by_label(jwt, "barometro")
        dev_topic = CONFIG['app']['tenant'] + ":" + dev_id + "/attrs"
        dev = MQTTClient(dev_id)
        self.logger.info("publicando com dispositivo: " + dev_id + ", barometro")
        dev.publish(dev_topic, {"pressao": 0.9})

        time.sleep(3)

        dev_id = Api.get_deviceid_by_label(jwt, "higrometro")
        dev_topic = CONFIG['app']['tenant'] + ":" + dev_id + "/attrs"
        dev = MQTTClient(dev_id)
        self.logger.info("publicando com dispositivo: " + dev_id + ", higrometro")
        dev.publish(dev_topic, {"umidade": 15})

        time.sleep(3)

        dev.publish(dev_topic, {"umidade": 21})

        time.sleep(3)

        dev_id = Api.get_deviceid_by_label(jwt, "termometro Celsius")
        dev_topic = CONFIG['app']['tenant'] + ":" + dev_id + "/attrs"
        dev = MQTTClient(dev_id)
        self.logger.info("publicando com dispositivo: " + dev_id + ", termometro Celsius")
        dev.publish(dev_topic, {"temperatura": 30})

        time.sleep(3)

        dev_id = Api.get_deviceid_by_label(jwt, "Pluviometro")
        dev_topic = CONFIG['app']['tenant'] + ":" + dev_id + "/attrs"
        dev = MQTTClient(dev_id)
        self.logger.info("publicando com dispositivo: " + dev_id + ", Pluviometro")
        dev.publish(dev_topic, {"chuva": 5})

        time.sleep(5)


        self.logger.info("publicando com dispositivo: " + dev_id + ", Pluviometro")
        dev.publish(dev_topic, {"chuva": 6})

        time.sleep(5)

        self.logger.info("publicando com dispositivo: " + dev_id + ", Pluviometro")
        dev.publish(dev_topic, {"chuva": 10})

        time.sleep(5)

        dev_id = Api.get_deviceid_by_label(jwt, "SensorNivel")

        dev_topic = CONFIG['app']['tenant'] + ":" + dev_id + "/attrs"
        self.logger.info("publicando com dispositivo: " + dev_id + ", SensorNivel")
        dev.publish(dev_topic, {"nivel": 1})
        time.sleep(5)

        dev_id = Api.get_deviceid_by_label(jwt, "linha_2")
        dev_topic = CONFIG['app']['tenant'] + ":" + dev_id + "/attrs"
        dev = MQTTClient(dev_id)
        self.logger.info("publicando com dispositivo: " + dev_id + ", linha_2")
        dev.publish(dev_topic, {"velocidade": 60})

        time.sleep(3)   


        # TESTE HTTP AGENT 
        self.logger.info("Starting Http Agent Insecure Mode")
        dev_id = add_a_simple_device(self, jwt)
        

        publish_http_agent = Api.publish_http_agent_insegure_mode_simple_device(jwt,dev_id)
        self.assertTrue(publish_http_agent == 204, "Invalid Code")
        self.logger.info('Device created : ' + dev_id)

        dev_id = Api.get_deviceid_by_label(jwt, "token")
        publish_http_agent = Api.publish_http_agent_insegure_mode_device_token(jwt,dev_id)
        self.assertTrue(publish_http_agent == 204, "Invalid Code")
        self.logger.info('Device created : ' + dev_id)


        dev_id = Api.get_deviceid_by_label(jwt, "linha_1")
        publish_http_agent = Api.publish_http_agent_insegure_mode_device_linha_1_bool(jwt,dev_id)
        self.assertTrue(publish_http_agent == 204, "Invalid Code")
        self.logger.info('Device created : ' + dev_id)


        publish_http_agent = Api.publish_http_agent_insegure_mode_device_linha_1_geo(jwt,dev_id)
        self.assertTrue(publish_http_agent == 204, "Invalid Code")
        self.logger.info('Device created : ' + dev_id)

        self.logger.info("Finished Http Agent ...")
        time.sleep(3)    

        self.logger.info("Starting test Cron")

        # Criação broker job
        current_time = int(time.time() * 1000)

        dev_id = Api.get_deviceid_by_label(jwt, "dispositivo")
        self.logger.info('creating cron jobs - EventRequest...' + str(dev_id))
        data = {
            "time": "*/1 * * * *",
            "timezone": "America/Sao_Paulo",
            "name": "Keep alive",
            "description": "This job sends a keep alive notification to a device every 1 minutes",
            "broker": {
                "subject": "dojot.device-manager.device.actuation",
                "message": {
                    "event": "configure",
                    "data": {
                        "attrs": {"mensagem": "keep alive"},
                        "id": str(dev_id)
                    },
                    "meta": {
                        "service": CONFIG['app']['tenant'],
                        "timestamp": str(current_time)
                    }
                }
            }
        }
        self.logger.info('data: ' + str(data))
        rc, res = Api.create_cron_job(jwt, str(dev_id), json.dumps(data))
        self.logger.info('Result: ' + str(res))

        self.assertTrue(int(rc) == 201, "codigo inesperado")


        # Criação http job
        dev_id = Api.get_deviceid_by_label(jwt, "device")
        self.logger.info("creating cron jobs - HTTPRequest..." + str(dev_id))
        data = {
            "time": "*/1 * * * *",
            "timezone": "America/Sao_Paulo",
            "name": "Keep alive",
            "description": "This job sends a keep alive notification to a device every 1 minutes",
            "http": {
                "method": "PUT",
                "headers": {
                    "Authorization": "Bearer " + str(jwt),
                    "Content-Type": "application/json"
                    },
                "url": "{0}:{1}/device/{2}/actuate".format(CONFIG['device_maneger']['url'],CONFIG['device_maneger']['port'],dev_id),
                "body": {
                    "attrs": {
                        "mensagem": "keep alive"
                    }
                    }
                }
            }
        self.logger.info('\n\ndata: ' + str(data))

        rc, res = Api.create_cron_job(jwt, str(dev_id), json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 201, "codigo inesperado")

        #CHECANDO OS AGENDAMENTOS DO CRON

        self.logger.info('Checando os agendamentos')

        rc, res = Api.get_cron_jobs(jwt)
        self.logger.info('\n\nResult: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        #Removendo os agendamentos 
        self.logger.info('Removendo os agendamentos')
        rc, res = Api.remove_cron_jobs(jwt)
        self.logger.info("Result: " + str(res))
        self.assertTrue(rc == 204, "** FAILED ASSERTION: Unexpected count value")

        #RETRIVER
        
        self.logger.info("Validação dos dados...")

        dev_id = Api.get_deviceid_by_label(jwt, "linha_1")
        rc, count = get_retriever_count_attr(self, jwt, dev_id, "velocidade")
        self.assertTrue(rc == 200, "** FAILED ASSERTION: received an unexpected result code: " + str(rc) + " **")
        self.assertTrue(count == 2, "** FAILED ASSERTION: Unexpected count value: " + str(count) + " **")

        time.sleep(3)

        rc, count = get_retriever_count_attr(self, jwt, dev_id, "gps")
        self.logger.info("total de registros: " + str(count))
        self.assertTrue(count == 2, "** FAILED ASSERTION: received an unexpected count **")
        time.sleep(3)


        dev_id = Api.get_deviceid_by_label(jwt, "dispositivo")
        rc, count = get_retriever_count_attr(self, jwt, dev_id, "int")
        self.logger.info("total de registros: " + str(count))
        self.assertTrue(count == 1, "** FAILED ASSERTION: received an unexpected count **")

        dev_id = Api.get_deviceid_by_label(jwt, "anemometro")
        rc, count = get_retriever_count_attr(self, jwt, dev_id, "velocidade")
        self.logger.info("total de registros: " + str(count))
        self.assertTrue(count == 1, "** FAILED ASSERTION: received an unexpected count **")
        time.sleep(3)

        dev_id = Api.get_deviceid_by_label(jwt, "barometro")
        rc, count = get_retriever_count_attr(self, jwt, dev_id, "pressao")
        self.logger.info("total de registros: " + str(count))
        self.assertTrue(count == 1, "** FAILED ASSERTION: received an unexpected count **")
        time.sleep(3)

        dev_id = Api.get_deviceid_by_label(jwt, "higrometro")
        rc, count = get_retriever_count_attr(self, jwt, dev_id, "umidade")
        self.logger.info("total de registros: " + str(count))
        self.assertTrue(count == 2, "** FAILED ASSERTION: received an unexpected count **")
        time.sleep(3)

        dev_id = Api.get_deviceid_by_label(jwt, "termometro Celsius")
        rc, count = get_retriever_count_attr(self, jwt, dev_id, "temperatura")
        self.logger.info("total de registros: " + str(count))
        self.assertTrue(count == 1, "** FAILED ASSERTION: received an unexpected count **")
        time.sleep(3)

        dev_id = Api.get_deviceid_by_label(jwt, "device")
        rc, count = get_retriever_count_attr(self, jwt, dev_id, "bool")
        self.logger.info("total de registros: " + str(count))
        self.assertTrue(count == 1, "** FAILED ASSERTION: received an unexpected count **")
        time.sleep(3)

        dev_id = Api.get_deviceid_by_label(jwt, "dispositivo")
        rc, res = get_retriever_count_attr(self, jwt, dev_id, "bool")
        self.logger.info("total de registros: " + str(count))
        self.assertTrue(count == 1, "** FAILED ASSERTION: received an unexpected count **")

        time.sleep(3)

        dev_id = Api.get_deviceid_by_label(jwt, "Pluviometro")
        rc, count = get_retriever_count_attr(self, jwt, dev_id, "chuva")
        self.logger.info("total de registros: " + str(count))
        self.assertTrue(count == 3, "** FAILED ASSERTION: received an unexpected count **")

        time.sleep(3)

        dev_id = Api.get_deviceid_by_label(jwt, "SensorNivel")
        rc, count = get_retriever_count_attr(self, jwt, dev_id, "nivel")
        self.assertTrue(count == 3, "** FAILED ASSERTION: received an unexpected count **")
        self.logger.info("total de registros: " + str(count))

        time.sleep(3)

        dev_id = Api.get_deviceid_by_label(jwt, "linha_2")
        rc, count = get_retriever_count_attr(self, jwt, dev_id, "velocidade")
        self.logger.info("total de registros: " + str(count))
        self.assertTrue(count == 1, "** FAILED ASSERTION: received an unexpected count **")

        time.sleep(3)
        
    
        # create device linha_4
        self.logger.info('Criação do device linha_4...')
        rc, res = Api.create_device(jwt, [template_ids[5]], "linha_4")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        time.sleep(3)

        # update device linha_4
        dev_id = Api.get_deviceid_by_label(jwt, "linha_4")
        self.logger.info('Atualização do device linha_4...' + str(dev_id))
        data = {"templates": [template_ids[5]], "label": "update_linha_4"}
        rc, res = Api.update_device(jwt, str(dev_id), json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

        # delete device linha_4
        device_id = Api.get_deviceid_by_label(jwt, "update_linha_4")
        self.logger.info('Remoção do device update_linha_4...')
        rc, res = Api.delete_device(jwt, str(device_id))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")


        self.logger.info('http-agent test...')

        device_id, _ = create_a_device_and_its_certificate(self, jwt)

        dev1 = HTTPSClient(device_id)

        payload = {"temperature": 90}
        rc, res = dev1.publish(payload)
        self.assertTrue(rc == 204,
                        "** FAILED ASSERTION: Unexpected result code value: " + str(rc) + ". Body: " + str(res))
        # waiting to process
        self.logger.info('Esperando o dado ser armazenado no influxdb')
        time.sleep(10)

        self.logger.info('Checando se o dado foi publicado')
        rc, count = get_retriever_count_attr(self, jwt, device_id, "temperature")
        self.logger.info("total de registros: " + str(count) + ", " + str(device_id))
        self.assertTrue(count == 1, "** FAILED ASSERTION: Unexpected count value")

        #File Mgmt


        self.logger.info("file-mgmt test...")

        file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(file))

        path = "arquivos/arquivo.txt"

        rc, res = Api.upload_file(jwt, file, path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "codigo inesperado")

        rc, res = Api.list_stored_files(jwt, 10)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "codigo inesperado")
