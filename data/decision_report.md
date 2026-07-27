# Decision Report

- generated_at: 2026-07-27T10:41:26.075966+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9626**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9626, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +2.75% | **+1.24%** |
| LIMIT_4PCT | 15/20 | 75.0% | +1.33% | **+1.00%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.96% | **+0.40%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.37% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +2.55% | **+2.04%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.26% | **+1.58%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.80% | **+1.53%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +2.00% | **+1.40%** |
| LIMIT_BB3S_LONG | 9/10 | 90.0% | +0.87% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 145件 (TP 50 / SL 90 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.92
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$461.45** / 初期 $100.00 (+361.45%)
- 確定: 3417件 (Win 1084 / Loss 1112 / Flat 1221) / skip 2770件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $461.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1223件 (Win 338 / Loss 275 / Flat 610) / skip 1814件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0019 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PRL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.02** / 初期 $100.00 (+9.02%)
- 確定: 648件 (Win 216 / Loss 245 / Flat 187) / pending 2件 / skip 445件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000433 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $109.02

## 6. Latest Market Context

- 更新: 2026-07-27T10:41:15.995600+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=65381.0
- Funnel: target 901 → liquid 156 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.3 >= 65=1, 4h RSI 85.2 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +50.22% | $40,149,947.43 |
| BTW/USDT:USDT | +43.32% | $3,205,501.25 |
| ON/USDT:USDT | +41.82% | $5,257,108.57 |
| NIL/USDT:USDT | +29.30% | $2,632,080.00 |
| DIA/USDT:USDT | +28.88% | $11,122,963.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.98% | +4.76% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +4.52% | +4.30% |
| AKE/USDT:USDT | below_1h_threshold | +2.18% | +1.96% |
| ZAMA/USDT:USDT | below_1h_threshold | +2.17% | +1.95% |
| TAG/USDT:USDT | below_1h_threshold | +1.48% | +1.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
