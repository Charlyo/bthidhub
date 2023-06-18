# Copyright (c) 2023 Charlyo. All rights reserved.


class QuickStormTKMessageFilter:

    def filter_message_to_host(self, msg):
        if len(msg) == 8:
            # Num lock bug still present. Light does not turn off
            return b'\xa1\x01' + msg
        else:
            return b'\xa1' + msg

    def filter_message_from_host(self, msg):
        msg = list(msg)
        msg[1] -= 1
        return bytes(msg)[1:]
