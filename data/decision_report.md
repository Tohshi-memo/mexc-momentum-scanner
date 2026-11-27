# Decision Report

- generated_at: 2026-11-27T01:46:14.983118+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19739**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=19739, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.55% | **+0.85%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.55% | **+0.77%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.66% | **+0.30%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.76** / 初期 $100.00 (+21.76%)
- 確定トレード: 292件 (TP 106 / SL 176 / EXP 10)
- 最新: SNXX/USDT:USDT EXPIRED PnL +2.62% 残高後 $121.76
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,948.16** / 初期 $100.00 (+1848.16%)
- 確定: 7639件 (Win 2199 / Loss 2459 / Flat 2981) / skip 8661件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,948.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$466.56** / 初期 $100.00 (+366.56%)
- 確定: 5263件 (Win 1403 / Loss 1129 / Flat 2731) / skip 7887件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0034 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $466.56

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7898件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000198 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-27T01:46:05.130237+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=60674.1
- Funnel: target 1097 → liquid 121 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BIGTIME/USDT:USDT | +14.81% | $2,213,315.88 |
| BULLA/USDT:USDT | +14.67% | $13,595,473.57 |
| NES/USDT:USDT | +11.85% | $1,061,648.96 |
| VELVET/USDT:USDT | +11.32% | $1,106,036.32 |
| MANTRA/USDT:USDT | +6.94% | $2,551,001.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONE/USDT:USDT | below_1h_threshold | +2.92% | +2.91% |
| NES/USDT:USDT | below_1h_threshold | +1.94% | +1.92% |
| SYRUP/USDT:USDT | below_1h_threshold | +1.72% | +1.71% |
| VELVET/USDT:USDT | below_1h_threshold | +1.46% | +1.44% |
| KORU/USDT:USDT | below_1h_threshold | +1.35% | +1.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
