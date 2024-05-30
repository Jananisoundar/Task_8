class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.volume = 50
        self.on = False

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"


class LedTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, backlight, display_details):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight
        self.display_details = display_details


class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, backlight, display_details):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight
        self.display_details = display_details


# Example Usage:
led_tv = LedTV("Sony", "Thin", "Low", "10 years", "120Hz", "178°", "Yes", "4K HDR")
plasma_tv = PlasmaTV("Samsung", "Thick", "High", "8 years", "60Hz", "160°", "No", "1080p")

print(led_tv.status())
print(plasma_tv.status())
