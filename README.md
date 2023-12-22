# P5 realization project: Cortex Challenge 
## Made by Jules Gohier and Calliste Meslard

### Libraries to install before starting:

```
pip install networkx[default]

pip install googletrans==4.0.0-rc1
```


**DISCLAIMER :** *you need to replace the line 222 of googletrans/client.py with :*
 ```
try:
translated_parts=list(map(lambda part: TranslatedPart(part[0], part[1] if len(part) >= 2 else []), parsed[1][0][0][5]))
except TypeError: # because of the gender-specific translate results
    translated_parts = [ TranslatedPart(parsed[1][0][1][0], [parsed[1][0][0][0], parsed[1][0][1][0]]) ]
```
 

### [Link GitHub Website](https://github.com/JulesGohier/Cortex-Challenge-Website)

### [Link Website](https://leria-etud.univ-angers.fr/~jugohier/cortex_challenge)
