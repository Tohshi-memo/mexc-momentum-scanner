# Decision Report

- generated_at: 2026-10-06T11:31:33.003719+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16200**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16200, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 5/20 | 25.0% | +2.69% | **+0.67%** |
| LIMIT_9PCT | 5/20 | 25.0% | +1.83% | **+0.46%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +2.01% | **+0.40%** |
| LIMIT_BB3S | 7/17 | 41.2% | +0.76% | **+0.31%** |
| LIMIT_8PCT | 5/20 | 25.0% | -0.92% | **-0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +3.40% | **+3.40%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +3.03% | **+2.27%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +3.84% | **+1.92%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +2.75% | **+0.96%** |
| LIMIT_8PCT_LONG | 3/20 | 15.0% | +5.33% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$120.39** / 初期 $100.00 (+20.39%)
- 確定トレード: 231件 (TP 83 / SL 141 / EXP 7)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.39
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,296.89** / 初期 $100.00 (+1196.89%)
- 確定: 6243件 (Win 1829 / Loss 1996 / Flat 2418) / skip 6518件
- 成長率目線: 平均log +0.000410 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,296.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3611件 (Win 1005 / Loss 845 / Flat 1761) / skip 6000件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RLC/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4361件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000097 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-06T11:31:21.200736+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=86185.2
- Funnel: target 1074 → liquid 169 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 98.0 >= 65=1, 4h RSI 86.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RLC/USDT:USDT | +89.94% | $36,005,233.54 |
| ORCA/USDT:USDT | +38.91% | $3,339,298.92 |
| BR/USDT:USDT | +30.55% | $42,930,527.94 |
| US/USDT:USDT | +29.25% | $1,234,455.01 |
| API3/USDT:USDT | +27.33% | $2,529,803.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +3.12% | +3.04% |
| API3/USDT:USDT | below_1h_threshold | +2.23% | +2.15% |
| RAY/USDT:USDT | below_1h_threshold | +0.94% | +0.86% |
| CHIP/USDT:USDT | below_1h_threshold | +0.89% | +0.81% |
| RENDER/USDT:USDT | below_1h_threshold | +0.85% | +0.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
