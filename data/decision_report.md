# Decision Report

- generated_at: 2026-06-06T18:16:23.248795+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5878**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5878, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +0.56% | **+0.56%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| LIMIT_BB3S | 3/14 | 21.4% | +0.97% | **+0.21%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +0.52% | **+0.08%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.15% | **+1.40%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.36% | **+1.16%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.48% | **+0.96%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +1.31% | **+0.87%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.74% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1014件 (Win 239 / Loss 313 / Flat 462) / skip 1425件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T18:16:19.907519+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=60440.3
- Funnel: target 771 → liquid 142 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +17.37% | $1,140,527.51 |
| SKYAI/USDT:USDT | +16.45% | $8,606,038.64 |
| BLUAI/USDT:USDT | +7.96% | $7,095,969.72 |
| BTW/USDT:USDT | +7.05% | $19,038,474.45 |
| HOME/USDT:USDT | +5.23% | $10,204,425.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.06% | +3.25% |
| PORTAL/USDT:USDT | below_1h_threshold | +2.50% | +2.69% |
| VELVET/USDT:USDT | below_1h_threshold | +2.27% | +2.45% |
| LAB/USDT:USDT | below_1h_threshold | +2.21% | +2.40% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +1.86% | +2.04% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
