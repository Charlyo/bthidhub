# Copyright (c) 2020 ruundii. All rights reserved.

class QuickStormTKMessageFilter:

    def filter_message_to_host(self, msg):
        return b'\xa1' + msg

    def filter_message_from_host(self, msg):
        return msg[1:]