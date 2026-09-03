# Decision Report

- generated_at: 2026-09-03T18:26:31.323697+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13524**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.13% / filled 20/20。**
- 全期間 MARKET基準: n=13524, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.13% | **+2.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.13% | **+2.13%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.27% | **+1.08%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.22% | **+0.67%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.88% | **+0.87%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.22% | **+0.61%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.22% | **+0.61%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.09% | **+0.52%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.88% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5008件 (Win 1516 / Loss 1644 / Flat 1848) / skip 5077件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BONER/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.36% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$184.60** / 初期 $100.00 (+84.60%)
- 確定: 2373件 (Win 671 / Loss 576 / Flat 1126) / skip 4562件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $184.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.65** / 初期 $100.00 (+16.65%)
- 確定: 2200件 (Win 656 / Loss 862 / Flat 682) / pending 6件 / skip 2792件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000381 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.65

## 6. Latest Market Context

- 更新: 2026-09-03T18:26:18.984599+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=80951.7
- Funnel: target 1046 → liquid 163 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +29.55% | $66,259,931.02 |
| PROM/USDT:USDT | +12.54% | $3,812,757.96 |
| MUBARAK/USDT:USDT | +6.71% | $3,676,524.73 |
| BR/USDT:USDT | +6.46% | $8,337,107.75 |
| BTW/USDT:USDT | +5.38% | $15,181,145.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKR/USDT:USDT | below_1h_threshold | +3.93% | +4.00% |
| ARB/USDT:USDT | below_1h_threshold | +2.42% | +2.49% |
| FF/USDT:USDT | below_1h_threshold | +1.68% | +1.75% |
| LDO/USDT:USDT | below_1h_threshold | +1.44% | +1.50% |
| 4/USDT:USDT | below_1h_threshold | +1.40% | +1.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
