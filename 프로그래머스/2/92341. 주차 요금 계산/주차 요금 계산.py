import math

def get_total_minute(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

def get_fee(fees, time):
    if time <= fees[0]:
        return fees[1]
    
    extra = math.ceil((time - fees[0]) / fees[2])
    return fees[1] + extra * fees[3]
        

def solution(fees, records):
    parking = {}
    total_time = {}
    
    for record in records:
        time, car, act = record.split()
        t = get_total_minute(time)
        
        if act == "IN":
            parking[car] = t
        else:
            in_time = parking.pop(car)
            total_time[car] = total_time.get(car, 0) + (t - in_time)
           

    # 출차 안한 차량 처리
    end_time = get_total_minute("23:59")
    for car in parking:
        total_time[car] = total_time.get(car, 0) + (end_time - parking[car])
        
    answer = []
    for car in sorted(total_time):
        fee = get_fee(fees, total_time[car])
        answer.append(fee)
    
    return answer