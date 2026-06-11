# Decision Report

- generated_at: 2026-06-11T18:02:18.535765+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6391**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6391, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.60% | **-0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.97% | **+0.73%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.12% | **+0.67%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.65% | **+0.66%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.21% | **+0.60%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.71% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$154.96** / 初期 $100.00 (+54.96%)
- 確定: 1308件 (Win 339 / Loss 415 / Flat 554) / skip 1644件
- 成長率目線: 平均log +0.000335 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIO/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $154.96

## 4. Latest Market Context

- 更新: 2026-06-11T18:02:14.271733+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=63667.3
- Funnel: target 782 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +32.23% | $97,437,319.71 |
| ESPORTS/USDT:USDT | +28.41% | $11,391,664.60 |
| SKYAI/USDT:USDT | +10.96% | $10,991,958.61 |
| HMSTR/USDT:USDT | +7.15% | $4,371,122.40 |
| A/USDT:USDT | +6.53% | $1,121,038.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARB/USDT:USDT | below_1h_threshold | +2.84% | +2.75% |
| COLLECT/USDT:USDT | below_1h_threshold | +1.04% | +0.95% |
| HMSTR/USDT:USDT | below_1h_threshold | +0.90% | +0.81% |
| JUP/USDT:USDT | below_1h_threshold | +0.88% | +0.80% |
| OP/USDT:USDT | below_1h_threshold | +0.83% | +0.75% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
