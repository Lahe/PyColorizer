# Image colorizer

![](https://i.imgur.com/ukn5Vke.png)

### Installimise juhend


1. Veendu, et Sinu arvutis on olemas õiged videokoodekid, et videote mängimine kasutajaliideses töötaks. 
    (Värvimine töötab ka ilma nendeta)  
    Vajadusel installi need siit: http://www.codecguide.com/download_k-lite_codec_pack_basic.html

1. Installi Anaconda: https://www.anaconda.com/

1. Tee uus Anaconda keskkond.
   ```shell script
   conda create --name PyColorizer python=3.8
   ```
   
1. Aktiveeri keskkond.
   ```shell script
   conda activate PyColorizer
   ```

1. Ava projekti kaust

1. Navigeeri kausta `models`

1. Kui kasutad Linuxit, käivita `get_models.sh` skript. Windowsi kasutajad tehke `get_models.sh` 
    lahti ning laadige mudelifailid manuaalselt alla ja paigutage need kausta `models`.  
    
    Mudeli kaust peaks lõpuks välja nägema selline:  
    
    ![](https://i.imgur.com/AVYdiWF.png)

1. Navigeeri tagasi projekti ülemkausta

1. Installi vajalikud pakid.
    ```shell script
    pip install -r requirements.txt
    ```
   
1. Käivita kasutajaliides.
    ```shell script
   python Colorizer.py
    ```
   
1. Importi suvaline pilt või video.

1. Vajuta nupule `Colorize`. *(Video värvimine võib kaua aega võtta)*

1. Värvitud pilti või videot on võimalik näha kasutajaliideses. Lisaks salvestatakse värvitud pilt/video kettale.