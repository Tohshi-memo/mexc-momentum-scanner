# Decision Report

- generated_at: 2026-09-16T15:41:40.637415+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14709**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14709, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.99% | **-0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.71% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.98% | **+1.98%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.27% | **+1.71%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.04% | **+1.63%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.54% | **+1.46%** |
| MARKET_LONG | 20/20 | 100.0% | +0.79% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,192.12** / 初期 $100.00 (+1092.12%)
- 確定: 5586件 (Win 1677 / Loss 1806 / Flat 2103) / skip 5684件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $1,192.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$242.81** / 初期 $100.00 (+142.81%)
- 確定: 3113件 (Win 865 / Loss 737 / Flat 1511) / skip 5007件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.029% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1943 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $242.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.75** / 初期 $100.00 (+23.75%)
- 確定: 2955件 (Win 878 / Loss 1164 / Flat 913) / pending 1件 / skip 3226件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000656 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.75

## 6. Latest Market Context

- 更新: 2026-09-16T15:41:20.334816+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=75732.9
- Funnel: target 1059 → liquid 154 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.2 >= 65=1, 4h RSI 84.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +136.32% | $35,014,556.36 |
| SYN/USDT:USDT | +134.06% | $27,425,985.89 |
| LSK/USDT:USDT | +61.08% | $30,454,124.12 |
| BULLA/USDT:USDT | +36.73% | $4,065,456.46 |
| HEI/USDT:USDT | +28.77% | $1,269,952.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +4.06% | +3.97% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.23% | +2.13% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.37% | +1.28% |
| RAY/USDT:USDT | below_1h_threshold | +1.08% | +0.98% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.01% | +0.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
