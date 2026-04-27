#   ______   ______   .__   __.  _______  __    _______  __    __  .______          ___   .___________. __    ______   .__   __. 
#  /      | /  __  \  |  \ |  | |   ____||  |  /  _____||  |  |  | |   _  \        /   \  |           ||  |  /  __  \  |  \ |  | 
# |  ,----'|  |  |  | |   \|  | |  |__   |  | |  |  __  |  |  |  | |  |_)  |      /  ^  \ `---|  |----`|  | |  |  |  | |   \|  | 
# |  |     |  |  |  | |  . `  | |   __|  |  | |  | |_ | |  |  |  | |      /      /  /_\  \    |  |     |  | |  |  |  | |  . `  | 
# |  `----.|  `--'  | |  |\   | |  |     |  | |  |__| | |  `--'  | |  |\  \----./  _____  \   |  |     |  | |  `--'  | |  |\   | 
#  \______| \______/  |__| \__| |__|     |__|  \______|  \______/  | _| `._____/__/     \__\  |__|     |__|  \______/  |__| \__| 




# --- POŁĄCZENIE --- #
MAVLINK_CONNECTION = 'udp:127.0.0.1:14550' # Adres do którego ArduPilot będzie wysyłał dane o położeniu drona.
VIDEO_SOURCE = 2

# --- WYBÓR MARKERA ARUCO --- #
ARUCO_DICT = "DICT_4X4_50" # Słownik z którego pochodzi marker
MARKER_ID = 0 # ID markera, który ma być śledzony

# --- PARAMETRY KAMERY --- #
HORIZONTAL_RES = 640 #
VERTICAL_RES = 480 # piksele
HORIZONTAL_FOV = 2 # radiany