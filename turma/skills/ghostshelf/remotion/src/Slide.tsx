import {AbsoluteFill, Img, staticFile, useCurrentFrame} from 'remotion';
import {SANS, MONO} from './fonts';
import {THEME, paletteFor, type ThemeName, type Palette} from './theme';

type Item = {label: string; note?: string};

export type SlideProps = {
  theme?: ThemeName;
  layout?: 'cover' | 'statement' | 'list' | 'prompt' | 'detail' | 'photo';
  kicker?: string;
  title?: string;
  subtitle?: string;
  body?: string;
  items?: Item[];
  prompt?: string;
  promptLabel?: string;
  tip?: string;
  tipLabel?: string;
  footnote?: string;
  slideNo?: number;
  slideTotal?: number;
  handle?: string;
  /** layout 'photo' only: filename in public/, or an absolute URL. */
  bg?: string;
};

const Texture: React.FC<{light: boolean}> = ({light}) => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill
      style={{
        opacity: light ? 0.35 : 0.05,
        mixBlendMode: light ? 'multiply' : 'soft-light',
        backgroundImage: `radial-gradient(circle at ${15 + (frame % 20)}% ${25 + (frame % 18)}%, ${
          light ? '#000' : '#fff'
        } 0.5px, transparent 1.5px)`,
        backgroundSize: '6px 6px',
        pointerEvents: 'none',
      }}
    />
  );
};

const Footer: React.FC<{
  c: Palette;
  handle: string;
  slideNo?: number;
  slideTotal?: number;
  footnote?: string;
}> = ({c, handle, slideNo, slideTotal, footnote}) => (
  <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center', opacity: 0.9}}>
    <div style={{display: 'flex', alignItems: 'center', gap: 14}}>
      {THEME.logo ? <Img src={staticFile(THEME.logo)} style={{height: 40, width: 'auto'}} /> : null}
      <div style={{fontFamily: SANS, fontWeight: 600, fontSize: 22, color: c.sub}}>{handle}</div>
    </div>
    <div style={{fontFamily: SANS, fontWeight: 600, fontSize: 22, color: c.sub, letterSpacing: '0.06em'}}>
      {footnote ? footnote : slideNo ? `${slideNo} / ${slideTotal ?? 7}` : ''}
    </div>
  </div>
);

const resolveSrc = (raw?: string) => (!raw ? undefined : raw.startsWith('http') ? raw : staticFile(raw));

export const Slide: React.FC<SlideProps> = ({
  theme = 'brand',
  layout = 'statement',
  kicker,
  title,
  subtitle,
  body,
  items = [],
  prompt,
  promptLabel = 'Prompt',
  tip,
  tipLabel = 'Tip',
  footnote,
  slideNo,
  slideTotal,
  handle = THEME.handle,
  bg,
}) => {
  const c = paletteFor(theme);
  const h1 = {fontFamily: SANS, fontWeight: 800 as const, color: c.ink, lineHeight: 1.05, letterSpacing: '-0.02em'};
  const photo = layout === 'photo';
  const src = resolveSrc(bg);

  // Photo layout gets its own ink: white over a scrim, whatever the palette says.
  const pc: Palette = photo
    ? {...c, ink: '#FFFFFF', sub: 'rgba(255,255,255,0.88)', line: 'rgba(255,255,255,0.3)'}
    : c;
  const shadow = photo ? {textShadow: '0 4px 22px rgba(0,0,0,0.75)'} : {};

  return (
    <AbsoluteFill style={{backgroundColor: photo ? '#101010' : c.bg, fontFamily: SANS}}>
      {photo && src ? (
        <>
          <AbsoluteFill style={{overflow: 'hidden'}}>
            <Img
              src={src}
              style={{width: '100%', height: '100%', objectFit: 'cover', transform: 'scale(1.04)'}}
            />
          </AbsoluteFill>
          <AbsoluteFill style={{backgroundColor: c.bg, mixBlendMode: 'multiply', opacity: 0.5}} />
          <AbsoluteFill
            style={{
              background:
                'linear-gradient(180deg, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.15) 32%, rgba(0,0,0,0.35) 62%, rgba(0,0,0,0.82) 100%)',
            }}
          />
        </>
      ) : null}

      {!photo ? <Texture light={theme === 'light'} /> : null}

      <AbsoluteFill style={{padding: photo ? 84 : 100, display: 'flex', flexDirection: 'column'}}>
        {photo && THEME.wordmark ? (
          <div
            style={{
              fontFamily: SANS,
              fontWeight: 800,
              fontSize: 30,
              letterSpacing: '0.18em',
              color: '#FFFFFF',
              textTransform: 'uppercase',
              ...shadow,
            }}
          >
            {THEME.wordmark}
          </div>
        ) : null}

        {kicker ? (
          <div
            style={{
              fontFamily: SANS,
              fontWeight: 700,
              fontSize: 26,
              letterSpacing: '0.16em',
              textTransform: 'uppercase',
              color: pc.accent,
              marginTop: photo && THEME.wordmark ? 12 : 0,
              ...shadow,
            }}
          >
            {kicker}
          </div>
        ) : (
          <div />
        )}

        <div
          style={{
            flex: 1,
            display: 'flex',
            flexDirection: 'column',
            justifyContent: photo ? 'flex-end' : 'center',
            paddingTop: 32,
            paddingBottom: 32,
          }}
        >
          {(layout === 'cover' || layout === 'photo') && (
            <div>
              {title ? <div style={{...h1, color: pc.ink, fontSize: photo ? 100 : 108, ...shadow}}>{title}</div> : null}
              {subtitle ? (
                <div
                  style={{
                    fontFamily: SANS,
                    fontWeight: 500,
                    fontSize: 42,
                    color: pc.sub,
                    marginTop: 26,
                    maxWidth: 860,
                    ...shadow,
                  }}
                >
                  {subtitle}
                </div>
              ) : null}
            </div>
          )}

          {layout === 'statement' && (
            <div>
              {title ? <div style={{...h1, fontSize: 92}}>{title}</div> : null}
              {subtitle ? (
                <div
                  style={{fontFamily: SANS, fontWeight: 500, fontSize: 40, lineHeight: 1.35, color: c.sub, marginTop: 28, maxWidth: 820}}
                >
                  {subtitle}
                </div>
              ) : null}
            </div>
          )}

          {layout === 'list' && (
            <div>
              {title ? <div style={{...h1, fontSize: 64, marginBottom: 36}}>{title}</div> : null}
              <div style={{display: 'flex', flexDirection: 'column'}}>
                {items.map((it, i) => (
                  <div
                    key={i}
                    style={{
                      display: 'flex',
                      gap: 26,
                      alignItems: 'baseline',
                      padding: '24px 0',
                      borderTop: i === 0 ? `2px solid ${c.line}` : 'none',
                      borderBottom: `2px solid ${c.line}`,
                    }}
                  >
                    <div style={{fontFamily: SANS, fontWeight: 800, fontSize: 40, color: c.accent, minWidth: 54}}>
                      {String(i + 1).padStart(2, '0')}
                    </div>
                    <div>
                      <div style={{fontFamily: SANS, fontWeight: 700, fontSize: 42, color: c.ink, lineHeight: 1.1}}>
                        {it.label}
                      </div>
                      {it.note ? (
                        <div style={{fontFamily: SANS, fontWeight: 400, fontSize: 30, color: c.sub, marginTop: 6}}>
                          {it.note}
                        </div>
                      ) : null}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {layout === 'prompt' && (
            <div>
              {title ? <div style={{...h1, fontSize: 60, marginBottom: 28}}>{title}</div> : null}
              <div style={{background: c.card, border: `2px solid ${c.line}`, borderRadius: 22, padding: 44}}>
                <div
                  style={{
                    fontFamily: MONO,
                    fontWeight: 700,
                    fontSize: 23,
                    letterSpacing: '0.08em',
                    textTransform: 'uppercase',
                    color: c.accent,
                    marginBottom: 22,
                  }}
                >
                  {promptLabel}
                </div>
                <div style={{fontFamily: MONO, fontWeight: 400, fontSize: 33, lineHeight: 1.5, color: c.ink}}>{prompt}</div>
              </div>
              {subtitle ? (
                <div style={{fontFamily: SANS, fontWeight: 500, fontSize: 32, color: c.sub, marginTop: 26}}>{subtitle}</div>
              ) : null}
            </div>
          )}

          {layout === 'detail' && (
            <div>
              {title ? <div style={{...h1, fontSize: 56, marginBottom: 26}}>{title}</div> : null}
              {body ? (
                <div style={{fontFamily: SANS, fontWeight: 400, fontSize: 37, lineHeight: 1.46, color: c.ink, maxWidth: 880}}>
                  {body}
                </div>
              ) : null}
              {tip ? (
                <div
                  style={{marginTop: 32, padding: '22px 28px', background: c.card, border: `2px solid ${c.line}`, borderRadius: 16, maxWidth: 820}}
                >
                  <div
                    style={{
                      fontFamily: SANS,
                      fontWeight: 700,
                      fontSize: 22,
                      letterSpacing: '0.08em',
                      textTransform: 'uppercase',
                      color: c.accent,
                      marginBottom: 8,
                    }}
                  >
                    {tipLabel}
                  </div>
                  <div style={{fontFamily: SANS, fontWeight: 400, fontSize: 28, lineHeight: 1.36, color: c.ink}}>{tip}</div>
                </div>
              ) : null}
              {subtitle ? (
                <div style={{fontFamily: SANS, fontWeight: 500, fontSize: 32, color: c.sub, marginTop: 24, maxWidth: 880}}>
                  {subtitle}
                </div>
              ) : null}
            </div>
          )}
        </div>

        <Footer c={pc} handle={handle} slideNo={slideNo} slideTotal={slideTotal} footnote={footnote} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
