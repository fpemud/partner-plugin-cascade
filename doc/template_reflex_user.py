#!/usr/bin/python3
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-


class ReflexObject:

    def on_system_instance_appear(self):
        assert False

    def on_system_instance_disappear(self):
        assert False

    def on_receive_message_from_system_instance(self, message):
        assert False

    def send_message_to_system_instance(self, message):
        assert False
