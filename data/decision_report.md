# Decision Report

- generated_at: 2026-07-16T02:56:22.136776+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8781**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.02% / filled 20/20。**
- 全期間 MARKET基準: n=8781, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+3.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.02% | **+3.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.02% | **+3.02%** |
| LIMIT_1PCT | 19/20 | 95.0% | +3.07% | **+2.91%** |
| LIMIT_2PCT | 17/20 | 85.0% | +2.96% | **+2.51%** |
| LIMIT_ATR | 12/20 | 60.0% | +3.21% | **+1.93%** |
| LIMIT_3PCT | 12/20 | 60.0% | +2.37% | **+1.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 7/20 | 35.0% | +2.03% | **+0.71%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.87% | **+0.65%** |
| LIMIT_8PCT_LONG | 12/20 | 60.0% | +0.67% | **+0.40%** |
| LIMIT_BB3S_LONG | 10/10 | 100.0% | -0.33% | **-0.33%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -2.30% | **-0.58%** |

## 2. $100 Live Portfolio

- 残高: **$106.34** / 初期 $100.00 (+6.34%)
- 確定トレード: 102件 (TP 37 / SL 63 / EXP 2)
- 最新: PI/USDT:USDT TP_HIT PnL +8.00% 残高後 $106.34
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$340.65** / 初期 $100.00 (+240.65%)
- 確定: 2897件 (Win 906 / Loss 942 / Flat 1049) / skip 2445件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PI/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $340.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.10** / 初期 $100.00 (+7.10%)
- 確定: 745件 (Win 170 / Loss 168 / Flat 407) / skip 1447件
- 成長率目線: 平均log +0.000092 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0938 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $107.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.49** / 初期 $100.00 (-1.51%)
- 確定: 64件 (Win 19 / Loss 41 / Flat 4) / pending 0件 / skip 189件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000581 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.09% 残高後 $98.49

## 6. Latest Market Context

- 更新: 2026-07-16T02:56:12.980564+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=64620.0
- Funnel: target 873 → liquid 172 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.3 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CAP/USDT:USDT | +19.52% | $1,999,734.34 |
| HOME/USDT:USDT | +17.27% | $2,062,566.42 |
| ROAM/USDT:USDT | +11.28% | $5,681,704.77 |
| ONDO/USDT:USDT | +10.68% | $51,655,848.09 |
| LDO/USDT:USDT | +9.26% | $7,700,053.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +3.47% | +3.59% |
| LAB/USDT:USDT | below_1h_threshold | +2.27% | +2.39% |
| PYTH/USDT:USDT | below_1h_threshold | +2.26% | +2.38% |
| CAP/USDT:USDT | below_1h_threshold | +1.81% | +1.93% |
| VELVET/USDT:USDT | below_1h_threshold | +1.79% | +1.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
