from datetime import date

iDevolucao = [int(i) for i in input().strip().split(' ')]
iDue_date = [int(i) for i in input().strip().split(' ')]
print(iDevolucao, iDue_date)
devolucao = date(iDevolucao[2],iDevolucao[1],iDevolucao[0])
due_date = date(iDue_date[2],iDue_date[1],iDue_date[0])
