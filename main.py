import sys
import cv2
import configuration as Config
from communication import DroneConnection
from cameraLanding import look_at_ground
from arucoDetector import ArucoDetector
from GeometryUtils import GeometryCalculator

def main():
    print("--- START SYSTEMU ARUCO DRONE ---\n")

    # 1. Próba połączenia z dronem.
    try:
        comm = DroneConnection()
    except Exception as e:
        print(f"\nBŁĄD KRYTYCZNY: {e}")
        sys.exit(1)

    # 2. Ustawienie kamery
    look_at_ground(comm.master)

    # 3. Interpretacja obrazu i obliczenia geometryczne
    aruco_detector = ArucoDetector()
    geometry = GeometryCalculator()

    # 4. Łaczenie z kamerą i sprawdzenie czy działa
    cap = cv2.VideoCapture(Config.VIDEO_SOURCE)
    if not cap.isOpened():
        print(f"\nBŁĄD: Nie można otworzyć strumienia wideo z ustawionego źródła ({Config.VIDEO_SOURCE}).")
        sys.exit(1)

    print("\nSzukanie lądowiska ArUco (aby przerwać naciśnij 'q')\n")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Utracono połączenie z kamerą.")
            break

        m_x, m_y, found = aruco_detector.detect(frame)

        if found:
            x_ang, y_ang = geometry.pixels_to_angles(m_x, m_y)
            print(f"Znaleziono marker. Kąty: X={x_ang:.3f} rad, Y={y_ang:.3f} rad")
            comm.send_landing_target(x_ang, y_ang)
        else:
            print("Szukam markera...", end="\r")
        cv2.imshow('Kamera Drona', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("\nPrzerwano przez użytkownika")
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Zakończono działanie skryptu")

if __name__ == "__main__":
    main()