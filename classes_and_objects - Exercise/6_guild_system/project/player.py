class Player:

    default_guild = 'Unaffiliated'

    def __init__(self, name: str, hp: int, mp: int) -> None:
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}  # {skill: mana cost}
        self.guild = self.default_guild

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name in self.skills.keys():
            return 'Skill already added'
        else:
            self.skills.update({skill_name: mana_cost})
            return f'Skill {skill_name} added to the collection of the player {self.name}'

    def player_info(self) -> str:
        retval = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}"
        if self.skills:
            retval += '\n===' + '\n==='.join([f'{key} - {value}' for key, value in self.skills.items()])

        return retval