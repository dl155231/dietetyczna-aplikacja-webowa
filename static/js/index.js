$(document).ready(()=>{
    if(sessionStorage.getItem('kolor') === 'true'){
        $('body').css('filter', 'hue-rotate(320deg)');
    }
    swapColor();
})
const swapColor = () =>{
    $('#swap-color').on('click', (e)=>{
        let myStorage = sessionStorage;
        if (myStorage.getItem('kolor') === 'true'){
            console.log('elo')
            $('body').css('filter', 'hue-rotate(0deg)');
            myStorage.removeItem('kolor');
        }
        else {
            myStorage.setItem('kolor', true);
            $('body').css('filter', 'hue-rotate(320deg)');
        }
    })
}