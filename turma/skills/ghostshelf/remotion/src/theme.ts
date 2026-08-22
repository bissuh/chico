/**
 * The one file a host project edits. Everything visual reads from here.
 *
 * Fill it from the project's brand.md (voice section names the register; the
 * visual identity section names the colors and the wordmark). If brand.md has
 * no visual section yet, pick the accent off the project's existing site and
 * write it back into brand.md so the next batch matches.
 */

export type Palette = {
  bg: string;
  ink: string;
  sub: string;
  accent: string;
  line: string;
  card: string;
};

export const THEME = {
  /** Shown bottom-left on every slide and reel. The account, not the person. */
  handle: '@yourhandle',

  /**
   * Optional logo in public/. Leave empty to render the handle alone.
   * Drop a transparent PNG at remotion/public/logo.png and set 'logo.png'.
   */
  logo: '',

  /**
   * Optional uppercase wordmark on photo-background slides (layout 'photo').
   * Leave empty to render nothing.
   */
  wordmark: '',

  /**
   * Google Fonts families. Any @remotion/google-fonts package works; swap the
   * imports in fonts.ts to match. Defaults are a neutral pair that reads on a
   * phone at arm's length.
   */
  fonts: {
    sans: 'Inter',
    mono: 'JetBrainsMono',
  },

  /**
   * Three palettes. 'brand' is the default and the one people recognize.
   * 'dark' and 'light' exist so a batch can breathe across a week without
   * looking like a different account.
   */
  palettes: {
    brand: {
      bg: '#2A2A2A',
      ink: '#FFFFFF',
      sub: 'rgba(255,255,255,0.85)',
      accent: '#E8E0D0',
      line: 'rgba(255,255,255,0.28)',
      card: 'rgba(255,255,255,0.12)',
    } as Palette,
    dark: {
      bg: '#101010',
      ink: '#FFFFFF',
      sub: 'rgba(255,255,255,0.66)',
      accent: '#C9C1B1',
      line: 'rgba(255,255,255,0.14)',
      card: '#1A1A1A',
    } as Palette,
    light: {
      bg: '#F3EEE3',
      ink: '#181818',
      sub: 'rgba(24,24,24,0.62)',
      accent: '#5A5145',
      line: 'rgba(24,24,24,0.16)',
      card: '#FBF8F1',
    } as Palette,
  },
} as const;

export type ThemeName = keyof typeof THEME.palettes;

export const paletteFor = (name: ThemeName = 'brand'): Palette =>
  THEME.palettes[name] ?? THEME.palettes.brand;

/** Slide canvas. 1080x1350 is the 4:5 that Instagram crops least. */
export const SLIDE = {width: 1080, height: 1350} as const;

/** Reel canvas plus pacing. 66 frames a line is ~2.2s at 30fps: readable, not slow. */
export const REEL = {
  width: 1080,
  height: 1920,
  framesPerLine: 66,
  ctaHoldFrames: 102,
} as const;

export const reelDuration = (lineCount: number) =>
  Math.max(1, lineCount) * REEL.framesPerLine + REEL.ctaHoldFrames;
