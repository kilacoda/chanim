# कैनिम
यह [Manim](https://www.github.com/ManimCommunity/manim) (जो [3Blue1Brown](https://github.com/3b1b/manim) के द्वारा प्रथमतः लिखा हुआ है) के लिए एक विस्तार उपकरण है, जिसका उद्देश्य रसायन विज्ञान के क्षेत्र में ऐनीमैटिड चलचित्र बनाने में सहायता करना है।

## स्थापन (`pip` के द्वारा)
`pip install chanim`

## स्थापन (सूत्र से)
१. अपने OS के अनुसार [यहाँ](https://docs.manim.community/en/latest/installation.html) पर लिखी प्रक्रिया का पालन करते हुए manim की बाहरी निर्भरताएँ संस्थापित करें।

२. इस रेपॉसीटोरी को क्लोन करें

३. क्लोन किए गए डायरेक्टरी में एक टर्मिनल विंडो खोलें, और `pip install -e .` चलाएं, अन्यतः यदि आपको [poetry](https://python-poetry.org) इस्तेमाल करना हों, तो आप `poetry install` का भी प्रयोग कार सकते हैं। दोनों तरीकों से manim भी स्थापित हों जाएगा। (लेकिन आपको बाहरी निर्भरताएँ फिर भी स्थापित करनी होंगी)

अब आप किसी भी अन्य Python पैकेज की तरह `from chanim import <*|किसी_वस्तु_का_नाम>` से इसे इस्तेमाल करना शुरू कर सकते हैं।

## प्रयोग

कैनिम को काम करते हुए देखने के लिए यह छोटा सा उदाहरण प्रस्तुत करता हूँ।

```py
from chanim import *

class ChanimScene(Scene):
    def construct(self):
        ## ChemWithName एक रसायन आरेख के साथ एक नाम का लेबल बनाता है।
        chem = ChemWithName("*6((=O)-N(-CH_3)-*5(-N=-N(-CH_3)-=)--(=O)-N(-H_3C)-)", "Caffeine")

        self.play(chem.creation_anim())
        self.wait()
```

इसे एक python (`.py`) फाइल में टाइप करें। मै मान रहा हूँ की आपने इसे `chem.py` के नाम से सहेजा होगा।

अपने कमांड प्रॉम्प्ट/टर्मिनल में यह लिखें (मानते हुए की आप फ़ाइल के मूल फ़ोल्डर में हैं):

```sh
manim -p -qm chem.py ChanimScene
```

इससे आपका सीन रेन्डर हों जाएगा और आपके पसंदीदा वीडियो प्लेयर में निम्न वीडिओ चल जानी चाहिए।



https://user-images.githubusercontent.com/65204531/124297601-dcafcf80-db78-11eb-936b-cdc913c91f25
