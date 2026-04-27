import configuration

class GeometryCalculator:
    def __init__(self):
        self.h_res = configuration.HORIZONTAL_RES
        self.v_res = configuration.VERTICAL_RES
        self.h_fov = configuration.HORIZONTAL_FOV

        # Środek obrazu
        self.img_center_x = self.h_res / 2
        self.img_center_y = self.v_res / 2

        # Pionowy FOV
        self.v_fov = self.h_fov * (self.v_res / self.h_res)

        # Skalowanie kątów na piksele
        self.x_angle_per_pixel = self.h_fov / self.h_res
        self.y_angle_per_pixel = self.v_fov / self.v_res

    def pixels_to_angles(self, m_x, m_y):
        """Przelicza pozycję w pikselach na odchylenie kątowe od środka kamery"""
        # Błąd względem środka obrazu
        x_error = m_x - self.img_center_x
        y_error = m_y - self.img_center_y

        # Kąty w radianach
        x_ang = x_error * self.x_angle_per_pixel
        y_ang = y_error * self.y_angle_per_pixel

        return x_ang, y_ang