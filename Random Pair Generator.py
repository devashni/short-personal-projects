import random
#katherine = []
ruth = ['JUNGWON GODA','MONISHA JACOB','KAE LEWIS', 'TIFFANY LUU', 'BEKAH MCCURRY', 'NATALIE OULMAN',
        'TANYA PRABHKAR','ENID SVYMBERSKY', 'YURI UCHIDA', 'KELSI ANDERSON', 'SYDNEY HOLDEN', 'LAUREN LI',
        'ALEXANDRA MILLIRON', 'ALEXANDRA MILLIRON', 'HEATHER PIVEROTTO', 'DEVASHNI PRIYADARSHNI', 'WOOYANG SON',
        'AMY TRICK', 'SARAH WONG', 'SELF']

def generate_random_index_and_pop_student_from_list(stu_lst):
    """This function generates a list of random pairs from a given list of students.
    The function assumes there is an even number of people in the input list.
    If the list is NOT even, 'self' is added to the list implying one person will be pairing with themself.
    Function assumes there are even number of people in the input list.
    If the list is NOT even, 'self' is added meaning one person will be parterning alone."""
    random_index = random.randrange (0, len(stu_lst))
    return stu_lst.pop(random_index)

def generate_random_lab_pairs (stu_lst):
    student_pairs_list = []
    #length_stu_list = len(stu_lst)

    while len(stu_lst)/2 > 0:
        rand_student_1 = generate_random_index_and_pop_student_from_list(stu_lst)
        rand_student_2 = generate_random_index_and_pop_student_from_list(stu_lst)
        student_pair = [rand_student_1, rand_student_2]
        student_pairs_list.append(student_pair)
        student_pair = []
        #length_stu_list -=2
    return student_pairs_list

print ("These are randomly generated pairs for house Ruth: ", generate_random_lab_pairs(ruth))