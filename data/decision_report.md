# Decision Report

- generated_at: 2026-08-27T23:16:14.507551+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12845**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.14% / filled 20/20。**
- 全期間 MARKET基準: n=12845, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.14% | **+2.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.14% | **+2.14%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.79% | **+0.51%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -1.08% | **-0.48%** |
| MARKET_LONG | 20/20 | 100.0% | -0.57% | **-0.57%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | -1.23% | **-0.86%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$716.03** / 初期 $100.00 (+616.03%)
- 確定: 4669件 (Win 1414 / Loss 1532 / Flat 1723) / skip 4737件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $716.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2003件 (Win 544 / Loss 483 / Flat 976) / skip 4253件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.79** / 初期 $100.00 (+14.79%)
- 確定: 1988件 (Win 580 / Loss 762 / Flat 646) / pending 0件 / skip 2328件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000193 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: WIF/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.79

## 6. Latest Market Context

- 更新: 2026-08-27T23:16:06.765077+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=80164.3
- Funnel: target 1019 → liquid 146 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BMT/USDT:USDT | +22.99% | $3,615,202.33 |
| HEMI/USDT:USDT | +20.94% | $2,715,922.76 |
| BLESS/USDT:USDT | +16.29% | $6,556,158.97 |
| MERL/USDT:USDT | +9.81% | $1,473,311.63 |
| BTR/USDT:USDT | +7.51% | $18,726,384.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTR/USDT:USDT | below_1h_threshold | +1.54% | +1.66% |
| UAI/USDT:USDT | below_1h_threshold | +1.27% | +1.39% |
| CYS/USDT:USDT | below_1h_threshold | +1.02% | +1.15% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.00% | +1.12% |
| BMT/USDT:USDT | below_1h_threshold | +0.95% | +1.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
