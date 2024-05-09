import contextlib
import sys
import time

from pyke import knowledge_engine, krb_traceback, goal

engine = knowledge_engine.engine(__file__)

def test_ingredientes():
    engine.reset()
    engine.activate('fc_rules')
    print("TEST INGREDIENTES")
    try:
        with engine.prove_goal('ingredientes.ingrediente_es($ingrediente,$tipo,$nutriente,$origen)') as gen:
            for vars, plan in gen:
                print("El ingrediente ", vars['ingrediente'], "es ", vars['nutriente']," y es de origen", vars['origen'])
    except Exception:
        print("Exception")
        krb_traceback.print_exc()
        sys.exit(1)
    print()

def test_plato_ingredientes():
    engine.reset()
    engine.activate('fc_rules')
    print("TEST PLATO INGREDIENTE")
    try:
        with engine.prove_goal('platos.plato_tiene_ingredientes($plato,$lista_ingredientes)') as gen:
            for vars, plan in gen:
                print("El plato", vars['plato'], "tiene los ingredientes:", vars['lista_ingredientes'])
                # print("El plato", vars['plato'], "tiene los ingredientes:", set(vars['lista_ingredientes']))
    except Exception:
        print("Exception")
        krb_traceback.print_exc()
        sys.exit(1)
    print()

def test_plato_tipos():
    engine.reset()
    engine.activate('fc_rules')
    print("TEST PLATO TIPO")
    try:
        with engine.prove_goal('platos.plato_tiene_tipos($plato,$lista_tipos)') as gen:
            for vars, plan in gen:
                print("El plato", vars['plato'], "tiene los tipos:", vars['lista_tipos'])
                # print("El plato", vars['plato'], "tiene los tipos:", set(vars['lista_tipos']))
    except Exception:
        print("Exception")
        krb_traceback.print_exc()
        sys.exit(1)
    print()

def test_plato_nutrientes():
    engine.reset()
    engine.activate('fc_rules')
    print("TEST PLATO NUTRIENTE")
    try:
        with engine.prove_goal('platos.plato_tiene_nutrientes($plato,$lista_nutrientes)') as gen:
            for vars, plan in gen:
                print("El plato", vars['plato'], "tiene los nutrientes:", vars['lista_nutrientes'])
                # print("El plato", vars['plato'], "tiene los nutrientes:", set(vars['lista_nutrientes']))
    except Exception:
        print("Exception")
        krb_traceback.print_exc()
        sys.exit(1)
    print()

def test_plato_valor_nutricional():
    engine.reset()
    engine.activate('fc_rules')
    print("TEST PLATO VALOR NUTRICIONAL")
    try:
        with engine.prove_goal('platos.plato_valor_nutricional($plato, $valor_nutricional)') as gen:
            for vars, plan in gen:
                print("El plato", vars['plato'], "tiene el valor nutricional ('Carbohidratos','Proteinas','Grasas')", vars['valor_nutricional'])
    except Exception:
        print("Exception")
        krb_traceback.print_exc()
        sys.exit(1)
    print()

def test_plato_dieta():
    engine.reset()
    engine.activate('fc_rules')
    print("TEST PLATO DIETA")
    try:
        with engine.prove_goal('platos.plato_es_dieta($plato,$dieta)') as gen:
            for vars, plan in gen:
                print("El plato", vars['plato'], "es:", vars['dieta'])
    except Exception:
        print("Exception")
        krb_traceback.print_exc()
        sys.exit(1)
    print()

def test_restaurante():
    engine.reset()
    engine.activate('fc_rules')
    print("TEST RESTAURANTE")
    try:
        with engine.prove_goal('restaurantes.restaurante_es_dieta($restaurante,$menu)') as gen:
            for vars, plan in gen:
                print("El", vars['restaurante'], "ofrece comida", vars['menu'])
    except Exception:
        print("Exception")
        krb_traceback.print_exc()
        sys.exit(1)
    print()

def test_dieta_restaurante_posibles_platos_menu():
    engine.reset()
    engine.activate('fc_rules')
    print("TEST POSIBLES COMIDAS PARA EL MENU")
    try:
        with engine.prove_goal('restaurantes.menu_es_dieta($restaurante,$listado_platos,$dieta)') as gen:
            for vars, plan in gen:
                print("El", vars['restaurante'], "es", vars['dieta']," para esta combinacion de platos para tu menu", vars['listado_platos'])
    except Exception:
        print("Exception")
        krb_traceback.print_exc()
        sys.exit(1)
    print()

def test_cliente_rest():
    engine.reset()
    engine.activate('fc_rules')
    print("TEST PLATO DIETA")
    try:
        with engine.prove_goal('restaurantes.restaurante_es_cliente($restaurante,$dieta)') as gen:
            for vars, plan in gen:
                print("El plato", vars['restaurante'], "es:", vars['dieta'])
    except Exception:
        print("Exception")
        krb_traceback.print_exc()
        sys.exit(1)
    print()