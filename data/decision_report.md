# Decision Report

- generated_at: 2026-09-16T15:36:35.038782+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14707**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14707, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.51% | **+0.41%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +3.49% | **+3.49%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.87% | **+2.44%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.17% | **+2.17%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.72% | **+1.91%** |
| MARKET_LONG | 20/20 | 100.0% | +0.99% | **+0.99%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,198.11** / 初期 $100.00 (+1098.11%)
- 確定: 5584件 (Win 1677 / Loss 1805 / Flat 2102) / skip 5684件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,198.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$243.66** / 初期 $100.00 (+143.66%)
- 確定: 3111件 (Win 865 / Loss 736 / Flat 1510) / skip 5007件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2000 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $243.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.75** / 初期 $100.00 (+23.75%)
- 確定: 2955件 (Win 878 / Loss 1164 / Flat 913) / pending 1件 / skip 3224件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000635 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.75

## 6. Latest Market Context

- 更新: 2026-09-16T15:36:20.232555+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=75643.4
- Funnel: target 1059 → liquid 154 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +136.14% | $34,840,999.65 |
| SYN/USDT:USDT | +131.98% | $27,198,459.73 |
| LSK/USDT:USDT | +60.38% | $30,345,435.61 |
| BULLA/USDT:USDT | +34.32% | $4,014,926.47 |
| HEI/USDT:USDT | +27.53% | $1,237,239.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +4.20% | +4.22% |
| SYN/USDT:USDT | below_1h_threshold | +4.19% | +4.21% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.65% | +1.67% |
| IOST/USDT:USDT | below_1h_threshold | +1.45% | +1.47% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.37% | +1.40% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
