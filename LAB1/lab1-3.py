print('Give name')
name = input()
print('Lab grade?')
lab = int(input())
print('Midterm grade?')
midterm = int(input())
print('Final grade?')
final = int(input())
lastscore = (int)(lab / 4 + midterm * 35 / 100 + final * 40 / 100)

print('Name: ', name)
print('Lab: ', lab)
print('Midterm: ', midterm)
print('Final: ', final)
print("Last score: ", lastscore)
