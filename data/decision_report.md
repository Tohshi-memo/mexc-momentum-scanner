# Decision Report

- generated_at: 2026-11-05T21:01:50.120469+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18207**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=18207, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.78% | **+0.66%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +3.09% | **+3.09%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.74% | **+0.37%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.72% | **+0.36%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.59% | **+0.33%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 263件 (TP 96 / SL 159 / EXP 8)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,507.12** / 初期 $100.00 (+1407.12%)
- 確定: 7016件 (Win 2022 / Loss 2243 / Flat 2751) / skip 7752件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOXS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,507.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$374.94** / 初期 $100.00 (+274.94%)
- 確定: 4599件 (Win 1234 / Loss 1030 / Flat 2335) / skip 7019件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0722 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UVXY/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $374.94

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6374件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000466 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-05T21:01:31.468267+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=76103.9
- Funnel: target 1084 → liquid 189 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.1 >= 65=1, 4h RSI 76.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UVXY/USDT:USDT | +13.66% | $2,056,491.48 |
| BLESS/USDT:USDT | +13.25% | $4,810,977.31 |
| BTW/USDT:USDT | +11.20% | $5,231,932.57 |
| CLANKER/USDT:USDT | +8.21% | $10,468,886.01 |
| ELSA/USDT:USDT | +6.12% | $8,295,240.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SQQQ/USDT:USDT | below_1h_threshold | +3.47% | +3.60% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +0.53% | +0.67% |
| ARIA/USDT:USDT | below_1h_threshold | +0.21% | +0.34% |
| BLESS/USDT:USDT | below_1h_threshold | +0.08% | +0.21% |
| NIL/USDT:USDT | below_1h_threshold | -0.02% | +0.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
