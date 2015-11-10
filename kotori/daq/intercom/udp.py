# -*- coding: utf-8 -*-
# (c) 2015 Andreas Motl, Elmyra UG <andreas.motl@elmyra.de>
from cornice.util import to_list
from twisted.logger import Logger
from twisted.internet.protocol import DatagramProtocol
from twisted.internet.defer import inlineCallbacks

logger = Logger()

class UdpBusForwarder(DatagramProtocol):
    # https://twistedmatrix.com/documents/15.0.0/core/howto/udp.html

    def __init__(self, bus, topic, transform):
        self.bus = bus
        self.topic = topic
        self.transform = to_list(transform)

        # TODO sanity checks

    @inlineCallbacks
    def datagramReceived(self, data, (host, port)):
        logger.info("Received via UDP from %s:%d: %r " % (host, port, data))

        # ECHO
        #self.transport.write(data, (host, port))
        data_out = data
        for transform in self.transform:
            data_out = transform(data_out)

        # forward
        logger.info("Publishing to topic '{}' with realm '{}': {}".format(self.topic, self.bus._realm, data_out))
        yield self.bus.publish(self.topic, data_out)
