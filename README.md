# pythonOpenGL
OpenGL (Open Graphics Library), 2D ve 3D grafikler oluşturmak, görselleştirmek ve işlemek için kullanılan bir API (Application Programming Interface) ve grafik kütüphanesidir. OpenGL, çeşitli platformlarda ve programlama dillerinde kullanılabilir ve genellikle bilgisayar oyunları, simülasyonlar, bilimsel görselleştirmeler ve diğer grafik yoğun uygulamalar için tercih edilir.
1) glClear(): Bu komut, ekranı temizlemek için kullanılır. Genellikle her çizim döngüsünün başında çağrılır ve ekranın üzerine çizilmiş önceki çizimleri siler.
``` glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) ```
2) glUseProgram(): Shader programını etkinleştirmek için kullanılır. Bu komut, çizim işlemlerinizin hangi shader programını kullanacağını belirtir.
   ``` glUseProgram(shaderProgram) ```
4) glBindVertexArray(): Vertex Array Object (VAO) kullanarak çizilecek nesneyi belirlemek için kullanılır. VAO, vertex verilerini düzenler ve bu verilere erişimi kolaylaştırır.
   ``` glBindVertexArray(VAO) ```
5) glBindBuffer(): Vertex verilerini saklamak için kullanılan buffer nesnelerini etkinleştirmek için kullanılır. Genellikle vertex pozisyonları ve renklerini içeren vertex bufferları kullanılır.
  ``` glBindBuffer(GL_ARRAY_BUFFER, vertexBuffer)  ```
6) glEnableVertexAttribArray() ve glDisableVertexAttribArray(): Vertex Attribute Array'leri (VAA) etkinleştirmek veya devre dışı bırakmak için kullanılır. Bu, vertex verilerinin hangi özelliklerini kullanacağınızı belirtir.
   ``` glEnableVertexAttribArray(0); // Birinci vertex özelliğini etkinleştir
    glDisableVertexAttribArray(1); // İkinci vertex özelliğini devre dışı bırak  ```
7) glDrawArrays(): Vertex dizisini kullanarak nesneleri çizmek için kullanılır. Hangi tür nesne çizdiğinizi ve kaç vertex'in çizileceğini belirtirsiniz.
    ``` glDrawArrays(GL_TRIANGLES, 0, vertexCount)  ```
8) glUniform()**: Shader programına veri göndermek için kullanılır. Bu komutlar, shader programındaki uniform değişkenlere değerler atamanıza olanak tanır.
    ``` glUniform3f(colorLocation, 1.0f, 0.0f, 0.0f) // Bir vektörü bir uniform değişkene atama  ```
9) glViewport(): Görünen pencere boyutunu ayarlamak için kullanılır. Bu komut, pencere içeriğinin hangi bölümünün görüntüleneceğini belirtir.
    ``` glViewport(0, 0, screenWidth, screenHeight);  ```

   

https://github.com/serapcengiz/pythonOpenGL/assets/73667009/7a7baedc-7df2-4673-86cc-7a0a305bbfe2

