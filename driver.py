import yaml

configs = ['input/fv3.yaml', 'input/fcst.yaml']

confDict = dict()
for conf in configs:
    with open(conf, 'r') as fh:
        confDict[conf] = yaml.load(fh, Loader=yaml.FullLoader)
