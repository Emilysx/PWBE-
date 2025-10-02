import { Component, inject, signal } from '@angular/core';
import { EditorasService } from '../../services/editoras.services';
import { AuthService } from '../../services/auth.services';
import { EmailValidator } from '@angular/forms';
import { Editora } from '../../models/editora';

@Component({
  selector: 'app-publisher.component',
  imports: [],
  templateUrl: './publisher.component.html',
  styleUrl: './publisher.component.css'
})

export class PublisherComponent {
  private svc = inject(EditorasService);
  private auth = inject(AuthService);   //Ver o token
  editoras = signal<Editora[]>([]);
  carregando = signal(true);
  erro = signal<string | null>(null);

  constructor() {
    console.log("Token de acesso: ", this.auth.token());
    
    this.svc.listar().subscribe({
      next: (data) => { this.editoras.set(data); this.carregando.set(false); },
      error: () => { this.erro.set('Falha ao carregar editoras'); this.carregando.set(false); }
    });
  }

}
