# Decision Report

- generated_at: 2026-05-02T11:02:14.214225+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2894**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2894, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +3.63% | **+1.27%** |
| LIMIT_5PCT | 12/20 | 60.0% | +1.54% | **+0.92%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.34% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +5.26% | **+3.68%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +4.49% | **+3.14%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +5.04% | **+2.27%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.38% | **+2.02%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +4.00% | **+1.80%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T11:02:12.404519+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=78162.5
- Funnel: target 755 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +206.76% | $112,683,723.23 |
| TAC/USDT:USDT | +36.10% | $1,480,648.61 |
| BIO/USDT:USDT | +19.55% | $1,900,697.18 |
| IRYS/USDT:USDT | +16.97% | $1,458,455.55 |
| KNC/USDT:USDT | +16.89% | $1,870,876.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +0.83% | +0.89% |
| PLAY/USDT:USDT | below_1h_threshold | +0.75% | +0.81% |
| USTC/USDT:USDT | below_1h_threshold | +0.64% | +0.70% |
| TAC/USDT:USDT | below_1h_threshold | +0.55% | +0.61% |
| CHILLGUY/USDT:USDT | below_1h_threshold | +0.37% | +0.42% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
