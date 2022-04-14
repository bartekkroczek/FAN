# TODO: Do wyjasnienia
# Change figures ignorue info o ile mamy zmienic ramke, czy to napewno ok? (102 trial.py)
# rel przestaje miec znaczenie gdy wiecej niz 3 powtorzenia tego samego triala

from os.path import join
from problemGenerator.concrete_experiment import concrete_experiment
info = dict()
info["Part_id"] = ''
info["Part_sex"] = ''
info["Part_age"] = ''
concrete_experiment(join('problemGenerator', 'experiment.csv'), info['Part_id'], info['Part_sex'], info['Part_age'])
