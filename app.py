from main import control

app = control.create_app()

if __name__=='__main__':
    app.run(debug=True)