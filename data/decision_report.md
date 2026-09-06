# Decision Report

- generated_at: 2026-09-06T04:56:22.869541+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13798**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13798, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.10% | **-1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.32% | **+0.11%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.11% | **+0.08%** |
| LIMIT_BB3S | 4/15 | 26.7% | -0.05% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +4.59% | **+2.76%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.84% | **+1.85%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.38% | **+1.43%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.55% | **+1.17%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.09% | **+1.05%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$858.64** / 初期 $100.00 (+758.64%)
- 確定: 5104件 (Win 1533 / Loss 1666 / Flat 1905) / skip 5255件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DASH/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $858.64

## 4. Robust Adaptive DryRun ($100)

- 残高: **$193.27** / 初期 $100.00 (+93.27%)
- 確定: 2543件 (Win 711 / Loss 602 / Flat 1230) / skip 4666件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0411 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DASH/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $193.27

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.02** / 初期 $100.00 (+20.02%)
- 確定: 2412件 (Win 719 / Loss 916 / Flat 777) / pending 4件 / skip 2855件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000198 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZEC/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $120.02

## 6. Latest Market Context

- 更新: 2026-09-06T04:56:10.435627+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=79838.2
- Funnel: target 1051 → liquid 126 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.3 >= 65=1, 4h RSI 80.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +45.48% | $129,321,766.25 |
| RAY/USDT:USDT | +37.96% | $1,954,385.72 |
| FLOCK/USDT:USDT | +24.46% | $1,115,038.69 |
| BASECAT/USDT:USDT | +23.77% | $2,178,741.25 |
| UAI/USDT:USDT | +14.68% | $10,662,096.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEN/USDT:USDT | below_1h_threshold | +4.93% | +5.12% |
| BASECAT/USDT:USDT | below_1h_threshold | +4.91% | +5.10% |
| BULLA/USDT:USDT | below_1h_threshold | +2.20% | +2.39% |
| LIT/USDT:USDT | below_1h_threshold | +1.63% | +1.82% |
| ZRO/USDT:USDT | below_1h_threshold | +1.02% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
