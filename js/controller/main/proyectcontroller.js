/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
    'use strict';
app.controller('proyectcontroller', function() {
    this.proyect = {
          barner: 'Asesorias en Contabilidad, Tributaria, Analisis Financiero y Sistemas',
          footer: 'Cali - Valle del Cauca - Accex Asociados Outsoursing',
          menus:[
                  {
                      name:'Inicio',
                      submenus:[{name:'Quienes Somos',item: 'I1'}]
                  },
                  {
                      name:'Contabilidad',
                      submenus:[
                          {name:'Actualizacion Contable',item: 'C1'},
                          {name:'Tributaria',item: 'C2'},
                          {name:'Auditoria y Revisoria Fiscal',item: 'C3'},
                          {name:'Normas Internacionales',item: 'C4'},
                          {name:'Medios Magneticos',item: 'C5'},
                          {name:'Costos y Sistema Productivo',item: 'C6'},
                          {name:'Analisis Financiero',item: 'C7'},
                          {name:'Implementacion Contable',item: 'C8'}
                      ]
                  },
                  /*{
                      name:'Sistemas',
                      submenus:[
                          {name:'Mantenimiento de Equipos',item: 'S1'},
                          {name:'Diseños Web',item: 'S2'},
                          /*{name:'Proyectos',item: 'S3'}*/
                      /*]
                  },*/
                  {
                      name:'Capacitaciones',
                      submenus:[
                          {name:'Contabilidad Basica',item: 'CA1'},
                          {name:'Contabilidad Intermedia',item: 'CA2'},
                          {name:'Contabilidad de Costos',item: 'CA3'},
                          {name:'Actualizacion Tributaria',item: 'CA4'},
                          {name:'CG-UNO',item: 'CA5'},
                          {name:'Normas Internacionales',item: 'CA6'}
                      ]
                  },
                  {
                      name:'Contactenos',
                      submenus:[{name:'Contactenos',item: 'CO1'}]
                  }
               ]
        };
});