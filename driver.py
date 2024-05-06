import contextlib
import sys
import time

from pyke import knowledge_engine, krb_traceback, goal

engine = knowledge_engine.engine(__file__)

def test_plato():
    engine.reset()
    engine.activate('fc_rules')
    print("doing proof")
    try:
        with engine.prove_goal('platos.plato_conteo_nutrientes($plato,$nutrientes,$tot)') as gen:
            for vars, plan in gen:
                print("El plato", vars['plato'], "tiene:")
                for nutriente in vars['nutrientes']:
                    indice = vars['nutrientes'].index(nutriente)
                    print(" -",nutriente,":", vars['tot'][indice])
    except Exception:
        print("Excepption")
        krb_traceback.print_exc()
        sys.exit(1)
    print()

def test_plato_dieta():
    engine.reset()
    engine.activate('fc_rules')
    print("doing proof")
    try:
        with engine.prove_goal('platos.plato_es_dieta($plato,$dieta)') as gen:
            for vars, plan in gen:
                print("El plato", vars['plato'], "es:", vars['dieta'])
    except Exception:
        print("Excepption")
        krb_traceback.print_exc()
        sys.exit(1)
    print()

def test_restaurante():
    engine.reset()
    engine.activate('fc_rules')
    print("doing proof")
    try:
        with engine.prove_goal('restaurantes.restaurante_es_dieta($restaurante,$menu)') as gen:
            for vars, plan in gen:
                print("El restaurante", vars['restaurante'], "ofrece", vars['menu'])
    except Exception:
        print("Excepption")
        krb_traceback.print_exc()
        sys.exit(1)
    print()
