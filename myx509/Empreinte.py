import OpenSSL
from OpenSSL import crypto
from base64 import encode, decode
from myx509.models import Ca, Cert
from web.models import Personne


class DigitalSignature:
    """
            Class with two static methods that sign or validate a file.
        """

    def Sign(self, id_p, pas, dat):
        """
                """
        personne = Personne.objects.get(user_id=id_p)
        id_Per = personne.id
        Certificat = Cert.objects.get(personne_id=id_Per)
        Privee = Certificat.private_key
        password = bytes(pas, encoding="utf-8")
        data=bytes(dat,encoding="utf-8")
        Private_key = crypto.load_privatekey(crypto.FILETYPE_PEM, Privee, password)
        sign = OpenSSL.crypto.sign(Private_key, data, "sha512")
        return sign

    def verify(self, id_p, sign, dat):
        personne = Personne.objects.get(user_id=id_p)
        id_Per = personne.id
        Certificat = Cert.objects.get(personne_id=id_Per)
        Certificat_P = Certificat.certificate
        data = bytes(dat, encoding="utf-8")
        Certificat_en_claire = crypto.load_certificate(crypto.FILETYPE_PEM, Certificat_P)
        try:
            if crypto.verify(Certificat_en_claire, sign, data, "sha512") is None:
                verify = True
        except OpenSSL.crypto.Error:
            verify = False
        return verify
