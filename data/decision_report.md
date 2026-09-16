# Decision Report

- generated_at: 2026-09-16T14:16:29.962032+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14695**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14695, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.19% | **-1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 5/20 | 25.0% | +8.00% | **+2.00%** |
| LIMIT_9PCT | 5/20 | 25.0% | +4.92% | **+1.23%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.63% | **+0.49%** |
| LIMIT_7PCT | 6/20 | 30.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +3.47% | **+3.12%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +3.43% | **+2.74%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.48% | **+2.36%** |
| LIMIT_BB3S_LONG | 6/10 | 60.0% | +3.13% | **+1.88%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +3.80% | **+1.14%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,158.11** / 初期 $100.00 (+1058.11%)
- 確定: 5572件 (Win 1669 / Loss 1801 / Flat 2102) / skip 5684件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,158.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$238.18** / 初期 $100.00 (+138.18%)
- 確定: 3099件 (Win 857 / Loss 732 / Flat 1510) / skip 5007件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1994 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $238.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.75** / 初期 $100.00 (+23.75%)
- 確定: 2955件 (Win 878 / Loss 1164 / Flat 913) / pending 1件 / skip 3211件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000501 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.75

## 6. Latest Market Context

- 更新: 2026-09-16T14:16:12.683192+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=75617.7
- Funnel: target 1059 → liquid 154 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +123.35% | $32,750,364.61 |
| SYN/USDT:USDT | +113.48% | $24,563,998.40 |
| LSK/USDT:USDT | +38.49% | $28,977,469.09 |
| BULLA/USDT:USDT | +16.61% | $3,246,022.89 |
| USELESS/USDT:USDT | +15.69% | $7,912,230.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +3.67% | +3.66% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.66% | +2.66% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +2.13% | +2.12% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.93% | +1.93% |
| SOXL/USDT:USDT | below_1h_threshold | +1.62% | +1.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
