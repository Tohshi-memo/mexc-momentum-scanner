# Decision Report

- generated_at: 2026-09-16T14:31:30.351593+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14696**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14696, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.19% | **-1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_9PCT | 4/20 | 20.0% | +4.15% | **+0.83%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.36% | **+0.36%** |
| LIMIT_7PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.80% | **+2.52%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +2.68% | **+2.14%** |
| LIMIT_BB3S_LONG | 6/10 | 60.0% | +3.13% | **+1.88%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.85% | **+1.76%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.69% | **+0.94%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,152.32** / 初期 $100.00 (+1052.32%)
- 確定: 5573件 (Win 1669 / Loss 1802 / Flat 2102) / skip 5684件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,152.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$237.34** / 初期 $100.00 (+137.34%)
- 確定: 3100件 (Win 857 / Loss 733 / Flat 1510) / skip 5007件
- 成長率目線: 平均log +0.000279 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1815 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $237.34

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.75** / 初期 $100.00 (+23.75%)
- 確定: 2955件 (Win 878 / Loss 1164 / Flat 913) / pending 1件 / skip 3214件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000474 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.75

## 6. Latest Market Context

- 更新: 2026-09-16T14:31:16.433668+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=75774.9
- Funnel: target 1059 → liquid 155 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +126.79% | $33,575,469.26 |
| SYN/USDT:USDT | +110.66% | $24,798,497.18 |
| LSK/USDT:USDT | +47.12% | $29,230,924.54 |
| HEI/USDT:USDT | +19.53% | $1,049,517.96 |
| BULLA/USDT:USDT | +16.14% | $3,450,518.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +4.36% | +4.15% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +3.67% | +3.46% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +2.13% | +1.92% |
| HEI/USDT:USDT | below_1h_threshold | +1.97% | +1.76% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.93% | +1.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
