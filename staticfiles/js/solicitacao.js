document.addEventListener('DOMContentLoaded', function() {
    const dataInput = document.getElementById('id_data');
    const horariosSelect = document.getElementById('id_horario');

    if (dataInput && horariosSelect) {
        dataInput.addEventListener('change', function() {
            const data = this.value;
            if (data) {
                fetch(`/api/horarios-disponiveis/?data=${data}`)
                    .then(response => response.json())
                    .then(data => {
                        horariosSelect.innerHTML = '<option value="">Selecione um horário</option>';
                        data.forEach(horario => {
                            const option = document.createElement('option');
                            option.value = horario.id;
                            option.textContent = `${horario.hora_inicio} - ${horario.hora_fim}`;
                            horariosSelect.appendChild(option);
                        });
                    })
                    .catch(error => console.error('Erro ao carregar horários:', error));
            }
        });
    }
});
