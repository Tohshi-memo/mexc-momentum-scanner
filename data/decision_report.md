# Decision Report

- generated_at: 2026-06-10T07:49:00.436949+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6198**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6198, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.95% | **-0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_BB3S | 3/19 | 15.8% | +0.75% | **+0.12%** |
| ASK | 20/20 | 100.0% | +0.08% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.45% | **+0.65%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.95% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$150.53** / 初期 $100.00 (+50.53%)
- 確定: 1214件 (Win 301 / Loss 376 / Flat 537) / skip 1545件
- 成長率目線: 平均log +0.000337 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $150.53

## 4. Latest Market Context

- 更新: 2026-06-10T07:48:57.512913+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.37% price=61666.1
- Funnel: target 781 → liquid 148 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +46.46% | $7,380,112.09 |
| BTW/USDT:USDT | +32.00% | $29,749,527.90 |
| ESPORTS/USDT:USDT | +27.30% | $22,743,689.80 |
| UB/USDT:USDT | +17.10% | $2,018,433.32 |
| UAI/USDT:USDT | +13.92% | $1,523,372.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IO/USDT:USDT | below_1h_threshold | +4.35% | +3.97% |
| BTW/USDT:USDT | below_1h_threshold | +4.31% | +3.93% |
| SENT/USDT:USDT | below_1h_threshold | +4.04% | +3.67% |
| STG/USDT:USDT | below_1h_threshold | +3.83% | +3.46% |
| UAI/USDT:USDT | below_1h_threshold | +3.08% | +2.70% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
