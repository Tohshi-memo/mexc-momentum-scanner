# Decision Report

- generated_at: 2026-06-10T06:47:37.405159+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6189**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6189, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.06% | **-0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +5.40% | **+1.62%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.20% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.64% | **+1.32%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +3.43% | **+1.20%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.81% | **+0.98%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.04% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.04** / 初期 $100.00 (+49.04%)
- 確定: 1205件 (Win 300 / Loss 376 / Flat 529) / skip 1545件
- 成長率目線: 平均log +0.000331 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_7PCT` SL_HIT account +0.35% 残高後 $149.04

## 4. Latest Market Context

- 更新: 2026-06-10T06:47:33.444913+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=61404.7
- Funnel: target 781 → liquid 146 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.1 >= 65=1, 4h RSI 71.4 >= 65=1, 4h RSI 77.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +40.71% | $6,245,561.72 |
| BTW/USDT:USDT | +28.38% | $29,099,594.66 |
| BLESS/USDT:USDT | +12.79% | $3,807,261.10 |
| BEAT/USDT:USDT | +11.50% | $111,228,530.60 |
| UB/USDT:USDT | +11.17% | $1,807,544.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KAS/USDT:USDT | below_1h_threshold | +4.44% | +4.30% |
| IO/USDT:USDT | below_1h_threshold | +4.08% | +3.95% |
| BLESS/USDT:USDT | below_1h_threshold | +3.32% | +3.18% |
| UAI/USDT:USDT | below_1h_threshold | +2.75% | +2.62% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +2.52% | +2.39% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
