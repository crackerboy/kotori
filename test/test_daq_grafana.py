# -*- coding: utf-8 -*-
# (c) 2020-2021 Andreas Motl <andreas@getkotori.org>
import logging

import pytest
import pytest_twisted

from test.settings.mqttkit import settings, grafana, PROCESS_DELAY
from test.util import mqtt_json_sensor, sleep

logger = logging.getLogger(__name__)


@pytest_twisted.inlineCallbacks
@pytest.mark.grafana
def test_mqtt_to_grafana_single(machinery, create_influxdb, reset_influxdb, reset_grafana):
    """
    Publish single reading in JSON format to MQTT broker and proof
    that a corresponding datasource and a dashboard was created in Grafana.
    """

    # Submit a single measurement, without timestamp.
    data = {
        'temperature': 42.84,
        'humidity': 83.1,
    }
    yield mqtt_json_sensor(settings.mqtt_topic_json, data)

    # Wait for some time to process the message.
    yield sleep(PROCESS_DELAY)
    yield sleep(PROCESS_DELAY)
    yield sleep(PROCESS_DELAY)

    # Proof that Grafana is well provisioned.
    logger.info('Grafana: Checking datasource')
    datasource_names = []
    for datasource in grafana.client.datasources.get():
        datasource_names.append(datasource['name'])
    assert settings.influx_database in datasource_names

    logger.info('Grafana: Checking dashboard')
    dashboard_name = settings.grafana_dashboards[0]
    dashboard = grafana.client.dashboards.db[dashboard_name].get()
    target = dashboard['dashboard']['rows'][0]['panels'][0]['targets'][0]
    assert target['measurement'] == settings.influx_measurement_sensors
    assert 'temperature' in target['query'] or 'humidity' in target['query']


@pytest_twisted.inlineCallbacks
@pytest.mark.grafana
def test_mqtt_to_grafana_bulk(machinery, create_influxdb, reset_influxdb, reset_grafana):
    """
    Publish multiple readings in JSON format to MQTT broker and proof
    that a corresponding datasource and a dashboard was created in Grafana.
    """

    # Submit multiple measurements, without timestamp.
    data = [
        {
            'temperature': 21.42,
            'humidity': 41.55,
        },
        {
            'temperature': 42.84,
            'humidity': 83.1,
            'voltage': 4.2,
        },
        {
            'weight': 10.10,
        },
    ]
    yield mqtt_json_sensor(settings.mqtt_topic_json, data)

    # Wait for some time to process the message.
    yield sleep(PROCESS_DELAY)
    yield sleep(PROCESS_DELAY)
    yield sleep(PROCESS_DELAY)

    # Proof that Grafana is well provisioned.
    logger.info('Grafana: Checking datasource')
    datasource_names = []
    for datasource in grafana.client.datasources.get():
        datasource_names.append(datasource['name'])
    assert settings.influx_database in datasource_names

    logger.info('Grafana: Checking dashboard')
    dashboard_name = settings.grafana_dashboards[0]
    dashboard = grafana.client.dashboards.db[dashboard_name].get()
    targets = dashboard['dashboard']['rows'][0]['panels'][0]['targets']

    # Validate table name.
    assert targets[0]['measurement'] == settings.influx_measurement_sensors

    # Validate field names.
    fields = set()
    for target in targets:
        fields.add(target["fields"][0]["name"])
    assert fields == set(["temperature", "humidity", "weight", "voltage"])
