import classBased as cb
Huffboth = cb.Huffboth()

# print(Huffboth)

robocon = """
ABU Robocon, SAE BAJA and SAE SUPRA
PCCOE has been participating in ABU Robocon India since 2011. This has proved to be a real trigger to the robotics activities in PCCOE campus where the official name of the ROBOCON team is 'TEAM AUTOMATONS'.They recently scored 2nd in the MathWorks Modelling Award at the National DD-Robocon 2019, New Delhi.[5]

PCCOE has been participating in SAE BAJA from 2012 where the official name is 'TEAM RED BARON' and their vehicle's name is Albatros. In 2014, 'TEAM RED BARON' bagged Best Design award and in 2016 they bagged Runner-up award for Best innovation.

PCCOE has participated in SAE SUPRA in 2015 where the official name is 'TEAM KRATOS RACING' and their vehicle's name in Fireblade. After brake test failure in SAE SUPRA 2015, in the very next year 2016, after an exciting last-lap duel, 'TEAM KRATOS RACING' secured the top stride of the platform at the fifth edition of the SUPRA SAEINDIA(2016) Formula Student title at the Buddh International Circuit. Additionally, they also bagged five other awards - namely 1st in Endurance, 1st in Skidpad, 1st in Autocross, Best Fuel Economy and Dronacharya award for their faculty adviser.

These competitions ensure that the students do not limit themselves to just theoretical knowledge and are exposed to handle practical and management based issues as well.
"""

# print(Huffboth.Encode(robocon))
print("_"*80, sep="")
Huffboth.Decode(Huffboth.Encode(robocon))
print("_"*80, sep="")
print("are they same ? ")
print(robocon == Huffboth.Decode(Huffboth.Encode(robocon)))
