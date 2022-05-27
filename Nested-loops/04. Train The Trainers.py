number_of_judges = int(input())
command = input()
total_score = 0
total_presentations = 0
while command != 'Finish':
    name_of_presentation = command
    presentation_score = 0
    for judges in range(1, number_of_judges + 1):
        judge_score = float(input())
        presentation_score += judge_score
        total_score += judge_score
        total_presentations += 1
    average_presentation_score = presentation_score / number_of_judges
    print(f'{name_of_presentation} - {average_presentation_score:.2f}.')
    command = input()

total_average_score = total_score / total_presentations
print(f"Student's final assessment is {total_average_score:.2f}.")
