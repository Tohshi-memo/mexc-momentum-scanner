# Decision Report

- generated_at: 2026-11-21T05:21:33.355627+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19277**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19277, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.75% | **-0.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +2.45% | **+0.37%** |
| LIMIT_10PCT | 3/20 | 15.0% | +2.45% | **+0.37%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.66% | **+0.33%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.28% | **+0.26%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.28% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.64% | **+1.23%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.87% | **+1.12%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.77% | **+1.06%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.60% | **+0.80%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.46% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,667.06** / 初期 $100.00 (+1567.06%)
- 確定: 7422件 (Win 2133 / Loss 2394 / Flat 2895) / skip 8416件
- 成長率目線: 平均log +0.000379 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DCTY/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,667.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$441.55** / 初期 $100.00 (+341.55%)
- 確定: 5088件 (Win 1355 / Loss 1088 / Flat 2645) / skip 7600件
- 成長率目線: 平均log +0.000292 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BARD/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.49% 残高後 $441.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7438件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000104 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-21T05:21:15.369163+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=56192.4
- Funnel: target 1086 → liquid 157 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +17.59% | $23,310,406.01 |
| AKE/USDT:USDT | +15.57% | $27,513,219.02 |
| PIEVERSE/USDT:USDT | +11.60% | $4,141,034.52 |
| UVXY/USDT:USDT | +10.25% | $6,215,909.38 |
| SOXS/USDT:USDT | +7.17% | $89,511,781.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +4.06% | +4.20% |
| SOXS/USDT:USDT | below_1h_threshold | +3.30% | +3.44% |
| EVAA/USDT:USDT | below_1h_threshold | +1.48% | +1.62% |
| XPL/USDT:USDT | below_1h_threshold | +1.26% | +1.40% |
| UVXY/USDT:USDT | below_1h_threshold | +1.06% | +1.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
