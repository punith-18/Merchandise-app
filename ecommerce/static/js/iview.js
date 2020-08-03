var updateView = document.getElementsByClassName('view-image')

for(var i = 0; i < updateView.length; i++){
    updateView[i].addEventListener('click', function(){
        var productImage = this.dataset.product
        var action = this.dataset.action
        console.log('productImage:', productImage, 'action:', action )
    })

}