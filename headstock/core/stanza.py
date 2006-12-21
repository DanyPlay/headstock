#!/usr/bin/env python
# -*- coding: utf-8 -*-

#####################################################################################
# From RFC 3920
# An XML stanza is a discrete semantic unit of structured information that is sent 
# from one entity to another over an XML stream. 
#####################################################################################

from headstock.error import *

from bridge import Element as E
from bridge import Attribute as A
from bridge.common import XMPP_CLIENT_NS

__all__ = ['Stanza']

class Stanza(object):
    def __init__(self, node_name, from_jid=None, to_jid=None, stanza_type=None, stanza_id=None):
        self.node_name = node_name
        self.from_jid = from_jid
        self.to_jid = to_jid
        self.stanza_id = stanza_id
        self.stanza_type = stanza_type

    def to_bridge(self, parent=None):
        stanza = E(self.node_name, attributes={u'type': self.stanza_type}, parent=parent)
        if self.from_jid:
            A(u'from', value=unicode(self.from_jid), parent=stanza)
        if self.to_jid:
            A(u'to', value=unicode(self.to_jid), parent=stanza)
        if self.stanza_id:
            A(u'id', value=self.stanza_id, parent=stanza)

        stanza.update_prefix(None, None, XMPP_CLIENT_NS, False)
            
        return stanza
    
    def xml(self):
        return self.to_bridge().xml(omit_declaration=True)
