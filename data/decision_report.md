# Decision Report

- generated_at: 2026-09-24T05:46:30.073029+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15461**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.49% / filled 20/20。**
- 全期間 MARKET基準: n=15461, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.67% | **+1.59%** |
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.23% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +3.42% | **+1.88%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.39% | **+1.79%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +3.39% | **+1.69%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.96% | **+1.08%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.61% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$120.20** / 初期 $100.00 (+20.20%)
- 確定トレード: 218件 (TP 79 / SL 134 / EXP 5)
- 最新: LSK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.20
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5898件 (Win 1739 / Loss 1890 / Flat 2269) / skip 6124件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$252.39** / 初期 $100.00 (+152.39%)
- 確定: 3408件 (Win 938 / Loss 791 / Flat 1679) / skip 5464件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0702 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $252.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.71** / 初期 $100.00 (+21.71%)
- 確定: 3151件 (Win 930 / Loss 1240 / Flat 981) / pending 4件 / skip 3777件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000439 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIL/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $121.71

## 6. Latest Market Context

- 更新: 2026-09-24T05:46:17.021795+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=84152.7
- Funnel: target 1066 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NOM/USDT:USDT | +50.32% | $2,509,792.36 |
| NIL/USDT:USDT | +40.91% | $18,050,253.94 |
| LSK/USDT:USDT | +22.41% | $6,564,490.32 |
| LTC/USDT:USDT | +14.46% | $46,689,589.19 |
| BTW/USDT:USDT | +12.93% | $4,754,698.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +5.00% | +4.82% |
| RAY/USDT:USDT | below_1h_threshold | +3.42% | +3.24% |
| CHR/USDT:USDT | below_1h_threshold | +2.09% | +1.91% |
| LSK/USDT:USDT | below_1h_threshold | +2.04% | +1.86% |
| ENA/USDT:USDT | below_1h_threshold | +1.39% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
