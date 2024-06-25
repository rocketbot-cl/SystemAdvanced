# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import sys
from random import *
import time

"""
    Obtengo el modulo que fueron invocados
"""
ProcessTime = time.perf_counter  #this returns nearly 0 when first call it if python version <= 3.6
ProcessTime()
module = GetParams("module")

try:
    if module == "export":
        path = GetParams("path")

        with open(path, 'w') as f:
            f.write(str(vars_))

    if module == "setVariable":
        data = GetParams("data")
        variables = GetParams("vars")

        try:
            data = eval(data)
            variables =  variables.split(",")

            for i, var in enumerate(variables):
                SetVar(var, data[i])
        except Exception as e:
            PrintException()
            raise e


    if module == "backup":
        try:
            try:
                os.mkdir("Logs")
            except:
                pass
            name = "Logs/app_{}.log".format(datetime.now()).replace(":", ".")
            os.rename("app.log", name)
        except Exception as e:
            PrintException()
            raise e

    if module == "cleanVars":

        variables = GetParams('vars')
        if not variables:
            variables = [var["name"] for var in vars_]
        else:
            variables = variables.split(',')

        for var in variables:
            SetVar(var, '')

    if module == "cleanVarsByCategory":
        global categoria
        categoria = GetParams("categoria")

        variables = [var["name"] for var in vars_ if var.get("category", "") == categoria]
        for var in variables:
            SetVar(var, '')

    if module == "random_":
        option = GetParams('option')
        value = GetParams('value')
        result = GetParams('var')

        value = eval(value)
        if option == "randint":
            rand_number = eval(option)(value[0], value[1])
        else:
            rand_number = eval(option)(value)

        if result:
            SetVar(result, rand_number)

    if module == "App_Foreground":

        import win32gui
        app_name = GetParams('app_name')

        def set_window_to_foreground(title):
            import win32gui
            import win32con
            import win32com
            try:
                handle = win32gui.FindWindow(None, title)
                if not handle:
                    raise Exception('Could not find a window with title "{}"'.format(title))

                win32gui.ShowWindow(handle, win32con.SW_SHOWMAXIMIZED)
                shell = win32com.client.Dispatch("WScript.Shell")
                shell.SendKeys('%')
                win32gui.SetForegroundWindow(handle)
            except Exception as ex:
                raise ex


            set_window_to_foreground(app_name)

    if module == "GetHandle":
        import win32gui
        result = GetParams("var")

        
        handleInfo = []


        def winEnumHandler(hwnd, ctx):
            global handleInfo, win32gui
            if win32gui.IsWindowVisible(hwnd):
                handleInfo.append((hwnd, win32gui.GetWindowText(hwnd)))


        win32gui.EnumWindows(winEnumHandler, None)

        SetVar(result, handleInfo)


    if module == "timer":
        var_ = GetParams("var")
        process_time = ProcessTime()
        SetVar(var_, int(process_time))

    if (module == "getArguments"):
        try:
            argumentsNeeded = eval(GetParams("argumentsNeeded"))
        except:
            argumentsNeeded = ""
        whereToStore = GetParams("whereToStore")

        arguments = sys.argv
        arguments = arguments[1:]
        argDic = {}
        for each in arguments:
            realEach = each.split("=")
            if (len(realEach) == 2):
                argDic[f"{realEach[0]}"] = realEach[1]


        if (len(argumentsNeeded) == 0):
            SetVar(whereToStore, argDic)
        else:
            realArg = {}
            for each in argumentsNeeded:
                realArg[f"{each}"] = argDic[f"{each}"]
            SetVar(whereToStore, realArg)

except Exception as e:
    print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
    PrintException()
    raise e
# if module == "import":
#     path = GetParams("path")

#     with open(path, 'r') as f:
#         var = f.read()
#         variables = eval(var)

#     for v in variables:
#         v.pop('$$hashKey')
    

#     vars_ = variables
#     print(vars_)
