from random import choice

capital = "Albany"

bird = "Eastern Bluebird"

flower = "Rose"

song = "I Love New York"

def randomfunfactNYC():
    funfacts = [
        "New York City\'s history began in the 1600s when the Dutch established a settlement at the southern tip of Manhattan Island, naming it New Amsterdam. In 1664, the English took control and renamed it New York, after the Duke of York, who later became King James II of England.",
        "New York City is home to an astonishing 275 species of birds. This diversity is due to the city\'s unique geography and climate.",
        "Many neighborhoods in New York City still retain Dutch names, a testament to the city\'s early history. The Dutch settlers introduced their language, customs, and architecture, which continue to shape the city\'s character.",
        "The nickname “The Big Apple” originated in the 1920s, referencing the prizes awarded at horse racing events. Over time, the term came to symbolize the city\'s excitement, energy, and allure.",
        "The Statue of Liberty, a gift from France, was assembled on Ellis Island in 1886. It took four months to complete the iconic landmark, which has become a symbol of freedom and democracy.",
        "Contrary to popular belief, New York City\'s famous yellow cabs were not always yellow. They were originally red and green, but the city standardized them to yellow in 1912.",
    ]
    
    index = choice("01234")
    print(funfacts[int(index)])
    
if __name__ == "__main__":
    randomfunfactNYC()