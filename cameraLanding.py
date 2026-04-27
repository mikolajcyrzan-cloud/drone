from pymavlink import mavutil

def look_at_ground(master):
    """Kieruje kamere w dół przy właczeniu skryptu"""
    if master is None:
        print("BŁĄD - Brak aktywnego połączenia z dronem")
        return
    
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
        0,                      
        10,                     # Numer serwomechanizmu
        1300,                   # Wartość sygnału PWM
        0, 0, 0, 0, 0           
    )
