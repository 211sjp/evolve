import json
from opcode import opname
e_queue = ['ogre','moldling','kobold','goblin','gnome']

base_target =  '''{
        "userEvolutionTarget": "entish",
        "prestigeType": "ascension",
        "challenge_plasmid": false,
        "challenge_crispr": true,
        "challenge_trade": true,
        "challenge_craft": false,
        "challenge_joyless": false,
        "challenge_steelen": false,
        "challenge_decay": false,
        "challenge_emfield": false,
        "challenge_inflation": false,
        "challenge_sludge": false,
        "challenge_junker": false,
        "challenge_cataclysm": false,
        "challenge_banana": false,
        "challenge_truepath": false
    }'''
base_target = json.loads(base_target)
script_config = open("铜柱.json",'r')
script_config = json.load(script_config)
e_queue =[e['userEvolutionTarget'] for e in script_config['evolutionQueue'] ] 
base = '''[{
        "userEvolutionTarget": "entish",
        "prestigeType": "mad",
        "challenge_plasmid": false,
        "challenge_crispr": false,
        "challenge_trade": false,
        "challenge_craft": false,
        "challenge_joyless": false,
        "challenge_steelen": false,
        "challenge_decay": false,
        "challenge_emfield": false,
        "challenge_inflation": false,
        "challenge_sludge": false,
        "challenge_junker": false,
        "challenge_cataclysm": false,
        "challenge_banana": false,
        "challenge_truepath": false
    }, {
        "userEvolutionTarget": "wendigo",
        "prestigeType": "mad",
        "challenge_plasmid": false,
        "challenge_crispr": false,
        "challenge_trade": false,
        "challenge_craft": false,
        "challenge_joyless": false,
        "challenge_steelen": false,
        "challenge_decay": false,
        "challenge_emfield": false,
        "challenge_inflation": false,
        "challenge_sludge": false,
        "challenge_junker": false,
        "challenge_cataclysm": false,
        "challenge_banana": false,
        "challenge_truepath": false
    }]'''
base = json.loads(base)
for target in e_queue:
    base.append(base[0])
    base.append(base[1])
    _t = dict()
    _t.update(base_target)
    _t['userEvolutionTarget'] = target
    base.append(_t)
script_config['evolutionQueue'] = base
f = open('cu.json','w')
print(json.dump(script_config,f))
f.close()