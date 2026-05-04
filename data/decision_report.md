# Decision Report

- generated_at: 2026-05-04T15:22:32.814778+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3223**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3223, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-1.96%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.96% | **-1.96%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.32% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.01% | **+2.01%** |
| MARKET_LONG | 20/20 | 100.0% | +1.61% | **+1.61%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.06% | **+1.54%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.07% | **+1.53%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.07% | **+1.38%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T15:22:27.840375+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.95% price=79411.6
- Funnel: target 761 → liquid 200 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.8 >= 65=1, 4h RSI 95.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ELIZAOS/USDT:USDT | +148.45% | $1,503,329.54 |
| SKYAI/USDT:USDT | +81.12% | $89,174,197.07 |
| TST/USDT:USDT | +78.33% | $18,640,889.86 |
| GIGA/USDT:USDT | +36.75% | $2,300,189.06 |
| ASTEROID/USDT:USDT | +30.92% | $4,670,596.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.82% | +5.77% |
| BSB/USDT:USDT | below_1h_threshold | +2.74% | +3.69% |
| B/USDT:USDT | below_1h_threshold | +2.45% | +3.40% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.27% | +3.22% |
| USOIL/USDT:USDT | below_1h_threshold | +1.91% | +2.86% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
