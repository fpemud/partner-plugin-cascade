#!/usr/bin/python3
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-


class ReflexObject:

    def on_user_instance_appear(self, uid):
        assert False

    def on_user_instance_disappear(self, uid):
        assert False

    def on_receive_message_from_user_instance(self, uid, message, data):
        assert False

    def send_message_to_user_instance(self, uid, message, data):
        assert False
