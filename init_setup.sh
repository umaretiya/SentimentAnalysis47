echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python 3.9 version"
conda create --prefix ./env python=3.9 -y

echo [$(date)]: "Activating a conda env"
source activate ./env

echo [$(date)]: "Installing a dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"