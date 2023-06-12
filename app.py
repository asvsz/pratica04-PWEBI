from flask import Flask, render_template, redirect, request

app = Flask(__name__)

topiks = []

@app.route('/')
def index():
  return render_template('paginas/index.html')

#Rota para Adicionar Dados de uma nova Topik
@app.route('/adicionar-topik', methods=['GET', 'POST'])
def adicionar_topik():
  if request.method == 'POST':
      horario = request.form['horario']
      motorista = request.form['motorista']
      destino = request.form['destino']
      topik = {'id': len(topiks), 'motorista': motorista, 'destino': destino, 'horario': horario}
      topiks.append(topik)
      return redirect('listar-topiks')
  else:
      return render_template('paginas/adicionar.html')

#Rota para Listar as Topiks
@app.route('/listar-topiks')
def listar_topiks():
    return render_template('paginas/listar.html', topiks=topiks)
  
#Rota para Editar uma Topik
@app.route('/editar-topik/<int:id>', methods=['GET', 'POST'])
def editar_topik(id):
    topik = next((topik for topik in topiks if topik['id'] == id), None)
     
    if topik:
        if request.method == 'POST':
            topik['motorista'] = request.form['motorista']
            topik['destino'] = request.form['destino']
            topik['horario'] = request.form['horario']
            return redirect ('/listar-topiks')
        return render_template('paginas/editar.html', topik=topik)
    return "Topik não encontrada." 
  
#Rota para Excluir uma Topik
@app.route('/excluir-topik/<int:id>')
def excluir_topik(id):
    del topiks[id]
    return redirect('/listar-topiks')

if __name__ == '__main__':
  app.run(debug=True)
