from tinamit.EnvolturasBF.SAHYSMOD.envoltura import leer_arch_egr
import Plotting
Path = 'D:\\Mars_new'
Haveli_Circle = Plotting.leer_datos(nombre='Haveli', archivo=Path)
Dataoes = Haveli_Circle.leer_arch_data(Path, 'Cr4#', 'A#', 'B#', 'Dw#', 'Cqf#')
#Result = {}
#Data = leer_arch_egr('D:\\Mars_new\\1\\1.out',2,215,1)
print(Dataoes)
