<template>
  <div class="min-h-screen bg-slate-50 dark:bg-[#060B14] text-slate-900 dark:text-slate-100 overflow-hidden font-sans transition-colors duration-300">
    
    <!-- Background Elements (Large Organic Blobs) -->
    <div class="fixed inset-0 pointer-events-none z-0">
      <div class="absolute top-[-10%] left-[-10%] w-[600px] h-[600px] bg-[#16D5D2]/10 blur-[150px] rounded-full"></div>
      <div class="absolute top-[20%] right-[-5%] w-[500px] h-[500px] bg-[#8B5CF6]/10 blur-[150px] rounded-full"></div>
      <div class="absolute bottom-[-10%] left-[20%] w-[700px] h-[700px] bg-[#4ADE80]/5 blur-[150px] rounded-full"></div>
    </div>

    <!-- NAVBAR -->
    <nav class="fixed top-0 w-full z-50 transition-all duration-300" :class="scrolled ? 'bg-white/80 dark:bg-[#060B14]/80 backdrop-blur-xl border-b border-slate-200 dark:border-white/5 py-4' : 'py-6'">
      <div class="max-w-7xl mx-auto px-6 lg:px-8 flex items-center justify-between">
        <!-- Logo (Text Only) -->
        <router-link to="/" class="flex items-center gap-2 group">
          <span class="font-sans font-bold tracking-wide text-2xl text-slate-900 dark:text-white transition-colors">Aether</span>
        </router-link>

        <!-- Desktop Links -->
        <div class="hidden md:flex items-center gap-10 text-sm font-medium text-slate-600 dark:text-slate-300">
          <a href="#" class="hover:text-slate-900 dark:hover:text-white transition-colors text-slate-900 dark:text-white">Home</a>
          <a href="#articles" class="hover:text-slate-900 dark:hover:text-white transition-colors">Articles</a>
          <a href="#features" class="hover:text-slate-900 dark:hover:text-white transition-colors">Features</a>
        </div>

        <!-- CTA -->
        <div class="hidden md:flex items-center gap-6">
          <ThemeToggle />
          <router-link to="/login" class="text-sm font-medium text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white transition-colors">Log In</router-link>
          <router-link to="/register" class="bg-[#16D5D2] hover:bg-[#36CFFF] text-[#060B14] text-sm font-bold px-6 py-2.5 rounded-full transition-all shadow-[0_0_15px_rgba(22,213,210,0.4)]">
            Sign In
          </router-link>
        </div>
      </div>
    </nav>

    <main class="relative z-10 pt-32 pb-20">
      
      <!-- HERO SECTION -->
      <section class="max-w-7xl mx-auto px-6 lg:px-8 grid lg:grid-cols-2 gap-8 items-center min-h-[85vh]">
        
        <!-- Left: Typography -->
        <div class="animate-fade-in-up flex flex-col justify-center relative z-20">
          
          <!-- Announcement Badge -->
          <div class="inline-flex items-center gap-3 px-4 py-2 rounded-full border border-slate-200 dark:border-[#16D5D2]/20 bg-white/50 dark:bg-[#16D5D2]/5 w-fit mb-8 relative overflow-hidden group backdrop-blur-md cursor-pointer shadow-sm">
            <div class="absolute inset-0 bg-gradient-to-r from-transparent via-black/5 dark:via-white/10 to-transparent -translate-x-full group-hover:animate-shimmer duration-1000"></div>
            <span class="flex h-2 w-2 rounded-full bg-[#16D5D2] shadow-[0_0_8px_#16D5D2] animate-pulse"></span>
            <span class="text-[11px] font-bold text-slate-800 dark:text-[#16D5D2] tracking-wider uppercase">Aether AI is Live</span>
          </div>

          <h1 class="text-6xl md:text-7xl font-serif font-bold leading-tight mb-6 text-slate-900 dark:text-white tracking-tight">
            Sehat Mental <br/>
            <span class="font-serif italic font-light text-[#16D5D2] dark:text-[#16D5D2]">Dimulai dari</span> <br/>
            Kamu
          </h1>
          
          <p class="text-base text-slate-600 dark:text-slate-300 mb-10 max-w-sm leading-relaxed font-sans">
            Platform pendamping kesehatan mental berbasis AI untuk mahasiswa dengan pendekatan CBT dan psikologi berbasis riset.
          </p>
          
          <div class="flex flex-wrap items-center gap-4">
            <router-link to="/register" class="bg-gradient-to-r from-[#16D5D2] to-[#36CFFF] text-[#060B14] font-bold px-8 py-3.5 rounded-full text-sm hover:shadow-[0_0_20px_rgba(22,213,210,0.5)] transition-all">
              Curhat dengan Aether
            </router-link>
            <a href="#articles" class="border border-slate-300 dark:border-white/20 text-slate-700 dark:text-white font-medium px-8 py-3.5 rounded-full text-sm hover:bg-slate-100 dark:hover:bg-white/10 transition-all">
              Baca Artikel
            </a>
          </div>
        </div>

        <!-- Right: 3D Mascot & Floating Pills -->
        <div class="relative h-[600px] w-full max-w-[600px] mx-auto flex items-center justify-center animate-blur-in">
          
          <!-- Neural Connecting Lines (SVG) -->
          <svg class="absolute inset-0 w-full h-full z-0 pointer-events-none drop-shadow-[0_0_8px_rgba(22,213,210,0.5)]" viewBox="0 0 600 600" fill="none" xmlns="http://www.w3.org/2000/svg">
            <!-- Line to Mood Stabil -->
            <path d="M300,300 C380,200 450,150 500,100" stroke="url(#cyan-glow)" stroke-width="2" class="opacity-60" stroke-linecap="round"/>
            <!-- Line to Mindfulness AI -->
            <path d="M300,300 C200,280 100,200 50,240" stroke="url(#cyan-glow)" stroke-width="2" class="opacity-60" stroke-linecap="round"/>
            <!-- Line to Sleep Quality -->
            <path d="M300,300 C200,400 150,480 100,450" stroke="url(#cyan-glow)" stroke-width="2" class="opacity-60" stroke-linecap="round"/>
            <!-- Line to Emotional Balance -->
            <path d="M300,300 C400,400 450,550 500,500" stroke="url(#cyan-glow)" stroke-width="2" class="opacity-60" stroke-linecap="round"/>
            
            <defs>
              <linearGradient id="cyan-glow" x1="0" y1="0" x2="1" y2="1">
                <stop offset="0%" stop-color="#16D5D2" stop-opacity="0.8"/>
                <stop offset="100%" stop-color="#36CFFF" stop-opacity="0.1"/>
              </linearGradient>
            </defs>
          </svg>

          <!-- Abstract Background Elements behind Mascot -->
          <div class="absolute inset-0 flex items-center justify-center z-10 pointer-events-none">
            <!-- Glowing aura behind robot -->
            <div class="absolute w-[350px] h-[350px] bg-gradient-to-tr from-[#16D5D2]/20 to-[#36CFFF]/20 blur-[80px] rounded-full animate-pulse" style="animation-duration: 4s;"></div>
            
            <!-- Floating Particles -->
            <div class="absolute top-[20%] right-[20%] w-2 h-2 bg-white rounded-full shadow-[0_0_10px_white] animate-pulse"></div>
            <div class="absolute bottom-[25%] left-[20%] w-1.5 h-1.5 bg-[#16D5D2] rounded-full shadow-[0_0_10px_#16D5D2] animate-pulse" style="animation-delay: 1s;"></div>
          </div>

          <!-- Mascot -->
          <img src="/images/aether7.png" alt="Aether Mascot" class="w-[420px] h-auto z-20 animate-float relative drop-shadow-[0_20px_50px_rgba(22,213,210,0.4)]" />
          
          <!-- Floating Glossy Pills -->
          <div class="absolute top-[12%] right-[2%] z-30 bg-[#060B14]/80 border border-[#16D5D2]/40 shadow-[0_0_20px_rgba(22,213,210,0.2)] backdrop-blur-md px-5 py-2.5 rounded-full flex items-center animate-float" style="animation-delay: 1s;">
            <div class="text-xs font-bold text-white tracking-wide">Mood Stabil</div>
          </div>

          <div class="absolute top-[38%] left-[-5%] z-30 bg-[#060B14]/80 border border-[#16D5D2]/40 shadow-[0_0_20px_rgba(22,213,210,0.2)] backdrop-blur-md px-5 py-2.5 rounded-full flex items-center animate-float-slow" style="animation-delay: 2s;">
            <div class="text-xs font-bold text-white tracking-wide">Mindfulness AI</div>
          </div>
          
          <div class="absolute bottom-[22%] left-[8%] z-30 bg-[#060B14]/80 border border-[#16D5D2]/40 shadow-[0_0_20px_rgba(22,213,210,0.2)] backdrop-blur-md px-5 py-2.5 rounded-full flex items-center animate-float-slow" style="animation-delay: 1.5s;">
            <div class="text-xs font-bold text-white tracking-wide">Sleep Quality</div>
          </div>

          <div class="absolute bottom-[12%] right-[0%] z-30 bg-[#060B14]/80 border border-[#8B5CF6]/40 shadow-[0_0_20px_rgba(139,92,246,0.2)] backdrop-blur-md px-5 py-2.5 rounded-full flex items-center animate-float" style="animation-delay: 0.5s;">
            <div class="text-xs font-bold text-white tracking-wide">Emotional Balance</div>
          </div>
        </div>
      </section>

      <!-- FEATURE SECTION -->
      <section id="features" class="max-w-7xl mx-auto px-6 lg:px-8 py-20">
        <div class="text-center mb-10">
          <h3 class="text-sm font-bold tracking-widest text-slate-400 uppercase">Feature Section</h3>
        </div>

        <div class="grid md:grid-cols-3 gap-6 relative">
          <!-- Decorative background glow for features -->
          <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-[200px] bg-[#16D5D2]/5 blur-[100px] pointer-events-none"></div>
          
          <div class="glass-panel p-8 rounded-3xl hover:bg-slate-100 dark:hover:bg-white/10 hover:border-[#16D5D2]/30 transition-all group relative overflow-hidden bg-white/50 dark:bg-transparent border border-slate-200 dark:border-white/5">
            <div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
               <Brain :size="80" class="text-slate-900 dark:text-white" />
            </div>
            <div class="w-12 h-12 rounded-2xl bg-[#16D5D2]/10 flex items-center justify-center text-[#16D5D2] mb-6 border border-[#16D5D2]/20 group-hover:scale-110 transition-transform">
              <Brain :size="24" />
            </div>
            <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-3">AI Emotional Support</h3>
            <p class="text-slate-600 dark:text-slate-400 leading-relaxed text-sm">AI pendamping suportif & empatik. Ceritakan permasalahan dan kecemasanmu kapan saja tanpa takut dihakimi.</p>
          </div>

          <div class="glass-panel p-8 rounded-3xl hover:bg-slate-100 dark:hover:bg-white/10 hover:border-[#36CFFF]/30 transition-all group relative overflow-hidden bg-white/50 dark:bg-transparent border border-slate-200 dark:border-white/5">
            <div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
               <Activity :size="80" class="text-slate-900 dark:text-white" />
            </div>
            <div class="w-12 h-12 rounded-2xl bg-[#36CFFF]/10 flex items-center justify-center text-[#36CFFF] mb-6 border border-[#36CFFF]/20 group-hover:scale-110 transition-transform">
              <Activity :size="24" />
            </div>
            <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-3">Mood Journal & Analytics</h3>
            <p class="text-slate-600 dark:text-slate-400 leading-relaxed text-sm">Pelacakan status emosi harian dan tren dinamika kesehatan mentalmu secara visual dan mudah dipahami.</p>
          </div>

          <div class="glass-panel p-8 rounded-3xl hover:bg-slate-100 dark:hover:bg-white/10 hover:border-[#8B5CF6]/30 transition-all group relative overflow-hidden bg-white/50 dark:bg-transparent border border-slate-200 dark:border-white/5">
            <div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
               <Sparkles :size="80" class="text-slate-900 dark:text-white" />
            </div>
            <div class="w-12 h-12 rounded-2xl bg-[#8B5CF6]/10 flex items-center justify-center text-[#8B5CF6] mb-6 border border-[#8B5CF6]/20 group-hover:scale-110 transition-transform">
              <Sparkles :size="24" />
            </div>
            <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-3">Evidence-based CBT</h3>
            <p class="text-slate-600 dark:text-slate-400 leading-relaxed text-sm">Latihan Cognitive Behavioral Therapy (CBT) terstruktur dan terpandu otomatis untuk membantumu merasa lebih baik.</p>
          </div>
        </div>
      </section>

      <!-- HOW IT WORKS SECTION -->
      <section id="how" class="max-w-7xl mx-auto px-6 lg:px-8 py-20">
        <div class="text-center mb-16">
          <h3 class="text-sm font-bold tracking-widest text-slate-400 uppercase">How It Works</h3>
        </div>

        <div class="flex flex-col md:flex-row justify-between items-center gap-8 relative">
          
          <!-- Connecting Line (Desktop) -->
          <div class="hidden md:block absolute top-16 left-16 right-16 h-[2px] bg-gradient-to-r from-transparent via-[#16D5D2]/30 to-transparent z-0"></div>

          <!-- Step 1 -->
          <div class="flex flex-col items-center text-center z-10 w-full md:w-1/4 group">
            <div class="w-32 h-32 bg-white dark:bg-[#0A172B] border border-slate-200 dark:border-white/10 rounded-full flex items-center justify-center mb-6 overflow-hidden relative group-hover:border-[#16D5D2]/50 transition-colors shadow-sm dark:shadow-[0_0_30px_rgba(0,0,0,0.5)]">
              <div class="absolute inset-0 bg-[#16D5D2]/5 opacity-0 group-hover:opacity-100 transition-opacity"></div>
              <img src="/images/aether8.png" class="w-20 object-contain drop-shadow-md group-hover:scale-110 transition-transform" />
            </div>
            <h4 class="text-lg font-bold text-slate-900 dark:text-white">1. Curhat</h4>
            <p class="text-slate-600 dark:text-slate-400 text-sm mt-2 max-w-[200px]">Ceritakan apa yang sedang membebani pikiranmu.</p>
          </div>

          <!-- Arrow -->
          <div class="hidden md:block flex-shrink-0 text-[#16D5D2]/50 z-10">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </div>

          <!-- Step 2 -->
          <div class="flex flex-col items-center text-center z-10 w-full md:w-1/4 group">
            <div class="w-32 h-32 bg-white dark:bg-[#0A172B] border border-slate-200 dark:border-white/10 rounded-full flex items-center justify-center mb-6 relative group-hover:border-[#16D5D2]/50 transition-colors shadow-sm dark:shadow-[0_0_30px_rgba(0,0,0,0.5)]">
               <div class="absolute inset-0 bg-[#16D5D2]/5 opacity-0 group-hover:opacity-100 transition-opacity rounded-full"></div>
               <svg class="w-10 h-10 text-[#16D5D2] group-hover:scale-110 transition-transform" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2a10 10 0 100 20 10 10 0 000-20zM12 6v6l4 2"/></svg>
            </div>
            <h4 class="text-lg font-bold text-slate-900 dark:text-white">2. Analisis</h4>
            <p class="text-slate-600 dark:text-slate-400 text-sm mt-2 max-w-[200px]">Aether menganalisis kondisi emosimu secara mendalam.</p>
          </div>

          <!-- Arrow -->
          <div class="hidden md:block flex-shrink-0 text-[#16D5D2]/50 z-10">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </div>

          <!-- Step 3 -->
          <div class="flex flex-col items-center text-center z-10 w-full md:w-1/4 group">
            <div class="w-32 h-32 bg-white dark:bg-[#0A172B] border border-slate-200 dark:border-white/10 rounded-full flex items-center justify-center mb-6 relative group-hover:border-[#16D5D2]/50 transition-colors shadow-sm dark:shadow-[0_0_30px_rgba(0,0,0,0.5)]">
              <div class="absolute inset-0 bg-[#16D5D2]/5 opacity-0 group-hover:opacity-100 transition-opacity rounded-full"></div>
              <svg class="w-10 h-10 text-[#16D5D2] group-hover:scale-110 transition-transform" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8l-6-6z M14 3v5h5 M16 13H8 M16 17H8 M10 9H8"/></svg>
            </div>
            <h4 class="text-lg font-bold text-slate-900 dark:text-white">3. Terapi CBT</h4>
            <p class="text-slate-600 dark:text-slate-400 text-sm mt-2 max-w-[200px]">Dapatkan latihan dan rekomendasi berbasis riset.</p>
          </div>

          <!-- Arrow -->
          <div class="hidden md:block flex-shrink-0 text-[#16D5D2]/50 z-10">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </div>

          <!-- Step 4 -->
          <div class="flex flex-col items-center text-center z-10 w-full md:w-1/4 group">
            <div class="w-32 h-32 bg-white dark:bg-[#0A172B] border border-slate-200 dark:border-white/10 rounded-full flex items-center justify-center mb-6 relative group-hover:border-[#16D5D2]/50 transition-colors shadow-sm dark:shadow-[0_0_30px_rgba(0,0,0,0.5)]">
              <div class="absolute inset-0 bg-[#16D5D2]/5 opacity-0 group-hover:opacity-100 transition-opacity rounded-full"></div>
              <svg class="w-10 h-10 text-[#16D5D2] group-hover:scale-110 transition-transform" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
            </div>
            <h4 class="text-lg font-bold text-slate-900 dark:text-white">4. Pulih</h4>
            <p class="text-slate-600 dark:text-slate-400 text-sm mt-2 max-w-[200px]">Pantau perkembangan mentalmu menuju keseimbangan.</p>
          </div>

        </div>
      </section>

      <!-- ARTICLES SECTION -->
      <section id="articles" class="max-w-5xl mx-auto px-6 lg:px-8 py-20">
        <div class="text-center mb-10">
          <h3 class="text-sm font-bold tracking-widest text-slate-400 uppercase">Article Section</h3>
        </div>

        <!-- Article Categories Nav -->
        <div class="flex flex-wrap justify-center md:justify-between items-center gap-4 mb-10 border-b border-white/10 pb-6">
          <button v-for="cat in categories" :key="cat" @click="selectedCategory = cat"
            class="text-sm font-bold transition-colors pb-1 border-b-2"
            :class="selectedCategory === cat ? 'text-[#16D5D2] border-[#16D5D2]' : 'text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white border-transparent'">
            {{ cat }}
          </button>
        </div>

        <!-- Dynamic Article Grid -->
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6 animate-fade-in-up">
          <div v-for="article in filteredArticles" :key="article.title" @click="openArticle(article)"
            class="glass-panel p-6 rounded-3xl cursor-pointer hover:bg-slate-100 dark:hover:bg-white/5 hover:-translate-y-1 transition-all group flex flex-col h-full bg-white/50 dark:bg-transparent border border-slate-200 dark:border-transparent hover:border-[#16D5D2]/30 shadow-sm dark:shadow-none">
            <div class="w-full bg-slate-100 dark:bg-[#0A172B] border border-slate-200 dark:border-white/5 rounded-2xl h-40 flex items-center justify-center overflow-hidden mb-6 group-hover:shadow-[0_10px_30px_rgba(22,213,210,0.15)] transition-shadow">
               <div class="text-5xl group-hover:scale-110 transition-transform">{{ article.emoji }}</div>
            </div>
            <div class="flex items-center gap-3 text-xs text-[#16D5D2] font-semibold mb-3">
              <span class="px-2 py-1 rounded-md bg-[#16D5D2]/10">{{ article.tag }}</span>
              <span class="text-slate-500">·</span>
              <span class="text-slate-500 dark:text-slate-400">{{ article.readTime }}</span>
            </div>
            <h3 class="text-xl font-serif font-bold text-slate-900 dark:text-white mb-3 line-clamp-2 group-hover:text-[#16D5D2] transition-colors">{{ article.title }}</h3>
            <p class="text-slate-600 dark:text-slate-400 text-sm leading-relaxed line-clamp-3 mb-4 flex-1">
              {{ article.fullContent }}
            </p>
            <div class="mt-auto text-[#16D5D2] text-sm font-bold flex items-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
              Baca Artikel <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </div>
          </div>
        </div>
      </section>

      <!-- CALL TO ACTION -->
      <section class="max-w-5xl mx-auto px-6 lg:px-8 py-20">
        <div class="text-center mb-10">
          <h3 class="text-sm font-bold tracking-widest text-slate-400 uppercase">Call to Action</h3>
        </div>

        <div class="glass-panel rounded-[40px] p-10 md:p-14 relative overflow-hidden flex flex-col md:flex-row items-center justify-between border-slate-200 dark:border-[#16D5D2]/30 bg-white/80 dark:bg-[#060B14]/80 dark:bg-gradient-to-r dark:from-[#16D5D2]/10 dark:to-[#8B5CF6]/10 shadow-lg dark:shadow-none">
          
          <div class="relative z-10 max-w-lg text-center md:text-left mb-10 md:mb-0">
            <h2 class="text-3xl md:text-4xl font-serif font-bold mb-8 leading-tight text-slate-900 dark:text-white">
              Kamu tidak harus menghadapi <br/> semuanya sendirian.
            </h2>
            <router-link to="/register" class="bg-[#16D5D2] hover:bg-[#36CFFF] text-[#060B14] font-bold px-8 py-3.5 rounded-full text-sm transition-all inline-block">
              Mulai Curhat Sekarang
            </router-link>
          </div>

          <div class="relative z-10 w-full md:w-1/3 flex justify-center">
            <img src="/images/aether1.png" alt="Aether" class="w-48 h-auto animate-float drop-shadow-[0_10px_30px_rgba(22,213,210,0.4)]" />
          </div>
        </div>
      </section>

    </main>
    
    <!-- FOOTER -->
    <footer class="border-t border-slate-200 dark:border-white/5 pt-16 pb-8 bg-slate-100 dark:bg-[#02050A] transition-colors">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">
          <div class="md:col-span-2">
            <div class="flex items-center gap-2 mb-6">
              <span class="font-sans font-bold text-2xl text-slate-900 dark:text-white">Aether</span>
            </div>
            <p class="text-slate-600 dark:text-slate-400 text-sm max-w-sm leading-relaxed mb-6">
              Platform AI pendamping kesehatan mental pertama yang didesain khusus untuk mahasiswa, menggunakan pendekatan psikologi dan Cognitive Behavioral Therapy (CBT).
            </p>
          </div>
          
          <div>
            <h4 class="text-slate-900 dark:text-white font-bold mb-6">Platform</h4>
            <ul class="space-y-4 text-sm text-slate-400">
              <li><a href="#" class="hover:text-[#16D5D2] transition-colors">Features</a></li>
              <li><a href="#" class="hover:text-[#16D5D2] transition-colors">How it Works</a></li>
              <li><a href="#" class="hover:text-[#16D5D2] transition-colors">Articles</a></li>
              <li><a href="#" class="hover:text-[#16D5D2] transition-colors">Pricing</a></li>
            </ul>
          </div>

          <div>
            <h4 class="text-slate-900 dark:text-white font-bold mb-6">Legal</h4>
            <ul class="space-y-4 text-sm text-slate-600 dark:text-slate-400">
              <li><a href="#" class="hover:text-[#16D5D2] transition-colors">Privacy Policy</a></li>
              <li><a href="#" class="hover:text-[#16D5D2] transition-colors">Terms of Service</a></li>
              <li><a href="#" class="hover:text-[#16D5D2] transition-colors">Crisis Support</a></li>
            </ul>
          </div>
        </div>

        <div class="border-t border-slate-200 dark:border-white/5 pt-8 flex flex-col md:flex-row items-center justify-between gap-4 text-sm text-slate-500">
          <p>© 2024 Aether Mental Health AI. All rights reserved.</p>
          <div class="flex gap-4">
             <span>Instagram</span>
             <span>Twitter</span>
             <span>LinkedIn</span>
          </div>
        </div>
      </div>
    </footer>

    <!-- ARTICLE MODAL -->
    <Teleport to="body">
      <Transition name="page">
        <div v-if="selectedArticle" class="fixed inset-0 z-[100] flex items-center justify-center p-4 bg-slate-900/60 dark:bg-[#020817]/80 backdrop-blur-sm" @click.self="selectedArticle = null">
          <div class="glass-panel w-full max-w-3xl max-h-[90vh] overflow-y-auto p-8 lg:p-12 bg-white dark:bg-[#060B14]">
            <button @click="selectedArticle = null" class="absolute top-6 right-6 text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg>
            </button>
            
            <div class="text-5xl mb-6">{{ selectedArticle.emoji }}</div>
            <div class="flex items-center gap-3 text-sm text-[#16D5D2] font-semibold mb-4">
              <span>{{ selectedArticle.tag }}</span>
              <span class="text-slate-500">·</span>
              <span class="text-slate-400">{{ selectedArticle.readTime }}</span>
            </div>
            
            <h2 class="text-4xl font-serif text-white mb-6">{{ selectedArticle.title }}</h2>
            <p class="text-lg text-slate-300 leading-relaxed mb-8 whitespace-pre-line">{{ selectedArticle.fullContent }}</p>
            
            <div v-if="selectedArticle.keyPoints?.length" class="bg-white/5 rounded-2xl p-6 border border-white/10 mb-8">
              <h3 class="text-xl font-bold text-white mb-4">📌 Poin-Poin Utama</h3>
              <ul class="space-y-3">
                <li v-for="pt in selectedArticle.keyPoints" :key="pt" class="flex gap-3 text-slate-300">
                  <span class="text-[#16D5D2] flex-shrink-0">✦</span>
                  {{ pt }}
                </li>
              </ul>
            </div>
            
            <div class="flex justify-end pt-6 border-t border-white/10 mt-8">
              <router-link to="/register" class="btn-primary-glass">Curhat dengan Aether →</router-link>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>

  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { Brain, Activity, Sparkles } from '@lucide/vue'
import ThemeToggle from '../components/ThemeToggle.vue'

const scrolled = ref(false)
const selectedArticle = ref(null)

const handleScroll = () => {
  scrolled.value = window.scrollY > 50
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})

const categories = ['Semua', 'Kecemasan', 'Burnout', 'Self-care', 'Mindfulness', 'Tidur Sehat']
const selectedCategory = ref('Semua')

const allArticles = ref([
  {
    emoji: '📚',
    tag: 'Burnout',
    title: 'Kenali 7 Tanda Burnout Akademik',
    readTime: '7 min',
    fullContent: 'Burnout bukan sekadar kelelahan biasa, tapi kondisi stres kronis yang membuatmu merasa kosong dan kehilangan motivasi belajar. Mari kenali tanda-tandanya sejak dini dan cegah dampaknya terhadap performamu.',
    keyPoints: [
      'Kelelahan fisik dan emosional yang terus-menerus',
      'Merasa sinis dan terasing dari kegiatan perkuliahan',
      'Penurunan prestasi dan produktivitas'
    ]
  },
  {
    emoji: '🌊',
    tag: 'Kecemasan',
    title: 'Cara Mengatasi Panic Attack Saat Ujian',
    readTime: '5 min',
    fullContent: 'Tiba-tiba jantung berdebar kencang dan napas sesak saat membalik kertas ujian? Itu bisa jadi serangan panik. Berikut adalah teknik grounding 5-4-3-2-1 yang bisa kamu lakukan diam-diam di bangku ujian.',
    keyPoints: [
      'Fokus pada 5 benda yang bisa dilihat',
      'Sentuh 4 benda di sekitarmu',
      'Tarik napas perlahan melalui hidung, buang lewat mulut'
    ]
  },
  {
    emoji: '🌱',
    tag: 'Self-care',
    title: 'Membangun Batasan: Kapan Harus Berkata "Tidak"',
    readTime: '6 min',
    fullContent: 'Sering merasa over-committed dengan kepanitiaan dan tugas kelompok? Belajar berkata "tidak" tanpa rasa bersalah adalah bentuk tertinggi dari merawat diri sendiri (self-care).',
    keyPoints: [
      'Pahami kapasitas waktu dan energimu',
      'Gunakan teknik penolakan asertif',
      'Ingat bahwa kamu tidak bertanggung jawab atas perasaan orang lain'
    ]
  },
  {
    emoji: '🧘‍♂️',
    tag: 'Mindfulness',
    title: 'Meditasi 10 Menit untuk Memulai Hari',
    readTime: '4 min',
    fullContent: 'Memulai pagi dengan tergesa-gesa akan mengatur ritme kecemasan sepanjang hari. Luangkan 10 menit pertama setelah bangun tidur untuk menyadari napasmu.',
    keyPoints: [
      'Duduk bersila di tempat yang tenang',
      'Fokus hanya pada udara yang keluar masuk hidung',
      'Jika pikiran mengembara, kembalikan fokus pada napas dengan lembut'
    ]
  },
  {
    emoji: '🌙',
    tag: 'Tidur Sehat',
    title: 'Bahaya Begadang untuk Skripsi',
    readTime: '8 min',
    fullContent: 'Mengerjakan skripsi semalaman mungkin terasa produktif, tapi sebenarnya merusak kemampuan memori jangka pendek otakmu. Tidur yang cukup justru kunci utama analisis yang tajam.',
    keyPoints: [
      'Otak mengkonsolidasi informasi saat fase Deep Sleep',
      'Begadang meningkatkan hormon kortisol (stres)',
      'Atur jadwal tidur yang konsisten, bahkan di akhir pekan'
    ]
  },
  {
    emoji: '❤️',
    tag: 'Self-care',
    title: 'Jurnal Syukur: Terapi Gratis Setiap Hari',
    readTime: '5 min',
    fullContent: 'Mencatat tiga hal kecil yang patut disyukuri setiap malam terbukti secara klinis dapat meningkatkan kebahagiaan dan menurunkan gejala depresi ringan pada mahasiswa.',
    keyPoints: [
      'Tuliskan hal-hal yang sangat spesifik',
      'Tidak perlu hal besar, es kopi yang enak pun bisa disyukuri',
      'Lakukan rutin minimal selama 21 hari'
    ]
  }
])

const filteredArticles = computed(() => {
  if (selectedCategory.value === 'Semua') {
    return allArticles.value
  }
  return allArticles.value.filter(a => a.tag === selectedCategory.value)
})

const openArticle = (art) => {
  selectedCategory.value = selectedCategory.value // dummy to keep eslint quiet if needed
  selectedArticle.value = art
}
</script>
