<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('chat_sessions', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')->constrained()->cascadeOnDelete();
            $table->text('user_message'); // Pesan curhatan mahasiswa
            $table->text('ai_response');  // Balasan dari sistem / Gemini
            $table->string('risk_indicator')->nullable(); // Warna indikator (Hijau/Kuning/Merah)
            $table->integer('total_score')->default(0); // Menyimpan total skor Rule-Based
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('chat_sessions');
    }
};
