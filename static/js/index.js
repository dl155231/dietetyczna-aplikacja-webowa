$(document).ready(()=>{
    if(sessionStorage.getItem('kolor') === 'true'){
        $('body').css('filter', 'hue-rotate(320deg)');
    }
    if(sessionStorage.getItem('bw-kolor') === 'true'){
        $('body').css('filter', 'grayscale(100%) contrast(200%)');
        $('body').css('background-image', '');
        $('body').css('background-color', 'black');
        $('a').css('color', 'white');
    }
    swapColor();
    blackWhiteColor();
})
const swapColor = () =>{
    $('#swap-color').on('click', (e)=>{
        let myStorage = sessionStorage;
        if (myStorage.getItem('kolor') === 'true'){
            $('body').css('filter', 'hue-rotate(0deg)');
            myStorage.removeItem('kolor');
        }
        else {
            myStorage.setItem('kolor', true);
            $('body').css('filter', 'hue-rotate(320deg)');
        }
    })
}

const  blackWhiteColor = () =>{
    $('#bw-color').on('click', (e)=>{
        let myStorage = sessionStorage;
        if (myStorage.getItem('bw-kolor') === 'true'){
            $('body').css('filter', '');
            $('body').css('background-color', '');
            $('body').css('background-image', 'linear-gradient(to right bottom, #212529, #212529, #212529, #233200)');
            $('a').removeAttr('style');
            myStorage.removeItem('bw-kolor');
        }
        else {
            myStorage.setItem('bw-kolor', true);
            $('body').css('filter', 'grayscale(100%) contrast(200%)');
            $('body').css('background-image', '');
            $('body').css('background-color', 'black');
            $('a').css('color', 'white');

        }
    })
}