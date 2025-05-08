from django.http import HttpResponse


def indexview(request):
    students = [
        {"name": "aria", "age": "37", "job": "customer support"},
        {"name": "parham", "age": "24", "job": "trader"},
        {"name": "reza", "age": "26", "job": "front-end dev"},
        {"name": "mamad", "age": "23", "job": "back-end dev"},
    ]

    html = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>

    body {
    	font-family: consolas;
    }
    #customers {
      border-collapse: collapse;
      width: 100%;
    }

    #customers td, #customers th {
      border: 1px solid #ddd;
      padding: 8px;
    }

    #customers tr:nth-child(even){background-color: #f2f2f2;}

    #customers tr:hover {background-color: #ddd;}

    #customers th {
      padding-top: 12px;
      padding-bottom: 12px;
      text-align: left;
      background-color: #8D0B41;
      color: white;
    }
    </style>
    </head>
    <body>

    <h1>Students Table</h1>

    <table id="customers">
      <tr>
        <th>Name</th>
        <th>Age</th>
        <th>Job</th>
      </tr>
    """

    for i in students:
        html += f"""
          <tr>
            <td>{i['name']}</td>
            <td>{i['age']}</td>
            <td>{i['job']}</td>
          </tr>    
        """

    html += """
    </table>
    </body>
    </html>
    """

    return HttpResponse(html)
