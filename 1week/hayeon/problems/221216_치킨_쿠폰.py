def solution(chicken):
    coupon = chicken
    total = 0

    while coupon // 10 != 0:
        service = coupon // 10
        coupon = coupon - (service * 10) + service
        total += service

    return total
