const btnDelete = document.querySelectorAll('a.btn-delete')

if(btnDelete){ 
    const btnArray=Array.from(btnDelete);
    btnArray.forEach((btn)=>{
        btn.addEventListener('click',(e)=>{
            if(!confirm('Desea eliminar este producto?')){
                e.preventDefault();
            }
        });
    })
}