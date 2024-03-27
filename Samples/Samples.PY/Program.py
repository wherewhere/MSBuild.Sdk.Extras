import clr;
from System import Environment
from System.Runtime.InteropServices import RuntimeInformation

print(Environment.Version)
print(RuntimeInformation.FrameworkDescription)
