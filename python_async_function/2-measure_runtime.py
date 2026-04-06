#!/usr/bin/env python3
"""Measure the runtime of wait_n"""

import asyncio   # pour exécuter des fonctions async
import time      # pour mesurer le temps

# On importe wait_n depuis ton fichier précédent
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Mesure le temps moyen d'exécution d'une coroutine wait_n.

    Arguments :
    n -- nombre de tâches à lancer
    max_delay -- délai maximum pour chaque tâche

    Retour :
    temps moyen par tâche (float)
    """

    # Étape 1 : prendre le temps de début
    start_time = time.time()

    # Étape 2 : exécuter wait_n avec asyncio.run
    asyncio.run(wait_n(n, max_delay))

    # Étape 3 : prendre le temps de fin
    end_time = time.time()

    # Étape 4 : calculer le temps total
    total_time = end_time - start_time

    # Étape 5 : retourner le temps moyen
    return total_time / n
