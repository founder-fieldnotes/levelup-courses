(function () {
    const params = new URLSearchParams(location.search);
    if (params.get('embed') === '1') {
      document.documentElement.classList.add('embed');
      document.body.classList.add('embed');
    }
  })();
  