#!/usr/bin/env python
# coding: utf-8

# # find out the non sheild members or hydra members

# In[1]:


def hydra_mem(transmission,fury):
    information= dict()
    for trans in transmission:
        _parse_transmission(trans,information)

    print(_find_hydra_mem(information, fury))

def _parse_transmission(trans, information):
    info = trans.split(':')
    sender = info[0].strip()
    receivers = [receiver.strip() for receiver in info[1].split(',')]
    information[sender] = receivers


def _find_hydra_mem(agents_info, fury):
    hydra, shield_agents, agents = set(), set(), [fury]

    while len(agents) > 0:
        current = agents.pop()
        shield_agents.add(current)

        if current in agents_info:
            for agent in agents_info[current]:
                if agent not in shield_agents:
                    agents.append(agent)

 
    for sender in agents_info.keys():
        if sender not in shield_agents:
            hydra.add(sender)

        for receiver in agents_info[sender]:
            if receiver not in shield_agents:
                hydra.add(receiver)

    return hydra


transmission = ["Nick Fury : Tony Stark, Maria Hill, Norman Osborn",
                 "Hulk : Tony Stark, HawkEye, Rogers",
                 "Rogers : Thor",
                 "Tony Stark: Pepper Potts, Nick Fury",
                 "Agent 13 : Agent-X, Nick Fury, Hitler",
                 "Thor: HawkEye, BlackWidow",
                 "BlackWidow:Hawkeye",
                 "Maria Hill : Hulk, Rogers, Nick Fury",
                 "Agent-X : Agent 13, Rogers",
                 "Norman Osborn: Tony Stark, Thor"]

hydra_mem(transmission, "Nick Fury")


# In[ ]:




