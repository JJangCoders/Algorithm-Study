possible_discounts = [10, 20, 30, 40]


def calculate_subscription_revenue(users, emoticons, discounts):
    # 각 이모티콘의 할인된 가격 계산
    discounted_prices = [(1 - discounts[i] * 0.01) * emoticons[i] for i in range(len(emoticons))]

    total_sales = 0
    subscribe_count = 0

    for user in users:  # 모든 사용자에 대해 현재 할인 비율을 적용했을 때의 구독자 수와 매출 계산
        min_discount_rate, max_spendable_amount = user
        discounted_total_emoticon_cost = 0

        for idx in range(len(emoticons)):
            if discounts[idx] >= min_discount_rate:
                # 할인율이 사용자의 최소 요구 할인율보다 큰거나 같은 경우
                discounted_total_emoticon_cost += discounted_prices[idx]

        if discounted_total_emoticon_cost >= max_spendable_amount:
            # 할인된 이모티콘 전체 가격이 사용자의 최대 구매 가능 금액보다 크거나 같은 경우
            # => 서비스 구독
            subscribe_count += 1
        else:
            # 할인된 이모티콘 전체 가격이 사용자의 최대 구매 가능 금액보다 작은 경우
            # => 할인된 이모티콘 구매
            total_sales += discounted_total_emoticon_cost

    return subscribe_count, total_sales


def search_best_discount(users, emoticons, current_discounts):
    if len(current_discounts) == len(emoticons):  # 모든 이모티콘에 할인율 적용완료 시
        return calculate_subscription_revenue(users, emoticons, current_discounts)

    best_subscribe_count = -1
    best_sales = -1

    for discount in possible_discounts:  # 가능한 할인율을 각각의 이모티콘에 적용
        current_result = search_best_discount(users, emoticons, current_discounts + [discount])

        if current_result[0] > best_subscribe_count or (
                current_result[0] == best_subscribe_count and current_result[1] > best_sales):
            # 구독자 수가 더 많거나, 구독자 수가 같은 경우 매출이 더 큰 경우
            best_subscribe_count, best_sales = current_result

    return [best_subscribe_count, int(best_sales)]


def solution(users, emoticons):
    return search_best_discount(users, emoticons, [])