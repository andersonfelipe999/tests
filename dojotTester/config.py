"""Environment configuration related module. """

import os

CONFIG = {
    'app': {
        'tenant': os.environ.get("TENANT", "automacao"),
        'passwd_keycloak': os.environ.get("PASSWD_KEYCLOAK", "master"),
        'user_keycloak': os.environ.get("USER_KEYCLOAK", "master"),    
    },

    'security': {
        'dns_cert': [],
        'ejbca_ca_name': "IOTmidCA",
        'cert_dir': os.environ.get("CERT_DIR", "resources/cert/"),
        'ca_cert_file': os.environ.get("CA_CERT_FILE", "ca.crt"),
    },

    'basic': {
        'url': os.environ.get("BASIC_URL", "http://localhost"),
        'port': int(os.environ.get("DOJOT_BASIC_PORT", 3002)),
    },

    'mqtt': {
        'host': os.environ.get("DOJOT_MQTT_HOST", "localhost"),
        'port': int(os.environ.get("DOJOT_MQTT_PORT", 1883)),
        'con_timeout': int(os.environ.get("DOJOT_MQTT_TIMEOUT", 120)),
        'qos': int(os.environ.get("DOJOT_MQTT_QOS", 0)),
    },
    
    'device_maneger': {
        'host': os.environ.get("DOJOT_MQTT_HOST", "localhost"),
        'url': os.environ.get("DOJOT_DEVICE_URL", "http://device-manager"),
        'port': int(os.environ.get("DOJOT_DEVICE_PORT", 5000)),
    },

    'http': {
        'host': os.environ.get("DOJOT_HOST", "localhost"),
        'url': os.environ.get("DOJOT_HTTP_URL", "http://localhost"),
        'port': int(os.environ.get("DOJOT_HTTP_PORT", 3001)),
        'con_timeout': int(os.environ.get("DOJOT_TIMEOUT", 120)),
    },

    'dojot': {
        'url': os.environ.get("DOJOT_URL", "http://localhost:8000"),
        'user': os.environ.get("DOJOT_USER", "admin"),
        'passwd': os.environ.get("DOJOT_PASSWD", "Dojot2022*"),
        'api': {
            'retries': int(os.environ.get("DOJOT_API_RETRIES", 3)),
            'time': float(os.environ.get("DOJOT_API_RETRY_TIME", 5000.0)) / 1000.0,
            'page_size': int(os.environ.get("DOJOT_DEVICES_PAGE_SIZE", 20))
        }
    },
    'log': {
        'level': os.environ.get("LOG_LEVEL", "info")
    }
}
