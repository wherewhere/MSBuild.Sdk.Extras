import clr;
from System import Environment
from System.Runtime.InteropServices import RuntimeInformation

print(Environment.Version)
print(RuntimeInformation.FrameworkDescription)
print("Press any key to exit...")

from System import Console
Console.ReadKey(True)
