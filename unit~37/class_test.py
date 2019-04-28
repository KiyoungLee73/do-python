class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))


maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()

print('이름:', maria.name)
print('나이:', maria.age)
print('주소:', maria.address)

class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print('베기')

x = Knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()

class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power

    def tibbers(self):
        damage = self.ability_power * 0.65 + 400
        print('티버: 피해량 {0}'.format(damage))

health, mana, ability_power = map(float, input().split())
 
x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()