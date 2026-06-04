# Decision Report

- generated_at: 2026-06-04T17:54:40.889935+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5655**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5655, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +1.54% | **+1.00%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| ASK | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_BB3S | 8/17 | 47.1% | +0.51% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| ASK_LONG | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.62% | **+0.46%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.61% | **+0.42%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$98.54** / 初期 $100.00 (-1.46%)
- 確定トレード: 98件 (TP 30 / SL 65 / EXP 3)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.54
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1007件 (Win 239 / Loss 312 / Flat 456) / skip 1209件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T17:54:34.476089+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=63439.2
- Funnel: target 771 → liquid 171 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%, rsi_15m 67%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +24.12% | $2,826,314.93 |
| LAB/USDT:USDT | +18.80% | $149,292,905.30 |
| PORTAL/USDT:USDT | +11.28% | $2,997,011.56 |
| BIANRENSHENG/USDT:USDT | +6.80% | $1,450,666.12 |
| ALLO/USDT:USDT | +6.34% | $5,762,163.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MEME/USDT:USDT | below_1h_threshold | +4.19% | +4.33% |
| BSB/USDT:USDT | below_1h_threshold | +4.17% | +4.32% |
| UB/USDT:USDT | below_1h_threshold | +4.12% | +4.27% |
| GRASS/USDT:USDT | below_1h_threshold | +3.92% | +4.07% |
| BEAT/USDT:USDT | below_1h_threshold | +2.77% | +2.92% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
