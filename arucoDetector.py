import cv2
import cv2.aruco as aruco
import numpy as np
import configuration

class ArucoDetector:
    def __init__(self):
        try:
            dictionary = getattr(aruco, configuration.ARUCO_DICT)
        except AttributeError:
            raise ValueError(f"{configuration.ARUCO_DICT} nie istnieje")
        
        self.aruco_dict = aruco.getPredefinedDictionary(dictionary)
        self.parameters = aruco.DetectorParameters()
        self.detector = aruco.ArucoDetector(self.aruco_dict, self.parameters)

    def detect(self, frame):
        """Wykrywa marker, zwraca jego pozycję w pikselach"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners, ids, rejected = self.detector.detectMarkers(gray)

        # Rysowanie ramek
        if ids is not None:
            cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        if len(rejected) > 0:
            cv2.aruco.drawDetectedMarkers(frame, rejected, borderColor=(0, 0, 255))

        # Ekstrakcja pozycji
        if ids is not None and configuration.MARKER_ID in ids:
            id_idx = np.where(ids == configuration.MARKER_ID)[0][0]
            c = corners[id_idx][0]

            # Środek markera (uśrednienie narożników) w pikselach
            m_x = np.mean(c[:, 0])
            m_y = np.mean(c[:, 1])
            
            return m_x, m_y, True

        return None, None, False