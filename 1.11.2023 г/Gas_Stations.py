def gas_stations(distance, tank_size, stations):
    stops = []  
    current_distance = 0  
    last_stop = 0
    i = 0
    while i < len(stations):
        station = stations[i]
        
        distance_to_next_station = station - current_distance
        
        if distance_to_next_station > tank_size:
            if last_stop < i:    
                stops.append(stations[i - 1])
                current_distance = stations[i - 1]  
                last_stop = i - 1
            else: 
                return []    
        else:
            i += 1
   
    if current_distance < distance:
        stops.append(stations[i-1])
    return stops 


if __name__=='__main__':
    distance = 320
    tank_size = 80
    stations = [50, 80, 140, 210, 230, 290]
    print(gas_stations(distance,tank_size,stations))