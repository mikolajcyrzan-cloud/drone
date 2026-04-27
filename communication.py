from pymavlink import mavutil
import configuration
import time

class DroneConnection:
    def __init__(self):
        # Adres do którego ArduPilot będzie wysyłał dane o położeniu
        self.address = configuration.MAVLINK_CONNECTION
        self.master = None
        self.connect()

    def connect(self):
        print(f"Próba połączenia: {self.address}")
        try:
            self.master = mavutil.mavlink_connection(self.address) 

            self.master.wait_heartbeat()
            print(f"Połączono")
            
            # Konfiguracja drona po połączeniu
            self.setup_precision_landing()
            
        except Exception as e:
            print(f"--- ERROR: Nie udało się połączyć: {e} ---")

    def _set_param(self, name, value):
        """Wysyła pojedynczy parametr do drona. Używane do konfiguracji PLND."""
        if not self.master: return
        self.master.mav.param_set_send(
            self.master.target_system, 
            self.master.target_component,
            name.encode('utf-8'),
            value, 
            mavutil.mavlink.MAV_PARAM_TYPE_REAL32
        )

    def setup_precision_landing(self):
        params = {
            'PLND_ENABLED': 1,
            'PLND_TYPE': 1,
            'PLND_ESTIM_TYPE': 1
        }
        for name, val in params.items():
            self._set_param(name, val)
            time.sleep(0.1)

    def send_landing_target(self, angle_x, angle_y):
        if not self.master: return
        self.master.mav.landing_target_send(
            int(time.time() * 1e6),
            0, 
            12, 
            angle_x, 
            angle_y, 
            0.0, 
            0, 
            0
        )