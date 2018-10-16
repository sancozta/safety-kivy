### Safetykivy

Recomenda-se utilizar um terminal bash para facilitar o desenvolvimeto e criação do ambiente local.

#### Instalando o Kivy

	python -m pip install --upgrade pip wheel setuptools
	python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
	python -m pip install kivy.deps.gstreamer
	python -m pip install kivy.deps.angle
	python -m pip install kivy 
    
#### Instalando Buildozer

    pip install --upgrade buildozer
    git clone https://github.com/kivy/buildozer
    cd buildozer
    python setup.py build
    python -m pip install -e .

#### Instalando Dependências

	pip install -r requirements.txt