# Decision Report

- generated_at: 2026-09-06T06:16:13.871041+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13803**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13803, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.07% | **+0.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 13/20 | 65.0% | +0.18% | **+0.12%** |
| LIMIT_5PCT | 2/20 | 10.0% | +0.95% | **+0.10%** |
| MARKET | 20/20 | 100.0% | +0.07% | **+0.07%** |
| LIMIT_BB3S | 4/15 | 26.7% | -0.05% | **-0.01%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.28% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +5.23% | **+3.14%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.79% | **+1.34%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.33% | **+0.93%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.08% | **+0.65%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.64% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$852.07** / 初期 $100.00 (+752.07%)
- 確定: 5109件 (Win 1534 / Loss 1669 / Flat 1906) / skip 5255件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $852.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$192.24** / 初期 $100.00 (+92.24%)
- 確定: 2548件 (Win 712 / Loss 605 / Flat 1231) / skip 4666件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0109 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $192.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.91** / 初期 $100.00 (+19.91%)
- 確定: 2416件 (Win 720 / Loss 918 / Flat 778) / pending 2件 / skip 2855件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000158 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.91

## 6. Latest Market Context

- 更新: 2026-09-06T06:16:04.033721+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=79893.8
- Funnel: target 1054 → liquid 124 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +43.59% | $135,324,304.64 |
| RAY/USDT:USDT | +35.09% | $2,383,395.44 |
| FLOCK/USDT:USDT | +28.16% | $1,143,739.38 |
| BASECAT/USDT:USDT | +17.35% | $2,199,296.93 |
| ZEC/USDT:USDT | +15.54% | $234,306,635.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAKE/USDT:USDT | below_1h_threshold | +0.73% | +0.81% |
| BOME/USDT:USDT | below_1h_threshold | +0.72% | +0.79% |
| NEAR/USDT:USDT | below_1h_threshold | +0.59% | +0.66% |
| ZEC/USDT:USDT | below_1h_threshold | +0.48% | +0.56% |
| SOXL/USDT:USDT | below_1h_threshold | +0.37% | +0.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
