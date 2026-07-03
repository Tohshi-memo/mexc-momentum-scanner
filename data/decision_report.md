# Decision Report

- generated_at: 2026-07-03T11:38:20.236040+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8156**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.04% / filled 20/20。**
- 全期間 MARKET基準: n=8156, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |
| ASK | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.14% | **+0.12%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.35% | **+0.35%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -0.03% | **-0.01%** |
| ASK_LONG | 20/20 | 100.0% | -0.04% | **-0.04%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.55% | **-0.25%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.66% | **-0.30%** |

## 2. $100 Live Portfolio

- 残高: **$102.11** / 初期 $100.00 (+2.11%)
- 確定トレード: 54件 (TP 19 / SL 34 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$288.02** / 初期 $100.00 (+188.02%)
- 確定: 2477件 (Win 762 / Loss 826 / Flat 889) / skip 2240件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: M/USDT:USDT `LIMIT_FIB1272_LONG` TP_HIT account +1.00% 残高後 $288.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.39** / 初期 $100.00 (+6.39%)
- 確定: 602件 (Win 145 / Loss 143 / Flat 314) / skip 965件
- 成長率目線: 平均log +0.000103 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_robust_growth_score) / robust_score -0.0498 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: M/USDT:USDT `LIMIT_FIB1272_LONG` TP_HIT account +0.69% 残高後 $106.39

## 5. Latest Market Context

- 更新: 2026-07-03T11:38:12.809438+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=61896.6
- Funnel: target 834 → liquid 164 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARPA/USDT:USDT | +58.15% | $3,443,356.15 |
| NEX/USDT:USDT | +46.78% | $2,599,082.87 |
| RIF/USDT:USDT | +35.56% | $8,369,977.34 |
| ZKP/USDT:USDT | +28.85% | $4,614,702.13 |
| BLESS/USDT:USDT | +28.57% | $6,149,115.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NOM/USDT:USDT | below_1h_threshold | +4.47% | +4.45% |
| MAGMA/USDT:USDT | below_1h_threshold | +3.42% | +3.40% |
| GRASS/USDT:USDT | below_1h_threshold | +3.00% | +2.99% |
| BLESS/USDT:USDT | below_1h_threshold | +2.99% | +2.97% |
| RIF/USDT:USDT | below_1h_threshold | +2.07% | +2.06% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
