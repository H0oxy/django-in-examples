(function(){
    if (window.myBookmarklet !== undefined){
        myBookmarklet();
    }
    else {
    document.body.appendChild(
        document.createElement('script')
    ).src='https://0bf1-185-25-17-134.eu.ngrok.io/static/js/bookmarklet.js?r=' + Math.floor(Math.random()*99999999999999999999);
    }
})();