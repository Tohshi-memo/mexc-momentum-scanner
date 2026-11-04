# Decision Report

- generated_at: 2026-11-04T02:31:28.432718+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18102**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.06% / filled 20/20。**
- 全期間 MARKET基準: n=18102, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=+2.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.79% | **+1.61%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.36% | **+1.02%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.06% | **+0.64%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.77% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 261件 (TP 96 / SL 157 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,502.37** / 初期 $100.00 (+1402.37%)
- 確定: 6923件 (Win 2002 / Loss 2220 / Flat 2701) / skip 7740件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLANKER/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,502.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$377.66** / 初期 $100.00 (+277.66%)
- 確定: 4516件 (Win 1209 / Loss 1007 / Flat 2300) / skip 6997件
- 成長率目線: 平均log +0.000294 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0560 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLANKER/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $377.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6264件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000129 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-04T02:31:16.963267+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.35% price=76747.0
- Funnel: target 1084 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLANKER/USDT:USDT | +30.43% | $1,349,644.25 |
| BMT/USDT:USDT | +19.35% | $1,162,811.99 |
| SOXS/USDT:USDT | +11.56% | $30,698,801.60 |
| AXIS/USDT:USDT | +8.73% | $1,241,387.42 |
| SQQQ/USDT:USDT | +6.64% | $1,212,901.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SQQQ/USDT:USDT | below_1h_threshold | +2.97% | +3.32% |
| BMT/USDT:USDT | below_1h_threshold | +2.52% | +2.86% |
| LYN/USDT:USDT | below_1h_threshold | +1.75% | +2.10% |
| AERO/USDT:USDT | below_1h_threshold | +1.38% | +1.73% |
| LSK/USDT:USDT | below_1h_threshold | +1.06% | +1.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
