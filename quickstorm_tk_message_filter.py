# Copyright (c) 2023 Charlyo. All rights reserved.

class QuickStormTKMessageFilter:

    """
    BYTES_PLAY_PAUSE = 0x0800
    BYTES_STOP = 0x0400
    BYTES_PREVIOUS = 0x0200
    BYTES_NEXT = 0x100

    BYTES_MUTE = 0x1000
    BYTES_VOLUME_DOWN = 0x4000
    BYTES_VOLUME_UP = 0x2000
    """

    def filter_message_to_host(self, msg):
        if len(msg) == 8:
            return b'\xa1\x01' + msg
        else:
            # Send depress
            if msg[-1] == b'\x00\x00\x00':
                return b'\xa1\x02' + msg[1:]

            # Send play control keys
            return b'\xa1\x02' + msg[2:4] + b'\x00'

    def filter_message_from_host(self, msg):
        msg = list(msg)
        msg[1] -= 1
        return bytes(msg)[1:]
