from collections import deque


def climb_the_peaks_func(food_portions, stamina_levels):
    food_portions, stamina_levels = deque(food_portions), deque(stamina_levels)
    mountain_peaks_data = {
        'Vihren': 80,
        'Kutelo': 90,
        'Banski Suhodol': 100,
        'Polezhan': 60,
        'Kamenitza': 70
    }
    conquered_peaks = []
    failed_condition = False

    for key, value in mountain_peaks_data.items():
        while True:
            daily_sum_of_elements = food_portions.pop() + stamina_levels.popleft()

            if daily_sum_of_elements >= value:
                conquered_peaks.append(key)
                break
            elif len(food_portions) == 0 or len(stamina_levels) == 0:
                failed_condition = True
                break
        if failed_condition:
            if len(conquered_peaks) == 0:
                return 'Alex failed! He has to organize his journey better next time -> @PIRINWINS'
            else:
                data_representation = '\n'.join(conquered_peaks)
                return f'Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK' \
                       f'\nConquered peaks:\n{data_representation}'

    data_representation = '\n'.join(conquered_peaks)
    return f'Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK' \
           f'  \nConquered peaks:\n{data_representation}'


food = list(map(int, input().split(', ')))
stamina = list(map(int, input().split(', ')))
print(climb_the_peaks_func(food, stamina))
