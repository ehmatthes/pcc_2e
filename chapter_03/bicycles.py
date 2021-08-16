bicycles = ['trek', 'trek', 'cannondale', 'redline', 'specialized']

set(bicycles)

# 4. parasyti cikla, kuris sarase paliktu tik unikalius elementus. input ['a', 'a', 'b', 'c', 'c'], output ['a', 'b', 'c']



bicycles.append('MTB')
bicycles.insert(2, 'new_MTB')
# del bicycles[0]
dviratis = bicycles.pop(0)
bicycles.remove('trek')
print(dviratis)
if __name__ == '__main__':
    print(bicycles)

# message = f"My first bicycle was a {bicycles[0].title()}."

# print(message)
