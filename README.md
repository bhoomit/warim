warim
=====
Wolfram alpha API wrapper, returns resut images in CSV.

Not so clean code. Use at your own risk :P


Usage:

1. Update Wolfram-alpha app_id in Service.py
2. Start Server with app.py

REST call example: [here](http://warim2.herokuapp.com/eqSearch?t=math&q=1+1)

Sample Response:

    {
      "data": {
        "Number line": "http://www5a.wolframalpha.com/Calculate/MSP/MSP9801e1c28881b9g2ea800003cg3i134hfd94d33?MSPStoreType=image/gif&s=49", 
        "Visual representation": "http://www5a.wolframalpha.com/Calculate/MSP/MSP9791e1c28881b9g2ea800004dc456h6aca2bi72?MSPStoreType=image/gif&s=49", 
        "Input": "http://www5a.wolframalpha.com/Calculate/MSP/MSP9761e1c28881b9g2ea800000hh3571g1e930636?MSPStoreType=image/gif&s=49", 
        "Number name": "http://www5a.wolframalpha.com/Calculate/MSP/MSP9781e1c28881b9g2ea8000034cg40g0aba5g3e2?MSPStoreType=image/gif&s=49", 
        "Result": "http://www5a.wolframalpha.com/Calculate/MSP/MSP9771e1c28881b9g2ea8000053e737chd5289f8b?MSPStoreType=image/gif&s=49", 
        "Illustration": "http://www5a.wolframalpha.com/Calculate/MSP/MSP9811e1c28881b9g2ea80000659fac5147bh0aff?MSPStoreType=image/gif&s=49"
      }, 
      "status": "success", 
      "dt": [
        "Math"
      ]
    }


