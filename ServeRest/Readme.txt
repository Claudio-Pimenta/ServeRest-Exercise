# Run Backend Collection
docker: docker run -p 3000:3000 paulogoncalvesbh/serverest:latest
collection: newman run ServerRest.json -e LocalHost.json

# Run pytest (Needs Pytest installed)
This command runs All Tests ( Run it Inside ServeRest\FrontEnd\Exercise )
python -m py.test

# Clear Front End Users Created (Inside Backend Folder)
newman run FrontEndClearUsers.json
