# Decision Report

- generated_at: 2026-11-23T08:16:19.801512+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19429**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19429, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.50% | **-0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 17/20 | 85.0% | +1.16% | **+0.98%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.26% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +3.01% | **+1.65%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +3.08% | **+1.39%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.19% | **+1.09%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.43% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 285件 (TP 103 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,859.67** / 初期 $100.00 (+1759.67%)
- 確定: 7528件 (Win 2163 / Loss 2424 / Flat 2941) / skip 8462件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SI/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.24% 残高後 $1,859.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$466.74** / 初期 $100.00 (+366.74%)
- 確定: 5191件 (Win 1385 / Loss 1117 / Flat 2689) / skip 7649件
- 成長率目線: 平均log +0.000297 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0844 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $466.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7591件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000148 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-23T08:16:07.779171+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.48% price=61133.6
- Funnel: target 1086 → liquid 119 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.2 >= 65=1, 4h RSI 73.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +107.81% | $1,850,657.47 |
| BULLA/USDT:USDT | +30.49% | $2,783,670.11 |
| EVAA/USDT:USDT | +26.65% | $45,913,747.94 |
| ARIA/USDT:USDT | +24.50% | $2,436,475.89 |
| ELSA/USDT:USDT | +19.42% | $2,222,000.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +2.04% | +2.53% |
| EVAA/USDT:USDT | below_1h_threshold | +1.86% | +2.34% |
| ELSA/USDT:USDT | below_1h_threshold | +1.03% | +1.51% |
| VELVET/USDT:USDT | below_1h_threshold | +0.95% | +1.44% |
| BEAT/USDT:USDT | below_1h_threshold | +0.67% | +1.16% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
