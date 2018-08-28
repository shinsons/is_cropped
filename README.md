# is_cropped
Determine if one jpeg image is a cropped version of another

## Installation
```
pip install -r requirements.txt
python setup.py install
```

## NOTE:
Depending on the age and or configuration of your system, you may need to update the following libraries:
`libXext libSM libXrender`
Running `is_cropped` without these updated will throw errors about these files.

## To Run Tests

`python setup.py test`

## Usage
```
bash-3.2$ is_cropped
usage: is_cropped [-h] image image
```
