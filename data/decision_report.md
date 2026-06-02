# Decision Report

- generated_at: 2026-06-02T08:52:23.508766+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5432**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5432, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 9/18 | 50.0% | +1.20% | **+0.60%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| ASK | 20/20 | 100.0% | +0.26% | **+0.26%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.33% | **+0.93%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.48% | **+0.48%** |
| ASK_LONG | 20/20 | 100.0% | +0.15% | **+0.15%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.22% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$96.14** / 初期 $100.00 (-3.86%)
- 確定トレード: 85件 (TP 24 / SL 58 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.14
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$134.97** / 初期 $100.00 (+34.97%)
- 確定: 944件 (Win 222 / Loss 282 / Flat 440) / skip 1049件
- 成長率目線: 平均log +0.000318 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $134.97

## 4. Latest Market Context

- 更新: 2026-06-02T08:52:19.663492+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.42% price=69782.2
- Funnel: target 772 → liquid 150 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.1 >= 65=1, 4h RSI 79.8 >= 65=1, 4h RSI 86.9 >= 65=1, 4h RSI 84.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +58.89% | $18,385,004.45 |
| US/USDT:USDT | +39.92% | $2,062,795.83 |
| ESPORTS/USDT:USDT | +28.09% | $12,482,150.07 |
| MRVLSTOCK/USDT:USDT | +27.08% | $3,475,722.88 |
| USELESS/USDT:USDT | +20.79% | $1,667,690.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.17% | +4.59% |
| BILL/USDT:USDT | below_1h_threshold | +3.82% | +4.25% |
| USELESS/USDT:USDT | below_1h_threshold | +3.45% | +3.87% |
| AVGOSTOCK/USDT:USDT | below_1h_threshold | +2.34% | +2.77% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.28% | +2.71% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
