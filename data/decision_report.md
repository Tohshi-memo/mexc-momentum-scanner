# Decision Report

- generated_at: 2026-09-06T05:36:28.173139+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13800**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13800, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.13% | **-1.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.16% | **+0.12%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.02% | **-0.01%** |
| LIMIT_BB3S | 4/15 | 26.7% | -0.05% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +5.23% | **+3.14%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.68% | **+1.74%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.67% | **+1.73%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.55% | **+1.17%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.09% | **+1.05%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$864.98** / 初期 $100.00 (+764.98%)
- 確定: 5106件 (Win 1534 / Loss 1666 / Flat 1906) / skip 5255件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DASH/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.74% 残高後 $864.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$194.28** / 初期 $100.00 (+94.28%)
- 確定: 2545件 (Win 712 / Loss 602 / Flat 1231) / skip 4666件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0400 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DASH/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $194.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.33** / 初期 $100.00 (+20.33%)
- 確定: 2414件 (Win 720 / Loss 916 / Flat 778) / pending 4件 / skip 2855件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000227 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DASH/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $120.33

## 6. Latest Market Context

- 更新: 2026-09-06T05:36:14.108151+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=79932.7
- Funnel: target 1054 → liquid 124 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.0 >= 65=1, 4h RSI 69.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +45.77% | $132,386,697.25 |
| RAY/USDT:USDT | +36.66% | $2,190,947.29 |
| FLOCK/USDT:USDT | +28.71% | $1,117,992.15 |
| UAI/USDT:USDT | +26.74% | $11,212,808.52 |
| BASECAT/USDT:USDT | +20.06% | $2,198,369.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DASH/USDT:USDT | below_1h_threshold | +4.52% | +4.39% |
| ZEC/USDT:USDT | below_1h_threshold | +2.89% | +2.75% |
| FLOCK/USDT:USDT | below_1h_threshold | +2.22% | +2.09% |
| SUSHI/USDT:USDT | below_1h_threshold | +1.99% | +1.86% |
| PENDLE/USDT:USDT | below_1h_threshold | +1.56% | +1.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
