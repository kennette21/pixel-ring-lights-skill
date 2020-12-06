from mycroft import MycroftSkill, intent_file_handler


class PixelRingLights(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('lights.ring.pixel.intent')
    def handle_lights_ring_pixel(self, message):
        self.speak_dialog('lights.ring.pixel')


def create_skill():
    return PixelRingLights()

