if grade_scholarship > 0:

    if 0 < soc_scholarship <= grade_scholarship:
        print(f"You get a scholarship for excellent results {floor(grade_scholarship)} BGN")
    else :
        print(f"You get a scholarship for excellent results {floor(grade_scholarship)} BGN")
if soc_scholarship > 0:
    if soc_scholarship > grade_scholarship > 0:
        print(f"You get a Social scholarship {floor(soc_scholarship)} BGN")
    elif soc_scholarship :
        print(f"You get a Social scholarship {floor(soc_scholarship)} BGN")
else:
    print("You cannot get a scholarship!")