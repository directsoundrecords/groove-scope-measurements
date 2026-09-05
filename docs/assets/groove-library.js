(() => {
  const list = document.getElementById('measurement-list');
  const controls = document.querySelector('.controls');
  const search = document.getElementById('search');
  const sort = document.getElementById('sort');
  const count = document.getElementById('result-count');
  const empty = document.getElementById('empty-state');
  if (!list || !controls || !search || !sort || !count || !empty) return;
  const cards = Array.from(list.querySelectorAll('.measurement-card'));
  const normalise = text => text.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase();
  const update = () => {
    const terms = normalise(search.value).trim().split(/\s+/).filter(Boolean);
    const ordered = [...cards].sort((a, b) => {
      if (sort.value === 'title') return a.dataset.title.localeCompare(b.dataset.title);
      const comparison = a.dataset.date.localeCompare(b.dataset.date);
      return sort.value === 'oldest' ? comparison : -comparison;
    });
    let visible = 0;
    for (const card of ordered) {
      const haystack = normalise(card.dataset.search || card.textContent);
      card.hidden = !terms.every(term => haystack.includes(term));
      if (!card.hidden) visible += 1;
      list.append(card);
    }
    count.textContent = `${visible} ${visible === 1 ? 'result' : 'results'}`;
    empty.hidden = visible !== 0;
  };
  search.addEventListener('input', update);
  sort.addEventListener('change', update);
  update();
  controls.hidden = false;
})();
