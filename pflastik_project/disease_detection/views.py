<!DOCTYPE html>
<html>
<head>
    <title>Create Disease Identification Request</title>
</head>
<body>
    <h2>Create Disease Identification Request</h2>
    <form method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
</body>
</html>
