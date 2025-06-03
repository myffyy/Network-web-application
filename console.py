#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ip_to_binary(ip):
    """Преобразует IP-адрес в двоичный формат"""
    octets = ip.split('.')
    binary = ''
    for octet in octets:
        binary += bin(int(octet))[2:].zfill(8)
    return binary

def binary_to_ip(binary):
    """Преобразует двоичное представление в IP-адрес"""
    octets = []
    for i in range(0, 32, 8):
        octets.append(str(int(binary[i:i+8], 2)))
    return '.'.join(octets)

def calculate_subnet_parameters(ip_address, current_mask, new_mask):
    """Рассчитывает параметры подсети"""
    # Преобразуем маски в числовой формат (количество бит)
    if '/' in current_mask:
        current_mask_bits = int(current_mask.split('/')[1])
    else:
        current_mask_bits = sum([bin(int(x)).count('1') for x in current_mask.split('.')])
    
    if '/' in new_mask:
        new_mask_bits = int(new_mask.split('/')[1])
    else:
        new_mask_bits = sum([bin(int(x)).count('1') for x in new_mask.split('.')])
    
    # Число бит подсети (это количество бит, выделенных для адресации подсети)
    subnet_bits = new_mask_bits - current_mask_bits
    
    # Число созданных подсетей
    subnets_created = 2 ** (new_mask_bits - current_mask_bits)
    
    # Число адресов в подсети
    addresses_in_subnet = 2 ** (32 - new_mask_bits)
    
    # Число узлов в подсети
    hosts_in_subnet = addresses_in_subnet - 2 if addresses_in_subnet > 2 else 0
    
    # Преобразуем IP-адрес в двоичный формат
    ip_binary = ip_to_binary(ip_address)
    
    # Получаем адрес подсети
    subnet_binary = ip_binary[:new_mask_bits] + '0' * (32 - new_mask_bits)
    subnet_address = binary_to_ip(subnet_binary)
    
    # Получаем адрес первого узла
    first_host_binary = subnet_binary[:-1] + '1' if subnet_bits < 31 else subnet_binary
    first_host = binary_to_ip(first_host_binary)
    
    # Получаем адрес последнего узла
    last_host_binary = subnet_binary[:new_mask_bits] + '1' * (32 - new_mask_bits - 1) + '0' if subnet_bits < 31 else subnet_binary
    last_host = binary_to_ip(last_host_binary)
    
    # Получаем широковещательный адрес
    broadcast_binary = subnet_binary[:new_mask_bits] + '1' * (32 - new_mask_bits)
    broadcast_address = binary_to_ip(broadcast_binary)
    
    # Создаем маску в формате IP
    mask_binary = '1' * new_mask_bits + '0' * (32 - new_mask_bits)
    mask_ip = binary_to_ip(mask_binary)
    
    return {
        'subnet_bits': subnet_bits,
        'subnets_created': subnets_created,
        'addresses_in_subnet': addresses_in_subnet,
        'hosts_in_subnet': hosts_in_subnet,
        'subnet_address': subnet_address,
        'first_host': first_host,
        'last_host': last_host,
        'broadcast_address': broadcast_address,
        'mask_ip': mask_ip
    }

def main():
    print("\n=== Калькулятор подсетей IPv4 ===\n")
    
    # Ввод данных
    ip_address = input("Введите IP-адрес узла (например, 192.168.1.1): ")
    current_mask = input("Введите текущую маску подсети (например, 255.255.255.0 или /24): ")
    new_mask = input("Введите новую маску подсети (например, 255.255.255.128 или /25): ")
    
    # Расчет параметров
    try:
        results = calculate_subnet_parameters(ip_address, current_mask, new_mask)
        
        # Вывод результатов
        print("\n=== Результаты ===\n")
        print(f"Число бит подсети: {results['subnet_bits']}")
        print(f"Число созданных подсетей: {results['subnets_created']}")
        print(f"Число адресов в подсети: {results['addresses_in_subnet']}")
        print(f"Число узлов в подсети: {results['hosts_in_subnet']}")
        print(f"IPv4-адрес подсети: {results['subnet_address']}")
        print(f"IPv4-адрес первого узла подсети: {results['first_host']}")
        print(f"IPv4-адрес последнего узла подсети: {results['last_host']}")
        print(f"Широковещательный IPv4-адрес подсети: {results['broadcast_address']}")
    except Exception as e:
        print(f"Ошибка: {e}")
        print("Пожалуйста, проверьте правильность введенных данных.")

if __name__ == "__main__":
    main()
    input("\nНажмите Enter для выхода...")