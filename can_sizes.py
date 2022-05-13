import math

def main():
    radius = input()
    height = input()
    volume_cylinder = compute_volume(radius, height)
    area_cylinder = compute_suface_area(radius, height)
    efficiency_cylinder = compute_storage_efficiency(volume_cylinder, area_cylinder)
    print(f'{volume_cylinder} {area_cylinder} {efficiency_cylinder}')
    
def compute_volume(radius, height):
    volume = math.pi*(radius**2)*height
    return volume

        
def compute_suface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area
    

def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency


print()