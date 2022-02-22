
# # ------Exercise 5-------------------------------------------------------------------------------
#
# number = int(input())
#
# for n1 in range(1, 10):
#     for n2 in range(1, 10):
#         for n3 in range(1, 10):
#             for n4 in range(1, 10):
#                 if number % n1 == 0 and number % n2 == 0 and number % n3 == 0 and number % n4 == 0:
#                     result_num = f'{n1}{n2}{n3}{n4}'
#                     print(result_num)
#
# #-------Exercise 6--------------------------------------------------------------------------------
#
# total_tickets = 0
# student_tickets = 0
# kid_tickets = 0
# standard_tickets = 0
#
# while True:
#     film = input()
#
#     if film == 'Finish':
#         student_tickets_percent = (1 / total_tickets * student_tickets) * 100
#         kid_tickets_percent = (1 / total_tickets * kid_tickets) * 100
#         standard_tickets_percent = (1 / total_tickets * standard_tickets) * 100
#         print(f'Total tickets: {total_tickets}\n'
#               f'{student_tickets_percent:.2f}% student tickets.\n'
#               f'{standard_tickets_percent:.2f}% standard tickets.\n'
#               f'{kid_tickets_percent:.2f}% kids tickets.')
#         break
#
#     free_places = int(input())
#
#     for place in range(1, free_places + 1):
#         ticket_type = input()
#         if ticket_type == 'standard':
#             standard_tickets += 1
#             total_tickets += 1
#
#         elif ticket_type == 'student':
#             student_tickets += 1
#             total_tickets += 1
#
#         elif ticket_type == 'kid':
#             kid_tickets += 1
#             total_tickets += 1
#
#         elif ticket_type == 'End':
#             cinema_full_percent = (1/free_places * (place - 1)) * 100
#             print(f'{film} - {cinema_full_percent:.2f}% full.')
#             break
#
        if place == free_places:
            cinema_full_percent = (1 / free_places * place) * 100
            print(f'{film} - {cinema_full_percent:.2f}% full.')
            break


for num in range(10):
    print(num)
