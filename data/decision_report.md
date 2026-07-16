# Decision Report

- generated_at: 2026-07-16T00:46:16.007472+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8779**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.02% / filled 20/20。**
- 全期間 MARKET基準: n=8779, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.02% | **+2.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.02% | **+2.02%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.97% | **+1.87%** |
| LIMIT_2PCT | 18/20 | 90.0% | +1.91% | **+1.71%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.97% | **+1.28%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +1.04% | **+0.31%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.85% | **+0.25%** |
| LIMIT_BB3S_LONG | 10/10 | 100.0% | -0.33% | **-0.33%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -2.28% | **-0.34%** |

## 2. $100 Live Portfolio

- 残高: **$104.25** / 初期 $100.00 (+4.25%)
- 確定トレード: 100件 (TP 35 / SL 63 / EXP 2)
- 最新: ROAM/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.25
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$340.65** / 初期 $100.00 (+240.65%)
- 確定: 2896件 (Win 906 / Loss 942 / Flat 1048) / skip 2444件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROAM/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $340.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.10** / 初期 $100.00 (+7.10%)
- 確定: 743件 (Win 170 / Loss 168 / Flat 405) / skip 1447件
- 成長率目線: 平均log +0.000092 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0994 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ROAM/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $107.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.49** / 初期 $100.00 (-1.51%)
- 確定: 64件 (Win 19 / Loss 41 / Flat 4) / pending 0件 / skip 184件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000488 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.09% 残高後 $98.49

## 6. Latest Market Context

- 更新: 2026-07-16T00:46:08.771729+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.35% price=64493.9
- Funnel: target 871 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HOME/USDT:USDT | +20.60% | $1,921,526.25 |
| ROAM/USDT:USDT | +16.74% | $5,620,230.16 |
| CAP/USDT:USDT | +14.34% | $1,703,826.74 |
| LDO/USDT:USDT | +9.08% | $6,779,005.44 |
| SKL/USDT:USDT | +7.98% | $1,858,789.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +2.64% | +2.99% |
| USELESS/USDT:USDT | below_1h_threshold | +1.32% | +1.68% |
| LDO/USDT:USDT | below_1h_threshold | +1.26% | +1.61% |
| EIGEN/USDT:USDT | below_1h_threshold | +0.99% | +1.35% |
| T/USDT:USDT | below_1h_threshold | +0.99% | +1.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
