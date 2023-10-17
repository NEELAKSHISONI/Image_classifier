from OpenSSL import crypto

def sign_csr(csr_data, ca_cert_path, ca_key_path):
    # Load the CSR
    req = crypto.load_certificate_request(crypto.FILETYPE_PEM, csr_data)

    # Load the CA's private key and certificate
    with open(ca_key_path, 'rb') as f:
        ca_key = crypto.load_privatekey(crypto.FILETYPE_PEM, f.read())
    with open(ca_cert_path, 'rb') as f:
        ca_cert = crypto.load_certificate(crypto.FILETYPE_PEM, f.read())

    # Create a certificate and set its properties
    cert = crypto.X509()
    cert.set_serial_number(1000)  # You can use a different method to generate serial numbers
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(365 * 24 * 60 * 60)  # Valid for one year
    cert.set_issuer(ca_cert.get_subject())
    cert.set_subject(req.get_subject())
    cert.set_pubkey(req.get_pubkey())
    cert.sign(ca_key, 'sha256')

    # Return the signed certificate
    return crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode('utf-8')
