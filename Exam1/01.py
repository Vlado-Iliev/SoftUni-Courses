from math import ceil, floor

number_of_paint_buckets = int(input())
number_of_lining_paper = int(input())
price_for_gloves = float(input())
price_for_brush = float(input())

number_of_gloves = ceil(0.35 * number_of_lining_paper)
number_of_brushes = floor(0.48 * number_of_paint_buckets)

total_for_paint = number_of_paint_buckets * 21.5
total_for_lining_paper = number_of_lining_paper * 5.2
total_for_gloves = number_of_gloves * price_for_gloves
total_for_brushes = number_of_brushes * price_for_brush

total_cost = total_for_brushes + total_for_gloves + total_for_paint + total_for_lining_paper
delivery_cost = total_cost / 15

print(f'This delivery will cost {delivery_cost:.2f} lv.')
