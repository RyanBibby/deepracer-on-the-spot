def reward_function(params):
    '''
    Example of penalize steering, which helps mitigate zig-zag behaviors
    '''
    
    abs_steering = abs(params['steering_angle']) 
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']

    reward = 1e-3

    if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.05:
        reward = 31 - abs_steering

    return float(reward)