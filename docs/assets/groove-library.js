(() => {
  const list = document.getElementById('measurement-list');
  const controls = document.querySelector('.controls');
  const search = document.getElementById('search');
  const sort = document.getElementById('sort');
  const count = document.getElementById('result-count');
  const empty = document.getElementById('empty-state');
  const total = document.getElementById('measurement-count');
  if (list && total) total.textContent = list.querySelectorAll('.measurement-card').length;
  if (!list || !controls || !search || !sort || !count || !empty) return;
  const cards = Array.from(list.querySelectorAll('.measurement-card'));
  const normalise = text => text.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase();
  const newestFirst = (a, b) => b.dataset.date.localeCompare(a.dataset.date);
  const metricScores = new Map([
    ['playback-rpm', rpm => Math.abs(rpm - 100 / 3)],
    ['speed-error', Math.abs],
    ['wow-flutter', value => value],
    ['separation', value => -value],
  ]);
  const sortCards = () => {
    const ordered = [...cards];
    const order = sort.value;
    if (order === 'title') return ordered.sort((a, b) => a.dataset.title.localeCompare(b.dataset.title));
    if (order === 'oldest') return ordered.sort((a, b) => newestFirst(b, a));
    const score = metricScores.get(order);
    if (!score) return ordered.sort(newestFirst);

    const scores = new Map(cards.map(card => {
      const metric = card.querySelector(`.levels [data-metric="${order}"]`);
      const value = Number.parseFloat(metric?.textContent.replace('−', '-'));
      return [card, Number.isFinite(value) ? score(value) : Infinity];
    }));
    return ordered.sort((a, b) => scores.get(a) - scores.get(b) || newestFirst(a, b));
  };
  const update = () => {
    const terms = normalise(search.value).trim().split(/\s+/).filter(Boolean);
    let visible = 0;
    for (const card of sortCards()) {
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
