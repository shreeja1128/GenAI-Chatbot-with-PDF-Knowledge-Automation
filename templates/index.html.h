<!DOCTYPE html>
<html>
<head>
    <title>AskMyPDF</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
    <h2>AskMyPDF (Flask Version)</h2>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="pdf_file">
        <input type="text" name="question" placeholder="Ask your question">
        <button type="submit">Submit</button>
    </form>
    {% if response %}
        <h4>Answer:</h4>
        <p>{{ response }}</p>
    {% endif %}
</body>
</html>