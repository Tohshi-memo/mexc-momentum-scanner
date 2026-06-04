# Decision Report

- generated_at: 2026-06-04T20:54:23.766790+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5667**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5667, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-2.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.65% | **-2.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_BB3S | 4/15 | 26.7% | +0.59% | **+0.16%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.51% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.65% | **+2.65%** |
| ASK_LONG | 20/20 | 100.0% | +1.58% | **+1.58%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.25% | **+1.46%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +3.17% | **+1.42%** |
| LIMIT_5PCT_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$98.05** / 初期 $100.00 (-1.95%)
- 確定トレード: 99件 (TP 30 / SL 66 / EXP 3)
- 最新: MONAD/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.05
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1008件 (Win 239 / Loss 312 / Flat 457) / skip 1220件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T20:54:21.333933+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=63487.7
- Funnel: target 771 → liquid 170 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +34.97% | $38,017,727.99 |
| BTW/USDT:USDT | +32.50% | $5,720,476.99 |
| AAOISTOCK/USDT:USDT | +11.88% | $1,104,786.24 |
| HOME/USDT:USDT | +8.79% | $5,202,403.90 |
| MEME/USDT:USDT | +7.97% | $1,789,465.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XMR/USDT:USDT | below_1h_threshold | +3.34% | +3.52% |
| BTW/USDT:USDT | below_1h_threshold | +3.02% | +3.19% |
| MONAD/USDT:USDT | below_1h_threshold | +2.43% | +2.60% |
| HOME/USDT:USDT | below_1h_threshold | +1.28% | +1.46% |
| BSB/USDT:USDT | below_1h_threshold | +1.15% | +1.33% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
