from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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

def validate_ip(ip):
    octets = ip.split('.')
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit() or not 0 <= int(octet) <= 255:
            return False
    return True

def parse_mask(mask):
    try:
        # Если маска в формате числа (например, 24)
        if mask.isdigit():
            mask_int = int(mask)
            if 0 <= mask_int <= 32:
                return mask_int
        
        # Если маска в формате IP (например, 255.255.255.0)
        if validate_ip(mask):
            binary = ip_to_binary(mask)
            return len(binary.rstrip('0'))
            
        return None
    except:
        return None

def cidr_to_mask(cidr):
    """Convert CIDR to subnet mask"""
    if not 0 <= cidr <= 32:
        return None
    mask = (0xFFFFFFFF << (32 - cidr)) & 0xFFFFFFFF
    return '.'.join([str((mask >> (24 - 8*i)) & 0xFF) for i in range(4)])

def get_host_range(network, mask):
    """Get first and last host addresses"""
    network_int = sum(int(octet) << (24 - 8*i) for i, octet in enumerate(network.split('.')))
    broadcast_int = network_int | (0xFFFFFFFF >> mask)
    first_host = network_int + 1
    last_host = broadcast_int - 1
    
    return (
        '.'.join(str((first_host >> (24 - 8*i)) & 0xFF) for i in range(4)),
        '.'.join(str((last_host >> (24 - 8*i)) & 0xFF) for i in range(4))
    )

def calculate_subnet_parameters(ip_address, current_mask, new_mask):
    """Рассчитывает параметры подсети"""
    # Преобразуем IP в числовой формат
    ip_int = sum(int(octet) << (24 - 8*i) for i, octet in enumerate(ip_address.split('.')))
    
    # Рассчитываем параметры новой подсети
    network_int = ip_int & (0xFFFFFFFF << (32 - new_mask))
    broadcast_int = network_int | ((1 << (32 - new_mask)) - 1)
    first_host = network_int + 1
    last_host = broadcast_int - 1
    
    subnet_bits = new_mask - current_mask
    subnets_count = 2 ** subnet_bits
    hosts_per_subnet = (broadcast_int - network_int - 1) if (broadcast_int - network_int) > 1 else 0
    
    def int_to_ip(ip_int):
        return '.'.join(str((ip_int >> (24 - 8*i)) & 0xFF) for i in range(4))
    
    return {
        'subnet_bits': subnet_bits,
        'subnets_created': subnets_count,
        'addresses_in_subnet': broadcast_int - network_int + 1,
        'usable_hosts': hosts_per_subnet,
        'subnet_address': int_to_ip(network_int),
        'first_host': int_to_ip(first_host) if hosts_per_subnet > 0 else 'N/A',
        'last_host': int_to_ip(last_host) if hosts_per_subnet > 0 else 'N/A',
        'broadcast_address': int_to_ip(broadcast_int),
        'new_mask_dotted': cidr_to_mask(new_mask),
        'new_mask': new_mask
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ip-converter')
def ip_converter():
    return render_template('ip_converter.html')

@app.route('/subnet-calculator')
def subnet_calculator():
    return render_template('subnet_calculator.html')

@app.route('/api/ip-to-binary', methods=['POST'])
def api_ip_to_binary():
    ip = request.form.get('ip')
    if not validate_ip(ip):
        return '<div class="error">Invalid IP address</div>', 400
    binary = ip_to_binary(ip)
    return f'''
        <div class="result-item">
            <div class="label"><i class="fas fa-code"></i> Binary</div>
            <div class="value">{binary}</div>
        </div>
    '''

@app.route('/api/binary-to-ip', methods=['POST'])
def api_binary_to_ip():
    binary = request.form.get('binary')
    try:
        ip = binary_to_ip(binary)
        return f'''
            <div class="result-item">
                <div class="label"><i class="fas fa-code"></i> IP Address</div>
                <div class="value">{ip}</div>
            </div>
        '''
    except Exception as e:
        return f'<div class="error">Invalid binary format</div>', 400

@app.route('/api/calculate-subnet', methods=['POST'])
def api_calculate_subnet():
    try:
        ip = request.form.get('ip')
        if not validate_ip(ip):
            return jsonify({'error': 'Invalid IP address'}), 400
            
        current_mask = parse_mask(request.form.get('current_mask'))
        new_mask = parse_mask(request.form.get('new_mask'))
        
        if current_mask is None or new_mask is None:
            raise ValueError("Invalid mask format")
        if not (0 <= current_mask <= 32) or not (0 <= new_mask <= 32):
            raise ValueError("Mask must be between 0 and 32")
        if new_mask < current_mask:
            raise ValueError("New mask must be greater than current mask")
            
        result = calculate_subnet_parameters(ip, current_mask, new_mask)
        return jsonify(result)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)
