# Decision Report

- generated_at: 2026-06-05T11:54:36.768643+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5720**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.18% / filled 20/20。**
- 全期間 MARKET基準: n=5720, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.76% | **+1.76%** |
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.01% | **+0.71%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +4.22% | **+1.05%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.50% | **+1.00%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.48% | **+0.81%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.98% | **+0.73%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +2.19% | **+0.55%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1010件 (Win 239 / Loss 313 / Flat 458) / skip 1271件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPN/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-05T11:54:34.357792+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.76% price=62037.0
- Funnel: target 773 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +81.73% | $24,590,496.19 |
| BABY/USDT:USDT | +52.53% | $8,567,533.37 |
| CLO/USDT:USDT | +12.23% | $1,190,564.26 |
| BEAT/USDT:USDT | +11.87% | $28,728,306.41 |
| HEI/USDT:USDT | +11.48% | $2,834,494.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UP/USDT:USDT | below_1h_threshold | +2.26% | +3.02% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.10% | +2.86% |
| GENIUS/USDT:USDT | below_1h_threshold | +2.08% | +2.84% |
| ALLO/USDT:USDT | below_1h_threshold | +1.19% | +1.96% |
| COPSTOCK/USDT:USDT | below_1h_threshold | +1.12% | +1.88% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
