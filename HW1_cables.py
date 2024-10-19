import heapq

def minimize_connection_cost(cables):
    # Створюємо мін-купу з довжин кабелів
    heapq.heapify(cables)  
    total_cost = 0

    # Об'єднуємо найкоротші кабелі доти, доки не залишиться один
    while len(cables) > 1:
        # Дістаємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Витрати на з'єднання двох кабелів
        cost = first + second
        total_cost += cost  # Додаємо витрати до загальних

        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
result = minimize_connection_cost(cables)
print(f"Мінімальні загальні витрати: {result}")
