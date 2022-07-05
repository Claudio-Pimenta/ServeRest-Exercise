# Run Backend Collection
newman run ServerRest.json -e LocalHost.json

# Clear Front End Users Created (Inside Backend Folder)
newman run FrontEndClearUsers.json

# Run pytest (Needs Pytest installed)
This command runs All Tests ( Run it Inside ServeRest\FrontEnd\Exercise )
python -m py.test
