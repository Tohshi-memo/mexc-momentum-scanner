# Decision Report

- generated_at: 2026-06-14T00:18:19.818197+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6620**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6620, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.57% | **+0.47%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.26% | **+1.13%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +1.62% | **+0.97%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.75% | **+0.52%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$167.72** / 初期 $100.00 (+67.72%)
- 確定: 1493件 (Win 401 / Loss 476 / Flat 616) / skip 1688件
- 成長率目線: 平均log +0.000346 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $167.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.06** / 初期 $100.00 (-0.94%)
- 確定: 31件 (Win 11 / Loss 10 / Flat 10) / skip 0件
- 成長率目線: 平均log -0.000305 / 幾何平均 -0.031% per trade / maxDD +1.93%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0262 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $99.06

## 5. Latest Market Context

- 更新: 2026-06-14T00:18:14.740544+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=64402.1
- Funnel: target 770 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TRADOOR/USDT:USDT | +31.11% | $2,436,027.66 |
| MEGA/USDT:USDT | +21.81% | $3,062,819.46 |
| H/USDT:USDT | +19.38% | $17,597,038.76 |
| RIF/USDT:USDT | +17.05% | $12,928,414.54 |
| BTW/USDT:USDT | +9.29% | $1,763,603.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.61% | +4.63% |
| PI/USDT:USDT | below_1h_threshold | +2.32% | +2.35% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.02% | +2.04% |
| BSB/USDT:USDT | below_1h_threshold | +1.93% | +1.95% |
| CHIP/USDT:USDT | below_1h_threshold | +1.78% | +1.81% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
