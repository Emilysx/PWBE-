import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { LivrosService } from '../../services/livros.services';

@Component({
  selector: 'app-search',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent {
  titulo: string = '';
  resultados: any[] = [];
  carregando = false;

  constructor(private livrosService: LivrosService) {}

  buscarLivros() {
    if (!this.titulo.trim()) return;
    this.carregando = true;

    this.livrosService.buscarPorTitulo(this.titulo).subscribe({
      next: (dados) => {
        this.resultados = dados;
        this.carregando = false;
      },
      error: (err) => {
        console.error('Erro ao buscar livros:', err);
        this.carregando = false;
      }
    });
  }
}
