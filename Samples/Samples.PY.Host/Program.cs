using IronPython.Runtime.Operations;
using System.Reflection;
using System;

try
{
    return PythonOps.InitializeModuleEx(Assembly.LoadFrom("Samples.PY.dll"), "__main__", null, ignoreEnvVars: false, null);
}
catch (Exception ex)
{
    Console.WriteLine("Error occurred: {0}", ex.Message);
    return -1;
}
