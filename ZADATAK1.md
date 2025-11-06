# BAZEL ZADATAK
Binary za timestamp_provider se builda pomocu komande `bazel build //c/timestamp_provider:timestamp_provider`

Kada se pokrene pomocu `bazel run //c/timestamp_provider:timestamp_provider` ispisace trenutni UNIX timestamp.

Upoznati se sa teorijom svrhe build sistema i Bazela. Potrebno je napraviti Bazel BUILD fajl za biblioteku timestamp_parser_lib koja omogucava parsiranje ovog timestampa u human-readable format. Ovu biblioteku treba dodati kao dependency za timestamp_provider da se u main.c moze otkomentarisati import, i print timestampa treba zamijeniti printom human readable stringa.

# DOCKER ZADATAK
Upoznati se sa konceptom Dockera i docker fajlova. Kreirati docker fajl baziran na ubuntu koji sadrzi dva build stage-a. U prvom stage-u je potrebno buildati timestamp_provider. U drugom stage-u je potrebno uzeti samo binary timestamp_provider iz bazel-bin direktorija i postaviti ga na lokaciju tako da ga dummy_logger direktno moze pozvati prilikom pozivanja `bazel run //python:dummy_logger`. Prilikom pokretanja dobijenog docker image-a ova komanda se treba izvrsiti.

Za prvi stage potrebno je obezbjediti Bazel kao dependency unutar image-a, dok je za drugi stage potreban Bazel i Python.