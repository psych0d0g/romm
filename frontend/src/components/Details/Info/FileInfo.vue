<script setup lang="ts">
import type { PlatformSchema } from "@/__generated__";
import VersionSwitcher from "@/components/Details/VersionSwitcher.vue";
import storeDownload from "@/stores/download";
import type { Rom } from "@/stores/roms";
import { formatBytes } from "@/utils";

defineProps<{ rom: Rom; platform: PlatformSchema }>();
const downloadStore = storeDownload();
</script>
<template>
  <v-row
    v-if="rom.sibling_roms && rom.sibling_roms.length > 0"
    class="align-center my-3"
    no-gutters
  >
    <v-col cols="3" sm="3" md="2" xl="1">
      <span>Ver.</span>
    </v-col>
    <v-col>
      <version-switcher :rom="rom" :platform="platform" />
    </v-col>
  </v-row>
  <v-row v-if="!rom.multi" class="align-center my-3" no-gutters>
    <v-col cols="3" sm="3" md="2" xl="1">
      <span>File</span>
    </v-col>
    <v-col class="text-body-1">
      <span>{{ rom.file_name }}</span>
    </v-col>
  </v-row>
  <v-row v-if="rom.multi" class="align-center my-3" no-gutters>
    <v-col cols="3" sm="3" md="2" xl="1">
      <span>Files</span>
    </v-col>
    <v-col>
      <v-select
        :label="rom.file_name"
        item-title="file_name"
        v-model="downloadStore.filesToDownloadMultiFileRom"
        :items="rom.files"
        class="my-2"
        density="compact"
        variant="outlined"
        return-object
        multiple
        hide-details
        clearable
        chips
      />
    </v-col>
  </v-row>
  <v-row class="align-center my-3" no-gutters>
    <v-col cols="3" sm="3" md="2" xl="1">
      <span>Size</span>
    </v-col>
    <v-col>
      <span>{{ formatBytes(rom.file_size_bytes) }}</span>
    </v-col>
  </v-row>
  <v-row v-if="rom.tags.length > 0" class="align-center my-3" no-gutters>
    <v-col cols="3" sm="3" md="2" xl="1">
      <span>Tags</span>
    </v-col>
    <v-col>
      <v-chip
        v-for="tag in rom.tags"
        class="mr-2 py-1"
        label
        variant="outlined"
      >
        {{ tag }}
      </v-chip>
    </v-col>
  </v-row>
</template>
